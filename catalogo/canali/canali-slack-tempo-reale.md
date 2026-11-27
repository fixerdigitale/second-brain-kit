---
slug: canali-slack-tempo-reale
titolo: "Slack e WhatsApp a eventi, non a orario"
area: canali
dove_gira: server
livello: avanzato
costo: "0 € per il filtro (solo regole, nessun modello); il giro che aggiorna le task usa l'abbonamento; server sempre acceso"
pacchetto: "nessuno: solo idea"
stato: "lo uso"
---
# Slack e WhatsApp a eventi, non a orario

**Il problema.** Seguire Slack e i gruppi WhatsApp di lavoro con controlli a orario voleva dire o troppe notifiche o risposte in ritardo di ore. E un tag importante si perdeva fra cento messaggi.

**Come l'ho risolto.** Un servizio resta collegato agli spazi Slack in tempo reale (Socket Mode); per WhatsApp lo stesso con un webhook. Un messaggio privato o un tag a me fa partire, dopo un momento di quiete, un giro che aggiorna le task. Se il testo dice «urgente» mi arriva subito un WhatsApp, e se non rispondo parte una chiamata. Di sera e di notte passano solo le task nuove ad alta priorità. Alcuni canali «seguiti» avviano un lavoro preciso a ogni messaggio. Il testo dei messaggi non finisce mai nei log. Un controllo a orario resta solo come riserva lenta, ogni qualche ora, per gli eventi persi.

**Perché così.** Un evento che arriva quando succede costa meno di cento controlli che non trovano niente, e risponde prima. Il filtro (privati, tag, urgente) decide cosa merita la mia attenzione, non l'orologio. Una cosa che ho imparato: una connessione sola per app Slack, perché due si dividono gli eventi.

**Quando ti serve.** Se stai in molti canali di lavoro e le richieste vere sono poche e sparse.

**Quando non ti serve.** Se usi Slack con poche persone: le notifiche native sui tag fanno già il lavoro. E senza un computer sempre acceso un collegamento in tempo reale non regge.

**Come prenderlo.** Nessun pacchetto: è solo l'idea, serve un server. Sul PC: attiva il connettore Slack ufficiale in claude.ai e chiedi quando ti serve «cosa mi sono perso nei canali X da ieri, solo dove mi hanno taggato»; per il resto le notifiche native di Slack sui tag e sulle parole chiave (per esempio «urgente»).
