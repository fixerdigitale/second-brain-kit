---
slug: skill-suite-gstack-stitch
titolo: "Suite di skill prese da fuori: gstack e Stitch"
area: skill
dove_gira: PC
livello: avanzato
costo: "0 € per gstack (MIT); Stitch è un servizio Google con i suoi limiti d'uso, da verificare sul tuo account"
pacchetto: "nessuno: skill di terzi dalla fonte"
stato: "lo uso"
---
# Suite di skill prese da fuori: gstack e Stitch

**Il problema.** Le suite grandi promettono «una squadra intera» in una cartella: decine di skill, comandi, hook. Installarle intere vuol dire tanto codice di altri e tanto contesto; prenderne pezzi a caso vuol dire perdere il motivo per cui funzionano insieme.

**Come l'ho risolto.** Ne uso due. gstack di Garry Tan (oltre 40 skill: revisione del piano, revisione del design, QA in un browser vero, revisione del codice, rilascio) l'ho installata intera, dopo averla scansionata e letta, con gli aggiornamenti automatici spenti: un controllo al mese mi dice se c'è una versione nuova e decido io. Quelle che uso davvero sono poche: design-review e qa (il ciclo «riproduci, correggi, riverifica», da cui ho preso la skill della scheda sulla prova del percorso utente), office-hours e plan-ceo-review per mettere alla prova un'idea, design-shotgun per avere più varianti. Le skill di Stitch (Google Labs, 7 skill) le uso solo per esplorare il layout di una sezione: una chiamata per sezione, passo screenshot, font, logo e colori, e ne prendo sfondo e gerarchia, mai i testi o i numeri, perché li inventa.

**Perché così.** Da gstack prendo il metodo dei controlli, che è la parte forte; le skill che non uso non mi costano niente finché non le apro. Stitch dà idee di composizione che alle pagine fatte solo a testo mancano, ma resta uno spunto, non la pagina finale.

**Quando ti serve.** gstack, se costruisci prodotti o strumenti tuoi e vuoi revisioni e QA con un metodo fisso. Stitch, se fai landing e ti serve una seconda direzione visiva prima di costruire.

**Quando non ti serve.** Se fai poco codice o poche pagine: per una persona sola 40 skill sono tante, e quelle di metodo nelle altre schede bastano. gstack ha parti che vogliono un browser senza sandbox, script di installazione e hook: se non hai tempo di leggerli, non installarla intera. Le skill di Stitch senza un account Stitch e la sua chiave non fanno niente.

**Come prenderlo.** Nessun pacchetto: si prendono dalla fonte. gstack: https://github.com/garrytan/gstack (MIT; leggi lo script di setup prima di lanciarlo). Stitch: https://github.com/google-labs-code/stitch-skills e il servizio https://stitch.withgoogle.com. La chiave di Stitch va in una variabile d'ambiente, non nel testo della skill né sulla riga di comando. Prima di installarle, `pacchetti/skill-cerca-strumento/`.
