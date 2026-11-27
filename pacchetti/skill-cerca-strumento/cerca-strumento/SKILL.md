---
name: cerca-strumento
description: Trova e valuta uno strumento nuovo (server MCP, skill, repo GitHub, libreria) prima di installarlo. Usala quando l'utente dice «mi serve una funzione per…», «c'è qualcosa che fa…», quando gira un link a una repo, a un MCP o a una skill chiedendo «può esserci utile?», e prima di installare qualsiasi cosa presa da GitHub o da un registro di skill.
---

# Cerca strumento: trovare e valutare prima di installare

Scopo: rispondere a «c'è già qualcosa che lo fa?» con **un verdetto in tre righe**, dopo aver
controllato che lo strumento sia vivo, affidabile e sicuro. In questa fase non si installa
niente: si cerca, si legge, si giudica.

## 0. Prima guarda in casa

1. Le skill e gli MCP che hai già (`~/.claude/skills/`, `.claude/skills/` del progetto, `claude mcp list`).
2. `valutati.md` in questa cartella: potrebbe essere già stato valutato e scartato.

## 1. Dove cercare, in quest'ordine

| Cosa serve | Dove |
|---|---|
| Server MCP | registro ufficiale: `https://registry.modelcontextprotocol.io/v0.1/servers?search=<parola>&limit=20` (JSON, senza chiave) |
| Server MCP controllati a mano | PulseMCP (`https://www.pulsemcp.com/servers?q=<parola>`), Glama (`https://glama.ai/mcp/servers?query=<parola>`) |
| Connettori già ospitati | Smithery (`https://smithery.ai/search?q=<parola>`) |
| Skill | skills.sh, SkillsMP, claudemarketplaces.com; come modello `github.com/anthropics/skills` |
| Repo e librerie | GitHub, ordinando per stelle (`gh search repos "<parola>" --sort stars --limit 15`) |
| Liste curate | `github.com/modelcontextprotocol/servers`, `github.com/wong2/awesome-mcp-servers` |

Registri aperti di skill (dove chiunque pubblica): usali solo per sapere che una skill esiste.
Nel 2026 ci sono state campagne di skill malevole (furto di chiavi SSH e token, nomi quasi uguali
a quelli veri). Una skill presa da lì si legge riga per riga, script compresi.

Se l'utente ha girato un link: parti da quello, poi cerca **due alternative** per confronto.

## 2. Come giudicare ogni candidato (massimo 3 finalisti)

- **Vivo?** Ultimo commit, release recenti, issue aperte senza risposta
  (`gh repo view <owner/repo> --json stargazerCount,pushedAt,licenseInfo,isArchived`).
- **Chi lo mantiene?** Per un servizio, l'MCP ufficiale del fornitore vince.
- **Cosa tocca?** File, rete, chiavi, shell. Script che scaricano ed eseguono codice, leggono
  `~/.ssh` o le variabili d'ambiente = no, salvo motivo fortissimo.
- **Come si collega?** MCP remoto (URL + chiave), MCP locale, CLI, libreria. Serve una chiave?
- **Funziona dove serve?** Claude Code sul PC, app claude.ai, telefono.
- **Licenza** compatibile con l'uso per clienti.
- **Leggi il codice** del punto d'ingresso, non solo il README.
- **Scanner di sicurezza** se ce l'hai (per esempio SkillSpector, github.com/NVIDIA/SkillSpector):
  0-20 ok; 21-49 leggi i finding; 50+ leggi ogni finding e, se anche uno è vero, il verdetto è
  LASCIO PERDERE. Molti finding statici sono falsi positivi (una skill che *cita* un file di
  chiavi prende un avviso alto): scrivi quali scarti e perché.

## 3. Il verdetto

Tre righe, niente muro di testo:

```
<nome> — <cosa fa in 6 parole>
Verdetto: INSTALLO / PROVO ISOLATO / LASCIO PERDERE
Perché: <il motivo principale, con un fatto verificato (stelle, ultimo commit, cosa tocca)>
Sicurezza: <cosa hai letto, finding veri o «falsi positivi: …»>
```

Se ci sono alternative serie, una riga ciascuna.

## 4. Regole ferme

- Mai installare in questa fase. L'installazione è un passo separato, dopo l'ok.
- Si controlla **la versione che si installa** (stesso commit o zip), non una qualsiasi.
- «Prova isolata» = cartella o utente separato, senza le tue chiavi, senza accesso alle tue note.
- Le chiavi vanno in un file di segreti fuori dal vault, mai nei file della skill.
- Dopo il verdetto aggiungi una riga a `valutati.md` (data, nome, link, verdetto, perché),
  anche per i no: la prossima volta non si rifà il giro.
