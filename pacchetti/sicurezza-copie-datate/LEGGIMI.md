# Copie datate prima di modificare

Due pezzi:

- `regola-claude-md.md`: il testo da incollare nel tuo `CLAUDE.md` (globale `~/.claude/CLAUDE.md` o del progetto). Claude fa la copia da solo prima di toccare un file.
- `copia_datata.py`: lo script per farla tu (o per farla fare a Claude con un comando sempre uguale).

## Dove si copia

- La regola: in fondo al `CLAUDE.md`.
- Lo script: dove vuoi, per esempio `<cartella-vault>/strumenti/copia_datata.py`.

## Come si prova

```
python3 copia_datata.py ~/.claude/settings.json permessi
```
Deve comparire `settings.json.bak-AAAAMMGG-permessi` accanto all'originale. Rilancialo: nasce `...-2`, la prima resta.
Su Windows usa `py` al posto di `python3`.

## Come si toglie

Togli il paragrafo dal `CLAUDE.md` e cancella lo script. Le copie `.bak-*` si cancellano a mano quando non servono più.

## Nota

Nelle cartelle sotto git le copie datate servono meno: lì basta un commit prima della modifica.
Le copie servono per i file fuori da git (config del PC, file del server, documenti esportati).

## English

A CLAUDE.md rule: before modifying an important file that isn't under git, Claude makes a copy next to it with date and reason (for example `settings.json.bak-20261127-permessi`), never overwrites an existing copy, and tells you its name. The optional `copia_datata.py` makes the copy with one consistent command.

Install: paste `regola-claude-md.md` into your `CLAUDE.md`; copy `copia_datata.py` if you want the script. Inside git repos a commit is better.
