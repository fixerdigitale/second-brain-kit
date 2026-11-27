# second-brain — il plugin

*English below.*

## Cos'è

È il modo in cui lavoro io con Claude Code, messo in un plugin perché chiunque possa prenderne i
pezzi che gli servono. Non è un metodo da seguire: è la mia esperienza, con quello che mi funziona,
quello che ho scartato e il perché.

Si entra da una porta sola: **`/second-brain:onboarding`**. Non è un installatore. È un giro che si
adatta a chi c'è davanti:

1. **Patto** (2 min): cosa guarda, cosa non fa mai, come lo fermi.
2. **Sguardo veloce** (1-2 min): solo nomi e conteggi, e una domanda sola: «qual è un lavoro che
   rifai spesso e che ti pesa?».
3. **Primo risultato** (10-15 min): se parti da zero, quel lavoro fatto insieme; se hai già un
   sistema, un difetto trovato e chiuso; se hai un vault, una pulizia mirata. Con il numero prima e
   dopo, anche se è piccolo.
4. **Rendilo ripetibile** (5-10 min): il pezzo minimo perché domani non serva rispiegare.
5. **Mappa** (5-8 min): `second-brain/MAPPA.md` e `.html`, con cosa funziona già, le 8 aree, cosa
   perderesti se domani perdi il PC, una prova di ripristino vera del backup.
6. **Piano** (3-5 min): al massimo 3 passi dal catalogo, in ordine fisso: non perdere, non
   rispiegare, non rifare, delegare.
7. **Passi scelti**: una missione alla volta, fino a 15 minuti ciascuna.
8. **Rimisura** dopo 14 giorni: stesse misure, confronto, pulizia.

Il primo giorno sono 30-45 minuti fino al piano, di solito in 2-3 sedute. Si riprende con
«riprendiamo». In ogni momento: `salta`, `più piano`, `più veloce`, `fermati`.

## Come si installa

1. In Claude Code aggiungi il marketplace della repo del kit:
   `/plugin marketplace add <proprietario>/second-brain-kit`
2. Installa il plugin: `/plugin install second-brain@second-brain-kit`, e scegli «per te».
3. Riavvia la sessione, apri la tua cartella di lavoro e scrivi `/second-brain:onboarding`.

## Cosa guarda e cosa non fa mai

- **Guarda** i nomi dei file in Documenti, Scrivania, Download e nella cartella di Claude. Apre il
  contenuto solo della cartella di Claude e della cartella di lavoro che indichi tu. Le
  conversazioni passate solo con un consenso a parte, e solo per conteggi e temi.
- **Lo studio è in sola lettura imposta:** lo fa il sotto-agente `studia`, che ha solo gli strumenti
  di lettura (Read, Glob, Grep). Non ha un terminale e non può scrivere. Il resto (regole deny,
  materiale del primo risultato, script) lo fa la regia, che ha gli strumenti normali di Claude: lì
  il limite è il tuo sì e i permessi del tuo Claude Code, non un blocco del programma.
- **Non fa mai da solo:** leggere fuori dalle cartelle autorizzate, aprire browser, email o chat,
  stampare segreti (di una chiave dice solo `file:riga:NOME`), scrivere o cancellare senza un sì per
  ogni voce (prima fa una copia datata; non cancella, sposta in `_da-cancellare/`), fare push o
  condividere, installare cose prese da fuori senza un controllo, attivare hook o permessi larghi
  senza spiegarli, mandare dati fuori. MAPPA e PIANO restano nella cartella di lavoro: se quella è
  sincronizzata (OneDrive, iCloud, Dropbox, Google Drive) o ha una copia online con git, finiscono
  anche lì, e l'onboarding te lo dice prima (nella mappa, dei segreti scrive solo il numero).
- **Cosa parte da solo:** un hook all'avvio di Claude (`hooks/hooks.json`) che, dal giorno 14 dopo
  il piano, propone la rimisura una volta sola; finché l'onboarding non c'è, esce subito. Le skill
  `buone-maniere` e `salva-in-memoria` si attivano quando servono (la seconda chiede il sì prima di
  scrivere); `contro-parere` e `smistamento` si accendono solo a mano.

## Cosa c'è dentro

| Pezzo | Cosa fa |
|---|---|
| `skills/onboarding/` | la regia: fasi, stato, ripresa, rimisura. Con `patto.md`, `criteri-aree.md`, `tono.md` |
| `skills/primo-risultato/` | il primo risultato secondo chi c'è davanti, con la misura |
| `skills/piano-upgrade/` | filtra il catalogo e scrive il PIANO (massimo 3 passi) |
| `skills/installa/` | esegue le missioni, una alla volta, idempotenti |
| `skills/mappa-vault/` | per chi ha già un vault: mappa in sola lettura, poi al massimo 3 proposte |
| `skills/salva-in-memoria/` | scrive fatti e correzioni, anche dentro un vault che c'è già |
| `skills/aiuto/`, `contro-parere/`, `buone-maniere/`, `soluzioni/`, `definisci-pipeline/`, `smistamento/`, `google-account/`, `aggiorna/` | le skill del kit 1.0, aggiornate |
| `agents/studia.md`, `agents/revisore.md` | sola lettura e controllo di MAPPA e PIANO |
| `agents/esecutore.md`, `agents/costruttore.md` | due sotto-agenti economici per lavori meccanici e modifiche già decise |
| `catalogo-indice.json` | l'indice delle schede del catalogo, con area, gruppo del piano e tono minimo |
| `modelli/` | MAPPA, PIANO (anche in `en/`), `stato.json`, `pagina.html`, i cassetti della memoria |
| `scripts/` | vedi sotto |
| `guide/` | le guide, che si aprono con `/second-brain:aiuto` |

### Script

Tutti in Python 3 con la sola libreria standard, per Mac, Windows e Linux. Quelli che guardano i tuoi
file sono in sola lettura.

| Script | Cosa fa |
|---|---|
| `cerca_segreti.py` (`cerca-segreti.sh`, `.ps1`) | trova chiavi e password, anche nei `.docx`/`.xlsx`, stampa solo `file:riga:NOME` (una riga per riga sospetta) |
| `config_claude.py` | legge connettori, hook e permessi senza stampare token; aggiunge le regole deny con copia datata |
| `prova_ripristino.py` (`prova-ripristino.sh`, `.ps1`) | riapre il backup in una cartella temporanea e controlla profilo, memoria, regole, segreti, visibilità |
| `controlla_nomi.py` (`controlla-nomi.sh`, `.ps1`) | prima di pubblicare una cartella, blocca se trova nomi di un elenco privato (che sta fuori) |
| `date_cartelle.py` | nomi di cartelle, conteggi e date: distingue una cartella viva da una ferma |
| `salute_vault.py` | note, doppioni, orfane, conflitti, copertura dell'indice |
| `temi_sessioni.py` | conteggi e temi delle sessioni passate, solo con consenso |
| `stato.py` | legge e aggiorna `second-brain/.onboarding/stato.json` |
| `pagina.py` | MAPPA e PIANO in una pagina HTML che si apre senza login |
| `rimisura.py` | l'hook di avvio della rimisura |
| `genera_indice_catalogo.py` | rigenera `catalogo-indice.json` dalle schede della repo (per chi mantiene il kit) |
| `second-brain.sh` | crea i cassetti della memoria e il blocco del `CLAUDE.md` (missione `cassetti-memoria`) |

**Senza Python 3** l'onboarding funziona lo stesso: Claude usa i suoi strumenti di lettura, e alcuni
numeri (date, copertura dell'indice) restano «da confermare». Su Windows, se uno script `.ps1` è
bloccato, Claude spiega la Execution Policy e lo lancia con `-ExecutionPolicy Bypass` solo per quella
volta e solo dopo il tuo sì; non cambia mai l'impostazione del computer.

### Dove scrive

Nella cartella di lavoro, dentro `second-brain/`: `.onboarding/stato.json` (fase, consensi, tono,
voti, misure, missioni: solo nomi e numeri), `output/` (i risultati), `MAPPA.md/.html`,
`PIANO-UPGRADE.md/.html`, le mappe vecchie con la data. La missione `cassetti-memoria` scrive anche
`memoria/`, `pipeline/`, `soluzioni/`, `_da-cancellare/`, `.second-brain/stato.txt` e il blocco del
`CLAUDE.md`, ognuno con il suo sì.

## Quando non ti serve

Se usi Claude Code ogni tanto per un compito singolo, l'onboarding è più lungo del guadagno: ti basta
un `CLAUDE.md` di cinque righe. E se sai già quale pezzo vuoi, apri direttamente la sua scheda nel
catalogo.

## Come si toglie

`/plugin uninstall second-brain@second-brain-kit`. I file che ha scritto restano tuoi: cancella la
cartella `second-brain/` se non ti serve più. Le regole deny e le altre modifiche a `settings.json`
hanno accanto la copia `settings.json.bak-AAAAMMGG-second-brain`. Dettagli in
`guide/05-tornare-indietro.md`.

## Per chi mantiene il kit

- Dopo aver cambiato le schede: `python3 plugin/second-brain/scripts/genera_indice_catalogo.py`
  (rigenera l'indice e `skills/mappa-vault/catalogo.md`), poi `--controlla` per verificare che ogni
  pacchetto citato esista.
- Prima di ogni rilascio: `python3 plugin/second-brain/scripts/controlla_nomi.py --elenco
  <elenco-fuori-dalla-repo> .` Se esce con 1, il rilascio si ferma.

---

## English

**What it is.** This is how I work with Claude Code, packed into a plugin so anyone can take the
pieces they need. It's not a method to follow: it's my experience, what works for me, what I dropped
and why.

There is one entry point: **`/second-brain:onboarding`**. It's not an installer, it's a walk-through
that adapts to you: an agreement (2 min), a quick look (names and counts only, plus one question:
"what's a task you do often that weighs on you?"), a **first real result** in 10-15 minutes (your task
done together, or a defect found and fixed if you already have a system, or a targeted clean-up of
your vault), making it repeatable, a **map** of what you have (with a real restore test of your
backup), a **plan** of at most 3 steps from the catalogue in a fixed order (don't lose, don't
re-explain, don't redo, delegate), the chosen steps one at a time, and a **re-measure** after 14
days. Claude answers in the language you write in (Italian or English). At any time: `skip`,
`slower`, `faster`, `stop`.

**Install.** `/plugin marketplace add <owner>/second-brain-kit`, then
`/plugin install second-brain@second-brain-kit`, restart, open your work folder and type
`/second-brain:onboarding`.

**What it looks at, what it never does.** File names in Documents, Desktop, Downloads and the Claude
folder; content only of the Claude folder and the work folder you choose; past conversations only
with a separate consent, counts and topics only. The study is done by the `studia` sub-agent, which
only has read tools: read-only is enforced, not promised. It never reads outside the authorised
folders, never prints secrets (only `file:line:NAME`), never writes or deletes without a yes per item
(dated copy first, nothing deleted: moved to `_da-cancellare/`), never pushes or shares, never
installs outside code without a check, never sends data out. One automatic step only: a start-up hook
that offers the re-measure once, from day 14. Scripts are Python 3, standard library only; without
Python the walk-through still works, with a few numbers marked "to be confirmed".

**When you don't need it.** If you use Claude Code now and then for single tasks, a five-line
`CLAUDE.md` is enough.

**Remove.** `/plugin uninstall second-brain@second-brain-kit`; the files it wrote stay yours (delete
`second-brain/` if you like). Settings changes have a dated `.bak` copy next to them.
