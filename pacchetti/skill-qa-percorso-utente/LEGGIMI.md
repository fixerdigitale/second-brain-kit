# QA sul percorso utente

**Cosa fa.** Prima di dire «la pagina va», Claude rifà il percorso di un utente vero in un browser, a desktop e telefono: clicca, compila, invia, guarda console e rete, apre la pagina di ringraziamento. Ogni difetto ha una prova; dopo la correzione rifà tutto il percorso dall'inizio. Chiude con un voto e un report corto.

**Dove si copia.** `qa-percorso-utente/` in `~/.claude/skills/qa-percorso-utente/`.
Serve un browser comandabile da Claude Code, per esempio Chrome DevTools MCP:
`claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest` (serve Node.js).

**Come si prova.** Chiedi «fai la QA del modulo contatti su <una tua pagina>». Devono uscire screenshot a 1440 e 393, l'elenco dei difetti con la prova, un voto.

**Come si toglie.** Cancella `~/.claude/skills/qa-percorso-utente/` e, se non ti serve più, `claude mcp remove chrome-devtools`.

## English

A `qa-percorso-utente` skill that tests a page the way a real user would, in a browser at 1440 px and 393 px: it clicks, fills in, submits, watches console and network, opens linked pages, records evidence for every defect, and after a fix replays the whole path (at most 3 rounds). It ends with a score; below 8, don't deliver.

Install: copy `qa-percorso-utente/` into `~/.claude/skills/` and add Chrome DevTools MCP (https://github.com/ChromeDevTools/chrome-devtools-mcp, needs Node.js).
