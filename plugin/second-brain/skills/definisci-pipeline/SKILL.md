---
name: definisci-pipeline
description: >
  Trasforma un lavoro che si ripete in una pipeline scritta (passi, chi li fa, strumenti,
  account, dove serve l'ok) in pipeline/PIPELINE.md, e la tiene aggiornata con le correzioni
  della persona. Usala quando un lavoro torna per la seconda volta, quando la persona dice
  «lo faccio ogni settimana», «è sempre la stessa cosa», «mettiamolo in automatico», «fammi
  la procedura», quando c'è un file lavori-ricorrenti.md da sistemare, e quando parte un
  lavoro che ha già una pipeline.
---

# Definisci una pipeline

Una pipeline è la ricetta di un lavoro che si ripete, per **un** cliente. Serve a due cose:

1. non reinventare ogni volta come si fa un lavoro già fatto;
2. non usare il metodo, lo strumento o l'account di un cliente per un altro.

Il formato e gli esempi sono in `pipeline/PIPELINE.md`. Le correzioni si registrano anche in `pipeline/STORICO.md`.

## La regola delle tre volte

1. **Prima volta**: fai il lavoro e alla fine **registra** i passi in fondo a `PIPELINE.md`, sezione «Registrazioni». Due righe bastano.
2. **Seconda volta**: proponi di trasformare la registrazione in pipeline. È il momento di questa skill.
3. **Dalla terza volta**: segui la pipeline e migliorala a ogni correzione.

Non scrivere una pipeline per un lavoro fatto una volta sola: si scrive su quello che si è fatto davvero, non su quello che si immagina.

## Come si scrive: l'intervista

Prima di scrivere, fai alla persona queste domande, **al massimo tre per volta**, ognuna con la risposta che proporresti tu (presa dalla registrazione, dalla nota del cliente o da `memoria/lavori-ricorrenti.md` se c'è):

1. **Cliente e nome**: per chi è, come lo chiamiamo? (per esempio `ROSSI-1 · Report del lunedì`)
2. **Quando parte**: a che ora o giorno, o da cosa (una task su Trello, un messaggio)?
3. **Da dove arrivano i dati**: quali piattaforme, quali file, con **quale account**?
4. **I passi**: cosa si fa, in che ordine? Uno per riga, un'azione per passo.
5. **Dove va il risultato**: quale foglio, quale scheda, quale canale? Chi lo riceve?
6. **Cosa vuol dire «fatto»**: cosa si deve vedere alla fine?
7. **Cosa può andare storto**: errori già capitati, numeri che spesso non tornano?
8. **Dove serve il tuo ok**: quali passi vuoi vedere prima?

Le risposte su account e strumenti vanno **anche** nella nota del cliente, sezione «Strumenti e account». È lì che Claude controlla prima di usarli.

## La forma di una pipeline

```markdown
### ROSSI-1 · Report del lunedì
Cliente: Rossi · Quando: lunedì entro le 10 · Account: <email Google del cliente>
Serve a: dare al cliente i numeri della settimana nel suo foglio.
Fatto quando: la scheda «Settimana» ha i numeri di lunedì-domenica e il commento in cima.

1. Leggere spesa, clic e lead da Meta Ads (account pubblicitario «Rossi Srl») · Claude · ok: no
2. Scrivere i numeri nel foglio, scheda «Settimana» · Claude · ok: sì, prima di scrivere
3. Commento di due righe: cosa va, cosa no · Claude prepara · ok: sì
4. Messaggio al cliente · lo manda la persona · ok: sempre manuale

Correzioni già entrate: decimali con la virgola (20/11).
```

Per ogni passo: **cosa si fa · chi lo fa · dove serve l'ok**. Se un passo usa un account o uno strumento, scrivi quale.

## Come si usa: fase 1

All'inizio nessun passo parte da solo:

1. Di' quale pipeline segui, in una riga: «Seguo ROSSI-1 · Report del lunedì».
2. **Prima di ogni passo** chiedi: «Faccio il passo 2, scrivo i numeri nella scheda Settimana?» e aspetta il sì.
3. **Dopo il passo** riferisci: «Ho scritto 7 righe nella scheda Settimana, celle B2:H8. Va bene?» e aspetta.
4. Un no o una correzione: scrivila **nel passo** a cui si riferisce («Correzioni già entrate»), e una riga in `STORICO.md`: data, passo, cosa è cambiato, chi l'ha deciso.
5. Quando un passo è stato approvato **5 volte di fila** senza correzioni, puoi proporre di farlo senza chiedere. Decide la persona. Mai senza ok: invii a persone vere, spese e budget, pubblicazioni, cancellazioni, scritture su dati del cliente che non hanno una copia.

## Quando diventa automatico

Una pipeline stabile può diventare:

- una **skill** (un file di istruzioni che Claude segue da solo quando serve);
- un **lavoro programmato** (per esempio ogni lunedì alle 8).

Proponilo solo quando la pipeline ha girato almeno 3 volte senza correzioni sui passi importanti, e spiega in una riga cosa cambierebbe e come si torna indietro. Prima di qualunque automatismo valgono le regole della skill `buone-maniere`.

## Se la persona ha un file lavori-ricorrenti.md

Se in `memoria/` c'è `lavori-ricorrenti.md` (nasce dall'importazione delle chat di claude.ai), usalo come punto di partenza: per ogni lavoro elencato proponi se è da registrazione, da pipeline o da skill. Una proposta alla volta, partendo da quello che fa risparmiare più tempo.
