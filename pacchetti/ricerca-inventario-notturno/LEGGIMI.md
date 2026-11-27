# Inventario di cosa c'e'

Uno script che scrive `INVENTARIO.md`: skill, agenti, comandi, hook, server MCP,
programmi installati e i **nomi** delle chiavi nei tuoi file `.env` (mai i valori).
Claude lo legge prima di dire «non ce l'ho» o di costruire uno strumento che esiste gia'.

## Cosa c'e'

- `genera_inventario.py`: solo libreria standard, Python 3.9 o piu' recente, Mac, Windows, Linux.

## Dove si copia

1. Metti lo script dove tieni i tuoi strumenti, per esempio `~/.claude/strumenti/`.
2. Lancialo dalla cartella del progetto:
   `python3 ~/.claude/strumenti/genera_inventario.py --progetto <tuo-progetto> --env <tuo-progetto>/.env`
3. Nel `CLAUDE.md` del progetto aggiungi: «Prima di dire che uno strumento non c'e', leggi
   INVENTARIO.md».

Per tenerlo aggiornato da solo hai due strade:

- **A ogni sessione** (consigliata su PC): un hook `SessionStart` in `~/.claude/settings.json`
  che lo rigenera solo se ha piu' di 20 ore.

  ```json
  {
    "hooks": {
      "SessionStart": [
        { "hooks": [ { "type": "command",
          "command": "python3 ~/.claude/strumenti/genera_inventario.py --progetto . --se-vecchio 20" } ] }
      ]
    }
  }
  ```

  Su Windows usa `python` e il percorso completo dello script se `~` non viene espanso.
- **Ogni notte**: Utilita' di pianificazione (Windows), `launchd` o `cron` (Mac). Gira solo se
  il PC e' acceso a quell'ora, per questo su PC l'hook va meglio.

## Come si prova

Lancia lo script a mano e apri `INVENTARIO.md`: dovrebbero comparire le tue skill e i server MCP.
Controlla che nella sezione chiavi ci siano solo nomi, nessun valore.

## Come si toglie

Togli l'hook da `settings.json`, cancella lo script, `INVENTARIO.md` e la riga nel `CLAUDE.md`.

## English

`genera_inventario.py` writes an INVENTARIO.md of what's really installed: skills, agents, commands, hooks, MCP servers, useful programs and only the names of keys in the .env files you point it to, never values. CLAUDE.md tells Claude to read it before saying a tool doesn't exist.

Install: copy `genera_inventario.py` into `~/.claude/strumenti/` and run it with `--progetto <your-project>` (plus `--env <file.env>` for key names). To keep it fresh, use the SessionStart hook shown above with `--se-vecchio 20`.
