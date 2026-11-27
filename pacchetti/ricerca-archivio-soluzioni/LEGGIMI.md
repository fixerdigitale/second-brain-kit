# Archivio soluzioni

Una cartella `soluzioni/` nel vault, una scheda markdown per ogni problema risolto, e una
skill che dice a Claude Code di cercarci prima di mettersi a diagnosticare e di scriverci
dopo aver risolto qualcosa di non banale.

## Cosa c'e'

- `SKILL.md`: la skill (nome `soluzioni`).
- `modello-scheda.md`: le sette sezioni di ogni scheda.
- `soluzioni.py`: comandi `cerca`, `mostra`, `elenco`, `nuova`, `indice`. Solo libreria
  standard, Python 3.9 o piu' recente, Mac, Windows e Linux. E' facoltativo: senza, Claude
  cerca nella cartella con i suoi strumenti.

## Dove si copia

1. Copia i tre file in `~/.claude/skills/soluzioni/` (su Windows
   `%USERPROFILE%\.claude\skills\soluzioni\`).
2. Crea la cartella `<cartella-vault>/soluzioni/`.
3. Di' allo script dove sta il vault, con una delle due variabili d'ambiente:
   `VAULT_DIR=<cartella-vault>` oppure `SOLUZIONI_DIR=<cartella-vault>/soluzioni`.
   Senza variabili usa `~/vault/soluzioni`.
4. Se vuoi, nel `CLAUDE.md` aggiungi una riga: «Prima di diagnosticare un problema tecnico
   cerca in `<cartella-vault>/soluzioni/` (skill soluzioni)».

## Come si prova

```bash
python3 ~/.claude/skills/soluzioni/soluzioni.py nuova prova-archivio
python3 ~/.claude/skills/soluzioni/soluzioni.py cerca prova
python3 ~/.claude/skills/soluzioni/soluzioni.py indice
```

Dovrebbe trovare la scheda `prova-archivio` e scrivere `INDICE.md`. Poi cancella la scheda di prova
e rilancia `indice`. In Claude Code prova con «questo errore l'abbiamo gia' visto?»: dovrebbe
aprire la skill e cercare.

## Come si toglie

Cancella `~/.claude/skills/soluzioni/` e la riga nel `CLAUDE.md`. Le schede restano nel
vault: sono note normali.

## English

An archive of solved problems: one markdown entry per problem with symptom, real cause, quick test, solution, verification, dead ends and reuse. A skill tells Claude to search it before diagnosing and to write an entry after any fix that took more than half an hour. The optional `soluzioni.py` command does search, show, list, new and index.

Install: copy `SKILL.md`, `modello-scheda.md` and `soluzioni.py` into `~/.claude/skills/soluzioni/`, create `<vault-folder>/soluzioni/` and set `VAULT_DIR` or `SOLUZIONI_DIR`. Without the script, Claude searches the folder with its own tools.
