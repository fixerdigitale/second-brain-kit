---
slug: impara-regole-proposte-con-ok
titolo: "Regole proposte di notte, fisse solo dopo il mio ok"
area: impara
dove_gira: PC acceso
livello: medio
costo: "0 €: nessun modello, solo uno script. 15 minuti."
pacchetto: "pacchetti/impara-regole-proposte-con-ok/"
stato: "versione per PC del mio"
---

# Regole proposte di notte, fisse solo dopo il mio ok

**Il problema.** Le correzioni che davo più volte meritavano di diventare regole fisse, quelle che Claude legge sempre. Ma se le promuoveva da solo, prima o poi entrava una regola sbagliata, o una frase scritta da qualcun altro diventava legge. E se dovevo ricordarmelo io, non succedeva mai.

**Come l'ho risolto.** Ogni notte un giro guarda le correzioni salvate in memoria e trova quelle tornate almeno due volte. Non le applica: me le propone, una per una, come domanda «la rendo fissa?». Al mattino rispondo sì o no. Un altro giro applica solo i sì, con una copia datata del file prima di scrivere, e tiene uno storico delle decisioni. Un no si ricorda, così la stessa proposta non torna. Il tetto di 20 Regole d'oro vale anche qui: a tetto pieno il sì aspetta che ne tolga una. Da me la domanda arriva come card sul telefono, e lo stesso giro vale anche per le regole comuni a tutti gli agenti. Sul PC la card è una riga di un file: metti [x] o [-].

**Perché così.** La macchina è brava a contare quante volte una correzione è tornata; decidere cosa diventa regola per sempre resta mio. Separare «proponi» da «applica» mi dà un momento per leggere, e la copia datata rende ogni sì annullabile.

**Quando ti serve.** Se salvi le correzioni in memoria (scheda [correzioni con Why e How](../memoria/memoria-feedback-why-how.md)) e tieni le Regole d'oro in cima all'indice (scheda [indice e Regole d'oro](../memoria/memoria-indice-e-regole-doro.md)).

**Quando non ti serve.** Se le tue correzioni sono poche: con meno di una ventina di file di memoria le rileggi tu in cinque minuti. E se già fai la revisione di fine giornata (scheda [revisore notturno](../memoria/memoria-revisore-notturno.md)), che propone anche le Regole d'oro: questo è il giro automatico e senza modello, e basta uno dei due.

**Come prenderlo.** Copia `regole_doro.py` e pianifica `proponi` di notte e `applica` al mattino, con il percorso della cartella della memoria. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/impara-regole-proposte-con-ok/LEGGIMI.md).
