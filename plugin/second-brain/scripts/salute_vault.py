#!/usr/bin/env python3
"""Numeri di salute di un vault di note Markdown, in sola lettura.

Misura: note, cartelle, note toccate negli ultimi 30 giorni, doppioni (stesso nome
in cartelle diverse), note orfane (nessun link in entrata), conflitti (copie di
sincronizzazione, segni di conflitto git), note molto lunghe, e quanta parte delle
note e' raggiungibile dall'indice.

Stampa solo nomi di file e numeri, mai il contenuto delle note.

Uso:
  salute_vault.py <cartella-vault> [--indice <file>] [--json] [--elenchi N]

Solo libreria standard di Python 3. Mac, Windows, Linux.
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cerca_segreti import percorso_sicuro  # noqa: E402  (nessun segreto nei nomi stampati)
import time

SALTA = {".git", ".obsidian", ".trash", ".Trash", "node_modules", ".claude", "_da-cancellare", ".venv",
         "second-brain"}
LINK_WIKI = re.compile(r"\[\[([^\]|#]+)")
LINK_MD = re.compile(r"\]\(([^)#\s]+\.md)")
CONFLITTO_NOME = re.compile(r"(conflict|conflitto|sync-conflict| \(\d\)\.md$|\.orig$)", re.I)
# nomi possibili dell'indice; se ce n'e' piu' d'uno vince quello con piu' link in uscita,
# e README/LEGGIMI solo se non c'e' altro (di solito spiegano, non indicizzano)
INDICI = ("indice.md", "index.md", "00-indice.md", "00-index.md", "MEMORY.md", "Home.md", "HOME.md",
          "_indice.md", "README.md", "LEGGIMI.md")
NON_ORFANE = {"claude.md", "agents.md", "readme.md", "leggimi.md", "memory.md", "handoff.md", "sistema.md"}


def main(argv):
    vault, indice, come_json, n_el = None, None, False, 10
    i = 0
    while i < len(argv):
        a = argv[i]
        v = argv[i + 1] if i + 1 < len(argv) else None
        if a == "--indice" and v:
            indice = v; i += 2; continue
        if a == "--elenchi" and v:
            try:
                n_el = int(v)
            except ValueError:
                print("--elenchi vuole un numero", file=sys.stderr); return 2
            i += 2; continue
        if a == "--json":
            come_json = True
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            vault = a
        i += 1
    if not vault or not os.path.isdir(os.path.expanduser(vault)):
        print(__doc__, file=sys.stderr)
        return 2
    vault = os.path.realpath(os.path.expanduser(vault))

    note = {}          # rel -> (dimensione, mtime)
    cartelle = set()
    per_nome = collections.defaultdict(list)
    conflitti = []
    for radice, sotto, files in os.walk(vault):
        sotto[:] = [d for d in sotto if d not in SALTA]
        for f in files:
            p = os.path.join(radice, f)
            rel = os.path.relpath(p, vault)
            if CONFLITTO_NOME.search(f):
                conflitti.append(rel)
            if not f.lower().endswith(".md"):
                continue
            try:
                st = os.stat(p)
            except OSError:
                continue
            note[rel] = (st.st_size, st.st_mtime)
            cartelle.add(os.path.dirname(rel) or ".")
            per_nome[os.path.splitext(f)[0].lower()].append(rel)

    entranti = collections.Counter()
    link_da = {}
    con_segni_conflitto = []
    for rel in note:
        try:
            with open(os.path.join(vault, rel), encoding="utf-8", errors="replace") as fh:
                testo = fh.read()
        except OSError:
            continue
        if "\n<<<<<<< " in testo or testo.startswith("<<<<<<< "):
            con_segni_conflitto.append(rel)
        destinazioni = set()
        for m in LINK_WIKI.findall(testo):
            destinazioni.add(os.path.basename(m.strip()).lower().removesuffix(".md"))
        for m in LINK_MD.findall(testo):
            destinazioni.add(os.path.splitext(os.path.basename(m))[0].lower())
        link_da[rel] = destinazioni
        for d in destinazioni:
            entranti[d] += 1

    adesso = time.time()
    recenti = [r for r, (_, mt) in note.items() if adesso - mt < 30 * 86400]
    lunghe = [r for r, (sz, _) in note.items() if sz > 50 * 1024]
    doppioni = {k: v for k, v in per_nome.items() if len(v) > 1 and not k.startswith("_modello") and k not in ("readme", "leggimi", "claude", "indice", "index")}
    nomi_indice = {os.path.basename(x) for x in INDICI}
    orfane = [r for r in note
              if entranti[os.path.splitext(os.path.basename(r))[0].lower()] == 0
              and os.path.basename(r) not in nomi_indice and os.path.basename(r).lower() not in NON_ORFANE
              and not os.path.basename(r).startswith("_")]

    file_indice = None
    if indice:
        file_indice = os.path.relpath(os.path.realpath(os.path.join(vault, indice)), vault)
    else:
        candidati = [n for n in INDICI if n in note]
        if candidati:
            # piu' link in uscita vince; a parita', l'ordine di INDICI (README per ultimo)
            file_indice = max(candidati, key=lambda n: (len(link_da.get(n, ())) if n.lower() not in ("readme.md", "leggimi.md") else -1,
                                                        -INDICI.index(n)))
    copertura = None
    if file_indice and file_indice in link_da:
        # raggiungibili dall'indice: link diretti e link a un passo
        livello1 = link_da[file_indice]
        raggiungibili = set(livello1)
        for r, dest in link_da.items():
            if os.path.splitext(os.path.basename(r))[0].lower() in livello1:
                raggiungibili |= dest
        tot = len(note) - 1
        coperte = sum(1 for r in note if r != file_indice and os.path.splitext(os.path.basename(r))[0].lower() in raggiungibili)
        copertura = round(100.0 * coperte / tot, 1) if tot > 0 else None

    ultima = max((mt for _, mt in note.values()), default=None)
    uscita = {
        "vault": os.path.basename(vault),
        "note": len(note),
        "cartelle": len(cartelle),
        "toccate_ultimi_30_giorni": len(recenti),
        "giorni_dall_ultima_modifica": int((adesso - ultima) // 86400) if ultima else None,
        "doppioni": len(doppioni),
        "orfane": len(orfane),
        "conflitti": len(conflitti) + len(con_segni_conflitto),
        "note_oltre_50kb": len(lunghe),
        "indice": file_indice,
        "copertura_indice_percento": copertura,
        "esempi": {
            "doppioni": [", ".join(v) for v in list(doppioni.values())[:n_el]],
            "orfane": sorted(orfane)[:n_el],
            "conflitti": (conflitti + con_segni_conflitto)[:n_el],
            "lunghe": sorted(lunghe)[:n_el],
        },
    }
    uscita["vault"] = percorso_sicuro(uscita["vault"])
    uscita["indice"] = percorso_sicuro(uscita["indice"]) if uscita["indice"] else None
    file_indice = uscita["indice"]
    uscita["esempi"] = {k: [percorso_sicuro(x) for x in v] for k, v in uscita["esempi"].items()}
    if come_json:
        print(json.dumps(uscita, ensure_ascii=False, indent=2))
        return 0
    print("Vault: %s" % uscita["vault"])
    print("- note: %d in %d cartelle; toccate negli ultimi 30 giorni: %d; ultima modifica: %s giorni fa" % (
        uscita["note"], uscita["cartelle"], uscita["toccate_ultimi_30_giorni"], uscita["giorni_dall_ultima_modifica"]))
    print("- doppioni: %d · orfane: %d · conflitti: %d · oltre 50 KB: %d" % (
        uscita["doppioni"], uscita["orfane"], uscita["conflitti"], uscita["note_oltre_50kb"]))
    if file_indice:
        print("- indice: %s, copre il %s%% delle note" % (file_indice, copertura))
    else:
        print("- indice: non trovato")
    for k, lista in uscita["esempi"].items():
        if lista:
            print("  %s: %s" % (k, "; ".join(lista)))
    return 0


if __name__ == "__main__":
    for _f in (sys.stdout, sys.stderr):
        try:
            _f.reconfigure(encoding="utf-8", errors="backslashreplace")
        except (AttributeError, ValueError):
            pass
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as e:
        print("errore: %s" % e, file=sys.stderr)
        sys.exit(2)
