# Pulizia automatica delle sessioni ferme

**Cosa fa.** Ogni sessione di Claude Code aperta (una chat nell'app, un terminale con `claude`)
tiene acceso un processo con i suoi server MCP. Da me ognuno pesava circa 500 MB fra memoria e
swap. Questo script trova le sessioni che non lavorano e non aspettano niente da 30 minuti e
chiude il loro processo. La conversazione resta salvata su disco: la riprendi con
`claude --resume` o riaprendo la chat.

Non chiude una sessione se:
- la sua conversazione è cambiata negli ultimi 30 minuti;
- ha un comando in corso (un processo figlio nato dopo l'avvio);
- l'ultimo strumento chiamato non ha ancora una risposta (sta lavorando o aspetta un tuo permesso);
- è nella lista «tieni»;
- è una sessione senza interfaccia (`claude -p`), che finisce da sola;
- non riesce a capire qual è la sua conversazione: nel dubbio la lascia stare.

La mia versione gira su un server ogni 5 minuti, per le chat dell'app, e riconosce anche i
lavori in background e i risvegli programmati. Questa è la versione minima per PC: più semplice,
quindi più prudente.

**Richiede.** Python 3. Su Linux e Mac basta la libreria standard (usa `ps`, e su Mac `lsof`).
Su Windows serve `pip install psutil`.

**Dove si copia.** `ferma_sessioni.py` in `~/.claude/strumenti/`.

**Come si usa.**
1. Prima guarda e basta: `python3 ferma_sessioni.py`. Stampa `tengo` (con il motivo) o
   `CHIUDEREI`, e non chiude niente.
2. Una sessione da non chiudere mai: `python3 ferma_sessioni.py tieni <id-sessione o cartella>`.
3. Quando ti fidi, pianifica ogni 10-15 minuti `python3 ~/.claude/strumenti/ferma_sessioni.py ferma`.
   Ogni chiusura finisce in `~/.claude/ferma-sessioni.jsonl` (solo ora, numero del processo,
   sessione e cartella, nessun testo).

**Attenzione.** In un terminale, chiudere il processo vuol dire che `claude` esce e torni al
prompt della shell. Se scrivi in un terminale lasciato fermo un'ora, prima rilancia
`claude --resume`. Il riconoscimento della conversazione dalla cartella dipende da come Claude
Code chiama le sue cartelle in `~/.claude/projects/`: con una versione diversa potrebbe non
trovarla, e allora lo script non chiude niente.

**Come si prova (su dati finti).**
1. Crea tre cartelle di prova e, per ognuna, una conversazione finta in
   `~/.claude/projects/<percorso con i segni cambiati in «-»>/prova.jsonl` (usa una home di prova).
2. Rendi vecchie due conversazioni (`touch -d '-2 hours' …`) e in una aggiungi una riga con un
   `tool_use` senza risposta.
3. In ogni cartella lancia un processo finto chiamato `claude` (una copia di `sleep`).
4. `python3 ferma_sessioni.py` deve dire: `CHIUDEREI` per la vecchia, `tengo` per quella attiva
   e per quella con lo strumento aperto. Con `ferma` deve chiudere solo la prima.

Io l'ho provato così, su Linux, il 27/11/2026. Su Mac e Windows non l'ho provato.

**Come si toglie.** Togli l'attività pianificata e cancella lo script,
`~/.claude/ferma-sessioni-tieni.txt` e `~/.claude/ferma-sessioni.jsonl`.

## English

Closes the process of Claude Code sessions that have been idle for 30 minutes (not working, not waiting for a tool, a permission or you), to free memory. It skips sessions with recent changes, running commands or on your "keep" list. Conversations stay on disk and resume with `claude --resume` or by reopening the chat.

Install: copy `ferma_sessioni.py` into `~/.claude/strumenti/`. Run it first with no arguments (dry run: it only shows what it would do), then schedule `ferma_sessioni.py ferma` every 10-15 minutes. On Windows run `pip install psutil` first.
