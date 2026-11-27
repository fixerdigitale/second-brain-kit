---
slug: memoria-raccolta-sessioni
titolo: "Raccolta delle richieste fatte nelle altre sessioni"
area: memoria
dove_gira: PC acceso
livello: medio
costo: "0 €. Lo script gira in pochi secondi."
pacchetto: pacchetti/memoria-raccolta-sessioni/
stato: versione per PC del mio
---

# Raccolta delle richieste fatte nelle altre sessioni

**Il problema.** Lavoro con molte sessioni in parallelo, anche dal telefono. Dicevo «come ti ho chiesto ieri» e la sessione nuova non ne sapeva niente.

**Come l'ho risolto.** Da me un servizio senza AI, tre volte al giorno (mattina, ora di pranzo, sera), raccoglie in un solo file le mie richieste delle ultime sessioni di Claude Code, più call registrate, task e calendario, e lo mette dove lo leggono sia Claude sia gli agenti. Prende solo i miei messaggi, non le risposte. CLAUDE.md dice: se parlo di un lavoro che qui non vedi, leggi quel file. Nel pacchetto c'è la parte che vale per un PC: uno script Python che legge le sessioni di Claude Code in `~/.claude/projects` e scrive un markdown con solo i tuoi messaggi, per progetto e per sessione, oscurando quello che sembra una chiave.

**Perché così.** Raccogliere non richiede intelligenza, quindi niente modello: costa zero e non sbaglia. Un file compatto si legge in un attimo; scavare ogni volta nei file delle sessioni costa contesto. Solo i miei messaggi perché sono quelli che dicono cosa voglio, e tengono il file corto e meno delicato.

**Quando ti serve.** Se apri tante sessioni sugli stessi progetti nella stessa giornata, o lavori da più posti.

**Quando non ti serve.** Se usi una sessione per progetto e la porti avanti finché è finita: il contesto c'è già. Da PC gira solo a PC acceso, e le sessioni di altri dispositivi non le vede. Se il vault va su GitHub o Drive, il file contiene le tue richieste: va escluso se ci sono cose dei clienti.

**Come prenderlo.** Copia `raccogli_sessioni.py` fuori dal vault e lancialo con `python3 raccogli_sessioni.py --ore 24 --out <cartella-vault>/Fonti/raccolta/ultima.md`. Facoltativo: pianificalo tre volte al giorno (Utilità di pianificazione su Windows, crontab sul Mac) e aggiungi la riga per CLAUDE.md del LEGGIMI.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-raccolta-sessioni/LEGGIMI.md).
