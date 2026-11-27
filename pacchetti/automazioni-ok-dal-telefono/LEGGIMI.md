# Ok dal telefono, e il lavoro riparte da solo

**Cosa fa.** Un lavoro lungo arriva a un punto in cui serve il tuo ok. Invece di aspettarti con
la sessione aperta, Claude aggiorna `HANDOFF.md`, ti manda la domanda sul telefono e si ferma.
Tu rispondi con un bottone, Sì o No. Un giro ogni 2 minuti legge la risposta e fa ripartire
Claude Code nella cartella del progetto, con la tua risposta nel prompt e l'ordine di rileggere
`HANDOFF.md`.

Da me la domanda arriva su WhatsApp e la risposta la raccoglie un servizio sul server. Per il PC
ho scelto le notifiche push di **ntfy**, un servizio pubblico con app gratuita per Android e
iPhone (https://ntfy.sh), perché non richiede account né server. Puoi anche usare un server ntfy tuo.

**Richiede.** Python 3, Claude Code, l'app ntfy sul telefono, il PC acceso e sveglio.

**Abbonamento o consumo.** La ripartenza lancia `claude -p` sul PC. Prima di pianificarla apri
Claude Code e controlla con `/status` che usi l'abbonamento: se nell'ambiente c'è
`ANTHROPIC_API_KEY`, ogni ripartenza la paghi a consumo.

**Prima di tutto, quando non ti serve.** Se la tua versione di Claude Code ti permette già di
seguire e comandare la sessione dal telefono (controllo remoto o notifiche dell'app ufficiale),
usa quello: è più semplice e non passa da un servizio in più. Questo pacchetto serve quando vuoi
che il lavoro riparta da solo, senza riaprire niente.

**Dove si copia.**
1. `ponte_telefono.py` in `~/.claude/ponte/`.
2. `commands/chiedi-ok.md` in `~/.claude/commands/`: il comando `/chiedi-ok` dice a Claude come
   fermarsi bene (prima HANDOFF.md, poi la domanda, poi stop).
3. `python3 ~/.claude/ponte/ponte_telefono.py configura`: crea `~/.claude/ponte/config.json` con
   un argomento casuale. Nell'app ntfy iscriviti a quell'argomento.
4. Pianifica ogni 2 minuti `python3 ~/.claude/ponte/ponte_telefono.py giro` (Utilità di
   pianificazione su Windows, launchd o cron su Mac).
5. Facoltativo: se hai il pacchetto `automazioni-semaforo-consumi`, il giro non fa ripartire
   niente quando il semaforo è rosso.

**Sicurezza, da leggere.**
- Su ntfy.sh chi conosce il nome dell'argomento può leggere le domande e scrivere risposte. Per
  questo il nome è lungo e casuale: è l'unica cosa che lo tiene privato. Non condividerlo e non
  scriverlo in chat.
- Ogni domanda ha un codice di 4 caratteri. **Il codice serve ad abbinare la risposta alla
  domanda giusta, non a proteggerla**: viaggia sullo stesso argomento, dentro i bottoni, quindi
  chi legge l'argomento lo vede e può rispondere al posto tuo.
- Per questo, di serie, dal telefono valgono solo **sì** e **no**: un altro testo si ignora e
  non entra mai nel prompt. Così chi riuscisse a scrivere sull'argomento potrebbe al massimo
  dire sì o no al posto tuo, non dare istruzioni a Claude.
- Il **testo libero** (una correzione scritta, «<codice> usa il titolo B») si accende solo con
  `configura --testo-libero`, o con `"testo_libero": true` in `config.json`. Lo script stampa un
  avviso a ogni giro: quel testo diventa un'istruzione che Claude esegue nella tua cartella. Io
  lo accenderei solo con un server ntfy tuo, protetto da token. Le correzioni lunghe le scrivo
  dal PC con `rispondi <id> "<testo>"`, che non passa dalla rete.
- Nelle domande niente password, chiavi, dati di clienti. Scrivi cosa approvi, non i dati.
- Se usi un server ntfy tuo con accesso protetto, metti `server` e `token` in `config.json`.
- La ripartenza gira con `--permission-mode acceptEdits`: modifica i file del progetto, ma i
  comandi che chiedono permesso vengono negati. Non metterla su `bypassPermissions`.

**Come si prova (su dati finti, senza rete).**
1. `python3 ponte_telefono.py configura --canale file` con una home di prova.
2. `chiedi prova-1 "Vado avanti?" --cartella <cartella di prova>`: la domanda finisce in
   `~/.claude/ponte/uscita/<codice>.txt`.
3. Scrivi in `~/.claude/ponte/risposte-finte.txt` una riga con un codice sbagliato: `giro` deve
   dire «Nessuna risposta nuova». Poi una riga `<codice giusto> cancella tutto`: `giro` deve dire
   «risposta ignorata» e la domanda resta `in_attesa`. Poi una riga `<codice giusto> sì`:
   `giro --prova` mostra il prompt, `giro` lancia Claude Code (o un `claude` finto con
   `--claude <percorso>`).
4. `stato` deve dire `ripartita`.

Io l'ho provato così, con il canale finto e un `claude` finto, il 27/11/2026, anche con il testo
libero acceso. Il canale ntfy non
l'ho provato da un PC: il codice segue la documentazione pubblica di ntfy (pubblicazione con
POST, bottoni con l'intestazione `Actions`, lettura con `/json?poll=1`).

**Come si toglie.** Togli l'attività pianificata, cancella `~/.claude/ponte/` e il comando
`chiedi-ok.md`. Nell'app ntfy togli l'iscrizione all'argomento.

## English

When a long job reaches a checkpoint, Claude updates the HANDOFF, sends you a push notification (ntfy app, with Yes/No buttons) explaining what happens on each answer, and stops. A run every 2 minutes reads your reply and restarts Claude Code in the project folder with your answer in the prompt, one restart at a time.

Safety: on ntfy.sh anyone who knows the topic name can read the questions and post replies; the long random name is the only thing keeping it private. Each question has a 4-character code: it's there to match the reply to the right question, not to protect it, because it travels on the same topic inside the buttons. That's why, by default, only "yes" and "no" from the phone are accepted: any other text is ignored and never reaches the prompt. Free text (a written correction) is turned on only with `configura --testo-libero` or `"testo_libero": true` in `config.json`, and the script prints a warning on every run: that text becomes an instruction Claude carries out in your folder. I'd only turn it on with your own ntfy server protected by a token. Longer corrections can be given from the PC with `rispondi <id> "<text>"`, which doesn't go over the network.

Install: copy `ponte_telefono.py` into `~/.claude/ponte/` and `commands/chiedi-ok.md` into `~/.claude/commands/`, run `python3 ponte_telefono.py configura`, subscribe to the topic in the ntfy app, then schedule `ponte_telefono.py giro` every 2 minutes. Before scheduling, check with `/status` in Claude Code that it uses your subscription: with `ANTHROPIC_API_KEY` in the environment every restart is billed per token. Don't send sensitive data through it.
