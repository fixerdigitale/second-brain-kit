# Stile delle risposte (caveman + i-have-adhd, adattate all'italiano)

**Cosa fa.** Un blocco da incollare nel tuo `CLAUDE.md` che tiene sempre accese due skill di terzi: `caveman` (risposte compresse, senza riempitivi) e `i-have-adhd` (prima riga = cosa fare, passi numerati, stato ricapitolato a ogni turno). Il pezzo nostro è l'adattamento: livello lite con articoli e frasi intere, perché in italiano i livelli più spinti si leggono male, e la lista di cose da non comprimere mai.

**Le due skill si prendono dalla fonte**, non da qui:
- caveman: https://github.com/JuliusBrussee/caveman
- i-have-adhd: https://github.com/ayghri/i-have-adhd (licenza MIT)

**Dove si copia.**
1. Installa le due skill in `~/.claude/skills/caveman/` e `~/.claude/skills/i-have-adhd/` seguendo le istruzioni delle due repo.
2. Incolla `blocco-claude-md.md` nel tuo `~/.claude/CLAUDE.md` (vale ovunque) o nel `CLAUDE.md` di un progetto.
3. Se nel blocco tieni la riga su grilling, installa anche `grilling` da https://github.com/mattpocock/skills.

**Come si prova.** Chiedi «come faccio a spostare il vault su un'altra cartella?». La risposta deve partire con il primo passo, numerata, senza «Certo!» in apertura, e chiudere con una sola azione breve.

**Come si toglie.** Togli il blocco dal `CLAUDE.md`. Le skill puoi lasciarle: senza il blocco si accendono solo se le chiami.

## English

A CLAUDE.md block that keeps the caveman and i-have-adhd skills always on and adapts them to Italian: lite compression with articles and full sentences, first line = the action, numbered steps, state recap every turn, and a list of things never compressed (numbers, paths, commands, negations, uncertainties, security warnings).

Install: install the skills from https://github.com/JuliusBrussee/caveman and https://github.com/ayghri/i-have-adhd, then paste `blocco-claude-md.md` into your `CLAUDE.md`. If you work in English you can use caveman's own levels and skip the Italian adaptation.
