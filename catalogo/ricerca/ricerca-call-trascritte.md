---
slug: ricerca-call-trascritte
titolo: "Call trascritte: ricercabili e senza impegni persi"
area: ricerca
dove_gira: PC
livello: medio
costo: "0 € in più con un registratore di call che già usi. 10 minuti per copiare script e skill; poi qualche secondo per ogni lancio."
pacchetto: pacchetti/ricerca-call-trascritte/
stato: versione per PC del mio
---

# Call trascritte: ricercabili e senza impegni persi

**Il problema.** Le trascrizioni delle call arrivavano come file di testo senza titolo, data né partecipanti, e la ricerca le trovava male: una decisione detta in call era come non detta. E dal riassunto automatico del registratore gli impegni si perdevano: in un pomeriggio ne aveva estratti sei e io ne avevo raccolti due, quasi sempre proprio quelli da delegare.

**Come l'ho risolto.** Due pezzi. Il primo è meccanico: ogni ora uno script prende le trascrizioni salvate dal registratore (uso Fathom) e scrive una nota markdown per call, con titolo, data, chi parla, link alla registrazione e la trascrizione intera; la cartella delle call è indicizzata insieme al vault, così la ricerca le trova come le altre note. Il secondo è di giudizio: quando una call finisce, il mio assistente principale divide ogni punto in lavoro chiesto adesso (diventa un task in bozza, con la fonte), idea per il futuro (resta nella nota) o accordo (va nella nota del cliente); ogni action item del registratore o diventa un task o ha scritto perché no; poi prepara il recap per il cliente, che parte solo dopo il mio sì. Per il PC ho fatto le due metà senza dipendere da Fathom: uno script che trasforma una cartella di .txt, .vtt o .srt in note, e una skill `scheda-call` che fa la scheda da una trascrizione incollata o già nel vault.

**Perché così.** Le call sono la fonte delle decisioni con i clienti: le uso per controllare un fatto prima di costruirci sopra («in call avevamo detto X?»). Trascrizione intera e non riassunto, perché il riassunto perde proprio il dettaglio che poi serve, e spesso scrive «iniziare a lavorare su…» anche quando nessuno l'ha chiesto. Separare lavori, idee e accordi evita task inventati. Il recap preparato ma non mandato mi fa allineare il cliente in un minuto, senza rischi.

**Quando ti serve.** Se fai più call a settimana con clienti o soci, le registri già con uno strumento che dà la trascrizione, e da lì nascono impegni.

**Quando non ti serve.** Se fai poche call, non le registri, o i clienti non sono d'accordo a essere registrati. Se prendi già appunti a mano bene, la skill ti fa perdere più tempo di quanto ne risparmi. Se il tuo registratore ha già una buona ricerca e non ti serve incrociarla con le note, è un doppione. E se il vault va su GitHub o Drive, le parole dei clienti ci vanno con lui: tienilo privato e salta le call delicate.

**Come prenderlo.** Copia `call_in_markdown.py` in `~/.claude/strumenti/` e `scheda-call/` in `~/.claude/skills/scheda-call/`. Scarica le trascrizioni in una cartella e lancia `python3 call_in_markdown.py <cartella-trascrizioni> <cartella-vault>/Call`; poi in Claude Code «fammi la scheda della call». La versione che parte da sola a fine call chiede un server.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/ricerca-call-trascritte/LEGGIMI.md).
