---
name: brief-mattino
description: Scrive il brief del mattino leggendo il vault (task, lavori aperti, note delle call, calendario se c'è un connettore). Usala quando scrivi «/brief-mattino», «brief», «cosa conta oggi», o quando un programma pianificato la lancia la mattina.
---

# Brief del mattino

Il brief non riporta i dati: dice cosa significano. Un solo messaggio corto, quattro parti in
quest'ordine, e niente altro. Una parte vuota si salta: non si riempie per simmetria.

1. **La cosa più importante di oggi.** Una riga. Non «ecco il riepilogo»: la cosa.
2. **Chi sta aspettando.** Persone ferme in attesa di una mia risposta, con da quanti giorni.
   Le persone battono i task: un task scaduto è un promemoria, una persona ferma da 9 giorni è
   un rapporto che si logora. Per le prime due scrivi già la bozza del messaggio, pronta da copiare.
3. **Cosa è in ritardo e conta davvero.** Due o tre cose che fanno danno, non l'elenco degli scaduti.
4. **Cosa serve da me.** Le decisioni che non puoi prendere da solo, una riga ciascuna.

## Dove leggere (adatta i percorsi al tuo vault)

- `<cartella-vault>/TASK.md` o la cartella dei task: aperti, scadenze, chi aspetta.
- `<cartella-vault>/**/HANDOFF.md`: lavori a metà e il loro prossimo passo.
- `<cartella-vault>/call/`: note delle call degli ultimi 3 giorni (decisioni e impegni).
- Calendario di oggi e domani, solo se hai un connettore del calendario attivo.
- Se una fonte manca o non si apre, dillo in una riga in fondo: un brief su dati vecchi dice
  cose false con sicurezza, ed è peggio di nessun brief.

## Come collegare i fatti

Un fatto da solo non è una notizia. Un fatto che ne incrocia un altro lo è quasi sempre. Cerca
soprattutto tre combinazioni:

- una **data che si avvicina** senza il lavoro di preparazione fatto;
- una **decisione presa in call** che non è diventata né task né evento;
- una **persona che ha chiesto** qualcosa e non ha avuto risposta.

Ogni fatto porta fonte e data («call 21/09», «TASK.md», «mail di X 22/09»). Un collegamento
dedotto e non scritto nella fonte si scrive «da confermare», mai come certo.

## Le cose in sospeso

Se ci sono task fermi oltre la loro data di revisione, proponine al massimo **cinque**, e per
ognuno chiedi una sola risposta fra: **fatto**, **butta**, **rimanda a quando**. Niente quarta
opzione: «ci penso» è il modo in cui sono arrivati a essere fermi da settimane. Un task
rimandato tre volte: proponi solo fatto o butta, e dillo.

## Cosa non scrivere

- Diagnostica interna, log, l'elenco di cosa hai controllato.
- Numeri messi per riempire se non servono a decidere.
- Saluti e preamboli. Si comincia dalla cosa.

## Cosa puoi fare da solo e cosa no

Da solo: aggiornare i file dei task (scadenze, note), preparare bozze.
Mai senza conferma: scrivere a qualcuno a mio nome, cancellare, toccare un sito o un sistema di
un cliente. Queste le prepari e le metti al punto 4.

## Dove salvarlo

Scrivi il brief anche in `<cartella-vault>/brief/AAAA-MM-GG.md`, così resta lo storico e lo
ritrovo dal telefono se il vault è sincronizzato.
