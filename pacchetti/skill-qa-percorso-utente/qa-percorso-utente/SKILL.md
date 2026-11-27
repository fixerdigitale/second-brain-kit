---
name: qa-percorso-utente
description: >
  Controllo di una pagina o di un flusso rifacendo il percorso di un utente vero in un browser,
  con prova prima/dopo. Usala quando si consegna o si corregge una landing, un modulo, un
  checkout, un'area clienti o un'app, e quando un errore va riprodotto «come lo vede l'utente»
  prima di toccare il codice. Ciclo: riproduci, scrivi la prova che fallisce, correggi, riverifica.
---

# QA sul percorso utente

Idea ripresa dal ciclo `/qa` di gstack (https://github.com/garrytan/gstack). Testo scritto da zero.

## Prima di cominciare

1. Dichiara **l'URL** (o l'ambiente di prova) e **il percorso**: da dove entra l'utente, cosa vuole fare, dove finisce.
2. Dichiara il **dispositivo**: desktop 1440 px e telefono 393 px. Entrambi, sempre.
3. Dati di prova con un nome riconoscibile (es. «TEST <iniziali>»). Dopo il controllo, cancella i dati di prova nei sistemi veri.
4. Non toccare la produzione oltre quello che il lavoro richiede. Nel dubbio, chiedi.

## Strumento

Un browser comandabile, per esempio Chrome DevTools MCP (https://github.com/ChromeDevTools/chrome-devtools-mcp):
un profilo separato, senza i tuoi login. Per le operazioni su piattaforme (CMS, CRM) vale: API
prima, browser solo per guardare.

## Il ciclo

1. **Riproduci.** Fai il percorso passo per passo come un utente: clic, compilazione, invio. Niente scorciatoie.
2. **Guarda, non solo il 200.** Per ogni passo:
   - screenshot a 1440 e a 393;
   - console: errori e avvisi;
   - rete: richieste fallite (4xx/5xx), tracciamento che parte (pixel, analytics, parametri UTM);
   - pagine e file collegati (ringraziamento, email di conferma, PDF), non solo la pagina d'ingresso.
3. **Scrivi la prova che fallisce.** Per ogni difetto una riga: *passo, cosa succede, cosa
   dovrebbe succedere, prova (screenshot o riga di console)*. Senza prova il difetto non è confermato.
4. **Correggi.** Una correzione per difetto. Niente modifiche non richieste, soprattutto sul copy.
5. **Riverifica.** Rifai lo **stesso** percorso dall'inizio, non solo il passo corretto.
6. **Ripeti** fino a zero difetti aperti, o al massimo 3 giri: oltre, segnala cosa resta e perché.

## Voto e chiusura

- Voto 0-10, con una riga di motivo per ogni punto tolto. Sotto 8 non si consegna.
- Report corto: risposta in cima («passa / non passa»), tabella dei difetti (passo, prima, dopo), dettagli in fondo.
- Non dire «fatto» senza aver guardato gli screenshot a 1440 e 393.

## Cosa non fare

- Non allargare il controllo a tutto il sito se la richiesta riguarda un problema preciso.
- Non scrivere password, token o chiavi che compaiono in rete o console: oscurali nel report.
- Non lasciare dati di prova nei sistemi veri.
