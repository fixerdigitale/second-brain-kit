# Criteri delle 8 aree

Il livello non si chiede: si legge dai file, area per area. Ogni livello ha un criterio che si può
verificare con un file, una riga o un conteggio. Il voto di un'area è il livello più alto di cui
**tutti** i criteri sono veri; se una situazione sta fra due righe (per esempio cartelle fisse ma un
indice sotto il 70%), vale il livello sotto: ogni livello comprende quelli prima. Ogni voto porta la
sua prova (`file:riga` o conteggio).

## Regole comuni a tutte le aree

1. **Conta solo quello che è vivo.** Una cosa vale per il livello solo se è stata toccata negli
   ultimi 90 giorni (data da `scripts/date_cartelle.py`, da `.git/logs/HEAD` o da una data scritta
   nel file). Se è più vecchia, scrivi «c'è, ferma da N mesi» e togli un livello. È la difesa
   contro il falso T3: una cartella piena ma abbandonata.
2. **Se non riesci a vedere la data**, il voto resta e accanto scrivi «data da confermare».
3. **«Non serve adesso» non è 0.** Se la persona dice che un'area non le serve (di solito
   Automazioni e canali, o gli agenti dentro Metodo), segnala così. Non entra nella media, non
   genera passi nel piano, e si richiede solo alla rimisura.
4. **Niente voti dal contenuto privato.** Per i voti bastano nomi, conteggi, titoli `##`,
   frontmatter e impostazioni. Il testo delle note dei clienti non serve.
5. **Provvisorio e completo.** Alla fase 1 il voto è provvisorio (solo nomi e conteggi). Alla fase 4
   diventa completo (lettura delle aree autorizzate). Nello stato: `"stato": "provvisorio"` o `"completo"`.
6. **I file del kit non sono della persona.** Dentro `~/.claude/` non contano `plugins/`, `projects/`
   (salvo la memoria automatica `projects/*/memory/`), `tmp/`, `file-history/`, `cache/`, `backups/`,
   `shell-snapshots/`: dopo l'installazione lì ci sono centinaia di `.md`, `CLAUDE.md`, `SKILL.md` e
   `HANDOFF.md` del kit stesso, che non dicono niente di chi c'è davanti. Neanche `second-brain/`
   nella cartella di lavoro conta.

Dove guardare, su tutti i sistemi: `~` è la cartella personale (`C:\Users\<nome>` su Windows).
`~/.claude/` contiene `CLAUDE.md`, `settings.json`, `skills/`, `agents/`, `projects/<cartella>/memory/`.
`~/.claude.json` contiene i server MCP (`mcpServers`) e la cronologia: non si apre con Read. Nomi,
tipo (locale o remoto), hook e permessi arrivano da `scripts/config_claude.py nomi`, lanciato dalla
regia.

---

## 1. Contesto — Claude sa chi sei e dove stanno le cose

| Livello | Criterio verificabile |
|---|---|
| 0 | Nessun `CLAUDE.md` (né in `~/.claude/` né nella cartella di lavoro) |
| 1 | Un `CLAUDE.md` con meno di 3 titoli `##`, oppure sotto le 20 righe |
| 2 | Un `CLAUDE.md` con almeno 3 sezioni fra: chi sono / come rispondere / dove stanno le cose / regole; toccato negli ultimi 90 giorni; sotto le ~300 righe |
| 3 | Livello 2 **più** un modo per tenerlo vero: file di passaggio (`HANDOFF.md`, `SISTEMA.md` o simili) nei lavori lunghi, oppure un hook `SessionStart` o `PreCompact`, oppure dettagli spostati in file a parte richiamati da `CLAUDE.md` |

Segnali di problema da annotare: regole che si contraddicono, fra due `CLAUDE.md` **o dentro lo
stesso file** (scrivi le due righe, `file:riga`), un `CLAUDE.md` oltre 300 righe.

## 2. Memoria — i fatti restano da una sessione all'altra

| Livello | Criterio verificabile |
|---|---|
| 0 | Niente: nessuna cartella di note, nessuna memoria in `~/.claude/projects/*/memory/` |
| 1 | Note sparse: file `.md` senza cartelle fisse, oppure memoria automatica senza indice, oppure cartelle fisse con un indice che copre meno del 70% |
| 2 | Cassetti con un indice: cartelle fisse (clienti, progetti, decisioni o simili) **e** un indice (`indice.md`, `MEMORY.md`, `Home.md`) che elenca almeno il 70% delle note (`scripts/salute_vault.py`) |
| 3 | Livello 2 **più** un controllo che li tiene in ordine: un giro programmato che rilegge o riordina, etichette nel frontmatter nella gran parte delle note, oppure un controllo di doppioni e orfane usato negli ultimi 90 giorni |

## 3. Correzioni — un errore corretto non si ripete

| Livello | Criterio verificabile |
|---|---|
| 0 | Nessuna correzione scritta da nessuna parte |
| 1 | Correzioni sparse: righe nel `CLAUDE.md` o note senza un posto fisso |
| 2 | Un posto fisso per le correzioni (`memoria/Correzioni/`, file `feedback_*.md` o simili) con il perché e il come si applica in almeno metà dei file, **oppure** un file di regole d'oro con un tetto |
| 3 | Livello 2 **più** un passaggio che promuove o rivede: regole proposte e approvate, revisore delle sessioni, storico delle regole tolte |

## 4. Metodo — i lavori che si ripetono hanno una procedura

| Livello | Criterio verificabile |
|---|---|
| 0 | Nessuna skill propria, nessuna procedura scritta |
| 1 | 1-2 procedure o skill scritte dalla persona, oppure prompt salvati in un file |
| 2 | Skill o pipeline per almeno 2 lavori ricorrenti, toccate negli ultimi 90 giorni; oppure sotto-agenti in `.claude/agents/` |
| 3 | Livello 2 **più** regia: una regola o skill che dice chi fa quale lavoro e chi controlla, oppure pipeline con uno storico delle correzioni |

## 5. Mestiere — le skill del lavoro che fai

| Livello | Criterio verificabile |
|---|---|
| 0 | Nessuna skill di mestiere (scrittura, design, analisi, legale, codice…) |
| 1 | Modelli o esempi salvati (preventivi, email, testi) senza una skill |
| 2 | Almeno una skill di mestiere installata o scritta, usata negli ultimi 90 giorni |
| 3 | Skill proprie con esempi e riferimenti **più** una revisione prima di mandare fuori |

## 6. Ricerca — ritrovare quello che c'è

| Livello | Criterio verificabile |
|---|---|
| 0 | Nessun ordine: file sparsi in Download e Scrivania, nomi senza schema |
| 1 | Cartelle e nomi coerenti (date, clienti) in almeno una cartella di lavoro |
| 2 | Un indice, un archivio delle soluzioni, un inventario, oppure link fra note in più di metà delle note |
| 3 | Ricerca per significato (un server MCP di ricerca nelle note, QMD o simili) **oppure** call e documenti lunghi trascritti e ricercabili |

## 7. Automazioni e canali — il lavoro che gira senza di te

| Livello | Criterio verificabile |
|---|---|
| — | «Non serve adesso», se la persona lo dice |
| 0 | Nessun hook, nessun lavoro programmato, nessun connettore |
| 1 | Un hook o una riga di stato in `settings.json`, oppure un lavoro programmato, oppure 1-2 connettori (MCP: Gmail, Slack, Drive…) collegati |
| 2 | Più hook (avvisi, notifiche, guardie) **oppure** lavori programmati con un registro **oppure** 3 o più connettori usati |
| 3 | Lavori in background o di notte con un controllo dei consumi, canali dal telefono, approvazioni in un posto solo |

## 8. Sicurezza e ripristino — se perdi il PC, non perdi il lavoro

| Livello | Criterio verificabile |
|---|---|
| 0 | Nessuna copia fuori dal PC (git senza remoto o una copia sullo stesso disco non contano) **e** nessuna regola `deny` sui segreti |
| 1 | Almeno una delle due: una copia fuori dal PC di qualunque tipo (cartella sincronizzata, git con remoto, disco esterno), oppure `permissions.deny` sui file dei segreti. Vale anche per chi ha git con remoto ma una chiave in chiaro |
| 2 | Copia fuori dal PC aggiornata negli ultimi 7 giorni (git con remoto privato o strumento di backup) **e** `permissions.deny` sui file dei segreti **e** nessuna chiave in chiaro nelle note (`cerca-segreti` pulito) |
| 3 | Livello 2 **più** una prova di ripristino riuscita, con la data (`scripts/prova-ripristino`), **più** una seconda copia in un altro posto |

Segnali da mettere in cima a «Dove si inceppa», qualunque sia il voto: una chiave in chiaro fuori
da `.gitignore`, un repository del backup pubblico, git e una cartella sincronizzata sulla stessa
cartella (rischio di `.git` rovinato).

---

## Dal voto al tono

Il tono si calcola solo da cinque aree: Contesto, Memoria, Correzioni, Metodo, Automazioni e canali.
Sono quelle che dicono quanto la persona usa già Claude come un sistema. Mestiere, Ricerca e Sicurezza
non alzano il tono: chi ha ottimi modelli di email e cartelle in ordine, ma nessun `CLAUDE.md`, resta T0.

Prendi il **secondo voto più alto** fra le cinque (così una sola skill installata non porta a T2):
0 → T0, 1 → T1, 2 → T2, 3 → T3. Se due letture sono possibili, scegli la più bassa e dillo. Il tono è
un modo di parlare, non un'etichetta: non si scrive mai «principiante» o «esperto».

## Come si mostrano i voti

- **T0-T1:** mai il numero. Tre colori: 🟢 c'è · 🔴 manca · ⚪ non serve adesso. Livello 0 = 🔴,
  livello 1 = 🔴 con «c'è un inizio», livello 2-3 = 🟢.
- **T2-T3:** numero 0-3 con la prova accanto.

## Impronta di un'area (per la ripresa)

Per ogni area salva in `stato.json` → `impronte_aree.<area>` una stringa corta con i numeri che
hai usato (per esempio `"claude_md=1;righe=84;sezioni=5;mod=2026-11-20"`). Alla ripresa rifai solo
lo sguardo veloce: se l'impronta di un'area è cambiata, rifai gli esami di quell'area e basta.
