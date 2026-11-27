---
slug: sicurezza-prova-ripristino
titolo: "Prova di ripristino: riaprire davvero il backup"
area: sicurezza
dove_gira: PC
livello: base
costo: 0 €. Circa 15 minuti al mese.
pacchetto: pacchetti/sicurezza-prova-ripristino/
stato: lo uso
---
# Prova di ripristino: riaprire davvero il backup

**Il problema.** Un backup che dice «riuscito» dice che è partito, non cosa contiene. Una cartella o un database esclusi per errore si vedono solo riaprendo la copia, e di solito lo si scopre nel momento peggiore.

**Come l'ho risolto.** Faccio la prova in una cartella a parte, mai sopra l'originale: riscarico la copia dal cloud come se il computer fosse perso, la decifro, la estraggo e controllo cose precise. I file ci sono, il file principale della memoria è identico, le cartelle importanti ci sono tutte, la configurazione si apre. Ho trasformato i passi in una checklist da compilare, che ripeto una volta al mese e dopo ogni cambio allo script di backup.

**Perché così.** Per me è l'unico modo di sapere che il backup funziona. Il ripristino vero lo fai sotto stress, quindi conviene averlo già fatto una volta con calma, compresa la domanda «la password la trovo anche senza questo PC?».

**Quando ti serve.** Una volta subito dopo aver impostato il backup, poi ogni mese o dopo ogni modifica allo script.

**Quando non ti serve.** Se il tuo unico backup è GitHub e cloni spesso il repo su un altro PC, in pratica lo stai già provando: basta controllare ogni tanto che il clone sia completo.

**Come prenderlo.** Copia la checklist nel vault e compilane una copia datata a ogni prova; la prima volta puoi farla seguire a Claude Code. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-prova-ripristino/LEGGIMI.md).
