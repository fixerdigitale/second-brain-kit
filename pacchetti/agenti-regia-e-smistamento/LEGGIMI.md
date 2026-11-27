# Regia e smistamento

**Cosa fa.** Due skill che lavorano insieme.
- `smistamento`: prima di ogni lavoro decide chi lo fa in base alla taglia (la sessione stessa,
  l'esecutore su Haiku, il costruttore su Sonnet, un agente per lavori lunghi) e lo dice in una riga.
- `delega-con-controllo`: quando il lavoro va a qualcun altro, la sessione principale scrive un
  brief corto con i criteri di «fatto», fa partire ogni giro in una sessione nuova e controlla i
  file prima di riferire. Massimo 2 giri di correzione, poi te lo dice.

La prima evita di spendere il modello più caro su lavori meccanici. La seconda evita i «fatto»
che non sono veri.

**Richiede.** I sotto-agenti del pacchetto `agenti-esecutore-costruttore`. La riga «lavori
lunghi» della tabella è facoltativa: se non usi Codex o un altro agente, cancellala.

**Dove si copia.**
- `.claude/skills/smistamento/SKILL.md` in `~/.claude/skills/smistamento/`;
- `.claude/skills/delega-con-controllo/SKILL.md` in `~/.claude/skills/delega-con-controllo/`.

Perché valgano senza nominarle, aggiungi al tuo `CLAUDE.md` una riga: «Prima di ogni lavoro che
dura più di qualche minuto, segui la skill smistamento; se deleghi, la skill delega-con-controllo».
Se vuoi che arrivi anche un promemoria nel momento giusto, c'è il pacchetto `hook-smistatore-procedure`.

**Come si prova.**
1. Chiedi «riassumi gli ultimi 50 file di log in <cartella>». La risposta deve dire a chi passa
   il lavoro (dovrebbe essere l'esecutore).
2. Chiedi un lavoro piccolo da delegare («fai scrivere al costruttore uno script che conta le note
   per cartella in <cartella-vault>»). Nel messaggio al sotto-agente ci deve essere il blocco
   «Fatto quando», e alla fine la sessione deve dire cosa ha verificato lei.

**Come si toglie.** Cancella le due cartelle delle skill e la riga nel `CLAUDE.md`.

## English

Two skills that make Claude act as a director. `smistamento` routes each job by size (do it now, executor, builder, long-jobs agent, or keep it on the main model) and says in one line who gets it. `delega-con-controllo` defines how to delegate: a short brief with "done when" criteria, a fresh session per round, a check of the touched files before reporting, at most 2 correction rounds.

Install: copy `.claude/skills/smistamento/` and `.claude/skills/delega-con-controllo/` into `~/.claude/skills/`, then add a line to your `CLAUDE.md` that points to them (see above). Works best with the executor/builder sub-agents and the routing hook (`pacchetti/hook-smistatore-procedure/`).
