---
tipo: mappa-vault
data: 2026-11-27
vault: ~/Documenti/vault-esempio
fatta_da: skill mappa-vault (sola lettura)
---

<!-- ESEMPIO CON DATI FINTI. Persona, cartelle, numeri e nomi sono inventati. -->

# Mappa del vault — 2026-11-27

> Fotografia in sola lettura. Niente è stato cambiato. I segreti sono indicati solo come file e riga.
> «non trovato» = cercato e non c'è. «da confermare» = dedotto, non misurato.

## 1. In breve

- Note: 412 in 9 cartelle · allegati: 138 (210 MB) · nota più recente: 2026-11-26
- Claude Code: CLAUDE.md sì, 342 righe · memoria automatica sì, 27 file · skill 6 · agenti 1 · hook 0
- Backup: git remoto sì, ultimo push 19 giorni fa · Google Drive sì · disco non trovato → copie: 2 di 3
- Uso: 31 sessioni in 14 giorni, 11 giorni attivi

## 2. Struttura

| Cartella | Note | Dimensione | Più recente | Più vecchia | A cosa serve |
|---|---|---|---|---|---|
| 00-inbox/ | 47 | 180 KB | 2026-11-26 | 2026-08-02 | appunti veloci da smistare |
| personale/ | 63 | 290 KB | 2026-11-24 | 2025-01-10 | salute, casa, idee |
| lavoro/ | 88 | 640 KB | 2026-11-26 | 2025-03-04 | strategia, numeri, decisioni |
| team/ | 71 | 410 KB | 2026-11-25 | 2025-06-18 | persone del team, riunioni |
| clienti/ | 90 | 1,1 MB | 2026-11-26 | 2025-02-11 | una cartella per cliente |
| contenuti/ | 39 | 220 KB | 2026-11-20 | 2025-09-01 | post, newsletter |
| modelli/ | 9 | 18 KB | 2026-04-02 | 2025-01-10 | modelli di nota |
| allegati/ | 0 | 210 MB | 2026-11-22 | 2025-01-15 | immagini e PDF |
| archivio/ | 5 | 22 KB | 2025-12-30 | 2025-01-10 | quasi vuota |

Convenzioni viste: frontmatter con `tipo:` e `cliente:` in 84 note di clienti su 90; nomi con data
`AAAA-MM-GG` in `team/`; link `[[...]]` in 61% delle note.
Da notare: 3 note sopra 50 KB (`lavoro/diario-2026.md` è 140 KB); 47 note ferme in `00-inbox/`,
la più vecchia da agosto.

## 3. Regole e memoria

- **CLAUDE.md**: radice del vault, 342 righe, 14 sezioni; la metà sono regole aggiunte in coda senza titolo.
- **Altri file di regole**: `~/.claude/CLAUDE.md` (40 righe).
- **Contraddizioni trovate**: `CLAUDE.md` riga 58 «rispondi sempre in elenco puntato» vs riga 301
  «niente elenchi, scrivi in prosa». `~/.claude/CLAUDE.md` riga 12 «salva le note in inbox» vs
  `CLAUDE.md` riga 90 «salva direttamente nella cartella giusta».
- **Memoria automatica**: `~/.claude/projects/<cartella-del-progetto>/memory/`, `MEMORY.md` 118 righe,
  27 file: 15 fatti su clienti, 9 correzioni, 3 sull'utente. Ultima: 2026-11-25.

## 4. Skill, agenti, comandi, plugin

| Nome | Tipo | Dove | Cosa fa (una riga) | Sua o presa da fuori |
|---|---|---|---|---|
| smista-note | skill | vault/.claude/skills | decide personale / lavoro / team | sua |
| verbale-riunione | skill | vault/.claude/skills | da appunti a verbale con azioni | sua |
| post-linkedin | skill | ~/.claude/skills | bozza post dal tono salvato | sua |
| skill-creator | skill | ~/.claude/skills | crea skill nuove | presa da fuori |
| frontend-design | skill | ~/.claude/skills | pagine web | presa da fuori |
| pdf | skill | ~/.claude/skills | legge e crea PDF | presa da fuori |
| ricercatore | agente | ~/.claude/agents | ricerche web, modello Sonnet | suo |

Skill che smista: `smista-note` guarda parole chiave («team», «riunione» → team; «fatturato»,
«strategia» → lavoro; il resto → personale). Non legge il frontmatter.

## 5. MCP e connettori (solo nomi)

| Nome | Locale o remoto | Dove è configurato |
|---|---|---|
| filesystem | locale | ~/.claude.json, progetto |
| google-calendar | remoto | ~/.claude.json, globale |

Connettori claude.ai dichiarati dalla persona: Gmail, Google Drive.

## 6. Hook e permessi

- Hook: nessuno.
- Permessi: allow 23 · ask 0 · deny 0 · defaultMode `acceptEdits`
- Da guardare: `Bash(git push:*)` è libero; nessun `deny` sui file `.env`.
- Altro: nessuna statusline, modello di serie, compattazione di serie.

## 7. Backup

| Copia | Dove | Ultimo aggiornamento | Note |
|---|---|---|---|
| Git | GitHub, `vault-esempio`, privato (confermato dalla persona) | ultimo commit 2026-11-08, ultimo push 2026-11-08 | 64 file modificati e non salvati |
| Sincronizzazione | Google Drive per desktop, cartella `Il mio Drive/vault-esempio` | continuo | git e Drive sulla stessa cartella, `.git` compreso |
| Disco | non trovato | — | la persona dice: «non ce l'ho» |

Regola 3-2-1: 3 copie a parole, ma Drive e git copiano la stessa cartella dallo stesso PC; 1 copia
fuori casa vera (GitHub). Prova di ripristino: mai.
`.gitignore`: esclude `.obsidian/workspace.json`; non esclude `.env` né `allegati/`.

## 8. Segreti trovati (solo posizione)

| File | Riga | Tipo | In git? |
|---|---|---|---|
| clienti/cliente-b/accessi.md | 12 | sembra una password | sì |
| .env | — | file di variabili (non aperto) | sì |

## 9. Come lo usi ogni giorno

- Temi delle richieste: verbali di riunione (19), post e newsletter (14), smistare l'inbox (11),
  preparare call con clienti (9), conti e numeri (6).
- Ripetizioni viste: «il verbale lo voglio con le azioni in cima» detto in 5 sessioni diverse;
  «riprendiamo da dove eravamo con cliente-a» all'inizio di 4 sessioni, ogni volta con 10-15
  righe di spiegazione.

## 10. Cosa funziona già (da tenere)

1. Frontmatter uguale nelle note dei clienti (84 su 90): Claude le ritrova e le filtra bene.
2. I tre brain (personale / lavoro / team) sono chiari e usati tutti: 63, 88 e 71 note.
3. La skill `verbale-riunione` è la più usata (19 volte) e la persona dice «quella è perfetta».
4. Repository privato su GitHub: c'è già una copia fuori casa.
5. I modelli di nota in `modelli/` sono pochi e usati.

## 11. Dove si inceppa (con le tue parole)

1. «Ogni volta gli devo rispiegare come voglio il verbale» — 5 sessioni con la stessa correzione;
   nessun file in memoria la contiene.
2. «Su cliente-a riparto sempre da zero» — 4 sessioni aperte con la stessa spiegazione.
3. «Le note delle riunioni del team a volte finiscono in lavoro» — 7 note di riunione in
   `lavoro/` con `tipo: riunione` nel frontmatter.
4. «Il backup? C'è GitHub… credo» — ultimo push 19 giorni fa, 64 file non salvati.

## 12. Miglioramenti proposti (massimo 3)

1. **Non hai** un backup che parte da solo né una copia separata da Drive → **significa** che gli
   ultimi 19 giorni di lavoro (64 file) esistono solo sul PC e su Drive, che copia anche gli errori e
   può rovinare la cartella `.git`; in più una password è dentro il repository → nel catalogo c'è
   **`sicurezza-backup-notturno`**, ti serve perché separa le copie (git fuori da Drive, un disco o un
   secondo servizio) e ti dice come togliere la password dalla storia di git.
   Livello: base · Gira su: PC · Tempo: ~30 min · Costo: 0 € in più (con un disco che hai già).
   Quando NON ti serve: se fai già push ogni giorno e hai una copia su un supporto diverso.
2. **Non hai** un posto dove finiscono le correzioni → **significa** «ogni volta gli devo
   rispiegare il verbale»: la regola vive solo nella chat e muore con la sessione → nel catalogo c'è
   **`memoria-feedback-why-how`**, ti serve perché ogni correzione diventa un file breve con il
   perché e il come, che Claude rilegge da solo.
   Livello: base · Gira su: PC · Tempo: ~15 min · Costo: 0 € in più.
   Quando NON ti serve: se correggi Claude raramente o ogni volta su cose diverse.
3. **Non hai** un file di stato per i lavori lunghi → **significa** «su cliente-a riparto sempre da
   zero»: 10-15 righe di spiegazione a ogni sessione → nel catalogo c'è **`memoria-handoff-e-sistema`**,
   ti serve perché `HANDOFF.md` tiene il lavoro aperto e `SISTEMA.md` i fatti fermi del cliente, e
   la sessione nuova parte da lì.
   Livello: base · Gira su: PC · Tempo: ~20 min per il primo cliente · Costo: 0 € in più.
   Quando NON ti serve: per clienti con lavori di un giorno, che non riprendi.

Lasciato fuori di proposito: lo smistamento sbagliato in `lavoro/` (punto 3 dei problemi) si
risolve facendo leggere a `smista-note` il frontmatter `tipo:`; è una modifica della sua skill, non
serve un pacchetto nuovo. Il CLAUDE.md con regole in contraddizione (`memoria-claude-md-a-sezioni`)
viene dopo questi tre.

## 13. Scelta

- Miglioramento scelto: `sicurezza-backup-notturno`
- Prossimo passo: aprire `pacchetti/sicurezza-backup-notturno/LEGGIMI.md` e seguirlo insieme.
