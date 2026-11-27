# Drive condiviso con cartelle fisse per cliente

**Cosa fa.** Ogni cliente ha la stessa struttura di cinque cartelle (01 Documenti iniziali, 02
Materiali, 03 Per le richieste, 04 Consegne, 05 Lavoro interno). Lo script le crea e dice a Claude
dove mettere un file; la regola nel `CLAUDE.md` gli dice cosa va dove e cosa non va mai nel
condiviso. Così il socio o l'assistente vedono i file senza che tu li condivida uno per uno.

**Cosa serve prima.** Un Drive condiviso (Google Workspace) o una cartella condivisa, sincronizzata
sul PC con Google Drive per desktop (o OneDrive/Dropbox). Lo script lavora sulla cartella locale:
Drive la carica da solo.

**Dove si copia.**
1. `cartella_cliente.py` dove vuoi (es. `<cartella-vault>/strumenti/`). In cima cambia `RADICE` con
   il percorso locale della cartella «Clienti» del Drive condiviso.
2. Il testo di `regola-per-CLAUDE.md` nel `CLAUDE.md` del vault, con il percorso giusto dello script.

**Come si prova.** `python3 cartella_cliente.py crea "Cliente Prova"`, poi `python3 cartella_cliente.py elenco`.
Controlla sul sito di Drive che le cartelle siano comparse. Poi cancella «Cliente Prova» a mano.

**Limiti.** Un Google Doc o un Foglio vero (non un file .docx) si crea dal sito o con un connettore
di Google; lo script crea solo cartelle. Lo script non cancella e non sposta mai niente.

**Come si toglie.** Cancella lo script e la sezione nel `CLAUDE.md`; le cartelle restano.

## English

A script that creates the same five folders for every client inside a folder synced with Google Drive for desktop (initial documents, materials, requests, deliveries, internal work), plus a rule for CLAUDE.md so new files are born in the right place. It lists what never goes into the shared drive (credentials, contracts, invoices, personal data).

Install: copy `cartella_cliente.py`, set `RADICE` to the local path of the shared drive's Clients folder and paste `regola-per-CLAUDE.md` into your CLAUDE.md. The script only creates folders; it never deletes or moves anything. Folder names are Italian: rename them in the script if you like.
