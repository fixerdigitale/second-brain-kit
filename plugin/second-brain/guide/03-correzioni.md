# 03 · Le correzioni

Claude sbaglia. Il punto non è che non sbagli mai, ma che **non sbagli due volte la stessa cosa**.

## Come funziona

1. Claude fa una cosa in un modo che non ti va. Glielo dici: «così no, i decimali vanno con la virgola».
2. Claude corregge, e scrive la correzione in un file in `memoria/Correzioni/`: la regola, il perché, quando si applica.
3. La volta dopo, in un'altra sessione, la regola c'è.

Se ti accorgi che non l'ha scritta, diglielo: «salvalo nelle correzioni».

## Perché il perché

Una correzione senza motivo vale solo per quel caso. Con il motivo («i report vanno al cliente italiano, che legge i decimali con la virgola»), Claude la applica anche ai casi nuovi: i grafici, le email, le tabelle.

## Le regole d'oro

Le correzioni sono tante e Claude non le legge tutte a ogni sessione: apre il file giusto quando serve. Le più importanti, invece, stanno in `memoria/Correzioni/REGOLE-ORO.md`, che si carica **sempre**.

- Massimo 20 righe, una regola per riga.
- Una regola entra lì solo con il tuo sì. Claude te lo propone quando la stessa correzione arriva due volte, o quando un errore costa soldi o un cliente.
- In cima a quel file c'è anche la riga «Modo: passo passo» oppure «Modo: diretto»: dice a Claude se spiegare le parole tecniche o andare dritto (guida `INIZIA-DA-QUI.md`).

## Un esempio

```markdown
---
tipo: correzione
regola: Nei report per i clienti i decimali si scrivono con la virgola
created: 2026-11-20
---

# Decimali con la virgola

Il 20/11 il report del lunedì aveva «1.250.5» al posto di «1.250,5» e il cliente ha chiesto spiegazioni.

**Perché conta:** i clienti sono italiani e leggono i numeri all'italiana; un numero letto male fa sembrare sbagliato tutto il report.

**Come si applica:** in tutto quello che va a un cliente (report, fogli, email, grafici) i decimali hanno la virgola e le migliaia il punto. Nei file tecnici (script, CSV per i programmi) resta il punto.
```

## Le correzioni che contano di più

Quelle su come *ragiona*, non solo su come *scrive*:

- «Non dirmi fatto se non hai controllato.»
- «Se non sai per quale cliente è, chiedimelo.»
- «Prima di scrivere nel foglio del cliente, fammi vedere cosa scrivi.»

Sono le più utili perché valgono per tutti i lavori.

## Prova adesso (2 minuti)

Pensa a un errore che Claude (anche su claude.ai) ti ha fatto più di una volta. Scrivi: «salva nelle correzioni: …» e guarda il file che crea.
