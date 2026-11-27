---
tipo: mappa-vault
data: <AAAA-MM-GG>
vault: <cartella-vault>
fatta_da: skill mappa-vault (sola lettura)
---

# Mappa del vault — <AAAA-MM-GG>

> Fotografia in sola lettura. Niente è stato cambiato. I segreti sono indicati solo come file e riga.
> «non trovato» = cercato e non c'è. «da confermare» = dedotto, non misurato.

## 1. In breve

- Note: <N> in <N> cartelle · allegati: <N> (<dimensione>) · nota più recente: <data>
- Claude Code: CLAUDE.md <sì/no, righe> · memoria automatica <sì/no, file> · skill <N> · agenti <N> · hook <N>
- Backup: <git remoto sì/no, ultimo push> · <Drive/iCloud/OneDrive sì/no> · <disco sì/no> → copie: <N> di 3
- Uso: <N> sessioni in 14 giorni, <N> giorni attivi (oppure: «sessioni non guardate, permesso non dato»)

## 2. Struttura

| Cartella | Note | Dimensione | Più recente | Più vecchia | A cosa serve |
|---|---|---|---|---|---|
| <cartella>/ | <N> | <KB/MB> | <data> | <data> | <una riga> |

Convenzioni viste: <frontmatter, prefissi di data, link [[...]], tag>
Da notare: <note sopra 50 KB, cartelle vuote, note orfane>

## 3. Regole e memoria

- **CLAUDE.md**: <percorso, righe, sezioni>
- **Altri file di regole**: <~/.claude/CLAUDE.md, AGENTS.md…>
- **Contraddizioni trovate**: <file A riga N vs file B riga N, oppure «nessuna»>
- **Memoria automatica**: <percorso, MEMORY.md righe, N file, tipi, data ultima>

## 4. Skill, agenti, comandi, plugin

| Nome | Tipo | Dove | Cosa fa (una riga) | Sua o presa da fuori |
|---|---|---|---|---|

Skill che smista: <nome, regole di smistamento in 2 righe>

## 5. MCP e connettori (solo nomi)

| Nome | Locale o remoto | Dove è configurato |
|---|---|---|

Connettori claude.ai dichiarati dalla persona: <…>

## 6. Hook e permessi

- Hook: <evento → cosa fa>
- Permessi: allow <N> · ask <N> · deny <N> · defaultMode <…>
- Da guardare: <es. «Bash(*) libero», «.env non in deny»>
- Altro: <statusline, modello, compattazione>

## 7. Backup

| Copia | Dove | Ultimo aggiornamento | Note |
|---|---|---|---|
| Git | <servizio/nome-repo, privato sì/no/da confermare> | <ultimo commit, ultimo push> | <file non salvati, commit non mandati> |
| Sincronizzazione | <Drive/iCloud/OneDrive> | <…> | <git e sync sulla stessa cartella?> |
| Disco | <…> | <…> | |

Regola 3-2-1: <N> copie, <N> supporti, <N> fuori casa. Prova di ripristino: <mai/data>.
`.gitignore`: <cosa esclude, cosa manca>

## 8. Segreti trovati (solo posizione)

| File | Riga | Tipo | In git? |
|---|---|---|---|

## 9. Come lo usi ogni giorno

- Temi delle richieste: <tema (N richieste)>
- Ripetizioni viste: <«…» detto N volte>

## 10. Cosa funziona già (da tenere)

1. <cosa> — prova: <numero/file/abitudine>

## 11. Dove si inceppa (con le tue parole)

1. «<frase della persona>» — <cosa lo conferma nei dati>

## 12. Miglioramenti proposti (massimo 3)

1. **Non hai** <X>. **Significa che** <Y>. **Potresti** <azione> (scheda **`<slug>`**) **perché** <…>.
   Livello: <base/medio/avanzato> · Gira su: <PC/PC acceso/server> · Tempo: ~<N> min · Costo: <€>.
   Quando NON ti serve: <…>

## 13. Scelta

- Miglioramento scelto: <slug o «nessuno per ora»>
- Prossimo passo: aprire `pacchetti/<slug>/LEGGIMI.md` e seguirlo insieme.
