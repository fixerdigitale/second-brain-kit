# Lavori lunghi su Codex (Claude decide, ChatGPT esegue)

**Cosa fa.** Se paghi sia Claude sia ChatGPT, i lavori lunghi (pagine, script grossi) li fa Codex con l'abbonamento ChatGPT, mentre Claude scrive il brief e controlla il risultato. Così la quota di Claude resta per decidere e rivedere.

**Richiede.** Codex CLI installata (`npm install -g @openai/codex`) e collegata al tuo account ChatGPT (`codex login`). Funziona su Windows, Mac e Linux.

**Dove si copia.** `.claude/skills/lavoro-lungo-codex/SKILL.md` → `~/.claude/skills/lavoro-lungo-codex/SKILL.md`.

**Come si prova.** In un progetto di prova (cartella con `git init`) chiedi: «passa a Codex: crea una pagina HTML che elenca i file .md di questa cartella». Controlla che compaiano `BRIEF-…md`, `CONSEGNA.md` e che Claude ti dica cosa ha verificato.

**Come si toglie.** Cancella la cartella della skill. Codex resta installato finché non lo disinstalli (`npm uninstall -g @openai/codex`).

**Attenzione.** `--sandbox workspace-write` lascia scrivere Codex solo nella cartella indicata. Non usare `--dangerously-bypass-approvals-and-sandbox`.

## English

A skill that hands long jobs (pages, components, long scripts, integrations) to OpenAI's Codex CLI, using a ChatGPT subscription you already pay for. Claude writes the brief to a file, launches `codex exec`, then checks the delivery itself before telling you it's done.

Install: `npm install -g @openai/codex`, run `codex login` with your ChatGPT account, then copy `.claude/skills/lavoro-lungo-codex/` into `~/.claude/skills/lavoro-lungo-codex/`. Don't use it on client data you promised to keep with a single provider.
