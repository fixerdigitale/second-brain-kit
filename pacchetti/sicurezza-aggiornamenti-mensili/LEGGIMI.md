# Aggiornamenti mai automatici: un controllo al mese, poi decido io

`controlla_aggiornamenti.py` guarda una volta al mese gli strumenti presi da fuori e scrive una nota con cosa è cambiato a monte. **Non aggiorna niente.**

Guarda:
- le skill installate con `git clone` in `~/.claude/skills/` (e le cartelle che aggiungi in `CARTELLE_EXTRA`): quanti commit nuovi ci sono e quali file «sensibili» cambiano (hook, script di installazione, impostazioni, file che lanciano comandi);
- se hai npm, i pacchetti globali con una versione nuova (`npm outdated -g`).

L'unica cosa che tocca è `git fetch`: scarica la storia nuova accanto alla tua, ma i file che usi restano com'erano.

## Dove si copia

1. Metti lo script dove vuoi, per esempio `<cartella-vault>/strumenti/controlla_aggiornamenti.py`.
2. Cambia `CARTELLA_NOTE` (dove finiscono le note mensili) e, se serve, `CARTELLE_EXTRA`.

## Come si prova

`python3 controlla_aggiornamenti.py` (Windows: `py controlla_aggiornamenti.py`). Deve dire `Nota scritta: …` e nella nota trovi una sezione per ogni cartella. Controlla con `git -C <cartella-skill> status` che i file non siano cambiati.

## Farlo girare da solo, il primo del mese

**Mac** (launchd), `~/Library/LaunchAgents/local.controlla-aggiornamenti.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>local.controlla-aggiornamenti</string>
  <key>ProgramArguments</key><array>
    <string>/usr/bin/python3</string><string>/Users/<tuo-utente>/<cartella-vault>/strumenti/controlla_aggiornamenti.py</string>
  </array>
  <key>StartCalendarInterval</key><dict><key>Day</key><integer>1</integer><key>Hour</key><integer>9</integer><key>Minute</key><integer>0</integer></dict>
</dict></plist>
```
poi `launchctl load ~/Library/LaunchAgents/local.controlla-aggiornamenti.plist`.

**Windows** (PowerShell):
```powershell
schtasks /Create /SC MONTHLY /D 1 /ST 09:00 /TN "Controllo aggiornamenti" /TR "py C:\<cartella-vault>\strumenti\controlla_aggiornamenti.py"
```

## Quando la nota dice «cambiato a monte»

1. Leggi i commit nuovi (il comando è scritto nella nota).
2. Se cambiano script, hook o impostazioni, rifai il controllo di sicurezza (scheda «Controllo di sicurezza prima di installare»).
3. Fai un commit o una copia datata, poi aggiorna una cosa alla volta (`git -C <cartella> pull`).

## Come si toglie

Mac: `launchctl unload …plist` e cancella il file. Windows: `schtasks /Delete /TN "Controllo aggiornamenti"`. Poi cancella lo script; le note restano.

## English

`controlla_aggiornamenti.py` checks once a month what changed upstream in skills installed with git and in global npm packages, and writes a note: how many new commits, which sensitive files (hooks, scripts, settings) were touched. It updates nothing: you decide, redoing the security check when sensitive parts changed.

Install: change the notes folder in `controlla_aggiornamenti.py`, run it once by hand, then schedule it for the first of each month.
