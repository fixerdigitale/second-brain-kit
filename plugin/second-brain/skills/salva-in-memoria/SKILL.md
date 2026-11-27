---
name: salva-in-memoria
description: >
  Writes facts about clients, projects, people and decisions, and corrections on how to work, into
  the second brain's memory: the kit's memoria/ folder or, if you already have a vault, your vault
  with its own drawers and format. Shows what and where before writing. Opened by the onboarding or
  with /second-brain:salva-in-memoria. — Scrive nella memoria del second brain i fatti su clienti,
  progetti, persone e decisioni, e le correzioni su come lavorare: nella cartella memoria/ del kit
  oppure, se c'è già un vault, nel vault con i suoi cassetti e il suo formato. Prima di scrivere
  mostra cosa e dove. La apre l'onboarding o /second-brain:salva-in-memoria.
disable-model-invocation: true
---

# Salva in memoria

Claude non si ricorda niente da una sessione all'altra: si ricorda solo quello che trova scritto in `memoria/`. Questa skill dice **dove** scrivere, **in che forma** e **cosa non scrivere mai**. Come è fatta la memoria: `memoria/COME-FUNZIONA.md`.

**Prima di scrivere, sempre:** mostra il percorso del file e il testo che aggiungi (o, per un file nuovo, il file intero) e aspetta il sì. Vale per i file nuovi come per quelli esistenti, per i fatti come per le correzioni. Se non c'è ancora né `memoria/` né un vault, non creare niente: proponi la missione `cassetti-memoria` (o un posto nel suo `CLAUDE.md`) e chiedi.

## 0. Dove sta la memoria: cassetti del kit o vault suo?

Prima di tutto capisci dove scrivere. In quest'ordine:

1. Se il `CLAUDE.md` della persona dice dove vanno fatti e correzioni, vale quello.
2. Se c'è `memoria/COME-FUNZIONA.md` (cassetti del kit), usa le tabelle qui sotto così come sono.
3. Se la persona ha **già un vault** (una cartella di note con cartelle sue, un indice, magari un
   frontmatter fisso), scrivi **lì, nel suo modo**:
   - trova il cassetto che corrisponde a ogni riga della tabella del punto 1 (per esempio la sua
     cartella `Persone/` per i clienti, `Diario/` per i fatti del giorno). Se `second-brain/MAPPA.md`
     esiste, le convenzioni del vault sono già descritte lì;
   - copia il formato di una nota vicina: frontmatter, titoli, link `[[...]]`, data nel nome;
   - aggiorna il **suo** indice, se ne ha uno, nel suo formato;
   - non creare `memoria/` accanto al suo vault, non rinominare e non spostare note sue;
   - se un tipo non ha un cassetto (per esempio non ha un posto per le correzioni), chiedi una volta
     dove vuole metterlo e proponi di scrivere la risposta nel suo `CLAUDE.md` (una riga, con il sì),
     così la volta dopo non serve chiedere.
   Le correzioni, se la persona usa la memoria automatica di Claude Code
   (`~/.claude/projects/<cartella>/memory/`), vanno lì nel suo formato, con una riga nel suo `MEMORY.md`.
4. Se non c'è niente di tutto questo, proponi la missione `cassetti-memoria` della skill `installa`.
   Nel frattempo scrivi in `memoria/inbox.md` e dillo.

Prima di cambiare una nota esistente del vault, mostra cosa aggiungi (una voce in fondo, non una
riscrittura). Se la nota non è tua da toccare (per esempio un file importato), chiedi.

## 1. Prima di scrivere: che cosa è?

| Se è… | Va in… |
|---|---|
| Un fatto su un cliente (persone, KPI, preferenze, strumenti, account, problemi) | `memoria/Clienti/<cliente>.md` |
| Un fatto su un lavoro con inizio e fine | `memoria/Progetti/<progetto>.md` |
| Una scelta importante, con il suo perché | `memoria/Decisioni/<data>-<decisione>.md` + una riga nella nota del cliente |
| Come si fa una cosa, un prompt che funziona, come va usato uno strumento | `memoria/Risorse/<argomento>.md` |
| Cosa è successo oggi (una call, una consegna) | `memoria/Fatti/<AAAA-MM-GG>.md` |
| Una correzione su come lavori tu, Claude | `memoria/Correzioni/<regola>.md` (vedi il punto 4) |
| Materiale grezzo (una trascrizione, un'esportazione) | `memoria/Fonti/` |
| Non sai dove va | `memoria/inbox.md`, e dillo |

Se un fatto riguarda un cliente ed è anche un fatto del giorno, scrivilo nella nota del cliente: il diario in `Fatti/` è facoltativo.

## 2. Cerca prima di creare

1. Cerca se la nota esiste già: nome del cliente o del progetto in `memoria/` (anche dentro `clienti.md` o `persone.md`, se ci sono file vecchi dell'importazione).
2. Se esiste, **aggiungi** una voce in fondo alla sezione `## Dalle sessioni`. Non riscrivere quello che c'è.
3. Se non esiste, copia `_modello.md` della cartella giusta, riempi solo quello che sai e lascia vuoto il resto. Mostra la nota nuova e la riga per `memoria/indice.md`, poi scrivi dopo il sì.
4. Se il fatto contraddice una cosa già scritta, non cancellare: scrivi la voce nuova e accanto a quella vecchia «superata dal GG/MM, vedi sotto». Poi dillo alla persona in una riga.

## 3. La forma di una voce

```markdown
### GG/MM/AAAA · argomento
- **Obiettivo:** cosa si voleva ottenere.
- **Fatto:** cosa è stato fatto o detto, con numeri e link.
- **Aperto:** cosa resta da decidere o da fare.
_(fonte: sessione del GG/MM, oppure «detto dalla persona», oppure il link)_
```

- La data si scrive com'è oggi, mai «ieri» o «la settimana scorsa».
- Una voce dice fatti, non impressioni. Se è una tua deduzione, scrivi «da verificare».
- La fonte c'è sempre. Senza fonte, il giorno che serve controllarla non si sa da dove viene.

## 4. Le correzioni su come lavori

Quando la persona ti corregge («così no», «te l'avevo già detto», «non farlo più»):

1. Cerca in `memoria/Correzioni/` se c'è già una regola sullo stesso tema.
   - Se c'è: aggiungi in fondo una riga «Aggiornamento GG/MM/AAAA: …» con il caso nuovo. Questa è la seconda volta: proponi di metterla fra le regole d'oro.
   - Se non c'è: proponi un file da `_modello.md` (nome e contenuto) e crealo dopo il sì. Il nome del file dice la regola, non l'episodio (`numeri-con-la-virgola.md`, non `errore-report-cliente-x.md`).
2. Scrivi il **perché** (il costo di sbagliare) e il **come si applica** (quando scatta e cosa fare). Con il perché puoi applicare la regola anche ai casi nuovi.
3. Le regole d'oro (`REGOLE-ORO.md`) si caricano a ogni sessione: massimo 20, una riga ciascuna. Una regola entra lì **solo con il sì della persona**. Se sono già 20, proponi quale togliere.

## 5. Cosa non scrivere mai

- Password, chiavi, token, codici di accesso, dati bancari: neanche in parte. Se servono, scrivi solo dove stanno («nel gestore password»).
- Dati personali di lead e contatti dei clienti (nomi, telefoni, email): bastano i totali.
- Cose che la persona ti ha detto come private, se non ti ha chiesto di salvarle.

## 6. Dopo aver scritto

Una riga alla persona: cosa hai scritto e in quale file. Per esempio: «Salvato in `memoria/Clienti/rossi.md`: report il lunedì alle 9, con i decimali con la virgola.»

Se il modo è «passo passo», aggiungi perché l'hai messo proprio lì.
