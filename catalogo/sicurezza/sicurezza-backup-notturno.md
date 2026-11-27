---
slug: sicurezza-backup-notturno
titolo: "Backup notturno con la regola 3-2-1: tre copie, due posti, una fuori casa"
area: sicurezza
dove_gira: PC acceso
livello: medio
costo: 0 € se hai già GitHub e un cloud (Drive, OneDrive, iCloud); restic è gratis. Qualche centinaio di MB per 7 zip di un vault di note. 20 minuti di configurazione.
pacchetto: pacchetti/sicurezza-backup-notturno/
stato: versione per PC del mio
---
# Backup notturno con la regola 3-2-1: tre copie, due posti, una fuori casa

**Il problema.** Pensavo che GitHub fosse già un backup. Ma se cancello per errore una cartella e faccio push, la cancellazione arriva anche lì; se perdo l'accesso all'account, perdo tutto insieme. E un backup sullo stesso disco o sullo stesso server sparisce con lui.

**Come l'ho risolto.** Seguo la regola classica 3-2-1: 3 copie, su 2 supporti diversi, 1 fuori casa. Sul server lo faccio con restic: ogni notte un backup cifrato e deduplicato (7 copie giornaliere, 4 settimanali, 6 mensili, controllo dell'integrità una volta a settimana), più un archivio cifrato della parte essenziale su un cloud diverso. Un controllo automatico segna rosso se uno dei due fallisce o è più vecchio di 30 ore. La password sta fuori dal server: senza di lei il backup non si apre. Per un vault su PC ho scritto una versione minima: commit e push su GitHub privato, più uno zip datato nella cartella sincronizzata dal cloud, con le ultime 7 copie. Lo script controlla nome e contenuto dei file con cerca_segreti e si ferma se trova una chiave; fa il push solo se riesce a verificare che il repo è privato; le copie oltre le 7 le cancella solo con `--ruota`.

**Perché così.** Ogni copia protegge da un guasto diverso: disco rotto, errore mio, account bloccato. Gli zip datati coprono la cancellazione che si propaga. E un backup che fallisce in silenzio per me è peggio di nessun backup, perché fa stare tranquilli: per questo ogni giro scrive il suo esito in un file che si può controllare.

**Quando ti serve.** Appena il vault contiene cose che non vuoi riscrivere: memoria, procedure, note di lavoro. Lo script per PC serve se oggi fai il push su GitHub a mano o ogni tanto.

**Quando non ti serve.** Se il vault è già sotto git con push automatico e il cloud lo sincronizza in tempo reale, hai già due copie: lo zip aggiunge solo la protezione da una cancellazione che si propaga. Una quarta copia (disco esterno, NAS) secondo me non serve se le tre ci sono e la prova di ripristino passa. La versione con restic e i dump dei database serve solo se hai un server con database. Lo zip non è cifrato: con dati di clienti uso restic.

**Come prenderlo.** Cambia le due righe di `backup_vault.py`, lancialo a mano, poi programmalo con launchd (Mac) o Utilità di pianificazione (Windows). Istruzioni, comandi restic e avvertenze: [LEGGIMI](../../pacchetti/sicurezza-backup-notturno/LEGGIMI.md). Il file `ultimo-backup.txt` che scrive si può far controllare dalla scheda [Controlli di salute](sicurezza-controlli-salute.md).
