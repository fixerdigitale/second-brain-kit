# Pipeline di lavoro

Una pipeline è la ricetta di un lavoro che si ripete, per un cliente: i passi in ordine, chi li fa, con quali strumenti e dove serve il tuo ok. Serve perché Claude non reinventi ogni volta come si fa un lavoro già fatto, e perché non usi il metodo di un cliente per un altro.

Le pipeline le scrive e le aggiorna Claude, con la skill `definisci-pipeline`. Tu le approvi e le correggi.

## Come si usano adesso: fase 1

Ogni passo chiede il tuo ok: prima «faccio X?», dopo «ho fatto questo, va bene?». Nessun passo parte da solo. Quando un passo è stato approvato 5 volte di fila senza correzioni, Claude può proporti di farlo diventare automatico: decidi tu. Mai automatici: invii a persone vere, spese, pubblicazioni, cancellazioni.

## La regola delle tre volte

1. **La prima volta** che fai un lavoro, Claude **registra** i passi in fondo a questo file (sezione «Registrazioni»).
2. **La seconda volta**, dalla registrazione nasce la **pipeline**.
3. **Dalla terza volta** la si **migliora**: ogni tua correzione va scritta nel passo a cui si riferisce, e in `STORICO.md`.

## Pipeline

<!-- Esempio inventato, da cancellare quando c'è la prima vera:

### CLIENTE-1 · Report settimanale KPI
Cliente: <nome> · Quando: ogni lunedì entro le 10 · Account: <email dell'account Google del cliente>
Serve a: dare al cliente i numeri della settimana, nel suo foglio.

1. Leggere i numeri dalle piattaforme pubblicitarie (account scritti nella nota del cliente) · Claude · ok: no
2. Copiare i numeri nel foglio del cliente, scheda «Settimana» · Claude · ok: sì, prima di scrivere
3. Due righe di commento: cosa va, cosa no · Claude prepara, tu correggi · ok: sì
4. Avviso al cliente · lo mandi tu · ok: sempre manuale

Correzioni già entrate: i decimali con la virgola (20/11).
-->

## Registrazioni

<!-- Lavori fatti una volta sola, senza pipeline. Forma:

### Registrazione · <lavoro> · <cliente> · GG/MM/AAAA
Passi fatti: … → … → …
Da ricordare se torna: …
-->
