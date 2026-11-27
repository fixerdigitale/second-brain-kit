---
slug: sicurezza-utente-separato-agenti
titolo: Gli agenti lavorano con un utente separato e pochi permessi
area: sicurezza
dove_gira: server
livello: avanzato
costo: 0 €. Qualche ora di configurazione su un server Linux, più la disciplina di non scavalcarla.
pacchetto: "nessuno: solo idea"
stato: lo uso
---
# Gli agenti lavorano con un utente separato e pochi permessi

**Il problema.** Sul server girano agenti AI (con OpenClaw, nel mio caso) che ricevono messaggi da fuori: chat, email, pagine web. Un messaggio scritto apposta potrebbe convincere un agente a fare qualcosa che non deve. Se l'agente avesse i permessi di amministratore, il danno non avrebbe limiti.

**Come l'ho risolto.** Gli agenti girano con un loro utente di sistema, non amministratore. Possono lanciare come amministratore solo pochi comandi precisi, scritti uno per uno nell'elenco di sudo (per esempio mandarmi un avviso). Io con Claude Code lavoro da amministratore, ma non eseguo mai file che stanno nelle cartelle degli agenti, perché un agente potrebbe averli cambiati. Non carico il loro file di segreti come uno script. Quando devo scrivere nei loro file uso un programmino apposta, che non segue i collegamenti creati da loro.

**Perché così.** Se un agente viene ingannato, il danno resta dentro la sua cartella. È lo stesso principio dei permessi di Claude Code: ognuno ha solo quello che gli serve.

**Quando ti serve.** Quando hai agenti che girano da soli su un server e leggono testo scritto da altri.

**Quando non ti serve.** Su un PC dove usi Claude Code solo tu non mi sembra utile un utente separato: bastano i permessi (scheda [Permessi](sicurezza-permessi-deny-ask.md)) e tenere i segreti fuori dalle cartelle di lavoro. È un'idea che ha senso solo con un server.

**Come prenderlo.** Non c'è un pacchetto: serve un server. L'idea in tre passi: crea un utente Linux dedicato agli agenti, non metterlo nel gruppo sudo, e se gli serve un'azione da amministratore concedi in `/etc/sudoers` solo quel comando preciso, con il percorso completo.
