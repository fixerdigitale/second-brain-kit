#!/usr/bin/env python3
"""Regole proposte di notte, fisse solo dopo il tuo ok.

Due comandi, da lanciare con un'attività pianificata (o a mano):

    python3 regole_doro.py proponi --memoria <cartella-memoria>
        Cerca le correzioni (feedback_*.md) tornate almeno SOGLIA volte, cioè con almeno
        SOGLIA righe «**Aggiornamento del …**». Quelle che non sono già fra le Regole d'oro
        di MEMORY.md finiscono in PROPOSTE-REGOLE.md come domanda: «la rendo fissa?».
        Non tocca MEMORY.md.

    python3 regole_doro.py applica --memoria <cartella-memoria> [--prova]
        Legge PROPOSTE-REGOLE.md. Per ogni proposta:
          [x]  sì: aggiunge la riga in fondo alle «Regole d'oro» di MEMORY.md (prima fa una copia datata);
          [-]  no: la scarta e se la ricorda, così non torna più;
          [ ]  non ancora deciso: resta lì.
        Se le Regole d'oro sono già TETTO, non aggiunge niente e lo scrive: prima ne togli una tu.
        Ogni decisione va in STORICO-REGOLE.md.

Il testo che entra è quello della proposta: se lo correggi nel file prima di mettere [x],
entra la tua versione. Solo libreria standard. Mac, Windows, Linux.
"""
import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

SOGLIA = 2   # quante volte deve essere tornata una correzione
TETTO = 20   # massimo di Regole d'oro
SEZIONE = "## Regole d'oro"
PROPOSTE = "PROPOSTE-REGOLE.md"
STORICO = "STORICO-REGOLE.md"
RIGA_PROPOSTA = re.compile(r"^- \[(?P<stato>[ xX-])\] (?P<file>feedback_[\w.-]+\.md) · (?P<testo>.+?)(?: · tornata \d+ volte)?$")


def descrizione(testo):
    m = re.search(r'^description:\s*"?(.*?)"?\s*$', testo, re.M)
    if m and m.group(1).strip():
        return m.group(1).strip()
    for riga in testo.splitlines():
        riga = riga.strip()
        if riga and not riga.startswith(("---", "name:", "metadata", "type:", "modified:", "#")):
            return riga[:160]
    return "(senza descrizione)"


def sezione_oro(memory):
    """Restituisce (inizio, fine) delle righe della sezione Regole d'oro."""
    righe = memory.splitlines()
    inizio = next((i for i, r in enumerate(righe) if r.startswith(SEZIONE)), None)
    if inizio is None:
        return righe, None, None
    fine = next((i for i in range(inizio + 1, len(righe)) if righe[i].startswith("## ")), len(righe))
    return righe, inizio, fine


def gia_decise(cartella):
    st = cartella / STORICO
    if not st.exists():
        return set()
    return set(re.findall(r"(feedback_[\w.-]+\.md)", st.read_text(encoding="utf-8")))


def proponi(cartella):
    memory = (cartella / "MEMORY.md").read_text(encoding="utf-8") if (cartella / "MEMORY.md").exists() else ""
    righe, i, f = sezione_oro(memory)
    nell_oro = "\n".join(righe[i:f]) if i is not None else ""
    file_prop = cartella / PROPOSTE
    esistenti = file_prop.read_text(encoding="utf-8") if file_prop.exists() else ""
    decise = gia_decise(cartella)
    nuove = []
    for p in sorted(cartella.glob("feedback_*.md")):
        testo = p.read_text(encoding="utf-8", errors="replace")
        volte = len(re.findall(r"^\*\*Aggiornamento del", testo, re.M))
        if volte < SOGLIA or p.name in nell_oro or p.name in esistenti or p.name in decise:
            continue
        nuove.append(f"- [ ] {p.name} · {descrizione(testo)} · tornata {volte} volte")
    if not nuove:
        print("Nessuna proposta nuova.")
        return 0
    if not esistenti:
        esistenti = ("# Regole proposte: la rendo fissa?\n\n"
                     "Metti [x] per sì, [-] per no, lascia [ ] se non hai deciso. Puoi correggere il testo prima del sì.\n"
                     "Poi lancia: python3 regole_doro.py applica --memoria <questa cartella>\n\n")
    oggi = dt.date.today().isoformat()
    file_prop.write_text(esistenti.rstrip("\n") + f"\n\n### Proposte del {oggi}\n" + "\n".join(nuove) + "\n", encoding="utf-8")
    print(f"{len(nuove)} proposte nuove in {file_prop}")
    return 0


def applica(cartella, prova):
    file_prop = cartella / PROPOSTE
    if not file_prop.exists():
        print("Nessun file di proposte.")
        return 0
    mem_path = cartella / "MEMORY.md"
    memory = mem_path.read_text(encoding="utf-8") if mem_path.exists() else f"# Indice della memoria\n\n{SEZIONE}\n"
    righe, i, f = sezione_oro(memory)
    if i is None:
        righe += ["", SEZIONE, ""]
        i, f = len(righe) - 2, len(righe)
    numerate = [r for r in righe[i:f] if re.match(r"^\d+\. ", r)]
    conteggio = len(numerate)
    restanti, storico, aggiunte = [], [], []
    oggi = dt.date.today().isoformat()
    for riga in file_prop.read_text(encoding="utf-8").splitlines():
        m = RIGA_PROPOSTA.match(riga)
        if not m or m.group("stato") == " ":
            restanti.append(riga)
            continue
        nome, testo = m.group("file"), m.group("testo").strip()
        if m.group("stato") == "-":
            storico.append(f"- {oggi} · NO · {nome} · {testo}")
            continue
        if conteggio >= TETTO:
            print(f"Tetto di {TETTO} raggiunto: {nome} resta in attesa. Togli prima una Regola d'oro.")
            restanti.append(riga)
            continue
        conteggio += 1
        nome_breve, sep, resto = testo.partition(":")
        if not sep or len(nome_breve) > 40:
            nome_breve, resto = " ".join(testo.split()[:3]), testo
        aggiunte.append(f"{conteggio}. **{nome_breve.strip()}**: {resto.strip()} [→]({nome})")
        storico.append(f"- {oggi} · SÌ · {nome} · {testo}")
    if not storico:
        print("Niente da applicare.")
        return 0
    for r in storico:
        print(r)
    if prova:
        print("(prova: non ho scritto niente)")
        return 0
    if aggiunte:
        if mem_path.exists():
            copia = mem_path.with_name(f"MEMORY.md.bak-{dt.datetime.now():%Y%m%d-%H%M}")
            shutil.copy2(mem_path, copia)
        # le righe nuove vanno dopo l'ultima regola numerata della sezione
        ultima = max((k for k in range(i, f) if re.match(r"^\d+\. ", righe[k])), default=i)
        righe[ultima + 1:ultima + 1] = aggiunte
        mem_path.write_text("\n".join(righe) + "\n", encoding="utf-8")
    file_prop.write_text("\n".join(restanti) + "\n", encoding="utf-8")
    st = cartella / STORICO
    vecchio = st.read_text(encoding="utf-8") if st.exists() else "# Storico delle regole proposte\n\n"
    st.write_text(vecchio.rstrip("\n") + "\n" + "\n".join(storico) + "\n", encoding="utf-8")
    print(f"Aggiunte {len(aggiunte)} Regole d'oro. Storico in {st}")
    return 0


def main():
    p = argparse.ArgumentParser(description="Regole proposte di notte, fisse solo dopo il tuo ok.")
    p.add_argument("comando", choices=["proponi", "applica"])
    p.add_argument("--memoria", required=True, help="cartella con MEMORY.md e i file feedback_*.md")
    p.add_argument("--prova", action="store_true", help="con applica: mostra senza scrivere")
    a = p.parse_args()
    cartella = Path(a.memoria).expanduser()
    if not cartella.is_dir():
        print(f"Cartella non trovata: {cartella}")
        return 2
    return proponi(cartella) if a.comando == "proponi" else applica(cartella, a.prova)


if __name__ == "__main__":
    sys.exit(main())
