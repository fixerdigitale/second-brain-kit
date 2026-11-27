---
slug: memoria-archivista-correzioni-agli-agenti
titolo: "L'archivista porta le correzioni agli agenti"
area: memoria
dove_gira: server
livello: avanzato
costo: "0 € in più con l'abbonamento Claude, ma richiede un server con una piattaforma di agenti (io uso OpenClaw)."
pacchetto: "nessuno: solo idea"
stato: lo uso
---

# L'archivista porta le correzioni agli agenti

**Il problema.** Ho diversi agenti AI (copy, grafica, codice, ricerca). Una correzione detta a uno di loro, o a Claude Code, spesso valeva per tutti, ma restava dov'era stata detta.

**Come l'ho risolto.** Ogni notte, dopo il revisore, un agente Archivista (Sonnet) legge le correzioni del giorno: quelle dette agli agenti e le memorie di correzione di Claude Code, che un piccolo ponte gli mette in coda. Le scrive nei file di istruzioni degli agenti giusti e tiene uno storico di cosa ha portato dove. Le regole che varrebbero per tutti non le applica: le propone come card, e entrano solo se approvo.

**Perché così.** Una correzione va scritta dove l'agente la legge sempre, cioè nei suoi file di istruzioni. Farlo a mano su dieci agenti non regge. Le regole comuni passano dal mio ok perché cambiano il comportamento di tutti, e perché l'archivista legge anche messaggi di altre persone: non voglio che una frase scritta in chat diventi una regola da sola.

**Quando ti serve.** Solo se hai più agenti AI, con file di istruzioni separati, che lavorano per te in autonomia.

**Quando non ti serve.** Se usi Claude Code da solo, anche con dei subagent in `.claude/agents/`: le correzioni le metti in CLAUDE.md o in memoria e valgono già per tutti. Su un PC l'equivalente è la scheda «Revisore notturno delle sessioni» nella versione archivista di fine giornata.

**Come prenderlo.** Solo idea: serve un server con più agenti sempre accesi. Su PC: una correzione ripetuta va in CLAUDE.md, che leggono anche i subagent.
