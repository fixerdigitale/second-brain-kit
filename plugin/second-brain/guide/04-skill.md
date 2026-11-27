# 04 · Le skill

Una **skill** è un manuale di istruzioni che insegni a Claude una volta sola. È una cartella con dentro un file `SKILL.md` (quando usarla e i passi da fare) e, se servono, modelli ed esempi. Claude la apre **da solo** quando la richiesta c'entra.

Con una skill il lavoro esce sempre con la stessa struttura e con le tue regole, senza ripeterle a ogni chat.

## Le skill di questo pacchetto

| Skill | Quando la usa Claude |
|---|---|
| `buone-maniere` | prima di modificare, cancellare, installare, pubblicare, inviare o spendere |
| `contro-parere` | quando la chiami tu (`/second-brain:contro-parere`); con il blocco del metodo nel `CLAUDE.md` le sue regole valgono sempre: controlla i fatti e ti dice quando non è d'accordo |
| `salva-in-memoria` | quando dici «salva», racconti un fatto o lo correggi; prima di scrivere ti mostra cosa e dove |
| `definisci-pipeline` | quando un lavoro si ripete |
| `smistamento` | quando la chiami tu (`/second-brain:smistamento`): domanda o lavoro, quale cliente, quanto è grande |
| `soluzioni` | prima e dopo un problema tecnico |
| `google-account` | quando un lavoro tocca file o email di Google |
| `aiuto` | quando chiedi come funziona qualcosa |

Le puoi anche chiamare a mano: `/second-brain:aiuto`, `/second-brain:definisci-pipeline`, e così via.

## Quando crearne una tua

Non tutto va trasformato in skill. Una skill conviene quando:

- un lavoro si ripete con **lo stesso metodo** (il report del lunedì, l'analisi delle creatività, il controllo errori di una campagna);
- hai corretto Claude più volte sullo **stesso lavoro**;
- c'è un **modello** da seguire (un formato di report, una struttura di brief).

Le informazioni su un cliente non sono una skill: vanno nella memoria. La skill dice **come** si fa un lavoro; la memoria dice **cosa** sai.

## Come si crea

1. Fai il lavoro una volta con Claude, correggendolo finché il risultato ti piace.
2. Alla fine chiedi: «trasforma quello che abbiamo fatto in una skill, con le mie correzioni dentro».
3. Rileggi il `SKILL.md` che ha scritto. Se manca una regola, aggiungila.
4. La volta dopo basta dire «fammi il report del lunedì per X»: usa la skill da solo.

Una skill tua va nella cartella `.claude/skills/` del tuo utente (vale per tutte le cartelle) oppure in `.claude/skills/` dentro la cartella di lavoro (vale solo lì). Claude sa dove metterla: chiediglielo.

Le skill di questo pacchetto si aggiornano con il pacchetto. Le tue no: sono tue.

## Dove trovarne altre

- Le skill ufficiali di Anthropic (Word, Excel, PowerPoint, PDF, creare skill): github.com/anthropics/skills
- Il catalogo ufficiale dei plugin: github.com/anthropics/claude-plugins-official
- La guida ufficiale alle skill in Claude Code: code.claude.com/docs/en/skills
- Se hai ricevuto l'elenco delle skill usate da chi ti ha dato il pacchetto, è un buon punto di partenza: prendine poche, quelle che servono al tuo lavoro.

## Prima di installare una skill presa da internet

Una skill può contenere istruzioni e programmi scritti da altri. Usa quelle ufficiali o di raccolte molto seguite, e prima di installarla chiedi sempre: «leggi questa skill e dimmi in parole semplici cosa fa e se fa qualcosa di strano. Non installarla finché non ti dico ok».

## Prova adesso (2 minuti)

Scrivi: «guarda le cose che ti ho chiesto di più nelle ultime settimane e dimmi quali 3 diventerebbero skill utili».
