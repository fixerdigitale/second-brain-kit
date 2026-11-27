#!/usr/bin/env python3
"""Controlla che in una cartella, un file o uno zip non compaiano nomi da tenere privati.

Serve prima di pubblicare o condividere una cartella (per esempio un kit, una repo,
uno zip): cerca i nomi di un elenco (clienti, persone, domini, percorsi) e blocca
se ne trova anche uno solo.

L'elenco e' un file di testo, un nome per riga, '#' per i commenti. Deve stare
FUORI da quello che si controlla: altrimenti finirebbe pubblicato anche lui, e lo
script si rifiuta.

Gli zip si aprono e si controllano i file dentro (anche .docx, .xlsx, .pptx, che
sono zip). I file che non si possono leggere (PDF, .doc vecchi, immagini...) si
elencano: per quelli lo script non puo' dire «pulito».

Uso:
  controlla_nomi.py --elenco <file-elenco> <cartella|file|zip> [--escludi <nome-cartella>]... [--storia]

  --storia   se c'e' un repository git, controlla anche la storia (git log -p) e i
             messaggi dei salvataggi: un nome tolto oggi resta nei salvataggi vecchi.

Stampa file:riga:NOME per ogni nome trovato. Codici di uscita: 0 pulito,
1 trovato qualcosa (rilascio da fermare), 2 errore d'uso, 3 nessun nome trovato
ma alcuni documenti non si sono potuti leggere (non verificato).
"""
import io
import os
import re
import subprocess
import sys
import zipfile

SALTA = {".git", "node_modules", "__pycache__", ".venv"}
IMMAGINI = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".woff", ".woff2", ".ttf", ".otf",
            ".mp3", ".mp4", ".mov", ".wav", ".m4a", ".ogg", ".heic", ".pyc"}
ZIP = {".zip", ".docx", ".xlsx", ".pptx", ".odt", ".ods", ".odp", ".docm", ".xlsm", ".epub"}


def righe_testo(dati):
    if b"\0" in dati[:4096]:
        return None
    testo = dati.decode("utf-8", errors="replace")
    if testo.lstrip().startswith("<") and ("<w:" in testo or "<a:" in testo or "<text:" in testo):
        # XML di Office: via i tag, un paragrafo per riga
        testo = re.sub(r"</(?:w:p|a:p|text:p|si|row)>", "\n", testo)
        testo = re.sub(r"<[^>]+>", "", testo)
    return testo.splitlines()


def controlla_dati(rel, dati, schemi, trovati, saltati):
    for nome, s in schemi:  # anche nel nome del file (per un file dentro uno zip, solo il suo nome)
        if s.search(rel.rsplit("!", 1)[-1]):
            print("%s:0:%s" % (rel, nome))
            trovati[0] += 1
    est = os.path.splitext(rel)[1].lower()
    if est in ZIP:
        try:
            with zipfile.ZipFile(io.BytesIO(dati)) as z:
                for interno in z.namelist():
                    if interno.endswith("/"):
                        continue
                    controlla_dati(rel + "!" + interno, z.read(interno), schemi, trovati, saltati)
            return
        except (zipfile.BadZipFile, RuntimeError, OSError):
            saltati.append(rel)
            return
    righe = righe_testo(dati)
    if righe is None:
        if est not in IMMAGINI:
            saltati.append(rel)
        return
    for n, riga in enumerate(righe, 1):
        for nome, s in schemi:
            if s.search(riga):
                print("%s:%d:%s" % (rel, n, nome))
                trovati[0] += 1


def main(argv):
    elenco, cartella, escludi, storia = None, None, set(SALTA), False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--elenco" and i + 1 < len(argv):
            elenco = argv[i + 1]
            i += 2
            continue
        if a == "--escludi" and i + 1 < len(argv):
            escludi.add(argv[i + 1])
            i += 2
            continue
        if a == "--storia":
            storia = True
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            cartella = a
        i += 1
    if not elenco or not cartella:
        print(__doc__, file=sys.stderr)
        return 2
    elenco_abs = os.path.realpath(os.path.expanduser(elenco))
    cartella_abs = os.path.realpath(os.path.expanduser(cartella))
    if not os.path.isfile(elenco_abs):
        print("elenco non trovato: " + elenco, file=sys.stderr)
        return 2
    if not os.path.exists(cartella_abs):
        print("non trovato: " + cartella, file=sys.stderr)
        return 2
    if elenco_abs == cartella_abs or elenco_abs.startswith(cartella_abs + os.sep):
        print("Rifiuto: l'elenco dei nomi sta dentro quello che va controllato. Spostalo fuori.", file=sys.stderr)
        return 2
    nomi = []
    with open(elenco_abs, encoding="utf-8") as fh:
        for riga in fh:
            riga = riga.strip()
            if riga and not riga.startswith("#"):
                nomi.append(riga)
    if not nomi:
        print("elenco vuoto", file=sys.stderr)
        return 2
    # parola intera per i nomi semplici, testo esatto per domini e percorsi
    schemi = []
    for n in nomi:
        if re.fullmatch(r"[\w' ]+", n):
            schemi.append((n, re.compile(r"(?<![^\W_])" + re.escape(n) + r"(?![^\W_])", re.I)))
        else:
            schemi.append((n, re.compile(re.escape(n), re.I)))
    trovati, saltati, controllati = [0], [], 0
    if os.path.isfile(cartella_abs):
        base = os.path.dirname(cartella_abs)
        elenco_file = [cartella_abs]
    else:
        base = cartella_abs
        elenco_file = []
        for radice, sotto, files in os.walk(cartella_abs):
            sotto[:] = [d for d in sotto if d not in escludi]
            elenco_file += [os.path.join(radice, f) for f in files]
    for p in elenco_file:
        rel = os.path.relpath(p, base)
        try:
            with open(p, "rb") as fh:
                dati = fh.read()
        except OSError:
            saltati.append(rel)
            continue
        controllati += 1
        controlla_dati(rel, dati, schemi, trovati, saltati)
    if os.path.isdir(os.path.join(cartella_abs, ".git")):
        if storia:
            r = subprocess.run(["git", "-C", cartella_abs, "log", "--all", "-p", "--format=commit %h%n%B"],
                               capture_output=True)
            if r.returncode == 0:
                commit = "?"
                for riga in r.stdout.decode("utf-8", "replace").splitlines():
                    if riga.startswith("commit "):
                        commit = riga[7:].strip()
                    for nome, s in schemi:
                        if s.search(riga):
                            print("git:%s:%s" % (commit, nome))
                            trovati[0] += 1
            else:
                print("nota: storia git non leggibile", file=sys.stderr)
        else:
            print("nota: c'e' un repository git. La storia dei salvataggi non e' stata controllata: "
                  "aggiungi --storia prima di pubblicarlo.", file=sys.stderr)
    if trovati[0]:
        print("BLOCCATO: %d occorrenze di nomi privati." % trovati[0], file=sys.stderr)
        return 1
    if saltati:
        print("NON VERIFICATO: %d file non si possono leggere (PDF, documenti vecchi, binari):" % len(saltati), file=sys.stderr)
        for s in saltati[:20]:
            print("  " + s, file=sys.stderr)
        return 3
    print("Pulito: nessun nome dell'elenco trovato in %d file." % controllati)
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
