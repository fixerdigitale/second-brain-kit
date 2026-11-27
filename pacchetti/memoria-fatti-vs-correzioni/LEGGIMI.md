# Fatti nel vault, correzioni nella memoria (skill «salva-in-memoria»)

**Cosa fa.** Separa le due memorie e dà un significato fisso a «salva in memoria»:
- i **fatti** (clienti, progetti, decisioni, persone) vanno nel tuo vault di note;
- le **correzioni** su come Claude deve lavorare vanno nella memoria automatica di Claude Code.

**Dove si copia.**
- La skill: cartella `salva-in-memoria/` in `~/.claude/skills/salva-in-memoria/`
  (Windows: `C:\Users\<tu>\.claude\skills\salva-in-memoria\`).
- Nel file `SKILL.md` sostituisci `<cartella-vault>` con il percorso del tuo vault.
- Facoltativo: una riga in CLAUDE.md, «"Salva in memoria" = vault, sempre. La memoria di Claude solo per le correzioni».

**Come si prova.** Scrivi «salva in memoria: il cliente Prova ha chiesto il preventivo entro venerdì».
Dovrebbe finire in `<cartella-vault>/Clienti/Prova.md`, non in `~/.claude/projects/...`. Poi cancella la nota di prova.

**Come si toglie.** Cancella la cartella `~/.claude/skills/salva-in-memoria/`.

## English

A small `salva-in-memoria` skill that splits the two memories: facts (clients, projects, decisions, people) go only into the right vault note, under a "## Dalle sessioni" section with Goal, Done and Open; Claude Code's own memory keeps only corrections about how to work. "Save to memory" always means the vault.

Install: copy `salva-in-memoria/` into `~/.claude/skills/salva-in-memoria/` and replace `<cartella-vault>` in SKILL.md. Optionally add the CLAUDE.md line shown above.
