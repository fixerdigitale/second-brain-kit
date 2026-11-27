---
slug: hook-plugin-claude-council
titolo: "Plugin claude-council: secondo parere da altri modelli"
area: automazioni
dove_gira: PC
livello: medio
costo: "0 € in più con i CLI degli abbonamenti già pagati; con chiavi API, il consumo di ogni domanda."
pacchetto: "nessuno: plugin di terzi dalla fonte"
stato: "lo uso"
---

# Plugin claude-council: secondo parere da altri modelli

**Il problema.** Su scelte tecniche importanti (architettura, un bug che non si trova, sicurezza) un modello solo può sbagliare con sicurezza, e io non ho sempre le competenze per accorgermene.

**Come l'ho risolto.** Ho installato claude-council, un plugin pubblico di terzi: con un comando manda la stessa domanda a più modelli (per esempio Codex con l'abbonamento ChatGPT, o Gemini) e mostra le risposte una accanto all'altra, con una sintesi di dove sono d'accordo e dove no.

**Perché così.** Quando due modelli diversi arrivano alla stessa risposta mi fido di più; quando divergono, so dove guardare. Usando i CLI degli abbonamenti che pago già, per me non costa niente in più.

**Quando ti serve.** Prima di decisioni tecniche difficili da annullare, o quando un problema resiste da ore.

**Quando non ti serve.** Per il lavoro di tutti i giorni: moltiplica tempo e consumo. Se non hai un altro abbonamento o CLI (Codex, Gemini…), servono chiavi API a consumo.

**Come prenderlo.** Dalla fonte originale: https://github.com/hex/claude-council (in Claude Code: `/plugin marketplace add hex/claude-marketplace`, poi `/plugin install claude-council`). Prima di installarlo leggi il README e la sezione sulla sicurezza, e passalo in un controllo come quello della scheda [cerca strumento](../skill/skill-cerca-strumento.md).
