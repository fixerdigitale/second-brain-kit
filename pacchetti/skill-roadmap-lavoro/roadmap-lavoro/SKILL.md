---
name: roadmap-lavoro
description: >
  Costruisce e tiene aggiornata la roadmap di qualsiasi lavoro (landing, report, automazione,
  sistema, assunzione, contratto): da una richiesta a fasi, task, chi fa cosa, quanto ci vuole,
  cosa serve dall'utente, quando è «fatto». Usala quando arriva un lavoro con più di un passo,
  quando l'utente chiede «ok ma come e quando», e ogni volta che serve capire a che punto è un
  lavoro. Se esiste una pipeline del lavoro, la pipeline vince sulla skill.
---

# Roadmap di lavoro

Serve a una cosa: dopo «sappiamo cosa fare» dire **come, chi, quando e a che punto siamo**.
Idee riprese (non il codice) da planning-with-files (cancello di chiusura), claude-task-master
(task, dipendenze, stato), Marcus (avanzamento a soglie) e agent-almanac (scomposizione col 100%).

## Regola madre: il modo di lavorare dell'utente vince

1. Se c'è una pipeline del lavoro (es. `<cartella-vault>/pipeline-lavoro/PIPELINE-LAVORO.md`), i
   **suoi passi sono la base**. La skill aggiunge solo ciò che manca: tempi, dipendenze, prova di
   fatto, chi controlla.
2. Se non c'è, scomponi con sei domande: cosa vuol dire «fatto», quali passi, chi fa cosa, cosa
   serve dall'utente, scadenza, cosa può andare storto.
3. Prima di ogni passo «faccio X?», dopo «ho fatto questo, va bene?».

## Taglia → forma

| Taglia | Forma |
|---|---|
| Piccola | una task con 3-5 righe di checklist |
| Media | una task, checklist completa, una sola fase |
| Grande | un progetto, 3-5 fasi, una task media per lavoro |

Di' la taglia in una riga prima di creare. Una richiesta che cresce passa alla taglia dopo.

## Come si scompone

1. Parti dai **risultati** finali (3-7), non dalle attività. «Landing online e tracciata», non
   «lavorare alla landing».
2. Scomponi ogni risultato in task. **Regola del 100%:** le task figlie coprono tutto il
   risultato, né di meno né di più.
3. Fermati quando ogni task è **stimabile** (minuti), **assegnabile** (un responsabile),
   **misurabile** (si vede se è fatta).
4. Al massimo 3 livelli: lavoro → fase → task. Se serve di più, il lavoro è due lavori.
5. Aggiungi sempre il ramo **gestione**: controllo, approvazione, messa online, chiusura.
6. **Stima solo le task**, mai le fasi. Se la fiducia è bassa su più del 30% delle task, serve
   prima un giro di domande all'utente.
7. Segna le **dipendenze**. La catena più lunga decide la scadenza. Dipendenze in cerchio =
   scomposizione sbagliata.
8. Ogni passo dice **cosa mi aspetto** e **cosa faccio se non va**. Richiesta vaga → domande,
   non indovinare.

## Cosa scrivere

**Per ogni fase** (solo taglia grande): obiettivo in una riga; **finita quando** (criterio
verificabile); scadenza vera; dove serve l'ok dell'utente.

**Per ogni task:** titolo = verbo + oggetto; **chi**; **stima in minuti**; **dipende da**;
**serve l'utente?** sì/no e cosa; **prova di fatto** (link, screenshot desktop e telefono,
numero, riga di log); **chi controlla**, sempre un altro da chi ha eseguito.

**Per ogni riga di checklist:** un'azione sola.

## Dove si tiene

Se non hai un gestore di task, basta un file: `<tuo-progetto>/ROADMAP.md` con una tabella
task · chi · stima · dipende da · serve l'utente · prova · stato. Se ne hai uno (Notion, Trello,
Asana, Linear…), le stesse colonne diventano campi. Prima di creare una task cerca se c'è già.

## Stati

| Momento | Stato |
|---|---|
| creata | Da fare |
| iniziata | In corso (avanzamento a 25 / 50 / 75 / 100 % delle righe fatte) |
| aspetta l'utente o un terzo | Attesa (scrivi cosa e da chi) |
| aspetta il controllo | In revisione (prova con il link) |
| bloccata | In pausa (perché, chi la sblocca) |
| finita e controllata | Fatto, con nota «Fatto / Manca» |

**Cancello di chiusura.** Una task non va a «Fatto» se manca la prova, se ha righe aperte non
dichiarate o se l'ha controllata chi l'ha eseguita.

## Richiesta nuova a lavoro partito

Non si aggiunge in silenzio. Una riga di **cambio**: cosa chiede, cosa sposta, cosa si toglie per
farle posto. Decide l'utente.

## Rapporto di stato («a che punto siamo?»)

Una pagina, leggibile in 2 minuti, dai dati e non dalla memoria.
1. **Risposta in cima:** in tempo / a rischio / in ritardo, con il motivo.
2. Fase per fase: fatto, in corso, prossimo. Numeri concreti.
3. **Blocchi**, ognuno con chi lo sblocca. Se non ce ne sono: «Nessun blocco».
4. **Decisioni che servono**, con la scadenza.
5. Mai «tutto verde» senza prova. Un dato mancante: «non so, manca X».

## Prima di dire «la roadmap è pronta»

1. Ogni task ha chi, stima, prova di fatto e chi controlla.
2. I punti di ok dell'utente sono segnati, nessuno nascosto.
3. Le scadenze sono date, non parole.
4. Le dipendenze non girano in tondo.
5. Sta in una pagina. Se serve di più, il lavoro va spezzato.
6. L'utente ha visto lo scheletro e ha detto sì.

## Cosa non fare

- Non inventare scadenze, stime o nomi: se mancano, «da chiedere».
- Non creare fasi per riempire. 3 fasi chiare battono 7 vaghe.
- Non scrivere chiavi o password nelle task.
