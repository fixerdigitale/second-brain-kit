# Board delle task (versione da PC della mia)

**Cosa fa.** Ogni lavoro diventa una task con quattro cose che io guardo sempre: la **stima** in minuti
(decisa prima), il **tempo vero** (contato mentre si lavora, mai copiato dalla stima), **chi ci lavora
adesso** (io, Claude, un collaboratore) e la **fonte** (la call, il messaggio o il link da cui nasce).
`board.py` tiene i dati in `task.json` e a ogni comando riscrive `TASK.md`, la vista da leggere:
Da fare, In corso, Fatto, con il segno ● su chi ci sta lavorando e «ferma da N giorni» sulle task
In corso che non si muovono.

Nel mio sistema la board è una pagina del Pannello su un server, e il tempo lo contano gli hook di
Claude Code. Qui è un file: niente server, niente database.

**Dove si copia.**
1. `board.py` dove vuoi, per esempio `<cartella-vault>/strumenti/board.py`. Serve solo Python 3.
2. Scegli la cartella della board, per esempio `<cartella-vault>/task/`, e passala con `--cartella`.
3. Il testo di `regola-per-CLAUDE.md` nel `CLAUDE.md` del vault, con i due percorsi giusti.

**Come si usa.**

    python3 board.py --cartella <cartella-vault>/task nuova "Bozza preventivo" --stima 45 --progetto clienti/x --fonte "call del 12/11"
    python3 board.py --cartella <cartella-vault>/task inizia T-1 --chi claude
    python3 board.py --cartella <cartella-vault>/task pausa T-1
    python3 board.py --cartella <cartella-vault>/task fatta T-1
    python3 board.py --cartella <cartella-vault>/task tempo T-1 20     # minuti fatti fuori da Claude
    python3 board.py --cartella <cartella-vault>/task elenco

Un tratto aperto e dimenticato conta al massimo 4 ore (`MAX_MINUTI_TRATTO` in cima al file).
Chi inizia una task nuova mette in pausa da solo quella su cui stava lavorando.

**Se vuoi il tempo contato da solo.** Il pacchetto `pacchetti/hook-tempo-per-progetto/` registra con
gli hook quanto lavori con Claude in ogni cartella. Le due cose si sommano a mano: il registro ti dice
i minuti, `board.py tempo` li scrive sulla task.

**Come si prova.** In una cartella di prova: `nuova`, `inizia`, aspetta due minuti, `fatta`. In
`TASK.md` la task deve stare in Fatto con 2 minuti di tempo vero e la stima intatta.

**Limiti.** È un file per una persona o un gruppo piccolo che condivide la cartella: se due persone
scrivono nello stesso istante, vince l'ultima. Niente notifiche.

**Come si toglie.** Cancella `board.py`, la sezione nel `CLAUDE.md` e, se vuoi, la cartella della board.

## English

A file-based task board: `board.py` keeps for each task its estimate, the real time spent, who's working on it now and its source, and writes a `TASK.md` view you can read from your phone. A rule for CLAUDE.md tells Claude to use it for every job longer than a few minutes.

Install: copy `board.py` into your vault, choose the board folder and paste `regola-per-CLAUDE.md` into your CLAUDE.md. For automatic time tracking add `pacchetti/hook-tempo-per-task/`; to break big jobs into tasks, `pacchetti/skill-roadmap-lavoro/`. For one person or a small group: no notifications, no concurrent writes.
