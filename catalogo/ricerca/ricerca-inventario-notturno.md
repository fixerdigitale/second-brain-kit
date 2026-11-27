---
slug: ricerca-inventario-notturno
titolo: "Inventario di cosa c'è davvero"
area: ricerca
dove_gira: PC
livello: base
costo: "0 €. 10 minuti per copiarlo e mettere l'hook. Rigenerarlo richiede meno di un secondo."
pacchetto: pacchetti/ricerca-inventario-notturno/
stato: versione per PC del mio
---

# Inventario di cosa c'è davvero

**Il problema.** Claude Code parte ogni sessione senza sapere cosa ho installato. Concludeva «non ce l'ho» su strumenti che c'erano (un client per Google, un sottodominio, dei moduli), e a volte iniziava a ricostruirne uno da capo.

**Come l'ho risolto.** Da me uno script rigenera ogni notte un file INVENTARIO.md: account collegati, sottodomini, container, agenti, server MCP, skill, programmi, servizi e i soli nomi delle chiavi, mai i valori. CLAUDE.md dice di leggerlo prima di dire che qualcosa non c'è o di costruire uno strumento. Se una sezione non si legge, al suo posto c'è una riga di avviso e le altre restano. Per il PC ho scritto una versione minima: skill, agenti, comandi, hook, server MCP, programmi utili e nomi delle chiavi nei file .env che gli indichi.

**Perché così.** Costa meno scrivere la mappa una volta al giorno che lasciare che l'assistente la ricostruisca a tentoni ogni sessione, o che rifaccia una cosa esistente. Delle chiavi solo i nomi, perché il file lo legge un modello e potrebbe finire in un log. Sul PC l'aggiornamento notturno funziona male (di notte è spento), quindi lo script si rigenera a inizio sessione se ha più di 20 ore.

**Quando ti serve.** Quando hai accumulato skill, server MCP e strumenti e non ti ricordi più cosa c'è. Anche quando più persone o assistenti lavorano sullo stesso PC o progetto.

**Quando non ti serve.** Se hai poche skill e due server MCP: li conosci a memoria e Claude li vede da solo (`/mcp`, elenco delle skill), l'inventario sarebbe un file in più da tenere. Non serve neanche su un solo progetto senza strumenti esterni.

**Come prenderlo.** Copia `genera_inventario.py` in `~/.claude/strumenti/` e lancialo con `--progetto <tuo-progetto>` (e `--env <file.env>` se vuoi i nomi delle chiavi). Per tenerlo aggiornato, l'hook SessionStart del LEGGIMI con `--se-vecchio 20`. In CLAUDE.md: «Prima di dire che uno strumento non c'è, leggi INVENTARIO.md».

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/ricerca-inventario-notturno/LEGGIMI.md).
