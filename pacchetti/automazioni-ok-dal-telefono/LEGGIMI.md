# Ok dal telefono, e il lavoro riparte da solo

**Cosa fa.** Un lavoro lungo arriva a un punto in cui serve il tuo ok. Invece di aspettarti con
la sessione aperta, Claude aggiorna `HANDOFF.md`, ti manda la domanda sul telefono e si ferma.
Tu rispondi quando puoi, anche con un bottone. Un giro ogni 2 minuti legge la risposta e fa
ripartire Claude Code nella cartella del progetto, con la tua risposta nel prompt e l'ordine di
rileggere `HANDOFF.md`.

Da me la domanda arriva su WhatsApp e la risposta la raccoglie un servizio sul server. Per il PC
ho scelto le notifiche push di **ntfy**, un servizio pubblico con app gratuita per Android e
iPhone (https://ntfy.sh), perché non richiede account né server. Puoi anche usare un server ntfy tuo.

**Richiede.** Python 3, Claude Code, l'app ntfy sul telefono, il PC acceso e sveglio.

**Prima di tutto, quando non ti serve.** Se la tua versione di Claude Code ti permette già di
seguire e comandare la sessione dal telefono (controllo remoto o notifiche dell'app ufficiale),
usa quello: è più semplice e non passa da un servizio in più. Questo pacchetto serve quando vuoi
che il lavoro riparta da solo, senza riaprire niente.

**Dove si copia.**
1. `ponte_telefono.py` in `~/.claude/ponte/`.
2. `commands/chiedi-ok.md` in `~/.claude/commands/`: il comando `/chiedi-ok` dice a Claude come
   fermarsi bene (prima HANDOFF.md, poi la domanda, poi stop).
3. `python3 ~/.claude/ponte/ponte_telefono.py configura`: crea `~/.claude/ponte/config.json` con
   un argomento casuale. Nell'app ntfy iscriviti a quell'argomento. Le risposte libere si
   pubblicano sull'argomento con `-risposte` in fondo.
4. Pianifica ogni 2 minuti `python3 ~/.claude/ponte/ponte_telefono.py giro` (Utilità di
   pianificazione su Windows, launchd o cron su Mac).
5. Facoltativo: se hai il pacchetto `automazioni-semaforo-consumi`, il giro non fa ripartire
   niente quando il semaforo è rosso.

**Sicurezza, da leggere.**
- Su ntfy.sh chi conosce il nome dell'argomento può leggere le domande e scrivere risposte. Per
  questo il nome è lungo e casuale, e ogni domanda ha un codice: una risposta senza il codice
  giusto si ignora. Non condividere il nome e non scriverlo in chat.
- Nelle domande niente password, chiavi, dati di clienti. Scrivi cosa approvi, non i dati.
- Se usi un server ntfy tuo con accesso protetto, metti `server` e `token` in `config.json`.
- La ripartenza gira con `--permission-mode acceptEdits`: modifica i file del progetto, ma i
  comandi che chiedono permesso vengono negati. Non metterla su `bypassPermissions`.

**Come si prova (su dati finti, senza rete).**
1. `python3 ponte_telefono.py configura --canale file` con una home di prova.
2. `chiedi prova-1 "Vado avanti?" --cartella <cartella di prova>`: la domanda finisce in
   `~/.claude/ponte/uscita/<codice>.txt`.
3. Scrivi in `~/.claude/ponte/risposte-finte.txt` una riga con un codice sbagliato: `giro` deve
   dire «Nessuna risposta nuova». Poi una riga `<codice giusto> sì`: `giro --prova` mostra il
   prompt, `giro` lancia Claude Code (o un `claude` finto con `--claude <percorso>`).
4. `stato` deve dire `ripartita`.

Io l'ho provato così, con il canale finto e un `claude` finto, il 27/11/2026. Il canale ntfy non
l'ho provato da un PC: il codice segue la documentazione pubblica di ntfy (pubblicazione con
POST, bottoni con l'intestazione `Actions`, lettura con `/json?poll=1`).

**Come si toglie.** Togli l'attività pianificata, cancella `~/.claude/ponte/` e il comando
`chiedi-ok.md`. Nell'app ntfy togli l'iscrizione all'argomento.

## English

When a long job reaches a checkpoint, Claude updates the HANDOFF, sends you a push notification (ntfy app, with Yes/No buttons) explaining what happens on each answer, and stops. A run every 2 minutes reads your reply and restarts Claude Code in the project folder with your answer in the prompt, one restart at a time.

Install: copy `ponte_telefono.py` into `~/.claude/ponte/` and `commands/chiedi-ok.md` into `~/.claude/commands/`, run `python3 ponte_telefono.py configura`, subscribe to the topic in the ntfy app, then schedule `ponte_telefono.py giro` every 2 minutes. Don't send sensitive data through it: on ntfy.sh anyone who knows the topic name can read it.
