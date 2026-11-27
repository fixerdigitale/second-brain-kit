# Backup notturno del vault (PC)

`backup_vault.py` fa due copie del vault ogni volta che gira:

1. **git**: commit e push sul tuo repo GitHub privato (la storia di ogni file);
2. **cloud**: uno zip datato nella cartella che Google Drive / OneDrive / iCloud sincronizzano sul PC. Ne tiene 7, le più vecchie le cancella.

Due freni: se fra i file da salvare ce n'è uno che sembra una chiave (`.env`, `.pem`, `id_rsa`…) il commit si ferma, e quei file non entrano nello zip; se hai `gh` e il repo risulta pubblico, il push si ferma.

Così hai la regola 3-2-1: il vault sul PC, la copia su GitHub, la copia su Drive (due servizi diversi, entrambi fuori casa).

## Dove si copia

1. Metti lo script dove vuoi, per esempio `<cartella-vault>/strumenti/backup_vault.py` (git ne terrà la storia).
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

## Come si prova

1. Lancialo a mano: `python3 backup_vault.py` (Windows: `py backup_vault.py`).
2. L'ultima riga deve dire `ESITO: OK`.
3. Controlla su GitHub che ci sia il commit «Backup automatico…» e nella cartella Drive lo zip nuovo.
4. Poi fai la prova di ripristino (pacchetto `sicurezza-prova-ripristino`): un backup mai riaperto non è un backup.

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

Mac: `launchctl unload ~/Library/LaunchAgents/local.backup-vault.plist` e cancella il file. Windows: `schtasks /Delete /TN "Backup vault"`. Poi cancella lo script; gli zip su Drive restano finché non li cancelli.

## English

`backup_vault.py` backs up a notes vault: commit and push to a private GitHub repo, plus a dated zip in a cloud-synced folder, keeping the last 7. It stops if a file looks like a key or the repo turns out to be public, and writes its outcome to `ultimo-backup.txt`. This guide also has restic commands for encrypted backups of sensitive data.

Install: change the two lines at the top of `backup_vault.py`, run it by hand, then schedule it every evening with launchd (Mac) or Task Scheduler (Windows). The zip isn't encrypted: for client data use restic.
