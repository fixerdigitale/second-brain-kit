# Pipeline di lavoro

**Cosa fa.** Una skill e due file modello. La skill, a ogni richiesta, decide se è un'informazione o un lavoro; per un lavoro cerca la pipeline (tipo di lavoro × cliente), la segue un passo alla volta chiedendo l'ok prima e dopo, e scrive ogni tua correzione nel posto giusto: nel pezzo generale se vale per tutti, nelle Direttive del cliente se vale solo per lui. Così le correzioni non si perdono a fine sessione.

**Cosa c'è.**
- `pipeline-lavoro/SKILL.md` — la skill.
- `modelli/PIPELINE-LAVORO.md` — il documento da riempire (tipi di lavoro, taglie, pezzi, Direttive, pipeline, registrazioni).
- `modelli/STORICO.md` — il registro delle correzioni.

**Dove si copia.**
1. `pipeline-lavoro/` in `~/.claude/skills/pipeline-lavoro/`.
2. I due modelli in `<cartella-vault>/pipeline-lavoro/`.
3. Nella skill sostituisci `<cartella-vault>` con il percorso vero.
4. Facoltativo, per averla sempre: nel `CLAUDE.md` una riga «Ogni richiesta nuova passa dalla skill pipeline-lavoro».

All'inizio il documento è quasi vuoto, ed è giusto così: si riempie lavorando. Le prime settimane quasi tutto sarà «Registrazione».

**Come si prova.** Chiedi «partiamo con una landing per Cliente 1». La risposta deve dire «Seguo CL1-1», la taglia, e fermarsi su «Faccio il passo 1: …?». Poi correggi un passo («il modulo sempre in alto») e controlla che compaia nelle Direttive e una riga nello STORICO.

**Come si toglie.** Cancella `~/.claude/skills/pipeline-lavoro/` e la riga nel `CLAUDE.md`. I file nel vault puoi tenerli: sono solo note.

## English

A `pipeline-lavoro` skill plus two templates (`PIPELINE-LAVORO.md` and its history). For each request the skill decides whether it's information or a job; for a job it finds the type × client pipeline, follows it one step at a time with a check before and after, and writes every correction into the shared piece or the client's directives, plus a history line.

Install: copy the skill into `~/.claude/skills/pipeline-lavoro/` and the templates from `modelli/` into `<vault-folder>/pipeline-lavoro/`, then replace the path placeholder. The document starts almost empty on purpose.
