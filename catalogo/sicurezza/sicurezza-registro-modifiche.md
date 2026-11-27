---
slug: sicurezza-registro-modifiche
titolo: Registro delle modifiche sui sistemi dove lavorano più persone
area: sicurezza
dove_gira: server
livello: base
costo: 0 €. Due minuti a modifica.
pacchetto: pacchetti/sicurezza-registro-modifiche/
stato: lo uso
---
# Registro delle modifiche sui sistemi dove lavorano più persone

**Il problema.** Su alcuni sistemi lavoriamo in più persone, ognuna con il suo Claude. Uno cambiava una configurazione, l'altro non lo sapeva e ci passava sopra, oppure perdeva un'ora a capire perché qualcosa si comportava in modo diverso.

**Come l'ho risolto.** Sul sistema stesso c'è un file REGISTRO-MODIFICHE.md con le voci più recenti in alto. Dopo ogni modifica si scrive una voce: data UTC, chi, cosa, perché, come tornare indietro, cosa si è verificato. Mai segreti: si scrive dove sta una cosa, non cosa contiene. Prima di toccare un servizio, Claude legge le ultime voci. In più lascio un commento sulla task del lavoro.

**Perché così.** Il registro sta dove lavorano tutti, non sul mio PC: chi entra dopo vede subito cosa è cambiato e come annullarlo, anche se non fa parte del mio team.

**Quando ti serve.** Quando su un server, un CRM o un sistema di automazioni lavorano più persone o più agenti.

**Quando non ti serve.** Se il sistema lo tocchi solo tu, per me bastano i commit di git o le note del progetto. Per un sito su un hosting gestito senza accesso ai file, il registro può stare in un documento condiviso con il cliente invece che sul server.

**Come prenderlo.** Copia `REGISTRO-MODIFICHE.md` sul sistema, in una cartella che vedono tutti, e incolla `regola-claude-md.md` nel `CLAUDE.md` del progetto. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-registro-modifiche/LEGGIMI.md).
