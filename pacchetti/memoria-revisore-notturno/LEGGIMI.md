# Archivista di fine giornata (versione per PC del mio revisore notturno)

**Cosa fa.** A fine giornata scrivi «fine giornata» in Claude Code. Un sotto-agente legge le tue richieste delle
sessioni di oggi e le note del vault cambiate oggi, e propone fino a 15 voci: fatti da salvare nel vault,
correzioni da portare nella memoria di Claude Code, note superate, doppioni, correzioni tornate abbastanza volte
da diventare Regole d'oro. Non scrive niente da solo: la skill `fine-giornata` ti mostra le proposte una alla
volta e applica solo i tuoi sì. Un sotto-agente di Claude Code non può farti domande a metà lavoro: per questo
le domande le fa la skill.

Funziona meglio con il pacchetto `pacchetti/memoria-raccolta-sessioni/` (lo script `raccogli_sessioni.py`):
senza, l'archivista vede solo le note cambiate e quello che gli racconta la sessione.

**File.**
- `.claude/agents/archivista.md` → `~/.claude/agents/archivista.md`
- `.claude/skills/fine-giornata/SKILL.md` → `~/.claude/skills/fine-giornata/SKILL.md`

Nel file dell'agente sostituisci `<cartella-vault>`, `<cartella-memoria>` (es. `~/.claude/projects/<nome-cartella-del-progetto>/memory`)
e `<percorso>` (dove hai messo `raccogli_sessioni.py`). Su Windows i percorsi sono del tipo `C:\Users\<tuo-utente>\...`.

**Come si prova.** Modifica una nota del vault, poi in Claude Code scrivi «fine giornata». Dovresti vedere una lista
numerata con le fonti e una domanda per volta. La prima volta rispondi «no» a tutto: così verifichi che senza il
tuo sì non cambia niente (`git status` pulito).

**Come si toglie.** Cancella i due file.

**Costo.** Una corsa su Sonnet di pochi minuti, dentro l'abbonamento. Poi 3-5 minuti tuoi per approvare.

**Differenza con il mio.** Da me un revisore gira da solo ogni notte alle 4:00 su un server: legge tutte le
sessioni delle ultime ore (Claude Code, Codex, agenti, call, chat di lavoro), decide con una sola chiamata a
Sonnet e scrive senza chiedere; le Regole d'oro invece le propone con una card che approvo io. Su un PC ho
preferito la versione che chiede l'ok: il PC di notte di solito è spento, e un errore salvato in memoria resta
per settimane.

## English

An "end-of-day archivist": write "fine giornata" and a sub-agent reads today's requests and changed notes, then proposes up to 15 items (fact to save, correction, outdated note, duplicate, Golden Rule candidate), each with its source. It writes nothing itself: the `fine-giornata` skill shows them one at a time and applies only your yeses.

Install: copy `.claude/agents/archivista.md` into `~/.claude/agents/` and `.claude/skills/fine-giornata/` into `~/.claude/skills/fine-giornata/`, replace the placeholders, then write "fine giornata" in Claude Code. Works best with `pacchetti/memoria-raccolta-sessioni/`.
