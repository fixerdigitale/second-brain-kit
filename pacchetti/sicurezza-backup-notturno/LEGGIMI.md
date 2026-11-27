# Backup notturno del vault (PC)

`backup_vault.py` fa due copie del vault ogni volta che gira:

1. **git**: commit e push sul tuo repo GitHub privato (la storia di ogni file);
2. **cloud**: uno zip datato nella cartella che Google Drive / OneDrive / iCloud sincronizzano sul PC. Le copie oltre le ultime 7 le cancella solo se glielo dici (`--ruota`, oppure «s» quando lo lanci a mano); altrimenti ti dice quante sono.

Tre freni:
- **segreti**: prima del commit passa i file pronti a `cerca_segreti.py`, che guarda il nome e il contenuto (token di GitHub, chiavi di Anthropic e OpenAI, chiavi private, righe con `password: …` e simili). Se trova qualcosa toglie tutto dal commit, si ferma e stampa solo `file:riga:tipo`, mai il valore. Gli stessi file restano fuori dallo zip. Si ferma anche per i file che nel nome hanno `.env`, `.pem`, `id_rsa`, `credentials`, `secrets`, `accessi`, `password` o `token`;
- **repo pubblico**: il push parte solo se `gh` conferma che il repo su GitHub non è pubblico. Senza `gh`, o senza il login di `gh`, il push si ferma e il commit resta sul PC. Se sei sicuro che il repo è privato, puoi lanciarlo con `--push-senza-verifica`: si ferma comunque se `gh` dice che è pubblico;
- **niente controllo, niente backup**: `cerca_segreti.py` sta già in questa cartella (è la stessa versione del plugin `second-brain`). Se manca, lo script non salva niente e lo scrive nell'esito.

I controlli riconoscono le forme più comuni, non tutte: un segreto scritto in un modo strano può passare. I segreti veri li tengo in un gestore di password, fuori dal vault.

Così hai la regola 3-2-1: il vault sul PC, la copia su GitHub, la copia su Drive (due servizi diversi, entrambi fuori casa).

## Dove si copia

1. Metti `backup_vault.py` e `cerca_segreti.py` **insieme** dove vuoi, per esempio in `<cartella-vault>/strumenti/` (git ne terrà la storia).
2. Apri lo script e cambia le due righe `CARTELLA_VAULT` e `CARTELLA_CLOUD`.
3. Il vault deve già avere `git remote` verso GitHub e il push deve funzionare senza password (chiave SSH o login di GitHub Desktop / `gh auth login`).

## Farlo girare da solo, ogni sera

Gira solo a PC acceso. Se il PC è spento all'ora fissata, salta quel giro.

**Mac** (launchd): crea `~/Library/LaunchAgents/local.backup-vault.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>local.backup-vault</string>
  <key>ProgramArguments</key><array>
    <string>/usr/bin/python3</string><string>/Users/<tuo-utente>/<cartella-vault>/strumenti/backup_vault.py</string>
  </array>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>21</integer><key>Minute</key><integer>0</integer></dict>
</dict></plist>
```
poi `launchctl load ~/Library/LaunchAgents/local.backup-vault.plist`. launchd lo recupera al risveglio se il Mac dormiva.

**Windows** (Utilità di pianificazione), da PowerShell:
```powershell
schtasks /Create /SC DAILY /ST 21:00 /TN "Backup vault" /TR "py C:\<cartella-vault>\strumenti\backup_vault.py"
```
Nelle proprietà dell'attività spunta «Esegui l'attività il prima possibile dopo un avvio pianificato mancato».

Quando gira da solo nessuno può rispondere alle domande: se vuoi che cancelli da solo le copie zip oltre le 7, aggiungi `--ruota` in fondo al comando (nel plist, una riga `<string>--ruota</string>` dopo il percorso dello script).

## Come si prova

1. Lancialo a mano: `python3 backup_vault.py` (Windows: `py backup_vault.py`).
2. L'ultima riga deve dire `ESITO: OK`. Se dice `push FERMATO`, leggi il motivo nella riga sopra (repo pubblico, oppure `gh` che non risponde).
3. Controlla su GitHub che ci sia il commit «Backup automatico…» e nella cartella Drive lo zip nuovo.
4. Prova il freno dei segreti, su una cartella finta e non sul vault vero: un file con una riga `GITHUB_TOKEN=ghp_` seguita da 36 lettere e cifre inventate. Il commit deve fermarsi e l'esito deve citare quel file con `token-github`, senza il valore.
5. Poi fai la prova di ripristino (pacchetto `sicurezza-prova-ripristino`): un backup mai riaperto non è un backup.

## Se dentro ci sono dati delicati: restic

Lo zip non è cifrato. Se nel vault hai dati di clienti, usa [restic](https://restic.net) (gratis, Mac e Windows): backup cifrato e deduplicato.
È quello che uso sul server, con 7 copie giornaliere, 4 settimanali e 6 mensili:
```
restic -r "<cartella-cloud>/restic-vault" init
restic -r "<cartella-cloud>/restic-vault" backup "<cartella-vault>" --exclude .git
restic -r "<cartella-cloud>/restic-vault" forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune
```
La password di restic va in un gestore di password, **non** nel vault né su Drive: senza di lei il backup non si apre.

## Come si toglie

Mac: `launchctl unload ~/Library/LaunchAgents/local.backup-vault.plist` e cancella il file. Windows: `schtasks /Delete /TN "Backup vault"`. Poi cancella i due script; gli zip su Drive restano finché non li cancelli.

Io l'ho provato il 27/11/2026 su dati finti, con un remote git locale al posto di GitHub: token finto fermato nel commit e tenuto fuori dallo zip, push fermato senza `gh`, copie vecchie cancellate solo con `--ruota`. Su Mac e Windows non l'ho provato.

## English

`backup_vault.py` backs up a notes vault: commit and push to a private GitHub repo, plus a dated zip in a cloud-synced folder. It writes its outcome to `ultimo-backup.txt`. This guide also has restic commands for encrypted backups of sensitive data.

Three brakes:
- **secrets**: before the commit it runs the staged files through `cerca_segreti.py` (name and content: GitHub tokens, Anthropic and OpenAI keys, private keys, `password: …` lines and similar). If something turns up it unstages everything, stops and prints only `file:line:type`, never the value; the same files stay out of the zip. It also stops on file names containing `.env`, `.pem`, `id_rsa`, `credentials`, `secrets`, `accessi`, `password` or `token`;
- **public repo**: it pushes only if `gh` confirms the GitHub repo isn't public. Without `gh`, or without `gh` logged in, the push stops and the commit stays on the PC. If you're sure the repo is private you can run it with `--push-senza-verifica`; it still stops if `gh` says the repo is public;
- **no check, no backup**: `cerca_segreti.py` is already in this folder (same version as the `second-brain` plugin). If it's missing, the script saves nothing and says so in the outcome.

Old zips beyond the last 7 are deleted only with `--ruota` (or if you answer "s" when running it by hand); otherwise it just tells you how many there are. The checks recognise common forms, not all of them: I keep real secrets in a password manager, outside the vault.

Install: copy `backup_vault.py` and `cerca_segreti.py` together, change the two lines at the top of `backup_vault.py`, run it by hand, then schedule it every evening with launchd (Mac) or Task Scheduler (Windows), adding `--ruota` if you want old zips deleted automatically. The zip isn't encrypted: for client data use restic. I tested it on 27/11/2026 on dummy data with a local git remote instead of GitHub; not tested on Mac or Windows.
