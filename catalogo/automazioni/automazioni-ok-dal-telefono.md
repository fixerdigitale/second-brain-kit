---
slug: automazioni-ok-dal-telefono
titolo: "Il lavoro lungo chiede l'ok sul telefono e riparte da solo"
area: automazioni
dove_gira: PC acceso
livello: avanzato
costo: "0 €: l'app ntfy è gratuita. Installazione: 30 minuti."
pacchetto: "pacchetti/automazioni-ok-dal-telefono/"
stato: "versione per PC del mio"
---

# Il lavoro lungo chiede l'ok sul telefono e riparte da solo

**Il problema.** Lavoro spesso dal telefono. Un lavoro lungo arrivava a un punto in cui serviva il mio ok, e lì restava fermo finché non tornavo al computer, a volte per ore.

**Come l'ho risolto.** Quando un lavoro arriva a un punto di controllo, Claude aggiorna l'HANDOFF, mi manda la domanda sul telefono con cosa succede con un sì e con un no, e si ferma. Quando rispondo, un giro ogni 2 minuti legge la risposta e fa ripartire Claude Code da solo, nella cartella del progetto, con la risposta nel prompt (di serie, dal telefono, solo sì o no dai bottoni). Una ripartenza alla volta, e solo se il semaforo dei consumi è verde. Da me la domanda arriva su WhatsApp, e la risposta la raccoglie un servizio sul server. Per il PC ho scelto le notifiche push dell'app ntfy, con i bottoni Sì e No: non serve un account né un server.

**Perché così.** Il lavoro non deve aspettare che io torni al computer, ma le decisioni restano mie. L'HANDOFF scritto prima di fermarsi fa sì che chi riparte non abbia bisogno della conversazione vecchia. La domanda si segna «in ripartenza» prima del lancio, così la stessa risposta non fa partire due volte il lavoro.

**Quando ti serve.** Se lanci lavori lunghi in più passi e poi ti allontani dal computer, e vuoi approvare dal telefono senza riaprire niente.

**Quando non ti serve.** Se la tua versione di Claude Code ti fa già seguire e comandare la sessione dal telefono (controllo remoto o notifiche dell'app ufficiale): è più semplice. Non usarlo per domande con dati sensibili: passano da un servizio di notifiche, e su ntfy.sh chi conosce il nome dell'argomento le può leggere. Il codice della domanda serve ad abbinare la risposta, non a proteggerla.

**Come prenderlo.** Copia `ponte_telefono.py` in `~/.claude/ponte/` e il comando `chiedi-ok.md` in `~/.claude/commands/`, lancia `configura`, iscriviti all'argomento nell'app ntfy e pianifica `giro` ogni 2 minuti. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/automazioni-ok-dal-telefono/LEGGIMI.md).
