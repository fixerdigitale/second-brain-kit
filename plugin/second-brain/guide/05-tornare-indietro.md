# 05 · Sicurezza e come tornare indietro

Claude lavora in fretta e non sa da solo cosa è prezioso per te. La regola è una sola: **anche se si sbaglia, si deve poter tornare indietro**. La skill `buone-maniere` la fa rispettare; questa guida ti spiega gli strumenti.

## Le tre domande

Prima di ogni azione che scrive (modifica, sposta, cancella, installa, pubblica, invia, spende), Claude si chiede e ti dice:

1. cosa cambia?
2. si può annullare?
3. come si torna indietro?

Se c'è un modo per tornare indietro, lo prepara **prima** (una copia, un salvataggio). Se non c'è (pubblicare, spendere, inviare, cancellare per sempre), aspetta il tuo «sì» scritto.

## Gli strumenti per tornare indietro

| Strumento | Cosa recupera | Cosa NON recupera |
|---|---|---|
| **Esc** | ferma Claude subito, mentre lavora | quello che ha già fatto |
| **Esc due volte** (con il campo di scrittura vuoto) oppure **`/rewind`** | riporta i file e la conversazione a prima di un tuo messaggio | i file cambiati con comandi del terminale, i fogli Google, le email, tutto quello che sta fuori dal computer |
| **Git** | qualunque file della cartella, a qualunque salvataggio fatto | quello che sta fuori dalla cartella |
| **Copia con la data** (`Report - copia del 20-11`) | il file o il foglio com'era | — |
| **`_da-cancellare/`** | i file «cancellati»: Claude li sposta lì invece di eliminarli | — |
| **Cronologia delle versioni** di Google Fogli e Documenti | il foglio o il documento a un'ora precisa | — |

La cosa da ricordare: `/rewind` vale **solo** per i file che Claude ha modificato con i suoi strumenti di modifica. Per tutto il resto servono git e le copie. Per questo Claude le fa prima.

## Le modalità di lavoro

Claude Code può chiederti il permesso a ogni passo oppure lavorare più da solo. Nell'app la modalità si sceglie accanto al campo di scrittura; nel terminale si cambia con **Shift+Tab**.

| Modalità | Cosa fa | Quando usarla |
|---|---|---|
| Normale (chiede) | chiede prima di ogni modifica e di ogni comando | sempre, all'inizio |
| Accetta le modifiche | modifica i file senza chiedere, chiede per i comandi | solo in una cartella con git |
| Piano | studia e propone senza toccare niente | prima dei lavori lunghi |
| Approva tutto da sola | non chiede mai | **mai**, finché non sai esattamente cosa fa |

Quando Claude chiede il permesso per un'azione:

- **Sì, una volta** per tutto quello che scrive;
- **Sì, sempre** solo per le letture;
- se non capisci cosa vuole fare, rispondi **no** e chiedi: «spiegami cosa fa questo comando».

## Le cose che non si annullano

Pubblicare un post o un'inserzione, cambiare un budget, avviare o fermare una campagna, mandare un messaggio o una email a persone vere, cancellare dati in un programma online. Per queste Claude ti scrive **cosa** sta per fare, **dove**, **con quali valori** e **se si può rimediare**, e aspetta il sì. Un sì vale per quell'azione sola: un sì di ieri, o di un'altra chat, non vale.

## Password e chiavi

Non incollarle mai in chat. Se ti scappa, cambiala subito: una chiave finita in chat si considera bruciata. Claude non apre i file con le chiavi (`.env` e simili); se serve una chiave, la metti tu nel file.

## Prova adesso (2 minuti)

Chiedi a Claude di creare un file di prova, poi premi Esc due volte con il campo vuoto e torna a prima della creazione. Guarda il file sparire.
