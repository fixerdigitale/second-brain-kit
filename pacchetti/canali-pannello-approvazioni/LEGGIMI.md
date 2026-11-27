# Approvazioni in un file (versione da PC del mio Pannello)

**Cosa fa.** Tutte le richieste di ok finiscono in un posto solo, `DA-APPROVARE.md`, come card con
tre risposte possibili (approvo / correggi / stop). Claude le scrive quando lavora senza di te e le
esegue quando trovi il tempo di decidere. Nel mio sistema è una pagina del Pannello con i bottoni;
qui è un file, che apri anche dal telefono se il vault si sincronizza.

**Dove si copia.**
1. `DA-APPROVARE.md` nella radice del vault. Cancella la card d'esempio.
2. Il testo di `regola-per-CLAUDE.md` nel `CLAUDE.md` del vault.

**Come si prova.** Chiedi a Claude «prepara una mail al cliente X ma non mandarla, mettila in
approvazione». Deve comparire una card. Scrivi «approvo» sotto Decisione, apri una sessione nuova
e controlla che te la segnali.

**Limiti.** È un file: niente notifica sul telefono. Se Claude non ha un modo per eseguire l'azione
(es. mandare mail), la card serve solo a ricordarti di farla tu.

**Come si toglie.** Togli la sezione dal `CLAUDE.md` e cancella il file.

## English

All requests for your ok in one place: a `DA-APPROVARE.md` file with one card per request (topic, what's asked, link, approve / reply with correction / stop) and a rule for CLAUDE.md that makes Claude and agents write their requests there instead of scattering them across chats.

Install: copy `DA-APPROVARE.md` into the root of your vault and paste `regola-per-CLAUDE.md` into your CLAUDE.md. The file sends no notifications: if you don't open it, the cards wait.
