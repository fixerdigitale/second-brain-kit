# Contro-parere

**Cosa fa.** Una skill che toglie a Claude l'abitudine di darti ragione. Controlla sulla fonte i fatti che riporti, sulle scelte importanti scrive prima il suo parere e poi lo confronta con il tuo, e quando non siete d'accordo risponde solo in tre forme: TENGO, CAMBIO, VERIFICO.

**Dove si copia.** La cartella `contro-parere/` in `~/.claude/skills/contro-parere/` (vale in tutti i progetti) oppure in `<tuo-progetto>/.claude/skills/contro-parere/`.
Per averla sempre accesa senza nominarla, aggiungi al tuo `CLAUDE.md`:

```
Contro-parere sempre attivo: segui la skill contro-parere. «Esegui e basta» la spegne per quel messaggio.
```

Prima di usarla, sistema la tabella della sezione 1 con le tue fonti vere (dove tieni call, note, task).

**Come si prova.** Scrivi a Claude un fatto sbagliato che può controllare, per esempio «nel file `<una nota del vault>` c'è scritto che la scadenza è venerdì» quando non è vero. La risposta giusta comincia con «La nota dice …, tu dici …: quale vale?».

**Come si toglie.** Cancella la cartella `contro-parere` e la riga nel `CLAUDE.md`.

## English

A `contro-parere` (counter-opinion) skill that keeps Claude from agreeing by default: it checks the facts you report against the sources, writes its own opinion before reading yours on important choices, and when you disagree answers only as HOLD, CHANGE or VERIFY. "Esegui e basta" ("just do it") turns it off for one message.

Install: copy `contro-parere/` into `~/.claude/skills/`, adapt the sources table to yours, and add the CLAUDE.md line shown above to keep it always on (the skill has `disable-model-invocation: true`). The skill text is in Italian.
