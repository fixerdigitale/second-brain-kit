---
slug: sicurezza-niente-password-in-chat
titolo: Niente password in chat né nelle note
area: sicurezza
dove_gira: PC
livello: base
costo: 0 €. 5 minuti.
pacchetto: pacchetti/sicurezza-niente-password-in-chat/
stato: lo uso
---
# Niente password in chat né nelle note

**Il problema.** Chat, email e messaggi dei clienti a volte contengono credenziali scritte da loro. Salvando le note nel vault rischiavo di portarmele dietro. E anche solo controllare se una password c'era la faceva comparire nei log della sessione.

**Come l'ho risolto.** Regola fissa: nessuna password, PIN o token in chiaro, né nelle risposte né nelle note, neanche una parte. Neanche mascherata con una regex: se la regex sbaglia, il resto del valore rimane nei log. Per sapere se un segreto c'è, Claude conta le righe o dà il numero di riga, mai il testo. Se incollo io una password per sbaglio, Claude me lo dice una volta con il rimedio (cambiarla) e poi non la ripete. Per il kit ho scritto anche un piccolo controllo che segnala file e riga sospetti nel vault senza mai mostrare il valore.

**Perché così.** Tutto quello che passa in chat resta nei log di sessione, e i log finiscono nei backup e a volte nella memoria. Il posto più sicuro per un segreto per me è uno solo, fuori dal vault.

**Quando ti serve.** Se nel vault finiscono note da chat, email o call con altre persone, o se il vault va su GitHub, anche privato.

**Quando non ti serve.** Se il vault contiene solo tue note di lavoro e non ci copi mai testi di altri, basta la regola: lo script aggiunge poco. Lo script trova solo le forme comuni, non una password scritta da sola su una riga.

**Come prenderlo.** Incolla `regola-claude-md.md` nel `CLAUDE.md`; lancia `cerca_segreti.py` sul vault prima di un push o quando importi note da altri. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-niente-password-in-chat/LEGGIMI.md).
