#!/usr/bin/env python3
"""Elenca le note del vault senza le etichette obbligatorie nel frontmatter.
Sola lettura: non modifica niente. Funziona su Mac, Windows e Linux (Python 3.8+, nessuna libreria esterna).

Uso:  python3 controlla_etichette.py <cartella-vault>
"""
import sys
from pathlib import Path

OBBLIGATORIE = ("entita", "livello", "visibile_a")
SALTA = {".git", ".obsidian", ".trash", "_attachments"}


def frontmatter(testo: str) -> dict:
    if not testo.startswith("---"):
        return {}
    fine = testo.find("\n---", 3)
    if fine == -1:
        return {}
    campi = {}
    for riga in testo[3:fine].splitlines():
        if ":" in riga and not riga.startswith((" ", "\t", "#")):
            chiave, valore = riga.split(":", 1)
            campi[chiave.strip()] = valore.split("#", 1)[0].strip()
    return campi


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    radice = Path(sys.argv[1]).expanduser()
    mancanti = 0
    totale = 0
    for nota in sorted(radice.rglob("*.md")):
        if any(parte in SALTA for parte in nota.relative_to(radice).parts):
            continue
        totale += 1
        campi = frontmatter(nota.read_text(encoding="utf-8", errors="ignore"))
        assenti = [c for c in OBBLIGATORIE if not campi.get(c) or campi.get(c) in ("[]", '""')]
        if assenti:
            mancanti += 1
            print(f"{nota.relative_to(radice)}  manca: {', '.join(assenti)}")
    print(f"\n{totale} note lette, {mancanti} senza etichette complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
