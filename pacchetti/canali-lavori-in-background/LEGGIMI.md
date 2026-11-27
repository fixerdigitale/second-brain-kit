# Lavori in background con avviso

**Cosa fa.** `lavora.py` lancia una sessione di Claude Code senza finestra (`claude -p`) con il
brief che gli dai, e ti lascia libero subito. Quando finisce scrive il risultato in un file
markdown e ti manda una notifica sul desktop («Fatto: titolo» o «Non riuscito: titolo»).
Al massimo 3 lavori insieme.

**Dove si copia.** Dove vuoi, per esempio `<cartella-vault>/strumenti/lavora.py`. Serve Python 3
e il comando `claude` nel PATH (Windows, Mac o Linux). In cima al file puoi cambiare
`CARTELLA_PREDEFINITA` (di serie `~/lavori-claude`; metterla dentro il vault la rende visibile anche
dal telefono, se il vault si sincronizza).

**Come si usa.**

    python3 lavora.py "Leggi le note in clienti/X e prepara la bozza di preventivo in clienti/X/preventivo.md" --titolo "preventivo X" --cwd <cartella-vault>
    python3 lavora.py --stato

Puoi anche chiedere a Claude Code, nella chat: «lancia questo con lavora.py e intanto
continuiamo». Il brief deve bastare a una sessione che parte da zero: obiettivo, file, cosa consegnare.

**Permessi.** Di serie `--permessi acceptEdits`: Claude può modificare file nella cartella `--cwd`,
mentre i comandi che chiedono un permesso vengono negati (non c'è nessuno a cliccare «sì»).
`--permessi plan` = solo lettura e piano. Le regole `allow`/`deny` del tuo `settings.json` valgono
anche qui. Non usare `bypassPermissions` per lavori su cartelle con dati veri.

**Come si prova.** `python3 lavora.py "Scrivi la data di oggi in prova.md" --titolo prova --cwd <cartella-di-prova>`:
dopo un minuto circa deve arrivare la notifica e comparire il file del risultato.

**Limiti.** Gira solo a PC acceso: se il PC va in sospensione il lavoro si ferma. Consuma lo stesso
piano di Claude che usi in chat.

**Come si toglie.** Cancella `lavora.py` e la cartella dei risultati.

## English

`lavora.py` launches a long job (`claude -p`) in the background with a full brief, writes the result to a markdown file and sends a desktop notification when it ends (Windows, Mac, Linux). You keep working in chat meanwhile.

Install: copy `lavora.py` wherever you like (for example `<vault-folder>/strumenti/`), change `CARTELLA_PREDEFINITA` if you want results in the vault, and try it with a dummy job. In the background commands can't be approved one by one, so those that need permission are denied.
