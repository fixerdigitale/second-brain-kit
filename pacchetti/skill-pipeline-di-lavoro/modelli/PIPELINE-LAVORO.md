# Pipeline di lavoro

Regola: la prima volta un lavoro si **registra** (si scrivono i passi fatti), la seconda nasce la
**pipeline**, la terza si **ottimizza**. Ogni correzione è un tassello: va scritta nel passo a cui
si riferisce. Le pipeline le aggiorna l'AI mentre lavora.

## 0. Come si usano

1. L'AI dice quale pipeline segue e la taglia del lavoro.
2. **Prima di ogni passo chiede:** «Faccio [passo]?» e aspetta il sì.
3. **Dopo il passo riferisce:** «Ho fatto questo, va bene?» con la prova.
4. Un no o una correzione va nel pezzo (se vale per tutti) o nelle Direttive del cliente, più una riga in STORICO.md.
5. Lavoro senza pipeline: si registrano i passi fatti (sezione «Registrazioni» in fondo).

Nessun passo diventa automatico da solo. Mai automatici: invii a persone vere, dati dei clienti,
cose che non si annullano.

## 1. Tipi di lavoro

Riempila guardando gli ultimi due o tre mesi di lavoro (task, email, sessioni).

| # | Tipo di lavoro | Quanto spesso | Clienti | Stadio (registrazione / pipeline / ottimizzata) |
|---|---|---|---|---|
| 1 | Landing e pagine | | | |
| 2 | Problema tecnico di un cliente | | | |
| 3 | Proposta / preventivo | | | |
| 4 | Report e KPI | | | |

## 2. Come si legge una pipeline

Pipeline = **tipo di lavoro × cliente** = pezzi generali + Direttive del cliente.
Ogni passo dice: chi lo fa · cosa consegna · skill · approvazione.

- `manuale` = serve il tuo ok, una scelta per volta.
- `auto` = già automatico.
- `candidato auto` = approvato più volte senza correzioni; si può proporre l'automatico dopo 5 di fila.

### Taglie del lavoro

| Taglia | Come si riconosce | Cosa si crea |
|---|---|---|
| Piccola | un passo, meno di un'ora | una task con 3-5 righe di checklist |
| Media | più passi, un cliente, qualche giorno | una task con la checklist completa (passi della pipeline + riga sulle Direttive) |
| Grande | più lavori, persone o settimane | un progetto con 3-5 fasi, una task media per lavoro |

## 3. Pezzi riutilizzabili

Passi che compaiono in più pipeline. Una pipeline li richiama per nome.

| Pezzo | Cosa fa | Approvazione |
|---|---|---|
| **P-stato** | Stato reale dalla fonte (API, foglio, log), mai dalla memoria | no |
| **P-archivio** | Cerca se il problema è già successo (archivio delle soluzioni) | no |
| **P-test** | Prova su un contatto di prova con un nome riconoscibile, poi cancellazione | no |
| **P-backup** | Copia → modifica su bozza → sistema vero → verifica caso per caso | manuale prima del sistema vero |
| **P-copy** | Il copy del cliente comanda: si cambiano solo link e segnaposto | manuale |
| **P-mobile** | Controllo a desktop e su telefono | candidato auto |
| **P-terzi** | Messaggi a clienti e fornitori: bozza, li mandi tu | manuale, mai auto |
| **P-scomposizione** | Lavoro senza pipeline: sei domande → cosa vuol dire «fatto» · quali passi · chi fa cosa · cosa serve da te · scadenza · cosa può andare storto | manuale: approvi lo scheletro |
| **P-chiusura** | HANDOFF e STORICO aggiornati, scheda soluzioni se non banale, task chiusa | no |

## 4. Cliente 1

### Direttive Cliente 1

Regole che valgono solo per questo cliente e vincono sui pezzi.
- (esempio) Il copy arriva sempre dal loro documento: non si riscrive.

### CL1-1 · Landing di lancio

Casi: (date dei lavori da cui è nata)

1. Copy dal documento del cliente, **P-copy** — AI legge — manuale.
2. Riferimenti grafici letti prima del brief — AI — no.
3. Decisioni di pagina (struttura, modulo, nomi) — AI prepara · tu scegli — manuale.
4. Prima bozza — AI o agente di design — manuale.
5. **P-mobile** — AI — candidato auto.
6. Pubblicazione — AI — manuale.

Correzioni già entrate: (data: correzione)

## 5. Lavori interni

### INT-1 · (nome)

## 6. Registrazioni (lavori fatti una volta sola)

### Registrazione · (nome del lavoro, data)

- Passi fatti: …
- Dove è servito l'ok: …
- Cosa rifarei diverso: …
