# HANDOFF prima della compressione

Quando una sessione si riempie, Claude Code la comprime: tiene un riassunto e perde i dettagli.
Questo pacchetto mette tre reti:

1. **Prima della compressione** (hook `PreCompact`): salva le tue ultime 15 richieste della
   sessione in `~/.claude/handoff-backup/<id-sessione>.md`.
2. **Subito dopo** (hook `SessionStart` con `matcher: "compact"`): dice a Claude di rileggere
   `HANDOFF.md`, confrontarlo con le richieste salvate e aggiornarlo prima di continuare.
3. **A mano, quando vuoi**: il comando `/salva-handoff` fa scrivere a Claude la sezione nuova di
   `HANDOFF.md` (richiesta, fatto, decisioni, file, aperto, prossimo passo).

Differenza onesta con la versione che uso io: la mia non è un hook di `settings.json` ma una
mod dell'app desktop di Claude Code, e fa scrivere l'HANDOFF *prima* della compressione, con una
copia della sessione. Con gli hook normali di Claude Code questo non si
può fare (durante `PreCompact` il modello non risponde), quindi qui l'HANDOFF si aggiorna
*subito dopo*, partendo dal riassunto più le tue richieste salvate.

## Dove si copia

1. `handoff_compressione.py` in `~/.claude/hooks/`.
2. `commands/salva-handoff.md` in `~/.claude/commands/` (vale in tutti i progetti) oppure in
   `<tuo-progetto>/.claude/commands/` (solo lì).
3. Il blocco di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`, aggiunto
   agli hook che hai già. Windows: `python` al posto di `python3`, o il percorso completo.

## Come si prova

1. In una sessione con qualche messaggio scrivi `/compact`.
2. Controlla che esista `~/.claude/handoff-backup/<id-sessione>.md` con le tue richieste.
3. Al primo messaggio dopo, Claude deve dirti che ha riletto (o creato) `HANDOFF.md`.
4. Scrivi `/salva-handoff`: deve comparire una sezione datata in cima a `HANDOFF.md`.

## Come si toglie

Togli i due blocchi da `settings.json`, cancella lo script e `salva-handoff.md`.
La cartella `~/.claude/handoff-backup/` contiene i tuoi messaggi: cancellala quando non serve.
Non metterla nel backup su GitHub se nei messaggi scrivi cose dei clienti.

## English

Saves the project state around compaction. A PreCompact hook saves your last 15 requests (passwords and keys masked); a SessionStart hook with the `compact` matcher tells Claude to reread HANDOFF.md, compare it with those requests and update it before continuing. A `/salva-handoff` command does it by hand.

Install: copy `handoff_compressione.py` into `~/.claude/hooks/`, `commands/salva-handoff.md` into `~/.claude/commands/` and the two blocks from `settings-esempio.json` into `~/.claude/settings.json`. Test it with a `/compact`. You need a HANDOFF.md per project first (`pacchetti/memoria-handoff-e-sistema/`).
