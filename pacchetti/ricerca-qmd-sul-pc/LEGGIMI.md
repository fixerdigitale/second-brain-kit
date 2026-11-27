# Ricerca per significato sul PC con QMD

QMD e' un motore di ricerca locale per cartelle di markdown: parole esatte (BM25), ricerca per
significato (vettori) e riordino dei risultati con un piccolo modello, tutto sul PC, senza
servizi esterni. Ha un server MCP, quindi Claude Code lo usa come uno strumento.

QMD non è mio: non lo ricopio qui. Io non l'ho installato, perché sul server ho già la ricerca per significato; su un PC senza ricerca è l'opzione che proverei per prima. Fonte ufficiale: https://github.com/tobi/qmd
(pacchetto npm `@tobilu/qmd`). Attenzione: esistono fork e progetti diversi con lo stesso
nome; installa solo da `tobi/qmd`.

## Cosa c'e' in questo pacchetto

- `mcp.json.esempio`: la voce da aggiungere al `.mcp.json` del progetto.
- `CLAUDE-riga.md`: le righe da incollare nel `CLAUDE.md` perche' Claude lo usi davvero.

## Come si mette

Comandi presi dalla documentazione di QMD a novembre 2026: se nel frattempo cambiano, vale
il README ufficiale.

1. Serve Node.js. Installa: `npm install -g @tobilu/qmd`
2. Registra il vault come raccolta: `qmd collection add <cartella-vault> --name vault`
3. Crea l'indice dei significati: `qmd embed` (la prima volta scarica i modelli locali e ci
   mette un po'; poi aggiorna solo le note cambiate).
4. Aggiungi a `<tuo-progetto>/.mcp.json` la voce di `mcp.json.esempio`, oppure usa il plugin
   per Claude Code indicato nel README di QMD.
5. Incolla `CLAUDE-riga.md` nel `CLAUDE.md`.

## Come si prova

- Da terminale: `qmd query "come avevo deciso i prezzi"` dovrebbe tirare fuori note che non
  contengono quelle parole esatte ma parlano di quello.
- In Claude Code: `/mcp` dovrebbe mostrare `qmd` collegato; poi chiedi qualcosa che sta nel vault.

## Tenere l'indice aggiornato

Le note nuove entrano nell'indice quando rilanci `qmd embed` (e `qmd update` per le parole).
Puoi farlo a mano, con un hook `SessionStart`, o con un'attivita' pianificata: gira solo a PC acceso.

## Come si toglie

Togli la voce `qmd` dal `.mcp.json` e le righe dal `CLAUDE.md`, poi `npm uninstall -g @tobilu/qmd`.
L'indice sta in una cartella di cache di QMD (vedi README) e si puo' cancellare. Le note non
vengono toccate.

## English

Setup notes for QMD (https://github.com/tobi/qmd), a local search engine over markdown folders that combines keyword search, search by meaning and re-ranking, all on your PC, with an MCP server Claude Code can use. I haven't installed it myself: on my server I use a different search by meaning.

Install: follow the steps above (npm package `@tobilu/qmd`, only from tobi/qmd), add the entry from `mcp.json.esempio` to your `.mcp.json` and the lines from `CLAUDE-riga.md` to your CLAUDE.md. Rerun the indexing to keep it updated. Commands come from the November 2026 docs: if they changed, the README wins.
