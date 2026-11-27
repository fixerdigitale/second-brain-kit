---
slug: sicurezza-chiave-finita-online
titolo: "Una chiave è finita in una copia online: cosa ho fatto"
area: sicurezza
dove_gira: PC
livello: base
costo: "0 €. 15-20 minuti, quasi tutti sul sito del servizio che ha dato la chiave."
pacchetto: "nessuno: solo idea"
stato: mi è successo, lo rifarei così
---

# Una chiave è finita in una copia online: cosa ho fatto

**Il problema.** Una chiave di accesso a un servizio stava in un file di note. Quella cartella aveva un salvataggio su GitHub (e in un altro caso era dentro una cartella sincronizzata con il cloud). Togliere la riga dal file non bastava: la chiave restava nei salvataggi vecchi e nella copia online.

**Come l'ho risolto.** In quest'ordine: 1) ho **cambiato la chiave alla fonte**, cioè sul sito del servizio che l'aveva data (si chiama «revoca» o «rigenera»): da quel momento la vecchia non vale più, ovunque sia finita; 2) ho messo la chiave nuova in un file `.env` fuori dalle note; 3) ho aggiunto `.env` al `.gitignore`; 4) se il file con la chiave era già salvato in git, l'ho tolto dai file seguiti con `git rm --cached <file>` (il file resta sul disco, git smette di salvarlo); 5) ho fatto un nuovo salvataggio e ho rilanciato `cerca-segreti` per vedere che fosse pulito. Per una cartella sincronizzata ho controllato anche il cestino e le versioni precedenti del servizio cloud.

**Perché così.** Il primo passo è l'unico che chiude davvero il rischio: la storia di git e le versioni del cloud tengono la chiave vecchia anche dopo averla tolta dal file, e riscrivere la storia è lungo e facile da sbagliare. Cambiata la chiave, quella vecchia è solo un testo inutile.

**Quando ti serve.** Se `cerca-segreti` trova una chiave in un file che è salvato in git con una copia online, o che sta in una cartella sincronizzata (OneDrive, iCloud, Dropbox, Google Drive).

**Quando non ti serve.** Se la chiave sta solo sul tuo computer, in una cartella non sincronizzata e mai salvata in git: lì basta spostarla in un `.env` (scheda [Un solo file di segreti](sicurezza-segreti-file-unico.md)). Se il valore trovato è un esempio finto o una chiave già scaduta, non c'è niente da cambiare.

**Come prenderlo.** Nessun pacchetto: è una sequenza da fare con calma. La parte sul sito del servizio la fa la persona, perché serve il suo accesso; Claude prepara `.env`, `.gitignore` e il comando `git rm --cached`, e li fa solo dopo un sì. La storia vecchia di git si può anche riscrivere (`git filter-repo`), ma io non lo faccio se la chiave è già cambiata.
