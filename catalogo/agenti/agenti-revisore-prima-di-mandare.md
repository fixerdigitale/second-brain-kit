---
slug: agenti-revisore-prima-di-mandare
titolo: "Revisore con occhi puliti prima di pubblicare o mandare"
area: agenti
dove_gira: PC
livello: base
costo: "0 € in più (modello compreso nell'abbonamento; puoi metterlo su Sonnet). Secondo parere con Codex: 0 € se hai già ChatGPT."
pacchetto: "pacchetti/agenti-revisore-prima-di-mandare/"
stato: "versione per PC del mio"
---

# Revisore con occhi puliti prima di pubblicare o mandare

**Il problema.** Le cose che mandavo fuori contenevano errori che rileggendo non vedevo più: una firma sbagliata, una data, un link interno. Chi ha scritto un testo legge quello che voleva scrivere, non quello che c'è.

**Come l'ho risolto.** Prima di ogni invio o pubblicazione che conta, il lavoro passa a un revisore che non l'ha scritto e non lo corregge. Rilegge la richiesta originale, controlla fatti, numeri e link, cosa vede il destinatario, dati che non devono uscire, e nel codice i percorsi di errore. Dà APPROVATO, RESPINTO con la lista o NON VERIFICABILE, e scrive il verdetto prima di leggere la mia opinione. Se ho ChatGPT, posso chiedere anche un secondo parere a Codex in sola lettura. Sul server lo fanno i revisori della squadra; questa è la versione per PC.

**Perché così.** Un revisore che corregge diventa autore e nessuno lo controlla più. Due modelli diversi sbagliano in modi diversi: dove concordano mi fido di più, dove divergono guardo io. A me costa qualche minuto; un errore mandato a un cliente mi costerebbe molto di più.

**Quando ti serve.** Prima di email a clienti, preventivi, pagine pubblicate, codice che scrive su dati veri.

**Quando non ti serve.** Per note interne, bozze per te, messaggi brevi a persone che conosci: la revisione rallenta senza ridurre un rischio vero.

**Come prenderlo.** Copia `revisore.md` in `~/.claude/agents/`. Per il secondo parere già pronto c'è la skill codex della raccolta pubblica gstack (https://github.com/garrytan/gstack): passala prima in un controllo di sicurezza. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/agenti-revisore-prima-di-mandare/LEGGIMI.md).
