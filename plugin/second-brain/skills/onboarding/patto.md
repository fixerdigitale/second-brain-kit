# Fase 0 — Il patto (testi e regole deny)

Il patto dura 2-4 minuti. Si legge alla persona nella sua lingua, con il tono più basso (T0), perché
alla fase 0 il tono non si conosce ancora. Chi è esperto lo capisce subito e può scrivere
`più veloce`.

## Testo del patto

### IT

> Ti propongo un giro di 30-45 minuti, che di solito si fa in 2-3 volte. Prima facciamo insieme
> un lavoro vero, poi ti mostro una mappa di quello che hai e al massimo 3 passi per migliorarlo.
>
> **Cosa guardo.** Nelle cartelle Documenti, Scrivania, Download (sul disco spesso si chiamano
> `Documents`, `Desktop`, `Downloads`, e su Windows possono stare dentro OneDrive) e nella cartella
> di Claude leggo **solo i nomi** dei file e delle cartelle, quanti sono e quando sono cambiati.
> Apro il contenuto solo della cartella di Claude (le istruzioni, la memoria, le skill; delle
> impostazioni leggo solo i nomi) e della cartella di lavoro che mi dici tu. Se vuoi, restringo a
> cartelle precise.
>
> **Cosa non faccio mai da solo.** Non apro browser, email o chat. Non copio password o chiavi: uno
> script le cerca e mi dice solo in che file e riga sono, e quei file non li apro, né io né gli
> assistenti che lancio per controllare. Non scrivo, sposto o cancello niente senza un tuo sì, per
> ogni voce o per un gruppo che ti mostro per intero. Prima faccio una copia con la data, poi scrivo,
> poi rileggo: non sposto né cancello un file prima che quello nuovo sia scritto e riletto. Se il
> programma mi blocca un comando o una scrittura, mi fermo e te lo dico: non provo un'altra strada
> senza un tuo sì su quella strada. Non pubblico, non condivido, non installo niente preso da fuori
> senza un controllo e un tuo sì. Non mando niente a nessuno.
>
> **Dove passa quello che leggo.** Quello che leggo, compresi i nomi delle cartelle, passa da Claude
> come ogni conversazione: vale la privacy del tuo account Anthropic. Il kit non aggiunge nessun
> altro invio.
>
> **Dove scrivo.** Solo nella cartella `second-brain/` dentro la tua cartella di lavoro: lo stato
> del giro, la mappa, il piano e i risultati. Tutto il resto con il tuo sì. Se la cartella di lavoro
> è sincronizzata (OneDrive, iCloud, Dropbox, Google Drive) o ha una copia online, quello che scrivo
> lì finisce anche online: te lo dico prima e scegliamo insieme.
>
> **Cosa parte da solo.** Un controllo all'apertura di Claude: fra 14 giorni ti propone, una volta
> sola, di rifare le misure; prima non fa niente. Le altre procedure del kit (per esempio «salva in
> memoria», che prima di scrivere ti mostra cosa e dove e aspetta il sì) non si accendono da sole:
> le apro io durante il giro, quando servono, oppure le chiami tu con `/second-brain:<nome>`.
>
> Su Mac il sistema può chiederti con una finestra se Claude può accedere a Scrivania, Documenti o
> Download. Se dici «Non consentire», quelle cartelle le vedo come chiuse, non come vuote.
>
> **Come mi fermi.** Premi Esc, oppure scrivi «fermati». Scrivi `salta` per saltare un passo,
> `più piano` o `più veloce` per cambiare ritmo.
>
> Va bene così? Se preferisci, dimmi quali cartelle guardare.

Se la persona non ha ancora scritto niente, sotto il testo va la riga che offre l'altra lingua
(`SKILL.md`, «Lingua»): «*(If you'd rather do this in English, just reply in English.)*»

### EN

> I suggest a walk-through of 30-45 minutes, usually done in 2-3 sittings. First we do a real piece
> of your work together, then I show you a map of what you have and at most 3 steps to improve it.
>
> **What I look at.** In Documents, Desktop, Downloads (on Windows they may live inside OneDrive)
> and the Claude folder I read **only the names** of files and folders, how many there are and when
> they changed. I open the content only of the Claude folder (instructions, memory, skills; of the
> settings I read only the names) and of the work folder you tell me. If you prefer, I limit this to
> specific folders.
>
> **What I never do on my own.** I don't open browsers, email or chats. I don't copy passwords or
> keys: a script looks for them and only tells me the file and line, and those files stay closed,
> for me and for the helpers I start to check things. I don't write, move or delete anything without
> your yes, for each item or for a group I show you in full. First a dated copy, then the write, then
> a re-read: I don't move or delete a file before the new one is written and checked. If the program
> blocks a command or a write, I stop and tell you: I don't try another way without your yes on that
> way. I don't publish, share or install anything from outside without a check and your yes. I don't
> send anything to anyone.
>
> **Where what I read goes.** What I read, folder names included, goes through Claude like any
> conversation: your Anthropic account's privacy applies. The kit adds no other sends.
>
> **Where I write.** Only in the `second-brain/` folder inside your work folder: the progress state,
> the map, the plan and the results. Everything else with your yes. If the work folder is synced
> (OneDrive, iCloud, Dropbox, Google Drive) or has an online copy, what I write there goes online too:
> I'll tell you first and we choose together.
>
> **What runs on its own.** A check when Claude opens: in 14 days it offers, once, to redo the
> measures; until then it does nothing. The kit's other procedures (for example "save to memory",
> which shows you what and where before writing and waits for your yes) don't switch on by
> themselves: I open them during the walk-through when they're needed, or you call them with
> `/second-brain:<name>`.
>
> On a Mac the system may ask you in a window whether Claude can access Desktop, Documents or
> Downloads. If you say "Don't Allow", I'll see those folders as closed, not as empty.
>
> **How to stop me.** Press Esc, or type "stop". Type `skip` to skip a step, `slower` or `faster` to
> change pace.
>
> Is this ok? If you prefer, tell me which folders to look at.

If the person hasn't written anything yet, add the line offering the other language below the text:
«*(Se preferisci l'italiano, rispondimi in italiano.)*»

## Regole fisse che il patto promette (valgono in ogni fase)

Sono le regole ferme 12-15 di `SKILL.md`, qui per esteso perché il patto le promette alla persona:

1. **Comando o scrittura negata da Claude Code.** Ti fermi e lo dici in chat, in parole semplici:
   cosa volevi fare, che è stato bloccato, le strade possibili. Non rifai la stessa operazione con
   un altro strumento (python3, Write, Edit, un'altra shell, un comando diverso con lo stesso
   effetto) senza un sì esplicito della persona su quella strada. EN: «The program blocked <what>. I
   won't try another way on my own. Options: <a>, <b>. Which one, or neither?»
2. **Prima copia, poi scrivi, poi rileggi.** Mai spostare o cancellare un file prima di aver scritto
   e riletto quello nuovo.
3. **File esclusi, anche per i sotto-agenti.** I file segnalati da `cerca-segreti` e quelli che la
   persona esclude non si aprono: niente Read, niente Grep in modo `content`, da te o da qualsiasi
   sotto-agente. Ogni sotto-agente riceve l'elenco.
4. **Dire il vero su cosa è stato aperto.** Mai «non ho aperto quel file» se non è vero; se un
   sotto-agente l'ha aperto, lo dici.

## Le tre domande dopo il sì (una alla volta)

1. **Cartella di lavoro** (prima di scrivere qualsiasi cosa, anche lo stato). «La cartella dove
   lavori di solito è `<nome della cartella aperta adesso>`?» Al tono T0 (che alla fase 0 vale per
   tutti) usa il nome della cartella e dove sta in parole («la cartella `Notes`, dentro la tua
   cartella personale»), non il percorso assoluto; il percorso intero solo se la persona lo chiede o
   scrive da esperta. Non proporre mai come cartella di lavoro la
   cartella personale intera, la Scrivania, Download o Documenti interi (anche dentro OneDrive). Se la
   cartella aperta è una di queste, chiedi di aprirne una dedicata (per esempio
   `Documents/Lavoro`). EN: «Is `<folder name>` the folder where you usually work?»
   **Cartella sincronizzata o con copia online.** Se il percorso contiene `OneDrive`, `iCloud`,
   `Mobile Documents`, `Dropbox`, `Google Drive` o `My Drive`, oppure la cartella è sotto git con un
   remoto (Glob `.git/config`, cerca `[remote`), dillo in due righe: «Questa cartella ha una copia
   online: anche la mappa e il piano finirebbero lì. Nella mappa scrivo quante chiavi ho trovato, ma
   non dove: il dove te lo dico solo qui in chat.» Con git, proponi anche (con il sì) di aggiungere
   `second-brain/` e `*.bak-*-second-brain` a `.git/info/exclude`: vale solo su questo PC e non tocca
   i file già salvati. Se una chiave sta già in un file sincronizzato o salvato online, va cambiata
   alla fonte (scheda `sicurezza-chiave-finita-online`). EN: «This folder has an online copy: the map
   and plan would end up there too. In the map I'll write how many keys I found, not where: where, I
   only tell you here in the chat.»
2. **Cartelle chiuse a chiave.** Proponi le regole deny qui sotto, con una riga di spiegazione:
   «Ti propongo di chiudere a chiave alcune cartelle dove di solito stanno password e chiavi:
   Claude non potrà aprirle nemmeno per sbaglio. Si tolgono quando vuoi.» EN: «I suggest locking a
   few folders where passwords and keys usually live: Claude won't be able to open them even by
   mistake. You can remove this any time.» Applica solo con il sì (vedi sotto).
3. **Sessioni passate (facoltativo).** «Posso guardare le tue conversazioni con Claude delle ultime
   2 settimane, solo quelle aperte in questa cartella? Prendo solo conteggi e temi, mai il testo
   intero; password, email e numeri li oscura lo script prima che li veda. Mi aiuta a capire cosa
   rifai spesso. Puoi dire di no: il giro funziona lo stesso.» EN: «May I look at your Claude
   conversations from the last 2 weeks, only the ones opened in this folder? I only take counts and
   topics, never the full text; the script hides passwords, emails and numbers before I see them. It
   helps me see what you do often. You can say no: everything still works.»

In T2-T3, o dopo `più veloce`, le domande 2 e 3 possono stare in un messaggio solo, con la scelta
proposta accanto («2: sì, le chiudo · 3: no, se non mi dici altro»).

Salva le risposte in una chiamata sola: `stato.py imposta-molti consensi.<campo>=<valore>
consensi.<campo2>=<valore2>`.

## Regole deny proposte

Da aggiungere in `~/.claude/settings.json` → `permissions.deny`, **senza togliere niente** di quello
che c'è. Si fa con lo script, che non stampa il file (dentro ci possono essere chiavi nelle variabili
d'ambiente):

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/config_claude.py" aggiungi-deny --prova
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/config_claude.py" aggiungi-deny
```

Lo script fa la copia `settings.json.bak-AAAAMMGG-second-brain` (con l'ora `-HHMM` se esiste già;
non sovrascrive mai una copia), si ferma se il file non è JSON valido, aggiunge solo le righe che
mancano e rilegge. Sceglie da solo le righe del sistema (Mac, Windows, Linux). Senza Python: fai a mano
gli stessi passi, ma non stampare il file in chat. L'elenco (è lo stesso dentro lo script):

```json
[
  "Read(~/.ssh/**)",
  "Read(~/.aws/**)",
  "Read(~/.gnupg/**)",
  "Read(~/.config/gcloud/**)",
  "Read(~/.config/gh/**)",
  "Read(~/.kube/**)",
  "Read(~/.docker/config.json)",
  "Read(~/.netrc)",
  "Read(~/.npmrc)",
  "Read(**/.env)",
  "Read(**/.env.*)",
  "Read(~/Library/Keychains/**)",
  "Read(~/Library/Application Support/Google/Chrome/**)",
  "Read(~/Library/Application Support/Firefox/Profiles/**)",
  "Read(~/Library/Safari/**)",
  "Read(~/.config/google-chrome/**)",
  "Read(~/.mozilla/firefox/**)",
  "Read(~/AppData/Local/Google/Chrome/User Data/**)",
  "Read(~/AppData/Local/Microsoft/Edge/User Data/**)",
  "Read(~/AppData/Roaming/Mozilla/Firefox/Profiles/**)",
  "Read(~/AppData/Roaming/Microsoft/Credentials/**)"
]
```

- Le regole `Read(...)` valgono anche per la ricerca nei file (Glob, Grep). Non fermano un comando
  di terminale come `cat`: per questo il patto dice anche che i segreti non si leggono, e lo script
  `cerca-segreti` stampa solo nomi. Il token di `gh` resta usabile dal programma `gh`: la regola
  impedisce solo a Claude di leggerne il file.
- Su un sistema metti solo le righe che lo riguardano (Mac: `~/Library/...`; Windows:
  `~/AppData/...`; Linux: `~/.config/...`, `~/.mozilla/...`). Le righe comuni vanno su tutti.
- Dopo la scrittura, rileggi il file e controlla che sia JSON valido.
- Come si toglie: si cancellano solo le righe aggiunte, oppure si rimette la copia datata.
- Se Claude Code nega la scrittura (o il comando dello script), regole fisse qui sopra: ti fermi e
  lo dici. Le strade da proporre: rispondere sì alla finestra del permesso quando ricompare, oppure il
  comando `/permissions` dentro Claude Code. Non chiedere alla persona di aprire il file a mano con un
  editor, e non riprovare con un altro strumento senza il suo sì.
- In T0 non mostrare il JSON: di' quali cartelle chiudi, a parole («le chiavi di accesso del
  computer, i file delle password dei programmi, i profili dei browser»).
