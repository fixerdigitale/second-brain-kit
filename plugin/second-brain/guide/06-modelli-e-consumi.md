# 06 · Modelli, impegno e consumi

I numeri esatti di limiti e prezzi cambiano spesso. Questa guida spiega come ragionare; per i numeri di oggi guarda sempre le pagine ufficiali (link in fondo) o chiedi a Claude di controllarle.

## Modello e impegno

Claude ha più **modelli**, come persone più o meno esperte. Più il modello è capace, più consuma.

| Modello | Com'è | Per cosa |
|---|---|---|
| **Haiku** | il più piccolo e veloce, consuma poco | cercare, contare, copiare dati già decisi, controlli meccanici |
| **Sonnet** | il medio, lavora bene e consuma il giusto | la maggior parte del lavoro: report, fogli, pagine semplici, ritocchi |
| **Opus** | il più capace, consuma di più | analisi difficili, decisioni, testi importanti, lavori lunghi con tanti file |

I nomi e le versioni cambiano: l'elenco aggiornato lo vedi con il comando `/model` o nel selettore del modello dell'app. Possono comparire anche altri modelli: chiedi a Claude cosa sono prima di usarli.

L'**impegno** (in inglese *effort*) è quanto il modello ragiona prima di rispondere: basso, medio, alto. Si sceglie insieme al modello. Stesso modello, più impegno = risposte più pensate e più consumo.

Il modello e l'impegno valgono **per la sessione** in cui li scegli: se li cambi in una chat, le altre restano come sono.

## Come scegliere

Pensa ai ruoli, come se avessi persone vere: un operativo che segue istruzioni già scritte non ha bisogno del più esperto; chi deve capire, decidere o coordinare sì.

| Lavoro | Scelta tipica |
|---|---|
| «Sposta questa colonna», «correggi questo titolo» | Sonnet, impegno basso |
| Il report del lunedì con la pipeline già scritta | Sonnet, impegno medio |
| Copiare i KPI da una piattaforma a un foglio | Sonnet (o l'aiutante `esecutore`) |
| Capire cosa hanno in comune 10 report di settori diversi | Opus, impegno medio o alto |
| Leggere tutte le chat esportate da claude.ai e costruire la memoria | Opus, impegno medio |
| Decidere come impostare un sistema nuovo | Opus, impegno alto |

Non serve indovinare: chiedi a Claude «che modello e che impegno useresti per questo lavoro, e perché?». La regola del pacchetto è già scritta nel `CLAUDE.md`: per i lavori meccanici Claude usa da solo l'aiutante `esecutore`, che costa poco.

L'unico modo vero di imparare è provare: stesso lavoro, due modelli, guardi il risultato e il consumo.

## I limiti d'uso

Con un abbonamento (Pro o Max) non paghi a messaggio: hai una **quota**. Due cose da sapere:

1. **La finestra di 5 ore.** La quota si ricarica a finestre di 5 ore. Se la finisci prima, aspetti la ricarica.
2. **Il limite settimanale.** Sopra le finestre c'è un tetto per la settimana, che si azzera in un giorno e a un'ora precisi.

La quota è **la stessa** per claude.ai e per Claude Code: se usi tanto la chat, ne resta meno per Claude Code. Con i piani Max la quota è un multiplo di quella del Pro.

### Dove vedi quanto hai consumato

- In Claude Code: il comando `/usage`.
- Su claude.ai: nelle impostazioni, alla voce dell'uso. Lì vedi anche quando si azzera la settimana.
- Se vuoi, Claude ti può mostrare i consumi sempre sotto il campo di scrittura (guida 10, «barra di stato»).

### Come non restare a secco

- Prima di un lavoro grande, guarda quanto ti resta. Se sei vicino al limite delle 5 ore, spezza il lavoro.
- Sai il giorno in cui si azzera la settimana: i lavori pesanti falli quando la quota c'è, e se la settimana sta finendo con tanta quota avanzata, usala (quella non si accumula).
- Per i lavori meccanici usa i modelli piccoli: è lì che si risparmia di più.
- Se un lavoro si interrompe per il limite, Claude scrive l'`HANDOFF.md`: alla ricarica riprendi da lì.

## Il contesto

Il **contesto** è quello che Claude ha «sotto gli occhi» in una sessione: i tuoi messaggi, le sue risposte, i file letti. Ha un limite (si misura in *token*, pezzetti di parola: indicativamente da 200.000 a 1 milione, a seconda del modello e del piano).

- Quando il contesto si riempie, Claude Code lo **comprime** da solo: riassume la conversazione e va avanti. Qualche dettaglio si perde.
- Più la sessione è lunga, più Claude è lento e meno preciso. Molti si trovano meglio a stare intorno alla metà del limite, invece di arrivare in fondo (guida 10 per l'impostazione).
- **Una sessione per lavoro**: per un lavoro nuovo apri una sessione nuova. Quello che serve è nella memoria, non nella chat vecchia.
- `/clear` svuota la conversazione e riparte pulito; `/compact` la comprime subito.

## Link ufficiali

- Claude Code con il piano Pro o Max (limiti e uso): support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan
- Scegliere il modello in Claude Code: code.claude.com/docs/en/model-config
- Prezzi dei piani: claude.com/pricing

## Prova adesso (2 minuti)

Scrivi `/usage` e guarda quanto hai usato nella finestra di 5 ore e nella settimana.
