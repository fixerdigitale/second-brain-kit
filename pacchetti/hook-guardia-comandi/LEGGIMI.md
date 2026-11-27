# Guardia dei comandi

Una regola scritta in CLAUDE.md Claude a volte la dimentica. Una regola in un hook non
dipende dalla sua memoria: prima di ogni comando lo script la controlla e, se il comando non va, lo ferma
e dice a Claude come farlo bene. Claude legge il motivo e di solito si corregge da solo.

**È un promemoria, non una barriera.** Le espressioni regolari coprono le forme che hai
previsto, non tutte quelle possibili: un alias, uno script o una variabile passano. Per me
serve a correggere gli errori ripetuti, non a fermare chi vuole aggirarla. Per bloccare
davvero uso `permissions.deny` in `settings.json` (pacchetto `sicurezza-permessi-deny-ask`), per esempio:

```json
{
  "permissions": {
    "deny": [
      "Bash(git push --force:*)",
      "Bash(git push -f:*)",
      "Bash(rm -rf:*)"
    ]
  }
}
```

Anche il `deny` ragiona sulle forme che scrivi: le cose che non devono succedere mai le
proteggo anche fuori da Claude (ramo protetto su GitHub, copie di backup).

Le regole sono in `regole_comandi.json`. Ne trovi tre d'esempio: push forzati (`--force`, `-f`,
`-uf`, il `+` davanti al ramo come in `origin +main`; passa solo `--force-with-lease` senza `+`),
cancellazioni ricorsive forzate (`rm -rf`, `rm -r -f`, `rm --recursive --force` e simili) e
scritture nei file `.env`. Cambiale con le tue. Ogni regola ha:

- `strumento`: quale strumento guardare (`Bash`, `Write|Edit`, `WebFetch`, `mcp__.*`…);
- `se_contiene`: l'espressione regolare che fa scattare la regola;
- `tranne_se` (facoltativo): un'eccezione, che vale solo per il pezzo di comando in cui compare;
- `azione`: `deny` ferma, `ask` chiede conferma a te;
- `messaggio`: cosa leggere al posto del comando. Scrivi anche il modo giusto: è quello che
  fa correggere Claude invece di farlo riprovare uguale.

Per Bash la guardia divide il comando in pezzi su `;`, `&&`, `||`, `|`, `&` e a capo, e valuta
ogni regola pezzo per pezzo. Così `git push --force-with-lease; git push -f` si ferma lo stesso:
l'eccezione del primo pezzo non copre il secondo. La divisione non capisce le virgolette, quindi
a volte ferma un comando innocuo (per esempio un messaggio di commit che contiene «push -f»).

Se aggiungi regole su altri strumenti, aggiorna `matcher` in `settings.json`.

## Dove si copia

1. `guardia_comandi.py` e `regole_comandi.json` insieme in `~/.claude/hooks/`.
2. Il blocco di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`.
   Windows: `python` al posto di `python3`, o il percorso completo.

## Come si prova

    echo '{"tool_name":"Bash","tool_input":{"command":"git push origin main --force"}}' | python3 guardia_comandi.py

Deve stampare un JSON con `"permissionDecision": "deny"`. Con `--force-with-lease` non stampa niente.
Prova anche le varianti che ti interessano, per esempio `git push origin +main`,
`cd x && git push -f` e `rm -r -f build` (questo deve stampare `"ask"`).
Io l'ho provato così il 27/11/2026, con 25 comandi fra forme da fermare e forme da lasciar passare.
Poi in Claude Code chiedi "fai git push --force": deve fermarsi e citare il messaggio.

## Come si toglie

Togli il blocco da `settings.json`. Per spegnere una sola regola, cancellala dal JSON.

## English

A PreToolUse hook that checks every command against rules in `regole_comandi.json` (tool, pattern, exception, block or ask, message). When it blocks, the message tells Claude the right way to do it, so Claude usually corrects itself instead of retrying. Three examples included: force pushes (`--force`, `-f`, `-uf`, a `+` before the branch as in `origin +main`; only `--force-with-lease` without `+` gets through), forced recursive deletes (`rm -rf`, `rm -r -f`, `rm --recursive --force` and similar), writes to .env files. For Bash the command is split into pieces on `;`, `&&`, `||`, `|`, `&` and newlines, and each rule (exception included) is checked piece by piece.

It's a reminder, not a barrier: regular expressions cover the forms you foresaw, not every possible one (an alias, a script or a variable gets through). To actually block, I use `permissions.deny` in `settings.json` (package `sicurezza-permessi-deny-ask`), for example `"deny": ["Bash(git push --force:*)", "Bash(git push -f:*)", "Bash(rm -rf:*)"]`, and for things that must never happen I also protect them outside Claude (protected branch on GitHub, backups).

Install: copy `guardia_comandi.py` and `regole_comandi.json` into `~/.claude/hooks/`, add the block from `settings-esempio.json` to `~/.claude/settings.json`, then rewrite the rules with your own. Test your regular expressions: a bad one blocks harmless commands.
