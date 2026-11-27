# Stato vero a inizio sessione

A ogni sessione nuova Claude riceve da solo:

- data, giorno e ora di oggi (così "venerdì prossimo" o "ieri" li calcola giusto);
- le prime 40 righe dei file che scegli tu, con la data di ultima modifica.

Serve quando hai un file che dice com'è la situazione *adesso* (progetti in corso, cosa è
attivo, cosa è spento) e non vuoi che Claude si basi su una memoria vecchia.

## Dove si copia

1. `stato_inizio.py` e `stato_file.txt` insieme in `~/.claude/hooks/`.
2. In `stato_file.txt` scrivi i percorsi dei tuoi file, uno per riga (togli il `#` davanti).
   Pochi e corti: tutto quello che scrivi lì entra in ogni sessione e occupa contesto.
3. Il blocco di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`.
   `matcher: "startup"` = solo sessioni nuove (non quelle riprese o compresse).
   Windows: `python` al posto di `python3`, o il percorso completo.

## Come si prova

    echo '{}' | python3 stato_inizio.py

Deve stampare un JSON con la data di oggi e il contenuto dei tuoi file. Poi apri una sessione
nuova e chiedi "che giorno è e cosa c'è in corso?".

## Come si toglie

Togli il blocco da `settings.json` e cancella i due file.

## English

A SessionStart hook that puts today's date and time into the context, plus the first lines of the state files you choose (ongoing projects, what's active) with their modification date, so the real current state wins over old memory.

Install: copy `stato_inizio.py` and `stato_file.txt` into `~/.claude/hooks/`, list your paths in the `.txt` and add the block from `settings-esempio.json` to `~/.claude/settings.json`. Keep the list short: everything in it enters every session.
