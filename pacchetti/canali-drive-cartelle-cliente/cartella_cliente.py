#!/usr/bin/env python3
"""cartella_cliente.py - crea (o completa) la cartella di un cliente con le cinque sottocartelle fisse,
e stampa il percorso della sottocartella giusta per un tipo di file.

Lavora su una cartella normale del PC. Se quella cartella e' dentro Google Drive per desktop
(o OneDrive, Dropbox), Drive la sincronizza da solo e la vedono le persone con cui e' condivisa.

Uso:
    python3 cartella_cliente.py crea "Nome Cliente"
    python3 cartella_cliente.py dove "Nome Cliente" consegne     # stampa il percorso
    python3 cartella_cliente.py elenco

Non cancella e non sposta mai niente: crea solo cio' che manca.
"""
import sys
from pathlib import Path

# Cambia qui: la cartella "Clienti" dentro il tuo Drive condiviso sincronizzato sul PC.
# Esempi: Windows  G:\Drive condivisi\<nome>\Clienti   Mac  ~/Library/CloudStorage/GoogleDrive-.../Drive condivisi/<nome>/Clienti
RADICE = Path("<cartella-drive-condiviso>/Clienti")

SOTTOCARTELLE = {
    "iniziali": "01 Documenti iniziali",   # brief, questionari, documenti di partenza
    "materiali": "02 Materiali",           # loghi, foto, testi che manda il cliente
    "richieste": "03 Per le richieste",    # allegati delle richieste del cliente
    "consegne": "04 Consegne",             # quello che consegno al cliente
    "lavoro": "05 Lavoro interno",         # bozze, verifiche, note mie
}


def crea(nome: str) -> Path:
    base = RADICE / nome
    for sotto in SOTTOCARTELLE.values():
        (base / sotto).mkdir(parents=True, exist_ok=True)
    return base


def main(argv) -> int:
    if len(argv) < 2 or argv[1] not in {"crea", "dove", "elenco"}:
        print(__doc__)
        return 2
    if not RADICE.parent.exists():
        print(f"Non trovo {RADICE.parent}: cambia RADICE in cima al file.")
        return 2
    if argv[1] == "elenco":
        for c in sorted(p for p in RADICE.glob("*") if p.is_dir()):
            mancano = [s for s in SOTTOCARTELLE.values() if not (c / s).exists()]
            print(f"{c.name}" + (f"  (mancano: {', '.join(mancano)})" if mancano else ""))
        return 0
    if len(argv) < 3:
        print("Serve il nome del cliente.")
        return 2
    nome = argv[2]
    if argv[1] == "crea":
        print(f"Pronta: {crea(nome)}")
        return 0
    tipo = argv[3] if len(argv) > 3 else "lavoro"
    if tipo not in SOTTOCARTELLE:
        print(f"Tipo sconosciuto. Scegli fra: {', '.join(SOTTOCARTELLE)}")
        return 2
    print(crea(nome) / SOTTOCARTELLE[tipo])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
