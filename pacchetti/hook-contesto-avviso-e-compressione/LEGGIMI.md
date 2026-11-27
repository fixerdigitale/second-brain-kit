# Avviso di contesto e compressione automatica

Due pezzi che da me lavorano insieme: un avviso quando la sessione diventa grande, e la
compressione che parte da sola a una soglia scelta da te, senza fermarti.

## 1. L'avviso (hook)

`avviso_contesto.py` è un hook `UserPromptSubmit`: a ogni tuo messaggio guarda quanto è grande
la conversazione. Sopra la prima soglia aggiunge un avviso, una volta sola, che Claude ti
riferisce in una riga («siamo a 130k, delego le letture a un sotto-agente»). Sopra la soglia alta
gli chiede, a ogni turno, di aggiornare `HANDOFF.md` prima che la sessione venga compressa.

Soglie in cima al file (`SOGLIA_AVVISO`, `SOGLIA_ALTA`) o con le variabili d'ambiente
`AVVISO_CONTESTO_SOGLIA` e `AVVISO_CONTESTO_ALTA`. Con una finestra da 200k, 120k e 170k sono un
buon inizio. Io, con la finestra da 1 milione, uso 250k e 450k.

## 2. La compressione automatica (due impostazioni)

- `autoCompactWindow`: la finestra su cui Claude Code calcola quando comprimere da solo. Nella
  versione che uso io il punto di compressione è circa finestra − 33k: con 480000 la sessione si
  comprime verso 447k. Serve solo con i modelli dalla finestra grande (1 milione): con 200k
  comanda il limite del modello e questo valore non cambia niente.
- `idleCompaction`: se la sessione resta ferma a lungo (nella mia versione circa un'ora) ed è
  grande, Claude Code la comprime mentre non la usi, così al ritorno il primo messaggio non
  rilegge tutto. Nella mia versione è già accesa di serie; `false` la spegne.

Verificato sulla versione 2.1.330 di Claude Code. I nomi possono cambiare: se dopo averle messe
non succede niente, la tua versione non le ha.

Da me c'è anche una mod dell'app desktop che comprime a fine turno se la compressione automatica
è spenta. Non è nel pacchetto: usa funzioni dell'app che non sono portabili.

## Dove si copia

1. `avviso_contesto.py` in `~/.claude/hooks/` (crea la cartella se non c'è).
2. Da `settings-esempio.json` in `~/.claude/settings.json`: le due chiavi al primo livello e il
   blocco sotto `"hooks"`. Se hai già altri hook su `UserPromptSubmit`, aggiungi questo alla
   lista, non sostituirla.
3. Windows: se `python3` non esiste, scrivi `python`, o il percorso completo
   (`python "C:/Users/<tuo-utente>/.claude/hooks/avviso_contesto.py"`).

Va insieme a `hook-handoff-prima-compressione`: comprimere da solo senza salvare lo stato fa
perdere il filo.

## Come si prova

Prova a mano, senza Claude Code (deve stampare niente o un JSON, mai un errore):

    echo '{"transcript_path": "non-esiste.jsonl", "session_id": "prova"}' | python3 avviso_contesto.py

Poi metti per un momento `SOGLIA_AVVISO = 1000`, apri una sessione nuova e scrivi due messaggi:
al secondo Claude ti dice a quanti token è. Rimetti la soglia vera.

## Come si toglie

Togli il blocco dell'hook e le due chiavi da `settings.json`, cancella il file. I segni «avviso
già dato» stanno nella cartella temporanea del sistema (`claude-avviso-contesto`).

## English

A UserPromptSubmit hook that reads the size of the conversation and, above a first threshold, adds a one-time warning for Claude (delegate reads and searches to a sub-agent); above a high threshold it asks Claude to update the HANDOFF every turn. Plus two settings that let automatic compaction start by itself near a large window.

Install: copy `avviso_contesto.py` into `~/.claude/hooks/` and copy the two keys and the hook block from `settings-esempio.json` into `~/.claude/settings.json`. Thresholds are at the top of the script. Setting names were verified on Claude Code 2.1.330; pair it with `pacchetti/hook-handoff-prima-compressione/`.
