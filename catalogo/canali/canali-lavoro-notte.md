---
slug: canali-lavoro-notte
titolo: "Il lavoro della notte, da rivedere al mattino"
area: canali
dove_gira: PC acceso
livello: medio
costo: "0 € in più: usa il piano già pagato che altrimenti andrebbe perso; un po' di corrente se lasci acceso il PC"
pacchetto: "pacchetti/canali-lavoro-notte/"
stato: "versione per PC del mio"
---
# Il lavoro della notte, da rivedere al mattino

**Il problema.** L'abbonamento Claude ha un limite settimanale: quello che non uso entro il reset si perde. Intanto avevo una coda di lavori che potevano andare avanti senza di me, ma solo se c'ero io a lanciarli.

**Come l'ho risolto.** La sera scrivo in una coda i lavori preparatori che possono andare avanti da soli (riordini, bozze, ricerche). Di notte girano uno dopo l'altro, e prima di ognuno si controlla il consumo: se la finestra delle 5 ore è al 90% si aspetta il reset, se la settimana è all'85% la coda si ferma. Di giorno c'è anche un turno che si accende da solo: ogni 15 minuti un controllo guarda se sono fermo da almeno 45 minuti e se c'è capacità che andrebbe persa. E i lavori lunghi di giorno passano da un semaforo con soglie che salgono man mano che il reset si avvicina: a quattro giorni dal reset si fermano al 50% della settimana, l'ultimo giorno al 90%. Al mattino trovo le consegne con un sì/no ciascuna, e le task restano «da rivedere» finché non le guardo. Di notte si prepara, non si manda niente a nessuno. Nel pacchetto: uno script per PC che legge `CODA.md` dal vault, fa girare i lavori in fila e scrive `DA-RIVEDERE.md`.

**Differenza con i lavori in background.** Quelli ([scheda](canali-lavori-in-background.md)) li lancio io, di giorno, uno alla volta, e li guardo appena finiscono. Questa è una coda preparata prima, che gira quando non ci sono, si ferma da sola sulle soglie di consumo e non chiude niente senza il mio sì.

**Perché così.** Capacità già pagata, lavoro che avanza mentre dormo, e io che al mattino decido invece di eseguire. Il «da rivedere» c'è perché un lavoro fatto in autonomia non è finito finché non l'ho guardato. Le soglie servono a non svegliarmi con il piano finito proprio il giorno in cui mi serve.

**Quando ti serve.** Se a fine settimana ti avanza piano e hai lavori preparatori chiari che puoi descrivere in un brief.

**Quando non ti serve.** Se il piano lo consumi già tutto di giorno, o se i tuoi lavori chiedono sempre tue decisioni a metà. Sul PC gira solo se il PC resta acceso e non va in sospensione. E lo script del pacchetto non legge il consumo del piano: si ferma solo a un'ora fissa (le 7), quindi la coda la tieni corta tu.

**Come prenderlo.** Copia `coda.py`, metti in `VAULT` il percorso del vault, scrivi i lavori in `CODA.md` (un «## titolo» e il brief sotto) e pianificalo di notte con l'Utilità di pianificazione (Windows, con «Riattiva il computer») o cron (Mac). Il turno che si accende da solo quando sei fermo resta un'idea da server. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/canali-lavoro-notte/LEGGIMI.md).
