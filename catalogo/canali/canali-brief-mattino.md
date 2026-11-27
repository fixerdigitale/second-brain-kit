---
slug: canali-brief-mattino
titolo: "Il brief del mattino"
area: canali
dove_gira: PC acceso
livello: base
costo: "0 € in più; pochi minuti per adattare i percorsi"
pacchetto: "pacchetti/canali-brief-mattino/"
stato: "versione per PC del mio"
---
# Il brief del mattino

**Il problema.** La mattina passavo mezz'ora a ricostruire dove ero rimasto: task, posta, chi aspettava, cosa era uscito dalle call. E spesso mi accorgevo tardi della persona ferma da una settimana.

**Come l'ho risolto.** Alle 08:00, dal lunedì al venerdì, uno script controlla le task sulle fonti, stima i tempi, pianifica il calendario e raccoglie lo stato. Poi il mio assistente principale scrive un solo messaggio WhatsApp in quattro parti: la cosa più importante di oggi; chi sta aspettando, da quanti giorni, con la bozza di risposta già pronta per i primi due; i due o tre ritardi che fanno danno davvero; le decisioni che servono da me. Al massimo cinque cose in sospeso, ognuna con tre risposte possibili: fatto, butta, rimanda a quando. Al terzo rinvio propone solo fatto o butta. Ogni fatto porta fonte e data. Nel pacchetto c'è la skill per PC, che legge il vault invece del server.

**Perché così.** Un fatto da solo non è una notizia; un fatto che ne incrocia un altro lo è (una data vicina senza preparazione, una decisione di una call che non è diventata una task, una persona senza risposta). Il brief fa questi incroci per me. «Fatto, butta, rimanda» toglie l'opzione «ci penso», che è il modo in cui le cose restano ferme per settimane.

**Quando ti serve.** Se ogni mattina perdi tempo a capire da dove partire, o ti scappano le persone che aspettano.

**Quando non ti serve.** Se le tue task e le persone che ti aspettano stanno in una lista di dieci righe: la leggi prima tu. E se il vault non ha le task scritte da qualche parte, il brief non ha niente da incrociare.

**Come prenderlo.** Copia `brief-mattino/` in `~/.claude/skills/brief-mattino/` e adatta i percorsi del vault. Si lancia con `/brief-mattino`; in automatico alle 8 con l'Utilità di pianificazione (Windows) o cron (Mac), solo a PC acceso. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/canali-brief-mattino/LEGGIMI.md).
