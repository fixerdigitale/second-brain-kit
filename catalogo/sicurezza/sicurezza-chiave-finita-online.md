---
slug: sicurezza-chiave-finita-online
titolo: "Se una chiave finisce in una copia online: cosa farei"
area: sicurezza
dove_gira: PC
livello: base
costo: "0 €. 15-20 minuti, quasi tutti sul sito del servizio che ha dato la chiave."
pacchetto: "nessuno: solo idea"
stato: "proposta nuova, non mi è successo: lo farei così"
---

# Se una chiave finisce in una copia online: cosa farei

**Il problema.** Una chiave di accesso a un servizio può finire in un file di note. Se quella cartella ha un salvataggio su GitHub, o sta dentro una cartella sincronizzata con il cloud, togliere la riga dal file non basta: la chiave resta nei salvataggi vecchi e nella copia online. A me non è successo; questa è la sequenza che seguirei.

**Come lo risolverei.** In quest'ordine: 1) **cambierei la chiave alla fonte**, cioè sul sito del servizio che l'ha data (si chiama «revoca» o «rigenera»): da quel momento la vecchia non vale più, ovunque sia finita; 2) metterei la chiave nuova in un file `.env` fuori dalle note; 3) aggiungerei `.env` al `.gitignore`; 4) se il file con la chiave è già salvato in git, lo toglierei dai file seguiti con `git rm --cached <file>` (il file resta sul disco, git smette di salvarlo); 5) farei un nuovo salvataggio e rilancerei `cerca-segreti` per vedere che sia pulito. Per una cartella sincronizzata controllerei anche il cestino e le versioni precedenti del servizio cloud.

**Perché così.** Il primo passo è l'unico che chiude davvero il rischio: la storia di git e le versioni del cloud tengono la chiave vecchia anche dopo averla tolta dal file, e riscrivere la storia è lungo e facile da sbagliare. Cambiata la chiave, quella vecchia è solo un testo inutile.

**Quando ti serve.** Se `cerca-segreti` trova una chiave in un file che è salvato in git con una copia online, o che sta in una cartella sincronizzata (OneDrive, iCloud, Dropbox, Google Drive).

**Quando non ti serve.** Se la chiave sta solo sul tuo computer, in una cartella non sincronizzata e mai salvata in git: lì basta spostarla in un `.env` (scheda [Un solo file di segreti](sicurezza-segreti-file-unico.md)). Se il valore trovato è un esempio finto o una chiave già scaduta, non c'è niente da cambiare.

**Come prenderlo.** Nessun pacchetto: è una sequenza da fare con calma. La parte sul sito del servizio la fa la persona, perché serve il suo accesso; Claude prepara `.env`, `.gitignore` e il comando `git rm --cached`, e li fa solo dopo un sì. La storia vecchia di git si può anche riscrivere (`git filter-repo`), ma io non lo farei se la chiave è già cambiata.
