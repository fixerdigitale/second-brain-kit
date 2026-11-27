# 08 · Le pipeline: i lavori che si ripetono

Una **pipeline** è la ricetta scritta di un lavoro che fai spesso, per un cliente: i passi in ordine, chi li fa, con quali strumenti e account, e dove vuoi vedere prima di andare avanti. Sta in `pipeline/PIPELINE.md`.

Serve a tre cose:

1. Claude non reinventa ogni volta come si fa un lavoro già fatto;
2. non usa il metodo o l'account di un cliente per un altro;
3. ogni tua correzione resta scritta nel passo giusto, e il lavoro migliora a ogni giro.

## La regola delle tre volte

1. **La prima volta** fai il lavoro con Claude. Alla fine: «registra i passi». Claude scrive due righe in fondo a `PIPELINE.md`.
2. **La seconda volta**: «trasformalo in pipeline». Claude ti fa qualche domanda (al massimo tre alla volta, con la sua proposta di risposta) e la scrive.
3. **Dalla terza volta** Claude la segue, e ogni tua correzione entra nel passo a cui si riferisce e in `pipeline/STORICO.md`.

## Com'è fatta

```markdown
### ROSSI-1 · Report del lunedì
Cliente: Rossi · Quando: lunedì entro le 10 · Account: alias «agenzia»
Serve a: dare al cliente i numeri della settimana nel suo foglio.
Fatto quando: la scheda «Settimana» ha i numeri da lunedì a domenica e il commento in cima.

1. Leggere spesa, clic e lead da Meta Ads (account «Rossi Srl») · Claude · ok: no
2. Scrivere i numeri nel foglio, scheda «Settimana» · Claude · ok: sì, prima di scrivere
3. Commento di due righe: cosa va, cosa no · Claude prepara · ok: sì
4. Messaggio al cliente · lo mandi tu · ok: sempre manuale
```

## All'inizio: fase 1

Ogni passo chiede il tuo ok: prima «faccio il passo 2?», dopo «ho fatto questo, va bene?». Sembra lento, ma è così che Claude impara come vuoi le cose, e tu impari a fidarti.

Quando un passo è stato approvato **5 volte di fila** senza correzioni, Claude può proporti di farlo senza chiedere. Decidi tu, passo per passo.

**Mai** senza il tuo ok: invii a persone vere, spese e budget, pubblicazioni, cancellazioni, scritture sui dati di un cliente senza copia.

## Quando diventa automatico

Una pipeline che gira bene può diventare:

- una **skill**, se il lavoro ha un metodo preciso da seguire (guida 04);
- un **lavoro programmato**, che parte da solo a un'ora fissa (per esempio ogni lunedì alle 8), se il computer è acceso o se lo fai girare su un server.

Prima di automatizzare, chiediti: se sbaglia mentre non guardo, cosa succede? Se la risposta è «niente di grave e si rimedia», si può. Altrimenti, resta un passo con il tuo ok.

## Se hai importato le chat da claude.ai

Il file `memoria/lavori-ricorrenti.md` è la lista dei lavori che ripeti. Chiedi: «guarda lavori-ricorrenti.md e dimmi quale lavoro conviene trasformare per primo in pipeline». Uno alla volta.

## Prova adesso (2 minuti)

Scrivi: «quale lavoro faccio più spesso? Registralo come prima volta, così la prossima volta facciamo la pipeline».
