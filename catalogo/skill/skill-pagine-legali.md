---
slug: skill-pagine-legali
titolo: "Pagine legali scritte su quello che il sito fa davvero"
area: skill
dove_gira: PC
livello: avanzato
costo: "0 € di strumenti; 1-2 ore per sito; la revisione del professionista è a parte"
pacchetto: "pacchetti/skill-pagine-legali/"
stato: "lo uso"
---
# Pagine legali scritte su quello che il sito fa davvero

**Il problema.** Privacy e cookie policy copiate da modelli generici dicevano cose false: strumenti che il sito non usa, e mancavano quelli che usa (pixel, calendari, moduli). E il banner cookie spesso caricava i tracciamenti prima della scelta.

**Come l'ho risolto.** Ho adattato in italiano una skill pubblica (licenza Apache 2.0). Prima scansiona il codice o l'HTML del sito e prova il banner nel browser: cosa parte prima della scelta, dopo «Rifiuta», dopo «Accetta». Poi raccoglie i fatti dal committente e scrive privacy, cookie policy, condizioni di servizio, informativa sull'uso dell'AI e testi del banner. Quello che non ha una fonte resta come segnaposto e va in un elenco da verificare. Quando devo citare un articolo dal testo vigente accendo anche il plugin legal-it di mcp-legal-it (pubblico, Apache 2.0), che legge Normattiva, EUR-Lex e Brocardi; di serie lo tengo spento, perché ogni sessione avvia un suo server e per il lavoro normale non mi serve.

**Perché così.** Prima si guarda il sito, poi si scrive: mai il contrario. Niente dati inventati e niente norme citate a memoria: solo quelle verificate su fonte primaria, con la data. Non è consulenza legale: sono bozze da dare a un professionista, che così rivede invece di scrivere da zero.

**Quando ti serve.** Una landing che va online, un sito che aggiunge tracciamenti o moduli, un controllo delle pagine legali esistenti.

**Quando non ti serve.** Se hai già un consulente privacy che segue il sito, o se il sito tratta dati delicati (sanità, minori): lì serve il professionista dall'inizio. Le bozze non vanno pubblicate senza revisione.

**Come prenderlo.** Copia `pagine-legali/` in `~/.claude/skills/` tenendo LICENSE e NOTICE. Servono Python 3 e, per la prova del banner, Node.js con Playwright e Chromium. Originale: https://github.com/gricyk/claude-skill-eu-web-compliance. Plugin facoltativo: https://github.com/capazme/mcp-legal-it. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/skill-pagine-legali/LEGGIMI.md).
