# Modello di CLAUDE.md a sezioni

**Cosa fa.** Un CLAUDE.md diviso in sezioni fisse: stile delle risposte, dove operare, inventario,
dove va la memoria, passaggio di consegne, regole ripetute. È lo scheletro del mio, senza i contenuti privati.

**Dove si copia.**
- Per tutti i progetti: `~/.claude/CLAUDE.md` (Windows: `C:\Users\<tu>\.claude\CLAUDE.md`).
- Per un solo progetto: `CLAUDE.md` nella cartella aperta in VS Code.

Sostituisci i segnaposto `<...>` e cancella le sezioni che non ti servono.

**Come si prova.** Apri una sessione nuova di Claude Code e chiedi: «Dove salvi un fatto su un cliente?».
Dovrebbe rispondere con la cartella del vault scritta nel file.

**Come si toglie.** Cancella il file (o rimettiti la copia di prima). Nessun altro effetto.

**Nota.** Tienilo corto: si carica a ogni messaggio e consuma contesto. Il mio è cresciuto a ~270 righe (23 KB)
ed è al limite: i dettagli vanno in file a parte, qui solo la regola e il percorso.

## English

A CLAUDE.md template with fixed sections: how to answer you, where to work (folders, what not to touch, where secrets are: path only), "read the inventory before saying you don't have it", where memory goes, handover with HANDOFF and SISTEMA, and a dated Rules section for corrections you had to repeat.

Install: copy `CLAUDE.md` to `~/.claude/CLAUDE.md` (all projects) or into a project folder, replace the `<...>` placeholders and delete the sections you don't need. The template is in Italian; translate the headings if you prefer. Keep it short: it's loaded with every message.
