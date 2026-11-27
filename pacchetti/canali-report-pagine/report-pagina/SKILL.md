---
name: report-pagina
description: Trasforma un testo o un markdown in una pagina HTML leggibile (un solo file, si apre con un doppio clic, si manda o si carica su Drive). Usala quando scrivi «fammi il report», «mettilo in una pagina», «report per il cliente», o quando un risultato va letto da qualcuno e non solo da te.
---

# Report in pagina

Un documento da leggere vale più come pagina che come file markdown: si apre dal telefono, si
gira a un cliente, ha un indice. Questa skill fa una pagina sola, autonoma, partendo da
`template.html` (accanto a questo file).

## Passi

1. **Chiedi a cosa serve e per chi, se non è chiaro.** Una riga: «per chi è e per quale progetto?».
   Un report senza destinatario diventa un file che nessuno ritrova.
2. **Scrivi il contenuto** in sezioni `##` numerate: in cima la conclusione (cosa ho trovato, cosa
   propongo), sotto i dettagli, in fondo le fonti con il link. Frasi corte, tabelle solo se si
   confrontano cose.
3. **Riempi il template**: copia `template.html` e sostituisci `{{TITOLO}}`, `{{SOTTOTITOLO}}`,
   `{{DATA}}`, `{{INDICE}}` (un `<a href="#s1">` per sezione) e `{{CONTENUTO}}` (l'HTML delle sezioni,
   ognuna in `<section id="sN">`). Niente librerie esterne, niente script: deve aprirsi anche offline.
4. **Salva** in `<cartella-vault>/report/<slug>.html` (slug corto, minuscolo, con trattini). Stesso
   slug = stessa pagina aggiornata, non una copia nuova.
5. **Registra** una riga in `<cartella-vault>/ELEMENTI.md` (se esiste): data, tipo «report»,
   titolo, progetto, per chi (interno/esterno), percorso del file.
6. **Rileggi la pagina finita** prima di dire «fatto»: apri il file e controlla che le sezioni ci
   siano tutte e che i link funzionino.

## Regole

- Per un cliente: niente nomi di strumenti interni, niente note private, niente prezzi non decisi.
- Mai password, chiavi o dati personali di terzi nella pagina: è un file che gira.
- Se il report va condiviso, il modo più semplice è caricarlo nella cartella Drive del cliente
  (Drive lo mostra in anteprima) oppure mandarlo come allegato.
