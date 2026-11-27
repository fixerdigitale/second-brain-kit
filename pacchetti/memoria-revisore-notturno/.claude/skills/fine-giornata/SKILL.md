---
name: fine-giornata
description: Chiude la giornata di lavoro sulla memoria. Lancia il sotto-agente archivista, poi presenta le sue proposte (fatti per il vault, correzioni per la memoria, note superate, candidate Regole d'oro) una alla volta e applica solo quelle approvate. Usala quando la persona dice «chiudiamo la giornata», «fine giornata», «revisione memoria» o «cosa abbiamo imparato oggi».
---

# Fine giornata

1. Lancia il sotto-agente `archivista`. Passagli il percorso del vault, quello della memoria e, se ce l'hai,
   un riassunto di cosa si è fatto oggi in questa sessione.
2. Ricevi la lista delle proposte. Controllane la fonte a campione: apri almeno due note o sessioni citate.
   Se una fonte non torna, togli la proposta e dillo.
3. Presenta le proposte **una alla volta**: la proposta, la fonte, e la domanda «la applico? sì / no / cambiala».
4. Applica solo quelle con «sì». Per «cambiala», scrivi la versione nuova e richiedi conferma.
5. Le candidate Regole d'oro: se la persona dice sì, aggiungi la regola in cima a `MEMORY.md` con il testo
   per intero. Se le Regole d'oro superano il tetto scritto nell'indice, chiedi quale togliere.
6. Alla fine: quante applicate, quante scartate, in quali file. Se il vault è un repo git, proponi il commit
   con un messaggio tipo «fine giornata <data>: N note aggiornate» e fallo solo con il sì.

Mai cancellare note: quelle superate si segnano «superata il <data>».
Mai scrivere password, token, chiavi o codici, né nel vault né in memoria.
