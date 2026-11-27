# File di correzione con Why / How to apply

**Cosa fa.** Un modello per i file della memoria automatica di Claude Code: una correzione per file,
con tre parti fisse. Cosa è successo, **Why** (perché), **How to apply** (come si applica).

Perché le tre parti: una regola senza il perché si applica alla lettera e sbaglia sui casi vicini.
Con il perché Claude generalizza. Gli aggiornamenti in fondo contano quante volte la correzione è tornata.

**Dove si copia.** Nella stessa cartella di MEMORY.md:
`~/.claude/projects/<nome-cartella-del-progetto>/memory/feedback_<nome>.md`
Poi aggiungi il nome nel gruppo giusto di MEMORY.md (o in «Da smistare»).

Puoi anche non copiare niente e dire a Claude, una volta, nel CLAUDE.md:
«Le correzioni salvale in memoria come `feedback_<nome>.md` con le parti Why e How to apply.»

**Come si prova.** Correggi Claude su una cosa qualsiasi e digli «salvala come correzione».
Controlla che il file abbia `description`, **Why** e **How to apply**.

**Come si toglie.** Cancella il file e la sua riga in MEMORY.md.

## English

A template for correction files (`feedback_<name>.md`): what happened (date and exact words), **Why** (the concrete damage the rule prevents), **How to apply** (what to do in practice, with exceptions), plus a one-sentence description in the frontmatter so Claude knows when to open it. Repeated corrections get an "update" line at the bottom, which tells you which rules deserve promotion.

Install: copy `feedback_esempio.md` into your Claude Code memory folder as a model, or add to CLAUDE.md: "save corrections as feedback_<name>.md with Why and How to apply parts".
