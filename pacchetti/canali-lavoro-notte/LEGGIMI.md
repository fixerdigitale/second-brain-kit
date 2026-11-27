# Lavoro della notte (coda + foglio del mattino)

**Cosa fa.** La sera scrivi in `<cartella-vault>/CODA.md` i lavori che possono andare avanti senza di
te. `coda.py` li fa girare uno dopo l'altro con `claude -p` e al mattino trovi
`<cartella-vault>/notte/AAAA-MM-GG/DA-RIVEDERE.md`: una riga per consegna, con «sì / no / correggi».
I lavori riusciti vengono segnati `[fatto]` in CODA.md; quelli falliti restano in coda.

Esempio di `CODA.md`:

    ## Riordino note call di novembre
    Leggi call/2026-11-*.md e per ognuna aggiungi in fondo la sezione "Impegni" se manca. Non cancellare niente.

    ## Bozza articolo su X
    Dalle note in idee/x.md scrivi una bozza di 800 parole in bozze/x.md.

**Dove si copia.** `coda.py` dove vuoi (es. `<cartella-vault>/strumenti/`). In cima cambia `VAULT`
con il percorso del tuo vault, oppure passa `--vault`. Serve Python 3 e `claude` nel PATH.

**Abbonamento o consumo.** Prima di pianificarlo apri Claude Code e controlla con `/status` che
usi l'abbonamento. Se nell'ambiente c'è `ANTHROPIC_API_KEY`, `claude -p` pagherebbe a consumo:
per questo `coda.py` in quel caso non parte e lo dice. Se vuoi davvero pagare a token, lancialo
con `--anche-a-consumo`.

**Permessi.** Di serie i lavori girano con `acceptEdits`: possono modificare i file del vault,
mentre i comandi che chiedono permesso vengono negati. Se il vault non è sotto git, `coda.py` non
usa `acceptEdits` e passa a `default` (le modifiche ai file vengono negate), perché senza una
storia dei file una modifica sbagliata della notte non si annulla. Lo scrive anche in
`DA-RIVEDERE.md`. Per farli scrivere: `git init` e un primo commit nel vault.

**Come si fa partire di notte (solo a PC acceso e non in sospensione).**
- Windows, Utilità di pianificazione: ogni giorno alle 01:00, `python` con argomento il percorso di
  `coda.py`; nella scheda Condizioni spunta «Riattiva il computer per eseguire questa attività».
- Mac: `crontab -e` e `0 1 * * * python3 <percorso>/coda.py`; per svegliare il Mac serve
  `pmset repeat wakeorpoweron`.

**Regole che ti consiglio di scrivere nei brief.** Niente messaggi a persone, niente cancellazioni,
niente pubblicazioni: di notte si prepara, di giorno si decide.

**Come si prova.** `python3 coda.py --prova` elenca cosa farebbe e con quali permessi, senza lanciare
niente. Poi un lavoro finto («scrivi la data in prova.md») lanciato a mano. Io l'ho provato il
27/11/2026 con un `claude` finto: fermo con la chiave nell'ambiente, `default` senza git,
`acceptEdits` con git.

**Come si toglie.** Cancella l'attività pianificata, `coda.py` e, se vuoi, la cartella `notte/`.

## English

`coda.py` runs at night the jobs you listed in `CODA.md` (a "## title" plus the brief underneath), one after another, and writes `DA-RIVEDERE.md` with a yes/no for each delivery to review in the morning. Nothing gets sent to anyone at night.

Install: copy `coda.py`, set `VAULT` to your vault path, write jobs in `CODA.md` and schedule it at night with Task Scheduler (Windows, with "Wake the computer to run this task") or cron (Mac). It doesn't read plan usage: it only stops at a fixed time (7 am), so keep the queue short. The PC must stay on and awake.

Before scheduling it, check with `/status` in Claude Code that it uses your subscription. If `ANTHROPIC_API_KEY` is in the environment, `claude -p` would bill per token, so `coda.py` doesn't start and says so; `--anche-a-consumo` runs it anyway. Jobs run with `acceptEdits` (they can edit vault files; commands that need permission are denied), but only if the vault is under git: without it `coda.py` falls back to `default` (file edits denied), because without file history a bad night edit can't be undone. It notes this in `DA-RIVEDERE.md` too.
