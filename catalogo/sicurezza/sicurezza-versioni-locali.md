---
slug: sicurezza-versioni-locali
titolo: Versioni locali di pagine e documenti, senza GitHub
area: sicurezza
dove_gira: PC acceso
livello: medio
costo: 0 €. 15 minuti.
pacchetto: pacchetti/sicurezza-versioni-locali/
stato: versione per PC del mio
---
# Versioni locali di pagine e documenti, senza GitHub

**Il problema.** Pagine, report e documenti di lavoro cambiano spesso, e a volte la versione buona era quella di tre giorni prima. Le copie datate vanno bene per un file di configurazione, non per decine di pagine. Ma mettere tutto su GitHub voleva dire far uscire dal PC anche dati di clienti, solo per avere la storia.

**Come l'ho risolto.** Ho deciso che GitHub è per il codice che gira. Per pagine e documenti tengo le versioni in locale: ogni notte, poco prima del backup, un commit registra quello che è cambiato. Nessun remoto, nessun push. Il .git sta fuori dalla cartella, così non finisce mai in un sito pubblicato né nella sincronizzazione del cloud. Entrano solo i file di testo sotto i 5 MB. Dopo una pubblicazione importante faccio anche un commit a mano con un messaggio. La storia poi entra nel backup della notte. Per il PC ho scritto la stessa cosa in uno script, con due comandi per vedere le versioni di un file e recuperarne una vecchia accanto all'originale.

**Perché così.** Tornare a una versione di ieri diventa un comando, e i dati restano dove sono. Facendolo prima del backup, la storia è protetta come tutto il resto.

**Quando ti serve.** Se lavori su pagine HTML, report o documenti in Markdown che cambiano spesso e non stanno già sotto git.

**Quando non ti serve.** Se la cartella è già un repo git (il vault, un progetto di codice), ha già la sua storia. Per file di Word, Google Docs o PDF la storia del servizio stesso serve meglio: git confronta bene solo il testo. Per un solo file ogni tanto bastano le copie datate.

**Come prenderlo.** Scrivi le cartelle in `versioni_locali.py`, lancialo una volta, poi programmalo un quarto d'ora prima del backup. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-versioni-locali/LEGGIMI.md).
