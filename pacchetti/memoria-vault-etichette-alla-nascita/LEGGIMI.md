# Vault con cartelle fisse ed etichette alla nascita

**Cosa fa.** Tre file:
- `CARTELLE.md`: lo schema delle cartelle (Clienti, Progetti, Decisioni, Risorse, Fatti, Fonti, `_Stato.md`);
- `nota-modello.md`: il frontmatter con le etichette (`entita`, `livello`, `visibile_a`) da mettere quando la nota nasce;
- `controlla_etichette.py`: elenca le note senza etichette. Sola lettura.

**Dove si copia.**
- `CARTELLE.md` e `nota-modello.md` nella radice del vault (in Obsidian puoi usare `nota-modello.md` come template).
- `controlla_etichette.py` dove vuoi, fuori dal vault (es. `<tuo-progetto>/strumenti/`).
- Una riga in CLAUDE.md: «Ogni nota nuova del vault nasce con il frontmatter di `<cartella-vault>/nota-modello.md`».

**Come si prova.**
`python3 controlla_etichette.py <cartella-vault>` (su Windows: `py controlla_etichette.py <cartella-vault>`).
Stampa le note senza etichette e il totale.

**Come si toglie.** Cancella i tre file. Il frontmatter già scritto nelle note non dà fastidio: Obsidian lo mostra come proprietà.

**Cosa non c'è.** Da me un servizio sul server rilegge le note ogni 15 minuti e mette le etichette da solo,
con un modello AI e un secondo controllo. Quello serve solo se più persone leggono lo stesso vault
con permessi diversi: qui c'è la versione manuale.

**Collegamento con la ricerca filtrata.** Sono un sistema solo: le stesse etichette (`livello`, `entita`, `visibile_a`)
sono quelle che, da me, decidono cosa può ritrovare ogni persona. Quella parte non ha un pacchetto, perché serve un
server: è la scheda «Ricerca filtrata per persona». Se un giorno vuoi filtrare, le etichette messe alla nascita sono il
pezzo che ti trovi già pronto.

## English

The manual version of labels at birth: a folder scheme for the vault (`CARTELLE.md`), a note template (`nota-modello.md`) whose frontmatter carries `entita` (client or project), `livello` (operational, financial, personal) and `visibile_a` (who may read it), and a read-only script that lists notes without labels.

Install: copy `CARTELLE.md` and `nota-modello.md` into the root of your vault (in Obsidian, use `nota-modello.md` as a template), then run `python3 controlla_etichette.py <vault-folder>` to find unlabeled notes.
