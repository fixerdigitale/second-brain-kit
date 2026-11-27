---
name: installa
description: >
  Runs the second brain's missions one at a time: the steps chosen in the onboarding PLAN (catalog
  cards with their package) and the kit's base missions (memory drawers and CLAUDE.md, profile,
  locked folders, local git). Every mission is idempotent: if the thing is already there, it skips
  it. Opened by the onboarding (phase 6) or with /second-brain:installa. — Esegue le missioni del
  second brain, una alla volta: i passi scelti nel PIANO dell'onboarding (schede del catalogo con il
  loro pacchetto) e le missioni di base del kit (cassetti della memoria e CLAUDE.md, profilo,
  cartelle chiuse a chiave, git locale). Ogni missione è idempotente: se la cosa c'è già, la salta.
  La apre l'onboarding (fase 6) o /second-brain:installa.
disable-model-invocation: true
argument-hint: "[id della missione o slug della scheda]"
---

# Installa: le missioni

Una missione = una cosa sola, fino a 15 minuti. Se la scheda o il pacchetto dicono di più
(per esempio 20-40 minuti), dividila in due missioni con un punto di arrivo ciascuna, e dillo prima. Prima chiedi «faccio X?», dopo dici «ho fatto
questo, guarda: <file>». Mai due missioni nello stesso messaggio. Rispondi nella lingua della
persona.

## Regole di ogni missione

1. **Idempotente.** Prima di tutto controlla se la cosa c'è già (i `segni_che_ce_l_hai` della
   scheda, i file che il pacchetto crea). Se c'è uguale: «C'è già, salto.» Se c'è diversa: mostra
   le differenze e chiedi cosa tenere. Rifare una missione non fa danni.
2. **Un sì per ogni file** che cambia o nasce fuori da `second-brain/`. Mostra percorso e contenuto
   (in T0 a parole, in T2-T3 il diff).
3. **Copia datata** prima di cambiare un file esistente: `<nome>.bak-AAAAMMGG-second-brain`
   (`-HHMM` se esiste già). L'ordine è sempre: copia, scrittura, rilettura. Mai spostare via il file
   per poi riscriverlo: se la scrittura fallisce, il file sparisce. Non cancellare: quello che va
   tolto finisce in `_da-cancellare/`, solo dopo che il nuovo è scritto e riletto.
4. **Hook, permessi, modalità automatica:** spiega l'effetto in una riga («da adesso, ogni volta che
   …, succede …») e come si toglie, poi il sì.
5. **Presi da fuori** (skill, MCP, plugin di terzi): leggi tutti i file prima di installare; cerca
   comandi che mandano dati fuori, che leggono chiavi o `.env`, `curl … | sh`, codice offuscato,
   aggiornamenti automatici. Se trovi qualcosa, fermati e mostralo con `file:riga`. Se la persona ha
   uno scanner di sicurezza per skill, usalo. Poi il sì.
6. **Dopo:** rileggi i file scritti, fai la prova scritta nel LEGGIMI del pacchetto, segna la
   missione: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/stato.py" --cartella "<cartella>" missione <id>
   fatta` (o `saltata` se la persona scrive `salta`). Su Windows `python` o `py -3` al posto di
   `python3`.
7. **Chiudi in tre righe:** cosa è cambiato, dove, come si torna indietro (copia, riga da togliere,
   la guida [tornare indietro](https://github.com/fixerdigitale/second-brain-kit/blob/main/plugin/second-brain/guide/05-tornare-indietro.md)).
   Niente percorsi della cartella del plugin: la persona non li apre.
8. **Comando o scrittura negata.** Se Claude Code nega un comando o una scrittura, ti fermi e lo dici
   in parole semplici: cosa volevi fare, che è stato bloccato, le strade possibili (rispondere sì alla
   finestra del permesso quando ricompare, il comando `/permissions`, lasciar perdere). Non rifai la
   stessa operazione con un altro strumento (python3, Write, Edit, un'altra shell) senza un sì
   esplicito su quella strada precisa. In T0-T1 non chiedi di aprire a mano file nascosti o JSON.
9. **Un comando per chiamata Bash**, con i percorsi interi fra virgolette: niente `;`, `&&`, `|`,
   `echo "exit=$?"`, variabili o cicli.

## Missione «scheda del catalogo» (id = slug)

1. Trova la scheda nell'indice `${CLAUDE_PLUGIN_ROOT}/catalogo-indice.json` e la repo del kit come
   dice `piano-upgrade` («Dove sta il catalogo»).
2. Leggi la scheda intera (`catalogo/<famiglia>/<slug>.md`) e, se c'è, tutto il pacchetto
   (`pacchetti/<slug>/`): il `LEGGIMI.md` e ogni file che verrebbe copiato. Non installare niente che
   non hai letto.
3. Se la scheda è «nessuno: solo idea»: non c'è niente da installare. Spiega l'idea in 5 righe e
   chiedi se vuole metterla da parte o costruirla insieme più avanti. Segna `saltata` con il motivo
   «solo idea».
4. Se è «nessuno: skill di terzi dalla fonte»: la fonte è nella scheda. Regola 5, poi il sì.
5. Altrimenti segui il `LEGGIMI.md` del pacchetto con la persona, un passo per messaggio, adattando
   i percorsi al suo sistema (Mac, Windows, Linux) e, se ha un vault, alla sua struttura. Se il
   pacchetto chiede un'intervista prima di una scelta difficile, usa la skill `grilling` (se c'è) o
   fai domande numerate con la tua risposta consigliata.

## Missione `cassetti-memoria`

Crea nella cartella di lavoro la memoria a cassetti del kit (`memoria/` con i modelli, `pipeline/`,
`soluzioni/`, `_da-cancellare/`) e il blocco del metodo nel `CLAUDE.md`. Non sovrascrive niente.
Se la persona ha già un vault, **non** proporla: proponi invece di usare il suo vault (la skill
`salva-in-memoria` lavora anche lì).

Prima conferma la cartella: mostra il percorso completo e chiedi «È questa la cartella di lavoro?».
Mai la cartella personale intera, la Scrivania o Download.

#### Mostra cosa manca

Se `bash` è disponibile, esegui sempre con `bash` davanti allo script:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/second-brain.sh" piano --cartella "<cartella>"
```

Spiega gli stati con parole semplici. Non applicare ancora nulla.

Su Windows converti prima i percorsi dalla forma `C:\...` alla forma `/c/...` e passa allo script soltanto percorsi con `/`.

Su Windows serve **Git Bash**, non un `bash` qualunque:

- Se il tuo strumento per i comandi è Bash (Git Bash), scrivi `bash` come sopra. La prima volta controlla con `bash --version`: deve contenere `msys`. Se contiene `linux`, stai usando WSL: non usarlo.
- Se il tuo strumento per i comandi è PowerShell, non scrivere `bash` da solo: su molti computer porta a `C:\Windows\System32\bash.exe`, cioè WSL, che non è adatto. Usa il percorso completo di Git Bash, per esempio `& "C:\Program Files\Git\bin\bash.exe" "<script>" piano --cartella "<cartella>"`. Se non è lì, cercalo in `%LOCALAPPDATA%\Programs\Git\bin\bash.exe`.
- Se Git Bash non c'è da nessuna parte, segui la sezione «Se bash non è disponibile».

Se lo script esce con codice 2, mostra alla persona il messaggio con parole semplici. Non riprovare con opzioni diverse: proponi il passo indicato dal messaggio, per esempio scegliere una cartella più sicura o risolvere con lei un blocco incompleto.

#### Cartelle e modelli

Raggruppa tutte le righe `NUOVO` del manifest. Mostra **tutti** i percorsi (è il «gruppo mostrato per intero» del patto) e chiedi un solo sì/no per creare cartelle e modelli, dicendo che può togliere singole voci. I file già presenti non vengono toccati.

#### CLAUDE.md

Mostra lo stato di `CLAUDE.md` e chiedi separatamente:

- se manca: se creare `CLAUDE.md`;
- se esiste senza blocco: se aggiungere il blocco in fondo;
- se il blocco esiste già: non proporre modifiche durante l'installazione.

Se `CLAUDE.md` usa fine riga Windows (CRLF), il blocco nuovo viene inserito con fine riga LF; la parte scritta dalla persona resta com'è.

#### Applica soltanto i sì

Se tutte le risposte sono no, non lanciare `applica`.

Esegui `applica` con un `--escludi` per ogni voce `NUOVO` rifiutata e aggiungendo l'opzione CLAUDE scelta:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/second-brain.sh" applica --cartella "<cartella>" [--escludi "<percorso>"] [--claude crea|aggiungi]
```

Se la persona accetta soltanto CLAUDE.md, usa lo script senza creare i file `NUOVO`:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/second-brain.sh" applica --cartella "<cartella>" --solo-claude --claude crea|aggiungi
```

Non scrivere mai `.second-brain/stato.txt` a mano. Se l'ultima riga di `CLAUDE.md` non ha un a capo, l'operazione ne aggiunge uno.

Dopo ogni scrittura, riapri il file o controlla il risultato.

Dopo l'applicazione, se il tono è T0-T1 imposta «Modo: passo passo» in cima a
`memoria/Correzioni/REGOLE-ORO.md`, se è T2-T3 «Modo: diretto» (con il sì). Non scrivere mai
«principiante» o «esperto»: il modo dice come parlare, non chi è la persona. Se la persona scrive
in inglese, nella sua parte del `CLAUDE.md` la prima riga diventa «Always answer in English.» al
posto di «Rispondi sempre in italiano.» (con il sì).

Se in `memoria/` esistono file come `chi-sono.md`, `clienti.md` o `lavori-ricorrenti.md`, dillo e
proponi i passi della guida `02-memoria.md`, ma non eseguirli in questa missione.

#### Se bash non è disponibile

Su Windows senza Git Bash, dillo chiaramente. Prima proponi di installare Git per Windows con `winget install --id Git.Git -e` (spiega che Windows può chiedere il permesso e che dopo va chiusa e riaperta l'app di Claude), e fallo solo dopo il sì. Se la persona non vuole installarlo, questo è l'unico caso in cui puoi eseguire le stesse verifiche e operazioni a mano con i tuoi strumenti, seguendo `modelli/MANIFEST.txt`: crea solo ciò che manca, non sovrascrivere mai, usa i modelli dentro `${CLAUDE_PLUGIN_ROOT}/modelli/`, crea una copia datata prima di ogni modifica a un file esistente e controlla il risultato. Spiega che senza bash lo stato automatico non può essere registrato e proponi di installare Git Bash prima di continuare.

## Missione `profilo`

Il profilo si ricava dalla fase 1 e dal primo risultato, non da un questionario. Proponi 5-8 righe
per la sezione «Chi sono» del `CLAUDE.md` (ruolo, lavoro che pesa, lingua, come vuole le risposte,
strumenti visti nei nomi delle cartelle). Se la persona usa già ChatGPT o un altro assistente,
proponi: «Se vuoi, incolla qui le tue istruzioni personalizzate o quello che la sua memoria dice di
te: ne tengo solo quello che serve.» Togli email, telefoni e nomi di clienti prima di proporre le
righe. Chiedi solo quello che manca, al massimo 2 domande. Niente
email, telefoni, dati di clienti. Mostra, sì, copia datata, scrivi.

## Missione `regole-deny`

Le cartelle chiuse a chiave proposte nel patto, se la persona le aveva saltate o rifiutate e adesso
le vuole. Testo e regole in `skills/onboarding/patto.md`.

## Missione `git-locale`

Controlla se la cartella è già sotto git. Spiega che git conserva versioni locali e si toglie solo rimuovendo la cartella nascosta `.git` con una scelta esplicita della persona. Chiedi se inizializzarlo. Con un secondo sì, crea o integra `.gitignore` senza cancellare righe esistenti, aggiungendo:

```gitignore
.env
.env.*
*.bak-*
```

Mostra `git status` e chiedi un altro sì prima del primo salvataggio. Prima lancia `cerca-segreti`
sui file che entrerebbero: se ne trova, prima si sistemano (una chiave salvata in git resta nella storia). Nel primo salvataggio includi soltanto i file del manifest, `CLAUDE.md`, `.second-brain/` e `.gitignore`; non aggiungere altri file. Non creare repository online e non fare push.

## Missione `compressione-contesto`

Proponi `autoCompactWindow` soltanto se hai verificato che il modello attivo abbia un milione di
token di contesto. Spiega che comprime prima la conversazione e che si toglie eliminando solo quella
chiave o rimettendo la copia. Se non puoi verificare il milione, non attivarla. Prima della modifica
fai una copia datata di `~/.claude/settings.json` e aggiungi la chiave senza cancellare altro. La
versione completa, con l'avviso sul contesto, è la scheda `hook-contesto-avviso-e-compressione`.
