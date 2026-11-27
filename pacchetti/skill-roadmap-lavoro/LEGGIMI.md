# Roadmap di lavoro

**Cosa fa.** Trasforma una richiesta con più passi in fasi e task con chi, stima in minuti, dipendenze, prova di fatto e chi controlla. Risponde anche a «a che punto siamo?» con una pagina: in tempo, a rischio o in ritardo, e perché.

**Dove si copia.** `roadmap-lavoro/` in `~/.claude/skills/roadmap-lavoro/`. Non serve nessun gestore di task: senza, la roadmap vive in `<tuo-progetto>/ROADMAP.md`. Se usi anche il pacchetto «pipeline di lavoro», le due skill si parlano: la pipeline dà i passi, la roadmap aggiunge tempi e controlli.

**Come si prova.** Chiedi «fammi la roadmap per rifare il sito in tre settimane». Deve uscire: taglia, 3-5 fasi con «finita quando», task con minuti e chi controlla, i punti dove serve il tuo ok. Poi chiedi «a che punto siamo?» e controlla che la prima riga sia un verdetto.

**Come si toglie.** Cancella `~/.claude/skills/roadmap-lavoro/`.

## English

A `roadmap-lavoro` skill that breaks a job down from outcomes, on at most three levels: each task has an owner, an estimate in minutes, dependencies, whether your ok is needed, the proof of "done" and a checker who isn't the author. The status report fits on one page and opens with on time, at risk or late.

Install: copy `roadmap-lavoro/` into `~/.claude/skills/`. Without a task manager the roadmap lives in `<your-project>/ROADMAP.md`; with `pacchetti/canali-board-task/` the tasks go to the board.
