---
slug: hook-contesto-avviso-e-compressione
titolo: "Avviso di contesto e compressione automatica"
area: automazioni
dove_gira: PC
livello: base
costo: "0 €. 15 minuti per copiarlo e provarlo."
pacchetto: "pacchetti/hook-contesto-avviso-e-compressione/"
stato: "lo uso"
---

# Avviso di contesto e compressione automatica

**Il problema.** Una sessione lunga rilegge tutto il contesto a ogni messaggio. Me ne accorgevo tardi: ho avuto sessioni oltre i 500k token per messaggio, e su circa 11.500 controlli registrati più di 5.000 erano sopra i 250k. Costava quota dell'abbonamento e rendeva Claude più lento e più confuso. Prima fermavo io i messaggi sopra una soglia e aprivo una sessione nuova: interrompeva il lavoro.

**Come l'ho risolto.** Due pezzi insieme. Un hook UserPromptSubmit legge la coda della conversazione e, sopra una prima soglia, aggiunge una volta sola un avviso che Claude mi riferisce in una riga («delego letture e ricerche a un sotto-agente»); sopra la soglia alta gli chiede, a ogni turno, di aggiornare l'HANDOFF. Poi la compressione parte da sola, senza fermarmi: con l'impostazione `autoCompactWindow: 480000` la mia versione comprime verso 447k (finestra meno circa 33k), e la compressione delle sessioni ferme le comprime mentre non le uso. Prima di ogni compressione parte il salvataggio dell'HANDOFF. Da me c'è anche una mod dell'app desktop che fa da rete se la compressione automatica è spenta: quella non è nel pacchetto.

**Perché così.** Non devo ricordarmelo io: il numero arriva nel momento in cui conta, e il contesto si gestisce da solo mentre lavoro. L'avviso una volta sola è voluto: resta nella storia, e ripeterlo a ogni turno sprecherebbe altro contesto. La soglia alta tiene più dettagli possibile prima di comprimere; l'HANDOFF evita di perderli.

**Quando ti serve.** Se fai sessioni lunghe (ore sullo stesso lavoro), usi un modello con finestra grande, o ti capita di finire i limiti prima del previsto o di vedere Claude dimenticare cose dette all'inizio.

**Quando non ti serve.** Se apri una sessione nuova per ogni lavoro e raramente superi qualche decina di migliaia di token. Con la finestra standard da 200k `autoCompactWindow` non cambia niente. Non usare la compressione automatica senza un salvataggio dello stato (scheda [HANDOFF salvato alla compressione](hook-handoff-prima-compressione.md)). I nomi delle impostazioni li ho verificati sulla versione 2.1.330: su un'altra potrebbero non esserci.

**Come prenderlo.** Copia `avviso_contesto.py` in `~/.claude/hooks/` e da `settings-esempio.json` le due chiavi e il blocco dell'hook in `~/.claude/settings.json`. Le soglie sono in cima al file. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-contesto-avviso-e-compressione/LEGGIMI.md).
