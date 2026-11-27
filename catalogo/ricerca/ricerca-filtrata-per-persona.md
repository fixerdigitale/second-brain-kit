---
slug: ricerca-filtrata-per-persona
titolo: "Ricerca filtrata per persona"
area: ricerca
dove_gira: server
livello: avanzato
costo: "0 € in più sul server che avevo già. Sviluppo e prove: qualche giornata di lavoro."
pacchetto: nessuno: solo idea
stato: lo uso
---

# Ricerca filtrata per persona

**Il problema.** Volevo che una collaboratrice potesse chiedere all'assistente lo stato dei suoi progetti senza vedere soldi, altri clienti o cose personali che stanno nello stesso vault. Fare un vault o un agente per ogni persona non regge: si duplica tutto.

**Come l'ho risolto.** Un solo vault, e un sistema solo con le etichette della scheda «Vault con cartelle fisse ed etichette alla nascita»: ogni nota nasce con `livello` (operativo, economico, personale), i clienti di cui parla e chi la può vedere. Da quelle etichette si rigenera ogni 15 minuti un indice con solo i pezzi di nota etichettati. L'agente che parla con la collaboratrice non legge i file: ha un solo strumento di ricerca, dove la persona è fissata nella configurazione e non arriva dalla chat. Un pezzo esce solo se è nell'indice, con lo stesso testo, e con livello e clienti permessi a quella persona. Un pezzo cambiato dopo l'etichetta non esce finché non viene rietichettato.

**Perché così.** La regola che mi sono dato è «un agente per ruolo, non per persona». Il filtro sta nello strumento, non nelle istruzioni al modello: un modello si può convincere, uno script no. E le etichette le metto alla nascita della nota perché è il momento in cui si sa meglio cosa c'è dentro: rimetterle dopo su tutto il vault è più lento e meno preciso.

**Quando ti serve.** Quando più persone (collaboratori, clienti) interrogano la stessa memoria e non tutti possono vedere tutto.

**Quando non ti serve.** Se il vault lo usi solo tu, o con soci che vedono tutto: è complessità pura. Non è una cosa da PC, perché deve rispondere quando scrivono gli altri. Se vuoi solo condividere qualcosa con un collaboratore, una cartella condivisa separata è più semplice e più sicura.

**Come prenderlo.** Solo idea: serve un server con un agente chiuso in un ambiente separato e uno strumento di ricerca su misura. Il pezzo che si prende da subito sono le etichette alla nascita: pacchetto `pacchetti/memoria-vault-etichette-alla-nascita/`.
