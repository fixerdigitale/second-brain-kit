# HANDOFF.md e SISTEMA.md per ogni cliente o progetto lungo

**Cosa fa.** Due file nella cartella del cliente, con compiti diversi:
- `SISTEMA.md` = fatti stabili (chi è chi, come passano i dati, accessi, decisioni ferme, errori già fatti,
  strumenti). Si **corregge sul posto**, non si allunga.
- `HANDOFF.md` = solo lavoro aperto, il più recente in alto. Serve quando una sessione si interrompe
  (limite d'uso, errore, contesto pieno) e un'altra dovrebbe ripartire senza rifare tutto.

**Dove si copia.** Nella cartella del progetto o del cliente: `<tuo-progetto>/SISTEMA.md` e `<tuo-progetto>/HANDOFF.md`.
Aggiungi in CLAUDE.md:
«Se un lavoro lungo si interrompe, scrivi stato, file, decisioni e prossimo passo nell'HANDOFF.md del progetto
prima di fermarti. Prima di mappare un sistema o attribuire un account a qualcuno, leggi SISTEMA.md.»

**Come si prova.** A metà di un lavoro scrivi «salva l'handoff». Apri una sessione nuova e scrivi «riprendi da HANDOFF.md»:
dovrebbe ripartire dal prossimo passo senza chiederti il contesto.

**Come si toglie.** Cancella i due file e la riga in CLAUDE.md.

## English

Two templates for long-running clients or projects. `SISTEMA.md` holds stable facts (who's who, how data flows, settled decisions, mistakes already made), corrected in place with dates. `HANDOFF.md` holds only open work: an "Open risks" section and new job sections at the top, each with goal, state, files touched, decisions and next step.

Install: copy `SISTEMA.md` and `HANDOFF.md` into the client's or project's folder and add to your CLAUDE.md the two lines shown above (update the HANDOFF before stopping; read SISTEMA.md before mapping a system).
