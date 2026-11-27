---
slug: memoria-fatti-vs-correzioni
titolo: "Fatti nel vault, correzioni nella memoria"
area: memoria
dove_gira: PC
livello: base
costo: "0 €. 10 minuti per copiare la skill e la riga in CLAUDE.md."
pacchetto: pacchetti/memoria-fatti-vs-correzioni/
stato: lo uso
---

# Fatti nel vault, correzioni nella memoria

**Il problema.** Avevo due memorie e le cose finivano a caso: l'esito di una call nella memoria di Claude Code invece che nel vault, doppioni nei due posti, e gli altri strumenti che leggono il vault non vedevano i fatti.

**Come l'ho risolto.** Ho diviso i compiti. I fatti (clienti, progetti, decisioni, persone, accordi) vanno solo nel vault, nella nota giusta, in coda alla sezione «## Dalle sessioni», con Obiettivo, Fatto e Aperto. La memoria di Claude Code tiene solo le correzioni su come lavorare. Quando dico «salva in memoria» vuol dire vault, sempre, senza copia nell'altra. L'ho scritto in CLAUDE.md e in una piccola skill che decide dove mettere la nota.

**Perché così.** Una cosa in un posto solo non si contraddice. Il vault lo legge tutto (Obsidian, gli agenti, la ricerca), la memoria di Claude Code no. E un «salva in memoria» detto di corsa o a voce non mi costringe a specificare ogni volta dove.

**Quando ti serve.** Se hai già un vault di note e usi anche la memoria automatica di Claude Code: è il caso tipico in cui le due si sovrappongono.

**Quando non ti serve.** Se non hai un vault e ti basta la memoria di Claude Code: questa divisione non serve.

**Come prenderlo.** Copia la cartella `salva-in-memoria/` in `~/.claude/skills/salva-in-memoria/` e sostituisci `<cartella-vault>` nel SKILL.md. La riga facoltativa per CLAUDE.md è nel LEGGIMI.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-fatti-vs-correzioni/LEGGIMI.md).
