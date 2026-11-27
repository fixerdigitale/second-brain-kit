---
slug: canali-board-task
titolo: "Ogni lavoro è una task: stima, tempo vero, chi ci lavora adesso"
area: canali
dove_gira: PC
livello: base
costo: "0 €; dieci minuti"
pacchetto: "pacchetti/canali-board-task/"
stato: "versione per PC del mio"
---
# Ogni lavoro è una task: stima, tempo vero, chi ci lavora adesso

**Il problema.** I lavori vivevano in chat, in messaggi e nella mia testa. Non sapevo quanto mi costava davvero un tipo di lavoro, chi lo stava facendo in quel momento (io, l'AI o un collaboratore) e quali lavori «in corso» erano fermi da giorni.

**Come l'ho risolto.** Ogni lavoro che dura più di qualche minuto è una task su una board, con la fonte da cui nasce (una call, un messaggio, un link). Ogni task ha due tempi separati: la stima, decisa prima, e il tempo vero, contato mentre si lavora. Nel mio sistema il tempo vero lo contano gli hook di Claude Code: quando una sessione lavora su una task la board la mostra «live» sull'avatar di chi ci sta lavorando, somma i minuti (le pause lunghe non contano, due sessioni sulla stessa task non raddoppiano) e segnala le task in corso che non si muovono. Chi pianifica con me vede tutto senza chiedermi «a che punto sei?». Quando parlo di una task scrivo sempre il suo link. Nel pacchetto c'è la versione da file: `board.py` tiene stima, tempo vero, chi ci lavora adesso e fonte, e scrive una vista `TASK.md` leggibile anche dal telefono.

**Perché così.** Se il tempo vero si scrive a mano, finisce che si copia la stima, e allora non insegna niente: per questo lo conta il sistema e la stima non si tocca. La differenza fra stima e tempo vero è quella che mi fa migliorare le stime successive e i preventivi. E «chi ci lavora adesso» evita che due persone, o due agenti, facciano la stessa cosa.

**Quando ti serve.** Se lavori con più clienti o con un collaboratore, se fatturi a ore o a progetto e vuoi sapere quanto ti costa davvero un lavoro, o se fai lavorare l'AI in autonomia e vuoi vedere cosa sta facendo.

**Quando non ti serve.** Se hai pochi lavori alla volta e li tieni bene a mente. Se usi già un gestore di task (Trello, Asana, Linear) con il tempo contato, resta su quello: due board si contraddicono in fretta. La versione da file è per una persona o un gruppo piccolo: niente notifiche, niente scrittura contemporanea.

**Come prenderlo.** Copia `board.py` nel vault, scegli la cartella della board e incolla `regola-per-CLAUDE.md` nel CLAUDE.md. Per contare il tempo in automatico si affianca il pacchetto `pacchetti/hook-tempo-per-task/`; per dividere un lavoro grosso in task, `pacchetti/skill-roadmap-lavoro/`. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/canali-board-task/LEGGIMI.md).
