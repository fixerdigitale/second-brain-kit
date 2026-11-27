# Permessi: cosa Claude può fare da solo, cosa chiede, cosa non fa mai

Modello di `settings.json` con tre liste.

**Cosa uso io e cosa è nuovo.** Nel mio `settings.json` ci sono solo due liste: `allow` e `deny`. La lista `ask` di questo modello è una proposta nuova, scritta per il kit: non la uso così. L'ho aggiunta perché su un PC, senza gli altri controlli che ho sul server, mi sembra la via di mezzo più comoda per le azioni difficili da annullare. Se non ti serve, cancellala. Nella modalità normale quello che non è in `allow` ti chiede già il permesso; da quanto so `ask` conta di più quando una regola `allow` larga coprirebbe anche un comando delicato, o nelle modalità che chiedono meno. Provalo con `/permissions` sulla tua versione.

- **allow**: comandi di sola lettura che passano senza chiedere (meno interruzioni).
- **ask**: azioni che si possono annullare a fatica (push, cancellazioni, installazioni, download): Claude Code chiede ogni volta.
- **deny**: cose che non deve fare mai, neanche se glielo chiedi per sbaglio: leggere file di segreti e chiavi SSH, `rm -rf`, `git push --force`.

## Dove si copia

- Per tutti i progetti: `~/.claude/settings.json` (Mac) o `%USERPROFILE%\.claude\settings.json` (Windows).
- Solo per un progetto: `<tuo-progetto>/.claude/settings.json`.

Se il file esiste già, copia solo il blocco `"permissions"` e unisci le liste a mano.
Se tieni le chiavi in una cartella precisa, aggiungi a `deny` una riga `Read(<quella cartella>/**)` con il percorso vero (nel modello non c'è, per non lasciare un segnaposto che resterebbe scritto così).

Sintassi dei percorsi: `~/` = cartella utente, `./` = cartella del progetto, `//` = percorso assoluto (`//Users/nome/...`).

## Come si prova

1. Apri una sessione nuova di Claude Code nel progetto.
2. Chiedi «leggi il file .env»: deve rifiutare.
3. Chiedi «fai git push»: deve chiederti il permesso.
4. Scrivi `/permissions` per vedere le regole caricate.

## Come si toglie

Cancella il blocco `"permissions"` (o le singole righe) dal `settings.json` e riapri la sessione.

## Nota

Il `deny` non è una cassaforte: blocca gli strumenti di Claude Code, ma un comando di shell inventato può comunque leggere un file.
Per questo `cat`, `head`, `tail` e `grep` non sono in `allow` (con loro liberi, un `cat .env` passerebbe senza domanda anche con il `deny` su `Read(./.env)`), e in `deny` ci sono anche `Bash(cat *.env*)` e simili. Restano modi per aggirarli: è una seconda difesa, non una cassaforte.
I segreti veri vanno tenuti fuori dalle cartelle su cui lavora Claude, e il deny è la seconda difesa.
`find` non è in `allow` apposta: con `-delete` o `-exec` cancella o lancia comandi.

## English

A `permissions` block for Claude Code's settings.json: allow read-only commands without prompts, always deny reading your secrets file, credentials folder and SSH keys, and (a new proposal I don't use this way) ask before actions that are hard to undo, like push, deletes, installs and downloads.

Install: copy the `permissions` block from `settings.json` into `~/.claude/settings.json` (all projects) or `<your-project>/.claude/settings.json`, add a `Read(<your secrets folder>/**)` line to deny if you keep keys in a specific folder, then check with `/permissions`. `cat`, `head`, `tail` and `grep` are not in allow on purpose. Deny stops Claude's tools, not every shell command: keep secrets outside work folders too.
