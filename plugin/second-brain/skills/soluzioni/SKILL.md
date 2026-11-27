---
name: soluzioni
description: >
  Solutions archive in soluzioni/: what broke, why and how it was fixed. Search it before diagnosing
  a technical problem, write a card after solving a non-trivial one. Opened with /second-
  brain:soluzioni; the CLAUDE.md block can make the habit permanent. — Archivio delle soluzioni in
  soluzioni/: cosa si è rotto, perché e come si è aggiustato. Si cerca prima di diagnosticare un
  problema tecnico, si scrive una scheda dopo averne risolto uno non banale. Si apre con /second-
  brain:soluzioni; il blocco del CLAUDE.md può rendere fissa l'abitudine.
disable-model-invocation: true
---

# Archivio delle soluzioni

Lo stesso problema torna. Una soluzione scritta una volta si rilegge molte: la volta dopo si parte dalla causa già trovata e dai vicoli ciechi già esplorati.

L'archivio è la cartella `soluzioni/` nella cartella di lavoro: una scheda Markdown per problema, più lo stampo `_modello.md`.

## Prima di diagnosticare: cerca

1. Cerca in `soluzioni/` con le parole del **sintomo**, non con la causa che sospetti: la causa è proprio quello che stai cercando. Due o tre parole bastano («foglio non aggiorna», «connettore 403», «lead doppi»). Usa lo strumento di ricerca di Claude Code sulla cartella.
2. Se trovi una scheda, leggi prima «Come si riconosce» e «Vicoli ciechi», poi di' alla persona: «È già successo il 12/11: era X. Controllo se è la stessa cosa.»
3. Se non trovi niente, procedi normalmente. Alla fine la scheda la scrivi tu.

## Dopo aver risolto: scrivi la scheda

Scrivi una scheda quando:

- la diagnosi è costata più di mezz'ora;
- la causa non era quella che sembrava;
- il problema può tornare su un altro cliente o un altro file.

Le cose ovvie e le correzioni da un minuto non vanno in archivio: lo diluiscono.

Il nome del file descrive il **sintomo**, non il cliente: `foglio-kpi-non-si-aggiorna.md`, non `problema-cliente-rossi.md`.

Copia `soluzioni/_modello.md` e riempi le sette sezioni. Le tre che fanno risparmiare più tempo:

- **Sintomo**: i sintomi fuorvianti sono quelli che fanno sbagliare strada la volta dopo.
- **Come si riconosce**: un controllo concreto, non una descrizione.
- **Vicoli ciechi**: valgono quanto la soluzione, e sono la parte che non si ricostruisce.

## Regole di scrittura

- Numeri, percorsi, comandi e messaggi di errore esatti, mai riassunti a parole.
- La causa vera, non il primo sospetto: se hai cambiato idea a metà, il primo sospetto va nei vicoli ciechi.
- Come hai verificato che funziona, con i numeri.
- Niente password, chiavi o dati di persone nelle schede.
