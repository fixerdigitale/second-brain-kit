# Cerca strumento

**Cosa fa.** Quando ti serve una funzione nuova o ti girano un link a una skill, un MCP o una repo, Claude cerca nei registri giusti, confronta al massimo tre candidati, legge il codice e ti dà un verdetto in tre righe: INSTALLO, PROVO ISOLATO o LASCIO PERDERE. Ogni verdetto finisce in `valutati.md`, così non rifai il giro.

**Dove si copia.** `cerca-strumento/` (con `valutati.md` dentro) in `~/.claude/skills/cerca-strumento/`.
Lo scanner è facoltativo: SkillSpector (https://github.com/NVIDIA/SkillSpector) gira in Docker; senza, la skill si appoggia alla lettura del codice.
Comando `gh` facoltativo (GitHub CLI): rende più veloci i controlli su stelle e ultimo commit.

**Come si prova.** Chiedi «c'è un MCP per leggere i miei file di Google Drive?». Deve uscire un verdetto in tre righe con un fatto verificato e una riga nuova in `valutati.md`.

**Come si toglie.** Cancella `~/.claude/skills/cerca-strumento/`.

## English

A `cerca-strumento` skill for evaluating a skill, MCP server or repo before installing it: it checks what you already have, searches the right registries, compares at most three candidates (alive, maintainer, what it touches, license, code actually read) and ends with INSTALL, TRY ISOLATED or LEAVE IT. Every verdict is logged in `valutati.md`.

Install: copy `cerca-strumento/` (with `valutati.md`) into `~/.claude/skills/`. Optional static scanner (needs Docker): https://github.com/NVIDIA/SkillSpector.
