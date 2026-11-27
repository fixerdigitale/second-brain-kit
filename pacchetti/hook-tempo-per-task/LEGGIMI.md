# Tempo per task, contato dagli hook

Conta da solo quanto tempo lavori con Claude su ogni task, senza cronometri da avviare. Ogni
tuo messaggio, ogni strumento usato e ogni fine turno lascia un segno con ora, cartella e task;
il riepilogo somma i tratti fra due segni a meno di 15 minuti.

Da me ogni sessione è legata a una task della board e la board mostra a chi coordina il lavoro
quali task sono «live» adesso, con i minuti sommati. Quella versione scrive su un database su un
server. Questa è la versione minima per PC: la task la dici tu, i segni vanno in un file.

## Come dici su quale task lavori

- Nel messaggio a Claude: `#task landing-corso`. Vale per quella sessione finché non ne scrivi
  un'altra; `#task fine` la chiude.
- Per una cartella intera: dalla cartella del lavoro, `python3 ~/.claude/hooks/registro_tempo.py task report-mese`.
- Senza task, il tempo va sotto «(senza task)» con il nome della cartella.

Riepilogo:

    python3 ~/.claude/hooks/registro_tempo.py riepilogo 30

    2026-11-24   2h 15m  landing-corso
    2026-11-24   0h 40m  (senza task) note

## Dove si copia

1. `registro_tempo.py` in `~/.claude/hooks/`.
2. I tre blocchi di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`,
   aggiunti a quelli che hai già. Windows: `python` al posto di `python3`, o il percorso completo.

## Come si prova

1. In una sessione scrivi `#task prova-tempo` e lavora qualche minuto.
2. `python3 ~/.claude/hooks/registro_tempo.py riepilogo 1` deve mostrare `prova-tempo`.

Io l'ho provato con eventi finti il 27/11/2026: una sessione con `#task`, una senza, e una task
data per cartella.

## Cosa non conta

Conta il tempo con Claude aperto e attivo, non il tempo di lavoro totale: call e lavoro fuori da
Claude non ci sono. Due sessioni in parallelo sulla stessa task non raddoppiano il tempo.

## Come si toglie

Togli i tre blocchi da `settings.json`. Il registro è `~/.claude/registro-tempo.jsonl` (solo
orari, cartelle e nomi delle task, nessun testo) e le task attive sono in
`~/.claude/task-attive.json`: cancellali se non ti servono.

## English

Three hooks (UserPromptSubmit, PostToolUse, Stop) that log time per task: write "#task name" in a message (or assign a task to a folder) and they record time, folder and task to a file. Pauses over 15 minutes don't count; two sessions on the same task don't double up. A command prints a summary by day and task.

Install: copy `registro_tempo.py` into `~/.claude/hooks/` and the three blocks from `settings-esempio.json` into `~/.claude/settings.json`. Summary of the last 30 days: `python3 ~/.claude/hooks/registro_tempo.py riepilogo 30`. It only counts time with Claude active.
