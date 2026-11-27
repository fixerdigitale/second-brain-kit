# Controlli di salute che avvisano solo quando cambia lo stato

- `controlli.py`: fa i controlli scritti in `controlli.json` e manda una notifica del sistema **solo** quando qualcosa si rompe o torna a posto. Se resta rotto, non ti riavvisa a ogni giro.
- `controlli.json`: l'elenco dei controlli, con tre esempi da cambiare.

L'idea: guardare il risultato, non se una cosa è partita. Un backup «partito» non vuol dire un backup fatto; una pagina che risponde 200 può avere uno script rotto e restare bianca per chi la apre.

## Tre tipi di controllo

| tipo | cosa guarda | esempio |
|---|---|---|
| `url` | la pagina risponde 200; con `file_collegati` anche script, css e immagini dello stesso dominio | il tuo sito, una landing |
| `file_recente` | il file esiste, è più giovane di `ore_max` e contiene un testo | `ultimo-backup.txt` del pacchetto `sicurezza-backup-notturno`, che deve dire `ESITO: OK` |
| `comando` | un comando esce con codice 0 | `git status` sul vault, un tuo script di verifica |

Il comando si scrive come lista (`["git", "-C", "...", "status"]`): non passa dalla shell.

## Dove si copia

1. Metti la cartella dove vuoi, per esempio `<cartella-vault>/strumenti/controlli-salute/`.
2. Apri `controlli.json`, cambia i segnaposto `<...>` e togli i controlli che non ti servono.
3. Stato e registro finiscono in `~/.controlli-salute/` (si cambia con `file_stato`).

## Come si prova

1. `python3 controlli.py --prova` (Windows: `py controlli.py --prova`): stampa OK o ROTTO per ogni riga, senza avvisare.
2. Per vedere un avviso vero, metti un indirizzo che non esiste (`https://esempio.invalid/`) e lancia `python3 controlli.py` due volte: la prima avvisa «ROTTO», la seconda no. Rimetti l'indirizzo giusto e rilancia: avvisa «di nuovo ok». Poi togli la riga di prova.

## Farlo girare da solo

Ogni ora va bene; più spesso serve solo per cose che ti costano soldi se restano giù.

**Mac** (launchd), `~/Library/LaunchAgents/local.controlli-salute.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>local.controlli-salute</string>
  <key>ProgramArguments</key><array>
    <string>/usr/bin/python3</string><string>/Users/<tuo-utente>/<cartella-vault>/strumenti/controlli-salute/controlli.py</string>
  </array>
  <key>StartInterval</key><integer>3600</integer>
</dict></plist>
```
poi `launchctl load ~/Library/LaunchAgents/local.controlli-salute.plist`.

**Windows** (PowerShell):
```powershell
schtasks /Create /SC HOURLY /TN "Controlli di salute" /TR "py C:\<cartella-vault>\strumenti\controlli-salute\controlli.py"
```

Gira solo a PC acceso: se il PC è spento non controlla niente, e lo dico apposta. Per controllare un sito anche quando dormi serve un servizio esterno di monitoraggio o un server.

## Come si toglie

Mac: `launchctl unload ~/Library/LaunchAgents/local.controlli-salute.plist` e cancella il file. Windows: `schtasks /Delete /TN "Controlli di salute"`. Poi cancella la cartella e `~/.controlli-salute/`.

## English

`controlli.py` runs the checks you list in `controlli.json` (URLs that must answer, files that must be recent, commands that must succeed) and sends a system notification only when a check's state changes: once when it breaks, once when it recovers.

Install: write your checks in `controlli.json`, test them with `python3 controlli.py --prova`, then schedule `controlli.py` every hour. It only runs while the PC is on: for sites that must stay up at night use an external monitor.
