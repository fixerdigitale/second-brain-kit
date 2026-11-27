---
slug: ricerca-per-significato-server
titolo: "Ricerca per significato in tutta la memoria"
area: ricerca
dove_gira: server
livello: avanzato
costo: "0 € in più se hai già un server: Ollama e nomic-embed-text sono gratuiti e il modello pesa 274 MB. Senza server, un VPS parte da qualche euro al mese, più qualche ora per installare e collegare tutto."
pacchetto: "nessuno: solo idea"
stato: lo uso
---

# Ricerca per significato in tutta la memoria

**Il problema.** Il vault è cresciuto oltre le 2.000 note, più di 100 trascrizioni di call. Cercando per parole esatte non trovavo le cose: avevo scritto «prezzo» e cercavo «preventivo», oppure una decisione era raccontata con parole diverse da quelle che ricordavo. Gli agenti rispondevano «non ho informazioni» su cose scritte da settimane.

**Come l'ho risolto.** Sul server gli agenti (uso OpenClaw) hanno uno strumento di ricerca nella memoria che indicizza il vault e la cartella delle call. Ogni pezzo di nota diventa un vettore calcolato in locale da Ollama con il modello nomic-embed-text, quindi la ricerca trova le note che parlano della stessa cosa anche con parole diverse. Claude Code ci arriva dallo stesso strumento, con un collegamento MCP verso gli agenti. Tutto gira sul server: nessuna nota esce verso servizi esterni per essere indicizzata.

**Perché così.** Il valore di un vault, per me, sta nel ritrovare più che nello scrivere. Ho scelto un modello di embedding locale perché le note contengono clienti, soldi e call: non volevo mandarle a un servizio esterno solo per indicizzarle, e così il costo è zero. Sta sul server perché lì gli agenti rispondono anche di notte e dal telefono.

**Quando ti serve.** Quando il vault supera qualche centinaio di note, quando scrivi in modo libero (dettato, appunti di call) e quando più persone o agenti scrivono con parole diverse. Anche se vuoi che un assistente sempre acceso risponda dalle tue note mentre il PC è spento.

**Quando non ti serve.** Se il vault è piccolo o lo tieni ordinato con titoli chiari: la ricerca per parole di Claude Code basta e non hai niente da mantenere. Se lavori solo dal PC, questa versione da server è eccessiva: guarda la scheda «Ricerca per significato sul PC con QMD». E se non hai già un server con agenti, non vale la pena montarne uno solo per questo.

**Come prenderlo.** Solo idea: serve un server con un sistema di agenti che abbia la ricerca nella memoria, impostato per usare un modello di embedding locale (Ollama) e le cartelle in più da indicizzare. Per il PC l'opzione pronta è nella scheda «Ricerca per significato sul PC con QMD».
