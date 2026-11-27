# Fatti da chat e vocali verso il vault

**Cosa fa.** Due pezzi, uno meccanico e uno di giudizio.
- `raccogli_chat.py` legge le esportazioni delle chat WhatsApp che salvi in una cartella, tiene solo le
  chat di lavoro che hai scritto in un elenco e solo gli ultimi giorni, e scrive un file unico. Se hai
  `faster-whisper`, trascrive anche i vocali sul tuo PC; può trascrivere pure una cartella di tuoi memo vocali.
  Niente AI che decide, niente rete.
- La skill `fatti-del-giorno` legge quel file, propone i fatti (decisioni, accordi, date, numeri, chi deve
  muoversi) con la nota di destinazione, e scrive nel vault solo le voci che approvi.

**Dove si copia.**
1. `raccogli_chat.py` fuori dal vault, per esempio in `~/.claude/strumenti/`.
2. `fatti-del-giorno/` in `~/.claude/skills/fatti-del-giorno/`. Nel `SKILL.md` sostituisci `<cartella-vault>`.
3. Crea `chat-di-lavoro.txt` con i nomi delle chat, uno per riga, scritti come compaiono in WhatsApp.
   Le chat che non sono nell'elenco restano fuori: è voluto, così la famiglia e gli amici non entrano mai.

**Come si usa.**
1. Dal telefono: chat → menu → Altro → Esporta chat (con o senza media). Salva i file in una cartella, per
   esempio `~/Chat-esportate/`. Ogni esportazione è una fotografia: per avere i messaggi nuovi va rifatta.
2. `python3 raccogli_chat.py --chat ~/Chat-esportate --solo chat-di-lavoro.txt --giorni 1 --out <cartella-vault>/Fonti/chat/AAAA-MM-GG.md`
   - aggiungi `--vocali` per trascrivere gli audio (prima: `pip install faster-whisper`; la prima volta scarica il modello);
   - aggiungi `--memo <cartella>` per i tuoi memo vocali.
3. In Claude Code: «fatti del giorno».

**Come si prova.** Esporta una chat di lavoro con due o tre messaggi di oggi, mettila nell'elenco e lancia lo
script senza `--out`: dovresti vedere i messaggi di oggi e nessun'altra chat. Poi una chat che non è nell'elenco:
non dovrebbe comparire.

**Cosa non ho provato.** Ho provato lo script con esportazioni finte nei due formati (Android e iPhone) e con
una password nel testo, che esce oscurata. La trascrizione dei vocali con faster-whisper sul PC non l'ho
provata: da me la stessa libreria gira sul server. Su un PC lento il modello `small` è il compromesso;
`large-v3-turbo` è più preciso ma più lento. Il formato delle esportazioni di WhatsApp può cambiare.

**Attenzione.** Il file di raccolta contiene parole di altre persone: tienilo fuori da un vault che va su
GitHub o su un Drive condiviso, oppure escludi `Fonti/chat/` con `.gitignore`.

**Come si toglie.** Cancella lo script, la cartella della skill e, se non ti servono, `Fonti/chat/`. Le note scritte restano.

**Differenza con il mio.** Da me la raccolta gira ogni notte alle 4:00 su un server, prende i messaggi
direttamente dal collegamento WhatsApp, entra nei gruppi solo quando vengo taggato (un'ora prima e un'ora
dopo il tag), unisce anche altre fonti di lavoro, e un agente scrive il diario dei fatti alle 4:30. Una raccolta
che trova zero chat di lavoro in un giorno feriale la tratto come errore, non come giornata vuota.

## English

Two pieces to bring decisions from chats and voice notes into your vault. `raccogli_chat.py` reads WhatsApp chat exports, keeps only the chats on your allow-list (`chat-di-lavoro.txt`) and transcribes voice notes locally with faster-whisper. The `fatti-del-giorno` skill proposes dated facts with their destination note and writes only the ones you approve.

Install: copy `raccogli_chat.py` into `~/.claude/strumenti/` and `fatti-del-giorno/` into `~/.claude/skills/fatti-del-giorno/`, write your allow-list, export the chats from your phone and run the script as described above. Then ask Claude for "fatti del giorno". Exports are manual; don't archive chats of people who haven't agreed.
