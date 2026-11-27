#!/usr/bin/env python3
"""Copia datata di un file prima di modificarlo: config.json -> config.json.bak-AAAAMMGG[-nota].

Uso:  python3 copia_datata.py <file> [nota-breve]
Se la copia di oggi esiste già, aggiunge -2, -3... invece di sovrascriverla.
Funziona su Mac, Windows e Linux (solo libreria standard).
"""
import datetime
import pathlib
import shutil
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    originale = pathlib.Path(sys.argv[1])
    if not originale.is_file():
        print(f"Non trovo il file: {originale}")
        return 2
    nota = "-" + sys.argv[2] if len(sys.argv) > 2 else ""
    base = f"{originale.name}.bak-{datetime.date.today():%Y%m%d}{nota}"
    copia = originale.with_name(base)
    n = 2
    while copia.exists():
        copia = originale.with_name(f"{base}-{n}")
        n += 1
    shutil.copy2(originale, copia)
    print(f"Copia fatta: {copia}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
