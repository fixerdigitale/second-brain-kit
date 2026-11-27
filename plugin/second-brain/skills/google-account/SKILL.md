---
name: google-account
description: >
  Lavora con Gmail, Drive, Fogli, Documenti e Calendar su più account Google (per esempio il
  proprio e quello di un'agenzia o di un cliente) usando il programma gog da terminale,
  scegliendo sempre l'account scritto nella nota del cliente. Usala quando un lavoro tocca
  file o email di Google, quando la persona dice «sull'altro account», «con l'account di X»,
  «nel foglio del cliente», e quando bisogna installare o collegare gog.
---

# Google con più account (gog)

I connettori di Google dentro Claude collegano di solito un account solo. Quando la persona lavora con più account Google (il suo, quello di un'agenzia, quello di un cliente) si usa **gog**: un programma da terminale, gratuito e open source, che parla con Gmail, Drive, Fogli, Documenti, Presentazioni, Calendar e altri servizi Google, **con tutti gli account che la persona ha collegato**.

Installazione e collegamento: guida `07-google-piu-account.md` (comando `/second-brain:aiuto google`). Non installare e non collegare niente senza il sì della persona, un passo alla volta.

## La regola dell'account

1. Prima di ogni comando gog, leggi la nota del cliente in `memoria/Clienti/`, sezione «Strumenti e account», e usa **quell'**account.
2. Scrivi sempre l'account nel comando, con `-a` o `--account`. Mai contare sull'account predefinito:
   ```bash
   gog -a nome@agenzia.it sheets get <ID-DEL-FOGLIO> "Settimana!A1:H20"
   ```
3. Se la nota non dice quale account usare, chiedi. Se la persona te lo dice, scrivilo nella nota (skill `salva-in-memoria`).
4. Per vedere gli account collegati: `gog auth list`. Gli alias aiutano a non sbagliare: `gog auth alias set agenzia nome@agenzia.it`, poi `gog -a agenzia …`.

## Leggere e scrivere

- **Per leggere** aggiungi `--readonly`: gog blocca qualunque modifica, anche per sbaglio.
- **Per scrivere** (celle, file, documenti) valgono le buone maniere: prima una copia o una tabella «prima / dopo», poi il sì della persona, poi rileggi il punto scritto.
- **Email**: per leggere usa `--gmail-no-send`. Una email si prepara come bozza; la manda la persona, salvo un suo «sì, mandala» scritto in questa conversazione.
- Per vedere cosa farebbe un comando senza farlo: `--dry-run`.
- Per avere risultati da leggere con calma: `--json`.

## Errori comuni

| Errore | Cosa vuol dire | Cosa fare |
|---|---|---|
| Token scaduto dopo 7 giorni | l'app Google della persona è ancora in modalità «Testing» | guida 07, punto «Rendere l'accesso stabile» |
| 403 / permesso negato | quell'account non vede il file | controlla di usare l'account giusto; non vuol dire che il file sia «di un altro» |
| L'account dell'agenzia non si collega | l'amministratore dell'agenzia blocca le app esterne | chiedi alla persona di sentire l'amministratore; non cercare altre strade |

## Cosa non fare mai

- Usare l'account di un cliente per il lavoro di un altro.
- Stampare in chat token, codici o il contenuto del file delle credenziali (`client_secret_….json`).
- Condividere file all'esterno, cambiare i permessi di un file o inviare email senza un sì scritto.
