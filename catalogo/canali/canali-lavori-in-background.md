---
slug: canali-lavori-in-background
titolo: "Lavori lunghi in background, con avviso alla fine"
area: canali
dove_gira: PC acceso
livello: medio
costo: "0 € in più, stesso abbonamento Claude; 10 minuti per installarlo"
pacchetto: "pacchetti/canali-lavori-in-background/"
stato: "versione per PC del mio"
---
# Lavori lunghi in background, con avviso alla fine

**Il problema.** Un lavoro lungo (una ricerca, un riordino di note, una bozza grossa) mi teneva ferma la chat: o aspettavo, o aprivo un'altra finestra e poi mi dimenticavo di andare a vedere.

**Come l'ho risolto.** Quando una richiesta dura più di un paio di minuti, il mio assistente non mi tiene appeso: lancia una sessione nuova di Claude Code in background con un brief completo (obiettivo, file, cosa consegnare), mi dice subito che è partita e, a fine lavoro, mi arriva «✅ titolo: …» o «❌ …». Massimo 3 lavori insieme. Nel pacchetto c'è la versione per PC: uno script che lancia `claude -p` in background, scrive il risultato in un file markdown e manda una notifica sul desktop (Windows, Mac, Linux).

**Differenza con il lavoro della notte.** Questo lo lanci tu, adesso, di giorno, un lavoro alla volta, mentre continui a lavorare in chat; finisce in minuti e ne guardi subito il risultato. La coda della notte ([scheda](canali-lavoro-notte.md)) è una lista preparata la sera, gira quando non ci sei (da me, sul server, controlla il consumo del piano prima di ogni lavoro; lo script per PC si ferma a un'ora fissa) e lascia tutto «da rivedere» al mattino.

**Perché così.** Separare il «chiedere» dall'«aspettare» mi lascia continuare a pensare. Il brief scritto per una sessione che parte da zero mi obbliga anche a chiarire cosa voglio, e il file del risultato resta come traccia.

**Quando ti serve.** Se lanci spesso lavori da 10-30 minuti e nel frattempo vuoi fare altro con Claude.

**Quando non ti serve.** Se i tuoi lavori durano un minuto, o preferisci seguire passo passo cosa fa Claude: in background non puoi approvare i comandi uno per uno, quindi quelli che chiedono permesso vengono negati.

**Come prenderlo.** Copia `lavora.py` dove vuoi (per esempio `<cartella-vault>/strumenti/`), cambia `CARTELLA_PREDEFINITA` se vuoi i risultati nel vault e prova con un lavoro finto. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/canali-lavori-in-background/LEGGIMI.md).
