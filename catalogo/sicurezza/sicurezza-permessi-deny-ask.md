---
slug: sicurezza-permessi-deny-ask
titolo: "Permessi: cosa passa da solo, cosa mai, e un livello «chiedi» da provare"
area: sicurezza
dove_gira: PC
livello: base
costo: 0 €. 10 minuti.
pacchetto: pacchetti/sicurezza-permessi-deny-ask/
stato: versione per PC del mio
---
# Permessi: cosa passa da solo, cosa mai, e un livello «chiedi» da provare

**Il problema.** Claude mi chiedeva il permesso anche per un ls, e a forza di cliccare «sì» avrei approvato anche la cosa sbagliata. Al contrario, certe azioni non volevo che le facesse mai, neanche su una mia richiesta distratta: leggere il file delle chiavi, le chiavi SSH.

**Come l'ho risolto.** Nel settings.json di Claude Code uso due liste. Allow: i comandi di sola lettura (ls, grep, git status, log) passano senza chiedere. Deny: lettura del file dei segreti, della cartella delle credenziali e delle chiavi SSH, bloccate sempre. Da me ci sono solo queste due. Nel modello per PC ho aggiunto una terza lista, ask, per le azioni difficili da annullare (push, cancellazioni, installazioni, download): è una proposta nuova, non la uso così, e la segno come tale.

**Perché così.** Meno richieste inutili vuol dire più attenzione su quelle vere. Il deny è una rete che non dipende da quanto sono stanco quel giorno.

**Quando ti serve.** Appena usi Claude Code su cartelle con dati veri, file di chiavi o repo collegati a GitHub.

**Quando non ti serve.** Se lavori nella modalità che chiede tutto e cliccare non ti pesa, la lista allow serve a poco; il deny secondo me conviene comunque. Il deny ferma gli strumenti di Claude, non ogni comando di shell possibile: un `cat` dalla shell può leggere un file che il deny blocca per lo strumento di lettura. I segreti restano meglio fuori dalle cartelle di lavoro. La lista ask, se ti basta la modalità normale, puoi anche toglierla.

**Come prenderlo.** Copia il blocco `permissions` di `settings.json` in `~/.claude/settings.json` (tutti i progetti) o in `<tuo-progetto>/.claude/settings.json`, aggiungi a deny la tua cartella dei segreti se ne hai una e controlla con `/permissions`. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-permessi-deny-ask/LEGGIMI.md).
