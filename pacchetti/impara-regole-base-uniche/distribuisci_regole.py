#!/usr/bin/env python3
"""Regole base uniche per tutti i tuoi agenti, ricopiate da sole.

Una fonte sola: REGOLE-BASE.md. Lo script ne mette il testo, fra due segni, dentro ogni file
elencato in destinazioni.txt (i file dei tuoi sotto-agenti, il CLAUDE.md o l'AGENTS.md di un
progetto, le regole di un altro strumento). Il resto di quei file non lo tocca.

Se qualcuno (tu, Claude o un agente) cambia il blocco dentro una copia, al giro dopo torna
uguale alla fonte. Per cambiare una regola si cambia REGOLE-BASE.md, e basta.

    python3 distribuisci_regole.py              copia dove serve
    python3 distribuisci_regole.py --verifica   non scrive; esce con 1 se una copia è diversa

Solo libreria standard. Mac, Windows, Linux.
"""
import hashlib
import os
import sys
import tempfile
from pathlib import Path

QUI = Path(__file__).resolve().parent
FONTE = QUI / "REGOLE-BASE.md"
ELENCO = QUI / "destinazioni.txt"
INIZIO = "<!-- regole-base: inizio (copia automatica, non modificare qui: cambia REGOLE-BASE.md) -->"
FINE = "<!-- regole-base: fine -->"


def blocco(testo):
    return f"{INIZIO}\n{testo.strip()}\n{FINE}"


def nuovo_contenuto(attuale, b):
    if INIZIO in attuale and FINE in attuale:
        prima, _, resto = attuale.partition(INIZIO)
        _, _, dopo = resto.partition(FINE)
        return prima + b + dopo
    # prima volta: il blocco va in cima, dopo l'eventuale intestazione YAML dei sotto-agenti
    if attuale.startswith("---\n"):
        fine_yaml = attuale.find("\n---", 4)
        if fine_yaml != -1:
            taglio = attuale.find("\n", fine_yaml + 4) + 1 or len(attuale)
            return attuale[:taglio] + "\n" + b + "\n\n" + attuale[taglio:]
    return b + "\n\n" + attuale


def scrivi_sicuro(dest, testo):
    fd, tmp = tempfile.mkstemp(dir=dest.parent, prefix=".regole-")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(testo)
    os.replace(tmp, dest)


def main():
    verifica = "--verifica" in sys.argv
    if not FONTE.exists() or not ELENCO.exists():
        print(f"Mancano {FONTE.name} o {ELENCO.name} accanto allo script.")
        return 2
    b = blocco(FONTE.read_text(encoding="utf-8"))
    errori = 0
    for riga in ELENCO.read_text(encoding="utf-8").splitlines():
        riga = riga.strip()
        if not riga or riga.startswith("#"):
            continue
        dest = Path(os.path.expandvars(riga)).expanduser()
        if dest.is_symlink():
            print(f"SALTATO {dest}: è un collegamento, non lo seguo")
            errori += 1
            continue
        if not dest.parent.is_dir():
            print(f"MANCA la cartella di {dest}")
            errori += 1
            continue
        attuale = dest.read_text(encoding="utf-8") if dest.exists() else ""
        voluto = nuovo_contenuto(attuale, b)
        if hashlib.sha256(attuale.encode()).digest() == hashlib.sha256(voluto.encode()).digest():
            print(f"ok        {dest}")
            continue
        if verifica:
            print(f"DIVERSA   {dest}")
            errori += 1
            continue
        scrivi_sicuro(dest, voluto)
        print(f"aggiornata {dest}")
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
