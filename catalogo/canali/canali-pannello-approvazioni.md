---
slug: canali-pannello-approvazioni
titolo: "Le richieste di ok in un posto solo"
area: canali
dove_gira: PC
livello: medio
costo: "0 € per la versione file; il mio Pannello è un'applicazione su misura, settimane di lavoro"
pacchetto: "pacchetti/canali-pannello-approvazioni/"
stato: "versione per PC del mio"
---
# Le richieste di ok in un posto solo

**Il problema.** Agenti e automazioni mi chiedevano conferme dappertutto: in chat, su Slack, su WhatsApp. Dimenticavo cosa avevo approvato, e alcune richieste restavano ferme giorni senza che lo sapessi.

**Come l'ho risolto.** Nel mio Pannello di controllo, accanto alla board delle task, c'è la pagina Approvazioni: una card per richiesta con argomento, cosa si chiede, link al lavoro e tre azioni (Approva, Rispondi con la correzione, Stop) più i commenti. Mi arriva solo un messaggio con il link alla card. Le richieste che toccano il server vogliono anche il codice a 6 cifre del mio login; dopo un codice giusto ho 5 minuti in cui le altre si approvano con un tocco. Ogni cambio di stato resta in un registro che non si cancella. Anche le task nate dalle call entrano in bozza, e le valuta chi pianifica con me prima che finiscano nella mia giornata. Nel pacchetto c'è la versione da vault: un file `DA-APPROVARE.md` con le card e una regola per il CLAUDE.md.

**Perché così.** Un posto solo vuol dire che so sempre cosa aspetta me. «Rispondi con la correzione» evita il giro «no» → «e allora come?». E il registro mi dice chi ha approvato cosa e quando.

**Quando ti serve.** Se fai lavorare Claude o altri agenti mentre non ci sei e vuoi che si fermino prima delle azioni delicate (mail a clienti, pubblicazioni, cancellazioni).

**Quando non ti serve.** Se lavori con Claude solo in chat, davanti allo schermo: le conferme in chat bastano. Il file non manda notifiche: se non lo apri, le card aspettano.

**Come prenderlo.** Copia `DA-APPROVARE.md` nella radice del vault e incolla `regola-per-CLAUDE.md` nel CLAUDE.md. Il Pannello con i bottoni, il codice e le notifiche resta un'idea: serve un server. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/canali-pannello-approvazioni/LEGGIMI.md).
