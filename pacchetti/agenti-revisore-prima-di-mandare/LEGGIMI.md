# Revisore prima di mandare

**Cosa fa.** Un sotto-agente che rilegge un lavoro prima che parta (email, documento, pagina, codice) e dà APPROVATO, RESPINTO o NON VERIFICABILE. Non corregge: chi ha fatto il lavoro sistema, poi si rilancia la revisione. Massimo due respinte sulla stessa cosa, poi decidi tu.

**Dove si copia.** `.claude/agents/revisore.md` → `~/.claude/agents/revisore.md`. Se vuoi spendere meno, cambia `model: opus` in `model: sonnet`.

**Come si usa.** «Prima di mandarla, passa l'email al revisore. La richiesta era: <...>». Oppure aggiungi al tuo `CLAUDE.md`: «Prima di pubblicare o mandare qualcosa a terzi, lancia il revisore».

**Secondo parere con Codex (facoltativo, se hai ChatGPT).** Con la CLI di Codex installata e collegata al tuo account ChatGPT, puoi chiedere a un modello diverso di rileggere in sola lettura:
```
codex exec --sandbox read-only "Rileggi <file>. La richiesta era: <...>. Dai APPROVATO, RESPINTO con la lista dei problemi o NON VERIFICABILE. Non modificare file."
```
Due modelli diversi sbagliano in modi diversi: dove sono d'accordo puoi fidarti di più, dove divergono guardi tu. Se preferisci una skill già pronta, c'è `codex` del pacchetto gstack (link nella scheda).

**Come si prova.** Scrivi una bozza di email con un errore voluto (una data sbagliata rispetto a una nota del vault) e chiedi la revisione: deve tornare RESPINTO con quell'errore.

**Come si toglie.** Cancella il file (e la riga nel `CLAUDE.md`, se l'hai aggiunta).

## English

A reviewer sub-agent with fresh eyes, used before sending or publishing anything that matters. It didn't write the work and doesn't fix it: it rereads the original request, checks facts, numbers, links, what the recipient sees and data that must not leak, and returns APPROVED, REJECTED (with a list) or NOT VERIFIABLE.

Install: copy `.claude/agents/revisore.md` into `~/.claude/agents/`. Optional second opinion: the codex skill from https://github.com/garrytan/gstack, after a security check.
