# Versioni locali di pagine e documenti, senza GitHub

`versioni_locali.py` fa un commit di quello che è cambiato nelle cartelle che scegli: pagine HTML, report, documenti in Markdown. Ogni versione resta sul tuo PC, senza remoto e senza push.

Perché senza GitHub: per me GitHub è per il codice che gira. Pagine e documenti di lavoro spesso contengono dati di clienti, e non voglio che escano dal PC solo per avere la storia.

Due scelte dello script:
- il `.git` sta **fuori** dalla cartella (in `~/.versioni-locali/`), così non finisce in un sito pubblicato né nella sincronizzazione di Drive o OneDrive;
- entrano solo i file di testo (html, css, js, json, md, svg, txt, csv, yaml) sotto i 5 MB, mai file che sembrano chiavi (`.env`, `.pem`, `credentials`…). Se qualcuno aggiunge un remoto, lo script si ferma.

## Dove si copia

1. Metti lo script dove vuoi, per esempio `<cartella-vault>/strumenti/versioni_locali.py`.
2. In `CARTELLE` scrivi un nome breve e il percorso di ogni cartella da seguire.
3. Se il vault è già sotto git, non metterlo qui: ha già la sua storia.

## Come si prova

1. `python3 versioni_locali.py` (Windows: `py versioni_locali.py`): la prima volta crea la storia e fa il primo commit.
2. Cambia una riga in una pagina e rilancia: deve dire `pagine: <codice> 1 file changed`.
3. `python3 versioni_locali.py storia pagine index.html` mostra le versioni.
4. `python3 versioni_locali.py recupera pagine <codice> index.html ~/index-vecchia.html` salva la versione vecchia accanto, senza toccare l'originale.

## Farlo girare da solo, ogni sera prima del backup

Mettilo un quarto d'ora prima del backup (pacchetto `sicurezza-backup-notturno`), così la storia nuova entra nella copia della notte. Se il backup gira alle 21:00:

**Mac** (launchd): stesso modello del LEGGIMI del backup, con `Label` `local.versioni-locali`, lo script `versioni_locali.py` e `Hour` 20, `Minute` 45.

**Windows** (PowerShell):
```powershell
schtasks /Create /SC DAILY /ST 20:45 /TN "Versioni locali" /TR "py C:\<cartella-vault>\strumenti\versioni_locali.py"
```

La cartella `~/.versioni-locali/` va messa nel backup (per esempio fra le cartelle di restic): se perdi il PC, perdi anche la storia.

Dopo una pubblicazione importante puoi lanciarlo a mano con un messaggio: `python3 versioni_locali.py "pubblicata la landing nuova"`.

## Come si toglie

Togli l'attività dal pianificatore e cancella lo script. La storia sta in `~/.versioni-locali/`: cancellala solo se non ti serve più. I tuoi file non vengono toccati.

## English

`versioni_locali.py` keeps local version history of pages and documents without GitHub: a nightly commit of what changed, no remote, no push, with the .git kept outside the folder and only text files under 5 MB. Two commands show a file's versions and restore an old one next to the original.

Install: write your folders in `versioni_locali.py`, run it once, then schedule it a quarter of an hour before your backup.
