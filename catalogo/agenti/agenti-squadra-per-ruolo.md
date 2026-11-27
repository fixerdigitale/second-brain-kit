---
slug: agenti-squadra-per-ruolo
titolo: "Una squadra di agenti per ruolo, con revisori separati"
area: agenti
dove_gira: server
livello: avanzato
costo: "Un server VPS da circa 15-40 €/mese più qualche ora di manutenzione a settimana; i modelli restano dentro gli abbonamenti Claude e ChatGPT."
pacchetto: "nessuno: solo idea"
stato: "lo uso"
---

# Una squadra di agenti per ruolo, con revisori separati

**Il problema.** Un assistente unico che fa tutto, per me, diventava mediocre in tutto e nessuno lo controllava. E avevo agenti nati per una persona o un cliente, che si sovrapponevano.

**Come l'ho risolto.** Sul server ho una squadra su OpenClaw (software open source per agenti), un agente per ruolo e non per persona. Il mio assistente principale parla con me su WhatsApp e smista. Poi ci sono un PM per progetti e task, Designer e Tecnico su ChatGPT per pagine e codice, Copywriter, Creativo, Ricercatore, Analista e Marketer su Sonnet, un Sistemista per server e sicurezza e un Archivista per memoria e correzioni. Chi costruisce non rivede: il Creativo rivede le cose visive, il Sistemista il codice con tre verdetti (approvato, respinto, non verificabile), il Marketer il marketing. Dopo i revisori controllo ancora io, con Claude Code.

**Perché così.** Ogni ruolo ha istruzioni corte e skill sue, e così lavora meglio. Il revisore separato mi ha trovato errori che né l'autore né io avevamo visto. La regola che mi sono dato: un ruolo diventa un agente solo se serve un permesso diverso, un modello diverso, occhi puliti per controllare o lavoro in parallelo. Il resto lo faccio con procedure e skill.

**Quando ti serve.** Se vuoi agenti che lavorano anche quando il tuo PC è spento, rispondono da WhatsApp o Slack e fanno girare code di notte.

**Quando non ti serve.** Quasi sempre all'inizio. Con Claude Code sul PC ottieni gran parte del valore con i sotto-agenti (esecutore, costruttore, revisore, sistemista) senza un server da mantenere. La squadra su server costa manutenzione vera: aggiornamenti, permessi, un servizio sempre acceso da sorvegliare.

**Come prenderlo.** Solo idea, serve un server. La versione per PC sono i sotto-agenti delle altre schede di quest'area. OpenClaw è un progetto pubblico: valutalo dalla sua documentazione ufficiale prima di installarlo.
