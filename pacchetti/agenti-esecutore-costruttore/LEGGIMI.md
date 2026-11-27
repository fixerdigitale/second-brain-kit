# Esecutore e costruttore: due sotto-agenti economici

**Cosa fa.** Due sotto-agenti di Claude Code. L'esecutore gira su Haiku e fa lavori meccanici (cercare, leggere log, contare, modifiche già decise). Il costruttore gira su Sonnet e scrive codice già deciso. La sessione principale (di solito Opus) decide e rivede; il lavoro ripetitivo va a loro e consuma meno della tua quota.

**Dove si copia.**
- Per tutti i progetti: `~/.claude/agents/esecutore.md` e `~/.claude/agents/costruttore.md`
  (Windows: `C:\Users\<tuo-utente>\.claude\agents\`).
- Solo per un progetto: `<tuo-progetto>/.claude/agents/`.

**Come si prova.** Apri una sessione nuova di Claude Code e scrivi `/agents`: devono comparire tutti e due. Poi chiedi: «usa l'esecutore per contare quanti file .md ci sono in <cartella-vault>». Nella risposta vedi che il lavoro è passato dal sotto-agente.

**Come si toglie.** Cancella i due file `.md`. Nient'altro da annullare.

**Nota.** Il campo `model:` accetta `haiku`, `sonnet`, `opus` o `inherit`. Se il tuo piano non comprende un modello, metti `inherit`.

## English

Two cheap Claude Code sub-agents. The executor (Haiku) does only mechanical work (searching files, reading logs, counting, applying an already-decided fix) and stops to ask when a choice is needed. The builder (Sonnet) writes code that has already been decided, follows the existing style and stops if the decision doesn't hold. The main session decides and reviews.

Install: copy `.claude/agents/esecutore.md` and `.claude/agents/costruttore.md` into `~/.claude/agents/` (or your project's `.claude/agents/`), then run `/agents` to check they show up. The agent instructions are in Italian; Claude follows them fine, but you can translate them.
