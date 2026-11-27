# Raccolta delle richieste fatte nelle altre sessioni

**Cosa fa.** `raccogli_sessioni.py` legge le sessioni di Claude Code delle ultime N ore (tutti i progetti)
e scrive un file markdown con **solo i tuoi messaggi**, per progetto e per sessione. Niente AI, niente rete.
Le cose che sembrano chiavi o password vengono oscurate.

A cosa serve: ogni sessione parte da zero. Con questo file una sessione nuova sa cosa hai chiesto nelle altre
(«ieri ho chiesto a Claude di…») senza che tu lo racconti.

**Dove si copia.**
- Lo script fuori dal vault, es. `<tuo-progetto>/strumenti/raccogli_sessioni.py`.
- Una riga in CLAUDE.md: «Cosa ho chiesto di recente nelle altre sessioni: `<cartella-vault>/Fonti/raccolta/ultima.md`.
  Leggilo quando parlo di un lavoro che qui non vedi.»

**Come si prova.**
`python3 raccogli_sessioni.py --ore 24` (Windows: `py raccogli_sessioni.py --ore 24`): stampa a schermo.
Con `--out <cartella-vault>/Fonti/raccolta/ultima.md` scrive il file.

**Come farlo girare da solo (facoltativo, solo a PC acceso).**
- Windows: Utilità di pianificazione → attività base → «py <percorso>\raccogli_sessioni.py --out <...>\ultima.md», 3 volte al giorno.
- Mac: `crontab -e` → `5 8,13,19 * * * /usr/bin/python3 <percorso>/raccogli_sessioni.py --out <...>/ultima.md`

**Attenzione.** Se il vault va su GitHub o Drive, il file contiene le tue richieste: tienilo in una cartella
esclusa (`.gitignore`) se dentro ci sono cose dei clienti.

**Come si toglie.** Cancella lo script, l'attività pianificata e il file `ultima.md`.

## English

`raccogli_sessioni.py` reads your Claude Code sessions in `~/.claude/projects` and writes one markdown file with only your own messages, by project and session, masking anything that looks like a key. A new session can read it when you say "as I asked yesterday". No model, runs in seconds.

Install: copy `raccogli_sessioni.py` outside the vault and run `python3 raccogli_sessioni.py --ore 24 --out <vault-folder>/Fonti/raccolta/ultima.md`. Optionally schedule it three times a day and add the CLAUDE.md line shown above. If the vault syncs to GitHub or Drive, exclude this file when it contains client material.
