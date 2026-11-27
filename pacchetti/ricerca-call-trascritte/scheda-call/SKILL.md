---
name: scheda-call
description: Trasforma una call (trascrizione incollata, file, o registrazione letta da un connettore come Fathom) in una scheda nel vault con decisioni, impegni e task, senza perdere nessun punto. Usala quando scrivi «fammi la scheda della call», «recap della call», o incolli una trascrizione.
---

# Scheda della call

La trascrizione è la fonte, il riassunto no: il riassunto automatico dice spesso «iniziare a
lavorare su…» anche quando nessuno l'ha chiesto. Prima di trasformare un punto in un lavoro,
controllalo sul testo della call.

## Passi

1. **Trova il testo.** Trascrizione incollata, file in `<cartella-vault>/Call/trascrizioni/`, o
   connettore del registratore di call se è attivo. Leggila tutta prima di scrivere.
2. **Titolo pulito**: `Cliente o progetto - Argomento` (mai «Riunione Google Meet»).
3. **Dividi ogni punto in una di tre cose:**
   - **Lavoro chiesto adesso**: qualcuno l'ha chiesto, o io mi sono impegnato, con un tempo detto o
     evidente → diventa un task.
   - **Idea o piano futuro** («potremmo», «fra tre mesi») → resta nella scheda, non diventa un task.
   - **Accordo o regola** (un modo di lavorare deciso) → nella scheda, e se riguarda un cliente
     anche nella sua nota principale.
4. **Se il registratore ha già una lista di action item, trattala come una checklist**: ogni voce
   o diventa un task o scrivi perché no. Nessuna sparisce in silenzio. Si perdono quasi sempre le
   cose delegabili al team, cioè proprio quelle che non dovrei fare io.
5. **Chi ha detto cosa**: la trascrizione a volte attribuisce le frasi alla persona sbagliata.
   Per capire se un impegno è mio o dell'altro guarda il senso (chi offre, chi chiede). Nel dubbio,
   scrivilo come dubbio.
6. **Scrivi la scheda** con il modello qui sotto. Se in `<cartella-vault>/Call/` c'è già la nota della call
   (la scrive `call_in_markdown.py`, con la sezione `## Trascrizione`), metti la scheda nella stessa nota, sopra
   `## Trascrizione`, e non toccare la trascrizione. Altrimenti crea `<cartella-vault>/Call/AAAA-MM-GG-<slug>.md`
   con la scheda e, in fondo, la trascrizione intera.
7. **Task**: aggiungi i lavori chiesti adesso al file dei task del progetto, ognuno con la fonte
   (`Fonte: call AAAA-MM-GG, <link registrazione>`), chi aspetta, e una scadenza solo se è stata detta.
   Mai una data inventata.
8. **Recap per l'altra persona: preparalo, non mandarlo.** In fondo alla scheda, una bozza breve in
   prima persona: di cosa abbiamo parlato, cosa faccio io, cosa serve da te (solo se serve).
   Niente note interne, niente prezzi non decisi.

## Modello

```markdown
# <Cliente - Argomento>
- Data: AAAA-MM-GG · Durata: N min · Con: <nomi e ruoli>
- Registrazione: <link>

## In breve
<3 righe: perché c'era la call e cosa ne è uscito>

## Decisioni e accordi
- ...

## Lavori chiesti adesso
- [ ] <cosa> · chi: <io / team / cliente> · entro: <data detta o "non detta">

## Idee per dopo
- ...

## Action item del registratore
- <voce> → task / no, perché ...

## Dubbi da chiarire
- ...

## Bozza di recap (da NON mandare senza il mio ok)
...
```
