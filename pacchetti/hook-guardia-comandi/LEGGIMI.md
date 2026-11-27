# Guardia dei comandi

Una regola scritta in CLAUDE.md Claude a volte la dimentica. Una regola in un hook no: prima
di ogni comando lo script la controlla e, se il comando non va, lo ferma e dice a Claude come
farlo bene. Claude legge il motivo e si corregge da solo.

Le regole sono in `regole_comandi.json`. Ne trovi tre d'esempio (push forzati, cancellazioni
ricorsive, scritture nei file `.env`): cambiale con le tue. Ogni regola ha:

- `strumento`: quale strumento guardare (`Bash`, `Write|Edit`, `WebFetch`, `mcp__.*`…);
- `se_contiene`: l'espressione regolare che fa scattare la regola;
- `tranne_se` (facoltativo): un'eccezione;
- `azione`: `deny` ferma, `ask` chiede conferma a te;
- `messaggio`: cosa leggere al posto del comando. Scrivi anche il modo giusto: è quello che
  fa correggere Claude invece di farlo riprovare uguale.

Ricordati di aggiornare `matcher` in `settings.json` se aggiungi regole su altri strumenti.

## Dove si copia

1. `guardia_comandi.py` e `regole_comandi.json` insieme in `~/.claude/hooks/`.
2. Il blocco di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`.
   Windows: `python` al posto di `python3`, o il percorso completo.

## Come si prova

    echo '{"tool_name":"Bash","tool_input":{"command":"git push origin main --force"}}' | python3 guardia_comandi.py

Deve stampare un JSON con `"permissionDecision": "deny"`. Con `--force-with-lease` non stampa niente.
Poi in Claude Code chiedi "fai git push --force": deve fermarsi e citare il messaggio.

## Come si toglie

Togli il blocco da `settings.json`. Per spegnere una sola regola, cancellala dal JSON.

## English

A PreToolUse hook that checks every command against rules in `regole_comandi.json` (tool, pattern, exception, block or ask, message). When it blocks, the message tells Claude the right way to do it, so Claude corrects itself instead of retrying. Three examples included: force pushes, recursive deletes, writes to .env files.

Install: copy `guardia_comandi.py` and `regole_comandi.json` into `~/.claude/hooks/`, add the block from `settings-esempio.json` to `~/.claude/settings.json`, then rewrite the rules with your own. Test your regular expressions: a bad one blocks harmless commands.
