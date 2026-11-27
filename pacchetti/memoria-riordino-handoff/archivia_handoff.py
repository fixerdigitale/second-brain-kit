#!/usr/bin/env python3
"""Archivia le sezioni vecchie di un HANDOFF.md troppo lungo.

Cerca la riga «## Lavori» e, se il file supera la soglia, sposta le sezioni «## ...» più vecchie
(quelle in fondo) in HANDOFF-ARCHIVIO-AAAA-MM.md finché il file torna sotto l'obiettivo.
Tiene sempre almeno 3 sezioni. Prima di scrivere fa una copia datata e controlla che nessuna riga si perda.

Uso:
  python3 archivia_handoff.py <cartella-progetto>            # a secco: dice cosa farebbe
  python3 archivia_handoff.py <cartella-progetto> --applica  # lo fa davvero

Mac, Windows, Linux. Python 3.8+, nessuna libreria esterna.
"""
import shutil
import sys
from datetime import datetime
from pathlib import Path

SOGLIA = 80_000      # byte: sopra questa si archivia
OBIETTIVO = 60_000   # byte: si archivia fino a scendere qui
MINIMO_SEZIONI = 3
TITOLO_LAVORI = "## Lavori"


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    applica = "--applica" in sys.argv
    if len(args) != 1:
        print(__doc__)
        return 2
    cartella = Path(args[0]).expanduser()
    handoff = cartella / "HANDOFF.md"
    if not handoff.is_file():
        print(f"Non trovo {handoff}")
        return 1
    testo = handoff.read_text(encoding="utf-8")
    dimensione = len(testo.encode("utf-8"))
    if dimensione <= SOGLIA:
        print(f"{handoff.name}: {dimensione} byte, sotto {SOGLIA}. Niente da fare.")
        return 0

    righe = testo.splitlines(keepends=True)
    inizio = next((i for i, r in enumerate(righe) if r.startswith(TITOLO_LAVORI)), None)
    if inizio is None:
        print(f"Manca la riga «{TITOLO_LAVORI}»: aggiungila sopra le sezioni dei lavori e riprova.")
        return 1

    testa = righe[: inizio + 1]
    sezioni, corrente = [], []
    for r in righe[inizio + 1:]:
        if r.startswith("## ") and corrente:
            sezioni.append(corrente)
            corrente = []
        corrente.append(r)
    if corrente:
        sezioni.append(corrente)
    # la parte prima della prima sezione «## » (righe vuote) resta in testa
    if sezioni and not sezioni[0][0].startswith("## "):
        testa += sezioni.pop(0)

    tenute = list(sezioni)
    spostate = []
    peso = lambda blocchi: sum(len("".join(b).encode("utf-8")) for b in blocchi)
    base = len("".join(testa).encode("utf-8"))
    while len(tenute) > MINIMO_SEZIONI and base + peso(tenute) > OBIETTIVO:
        spostate.insert(0, tenute.pop())  # la più vecchia sta in fondo

    if not spostate:
        print("Niente da spostare: le sezioni rimaste sono il minimo.")
        return 0

    nuovo = "".join(testa) + "".join("".join(s) for s in tenute)
    archivio = cartella / f"HANDOFF-ARCHIVIO-{datetime.now():%Y-%m}.md"
    aggiunta = "".join("".join(s) for s in spostate)

    # controllo: nessuna riga persa o doppia
    prima = sorted(righe)
    dopo = sorted(nuovo.splitlines(keepends=True) + aggiunta.splitlines(keepends=True))
    if prima != dopo:
        print("Controllo fallito: le righe non tornano. Non scrivo niente.")
        return 1

    print(f"{handoff.name}: {dimensione} byte → {len(nuovo.encode('utf-8'))} byte.")
    print(f"Sposto {len(spostate)} sezioni in {archivio.name}:")
    for s in spostate:
        print("  " + s[0].strip())
    if not applica:
        print("\nA secco: non ho scritto niente. Rilancia con --applica.")
        return 0

    copia = cartella / f"HANDOFF.md.bak-{datetime.now():%Y%m%d-%H%M}"
    shutil.copy2(handoff, copia)
    with archivio.open("a", encoding="utf-8") as f:
        if archivio.stat().st_size == 0:
            f.write(f"# Archivio HANDOFF {datetime.now():%Y-%m}\n\n")
        f.write(aggiunta)
    handoff.write_text(nuovo, encoding="utf-8")
    print(f"Fatto. Copia di prima: {copia.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
