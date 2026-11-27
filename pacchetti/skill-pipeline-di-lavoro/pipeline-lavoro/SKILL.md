---
name: pipeline-lavoro
description: Primo passo su ogni richiesta nuova. Capisce se è un'informazione (link, cosa detta tempo fa, ricerca nelle note) o un lavoro; per un lavoro cerca la pipeline tipo × cliente in PIPELINE-LAVORO.md, la dice in una riga e la segue un passo alla volta (prima «faccio X?», dopo «ho fatto questo, va bene?»). Ogni correzione dell'utente la scrive nel pezzo generale o nelle Direttive del cliente, più una riga nello STORICO. Usala quando l'utente dice «partiamo con…», «fammi…», «sistemami…», e ogni volta che corregge un passo.
---

# Pipeline di lavoro

Il documento che comanda è `<cartella-vault>/pipeline-lavoro/PIPELINE-LAVORO.md` (tipi di lavoro,
pezzi riutilizzabili, Direttive per cliente, pipeline). Le correzioni vanno in
`<cartella-vault>/pipeline-lavoro/STORICO.md`. Rispondi breve, **una domanda per volta**.

Regola di fondo: la prima volta che fai un tipo di lavoro lo **registri** (scrivi i passi fatti),
la seconda nasce la **pipeline**, la terza la **ottimizzi**.

## 1. Informazione o lavoro?

| È un'informazione se… | È un lavoro se… |
|---|---|
| chiede un link, un file, dove sta una cosa | chiede di produrre o cambiare qualcosa |
| chiede una cosa detta o fatta tempo fa | coinvolge un cliente e un risultato da consegnare |
| chiede di cercare nelle note o nelle sessioni | servono più passi, file toccati, approvazioni |
| si chiude con una risposta | si chiude con una consegna |

Dubbio vero → una domanda: «È una ricerca o partiamo con un lavoro?».

## 2. Informazione

1. Cerca nella fonte giusta (note del vault, HANDOFF.md e STORICO.md del progetto, email), non
   nella memoria della sessione.
2. Prima riga = la risposta o il link. Poi da dove viene, in una riga.
3. Non trovata → dillo, con dove hai cercato. Niente «forse» spacciati per fatti.

## 3. Lavoro: trova la pipeline

1. Individua **cliente** e **tipo di lavoro** (tabella «Tipi di lavoro» del documento).
2. Cerca la pipeline: un codice per cliente e numero (es. `CL1-1`, `INT-2`).
3. Dillo in **una riga**: «Seguo CL1-1 Landing di lancio.» Se il match non è sicuro, chiedi.
4. Prima di partire leggi: i passi, le **Direttive del cliente** (valgono sopra i pezzi), i
   **pezzi** richiamati, le skill indicate nei passi.
5. Di' la **taglia** in una riga (piccola, media, grande: tabella nel documento).

Tre casi:
- **Pipeline vera** → sezione 4.
- **Routine** (lavori ripetitivi e piccoli): niente passi uno per uno, segui la checklist di 3-4
  righe. Restano le regole fisse: copia prima di modificare, messaggi a terzi solo in bozza,
  conferma prima di scrivere nei dati veri.
- **Nessuna pipeline** (prima volta): dillo («Per questo non c'è ancora una pipeline: registro i
  passi»), lavora con gli stessi check e alla fine scrivi i passi fatti nel documento come
  «Registrazione» (cosa, chi, skill, dove è servito l'ok), più una riga nello STORICO.

Se usi un gestore di task: prima di crearne una, **cerca se c'è già**. Ogni task nuova porta la
sua **fonte** (canale, messaggio, link), così dopo si capisce se è doppia.

## 4. Un passo alla volta, sempre col check

Per ogni passo della pipeline, in ordine:

1. **Prima:** «Faccio [passo N: cosa]?» e aspetta il sì. Una scelta per domanda: mai due cose
   insieme nella stessa approvazione.
2. Fai il passo, con la skill che il passo indica.
3. **Dopo:** «Ho fatto questo, questo e questo. Va bene?» con il link o la prova concreta
   (pagina, file, numero), non un riassunto vago.
4. Sì → passo successivo. No o correzione → sezione 5, poi rifai il passo.

Ricapitola lo stato a ogni turno: «Passo 3 di 9 fatto, adesso il 4».

Niente automatico finché l'utente non lo accende, neanche i passi segnati «candidato auto».
Mai senza chiedere: invii a persone vere, scritture nei dati dei clienti, cose che non si annullano.

## 5. Correzioni: diventano tasselli

Ogni no, correzione o regola nuova su un passo:

1. **Dove va:**
   - vale per tutti i clienti → nel **pezzo** (colonna «Cosa fa») o nel passo della pipeline;
   - vale solo per quel cliente → nelle **Direttive** del cliente;
   - dubbio → chiedi: «Vale per tutti o solo per [cliente]?».
   Nelle pipeline con la riga «Correzioni già entrate», aggiungi lì data e correzione.
2. **STORICO:** una riga sotto la data del giorno:
   `- [codice pipeline o pezzo] correzione: … → scritta in …`.
3. Dillo in una riga: «Segnato nelle Direttive di [cliente].»

## 6. Esempi

- «Mandami il link del preventivo di ottobre» → informazione. «Eccolo: <link> (da STORICO.md).»
- «Partiamo con la landing del prossimo lancio» → lavoro, Cliente 1 × Landing. «Seguo CL1-1
  Landing di lancio. Taglia media. Faccio il passo 1: leggo il copy dal documento del cliente?»
- Al passo 4: «le proposte grafiche fammele sempre in verticale» → «Vale per tutti o solo per
  Cliente 1?» → scritto nel posto giusto, riga nello STORICO.
