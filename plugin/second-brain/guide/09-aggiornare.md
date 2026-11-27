# 09 · Aggiornare il pacchetto

Il pacchetto migliora nel tempo: skill corrette, guide nuove, regole aggiunte. Gli aggiornamenti li prendi **quando vuoi tu**, e non cancellano mai il tuo lavoro.

## Cosa si aggiorna e cosa no

| Si aggiorna da solo con il pacchetto | Si aggiorna solo se dici sì | Non si tocca mai |
|---|---|---|
| le skill del pacchetto, i due aiutanti, le guide | il blocco del metodo nel tuo `CLAUDE.md`; le cartelle e i modelli nuovi in `memoria/`, `pipeline/`, `soluzioni/` | la tua parte del `CLAUDE.md`, le tue note, le tue correzioni, le tue pipeline, le tue skill |

Le skill, gli aiutanti e le guide stanno nella cartella di sistema di Claude Code, non nella tua cartella di lavoro: aggiornarli non tocca i tuoi file.

## Come si aggiorna, in 2 passi

1. **Prendi la versione nuova.** In Claude Code scrivi `/plugin`, vai su **Marketplaces**, scegli `second-brain-kit` e premi **Update** (aggiorna). Oppure scrivi `/plugin marketplace update second-brain-kit`. Poi riavvia la sessione.
2. **Porta le novità nella tua cartella.** Scrivi `/second-brain:aggiorna`. Claude ti dice cosa è cambiato, in due righe per novità, e per ogni cosa che tocca la tua cartella ti chiede sì o no. Prima di cambiare un file ne fa una copia con la data.

Se nel blocco del metodo avevi cambiato qualcosa a mano, `/second-brain:aggiorna` te lo mostra e ti chiede cosa tenere. Il consiglio: le tue modifiche scrivile nella tua parte del `CLAUDE.md`, fuori dal blocco.

## Aggiornamento automatico

Di serie è **spento**: niente cambia senza che tu lo chieda. Se vuoi che Claude Code controlli da solo le versioni nuove, in `/plugin` → **Marketplaces** → `second-brain-kit` accendi l'aggiornamento automatico. Il passo 2 (`/second-brain:aggiorna`) resta sempre manuale.

Una cosa da sapere prima di accenderlo: un aggiornamento porta codice nuovo (skill, hook, script) che poi gira sul tuo PC, con i permessi che dai a Claude Code. Con l'aggiornamento automatico arriva senza che tu lo veda. Io preferisco leggere prima il `CHANGELOG.md` della versione nuova, e aggiornare a mano quando mi torna.

## Cosa è cambiato

Le novità di ogni versione sono in `CHANGELOG.md`, nella pagina del pacchetto su GitHub. `/second-brain:aggiorna` te le riassume.

## Se qualcosa va storto

- Ogni file cambiato ha una copia accanto, con la data nel nome (`CLAUDE.md.bak-20261120-second-brain`). Per tornare indietro: «rimetti la copia di CLAUDE.md di oggi».
- Se una versione nuova del pacchetto non ti convince, puoi lasciare le novità fuori dalla tua cartella: a `/second-brain:aggiorna` rispondi no, oppure rimetti le copie con la data. Se trovi un problema, puoi aprire una issue sulla pagina del kit su GitHub.
- Il repository è pubblico: per aggiornare non serve un accesso a GitHub. Se il passo 1 si ferma con un errore di rete, controlla la connessione e riprova più tardi.

## Prova adesso (2 minuti)

Scrivi `/second-brain:aggiorna`: se sei già all'ultima versione, te lo dice e non cambia niente.
