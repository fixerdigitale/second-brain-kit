# Come funziona la memoria

Questa cartella è la **memoria unica** del tuo lavoro con Claude (in giro la chiamano anche «vault»). È fatta di file di testo normali, in formato Markdown (`.md`): li puoi aprire con qualsiasi editor, con Obsidian o con il Blocco note.

Claude non si ricorda niente da una sessione all'altra. Si ricorda solo quello che trova scritto qui. Per questo vale una regola sola: **una cosa si scrive una volta, nel posto giusto, con la fonte**.

## Le cartelle

| Cartella | Cosa contiene | Un file per… |
|---|---|---|
| `Clienti/` | Tutto quello che sai di un cliente: persone, piattaforme, KPI che contano, **strumenti e account da usare**, decisioni, problemi ricorrenti | cliente |
| `Progetti/` | Lavori con un inizio e una fine (un lancio, una dashboard, un'automazione) | progetto |
| `Risorse/` | Come si fa una cosa, come funziona uno strumento, prompt che funzionano | argomento |
| `Decisioni/` | Scelte importanti, con il perché e cosa resta aperto | decisione |
| `Fatti/` | Il diario: cosa è successo in un giorno (call, consegne, eventi) | giorno |
| `Fonti/` | Materiale grezzo copiato da fuori: esportazioni di chat, trascrizioni di call | fonte |
| `Correzioni/` | Come vuoi che Claude lavori: le correzioni che gli hai fatto, e le regole d'oro | correzione |
| `inbox.md` | Appunti buttati lì, da smistare dopo | — |
| `indice.md` | L'elenco delle note, per orientarsi | — |

In ogni cartella c'è un file `_modello.md`: è lo stampo da cui Claude crea le note nuove. Non va riempito, va copiato.

Se hai importato le chat da claude.ai, qui ci sono già file come `chi-sono.md`, `clienti.md`, `persone.md`, `lavori-ricorrenti.md`, `preferenze.md`. Restano dove sono. Quando vuoi, chiedi a Claude di spostare un cliente alla volta da `clienti.md` a una nota sua in `Clienti/`: più le note sono piccole e separate, meno Claude confonde un cliente con un altro.

## Come è fatta una nota

1. Un'intestazione con pochi campi (fra le righe `---`): che tipo di nota è, di chi parla, quando è nata.
2. Un riassunto stabile in alto: le cose che valgono sempre.
3. Una sezione `## Dalle sessioni` che cresce nel tempo, con una voce per ogni volta che succede qualcosa.

Ogni voce di `## Dalle sessioni` ha questa forma:

```markdown
### 20/11/2026 · report settimanale
- **Obiettivo:** cosa si voleva ottenere.
- **Fatto:** cosa è stato fatto, con numeri e link.
- **Aperto:** cosa resta da decidere o da fare.
_(fonte: sessione del 20/11, chat «report lunedì»)_
```

Senza fonte una riga non si può controllare: il giorno che serve, nessuno sa più da dove viene.

Le voci nuove si aggiungono in fondo. Una voce superata non si cancella: si scrive accanto «superata dal 25/11, vedi sotto».

## Come entrano le informazioni

Quasi niente si scrive a mano. Lo fa Claude, in tre momenti:

1. **Quando lo chiedi**: «salva in memoria che il cliente X vuole i report il lunedì alle 9».
2. **Quando lo correggi**: «così no, i numeri vanno con la virgola». La correzione va in `Correzioni/`.
3. **Alla fine di un lavoro importante**: Claude propone una voce nella nota del cliente o del progetto, e tu dici sì o no.

## Cosa non mettere mai qui

- Password, chiavi, codici di accesso, dati bancari. Se servono, si scrive solo *dove* stanno («la chiave di X è nel gestore password»), mai il valore.
- Dati personali di lead e contatti dei clienti (telefoni, email): bastano i totali e i numeri.

## Ogni tanto, pulizia

Una memoria vale quanto è pulita. Una volta al mese chiedi a Claude: «rileggi la memoria e dimmi cosa è vecchio, doppio o in contraddizione». Decidi tu cosa correggere; quello che non serve va in `_da-cancellare/`.
