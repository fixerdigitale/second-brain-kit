# 01 · La cartella di lavoro

Claude Code lavora **dentro una cartella** del tuo computer: legge, crea e modifica file lì dentro, chiedendoti il permesso. Quella cartella è il tuo «centro di comando».

## Una cartella sola per il lavoro

- Crea una cartella per il lavoro (per esempio `Documenti\Lavoro` su Windows, `Documenti/Lavoro` su Mac) e apri sempre Claude Code lì.
- Le cose personali in un'altra cartella: così la memoria del lavoro non si mescola con il resto.
- Non serve dividere le cartelle per cliente: la divisione la fa la memoria (una nota per cliente), non le cartelle. Per i file dei clienti (report, creatività) Claude crea le sottocartelle quando servono, e te lo dice.

## Cosa c'è dentro dopo l'installazione

```
Lavoro/
├── CLAUDE.md          le istruzioni che Claude legge a ogni sessione
├── memoria/           la memoria unica: clienti, progetti, decisioni, correzioni
├── pipeline/          i lavori che si ripetono, scritti a passi
├── soluzioni/         i problemi già risolti
└── _da-cancellare/    quello che non serve più (lo svuoti tu)
```

Il `CLAUDE.md` ha due parti:

- **la tua parte**, in alto: chi sei, le tue regole. Gli aggiornamenti non la toccano mai;
- **il blocco del metodo**, fra le righe `second-brain:inizio` e `second-brain:fine`: arriva dal pacchetto e si aggiorna con `/second-brain:aggiorna`, che prima ti mostra le differenze.

Se vuoi cambiare una regola del metodo, non modificare il blocco: scrivi la tua versione nella tua parte («invece di X, fai Y»). Così l'aggiornamento non te la riporta indietro.

## Se sposti la cartella

Claude Code non la ritrova da solo: riaprilo nella cartella nuova (nell'app: scegli la cartella dal menu in basso quando apri una sessione nuova). Dentro non cambia niente, perché tutto è scritto nei file.

## Il backup

Tutto quello che conta è in questa cartella. Il backup è semplice:

1. **Git** (facoltativo, consigliato): salva le versioni dei file, così puoi tornare a com'era ieri. Claude lo installa e lo usa per te: chiedigli «metti la cartella sotto git e fai un salvataggio».
2. **Copia fuori dal computer**, una volta a settimana in un giorno fisso: una copia della cartella su un disco online (Google Drive, OneDrive, iCloud) oppure una repository **privata** su GitHub. Mai pubblica: dentro ci sono i tuoi clienti.

Se il computer si rompe o viene rubato, con la copia riparti in mezz'ora: installi Claude Code e il pacchetto, rimetti la cartella, e Claude sa di nuovo tutto.

## Prova adesso (2 minuti)

Scrivi a Claude: «spiegami cosa c'è in questa cartella e a cosa serve ogni parte».
