# Regole base uniche per tutti gli agenti

**Cosa fa.** Tieni le regole che valgono per tutti (come si scrive, come si verifica, cosa non
si manda fuori) in un file solo, `REGOLE-BASE.md`. Lo script le copia, fra due segni, dentro i
file di ogni agente che elenchi in `destinazioni.txt`. Fuori dai segni non tocca niente.

Se qualcuno cambia il blocco dentro una copia, al giro dopo torna uguale alla fonte. Una regola
si cambia in un posto solo, e vale per tutti al giro successivo.

Da me le regole base vivono in un file che gli agenti non possono modificare e si ricopiano
ogni ora. Le regole nuove ci entrano solo dopo un mio ok (pacchetto `impara-regole-proposte-con-ok`).

**Richiede.** Python 3, nessuna libreria in più. Ha senso se hai almeno due o tre file di
istruzioni diversi: sotto-agenti in `~/.claude/agents/`, un `AGENTS.md` per Codex, le regole di
un altro strumento.

**Dove si copia.** I tre file nella stessa cartella, per esempio `~/.claude/regole-base/`:
- `REGOLE-BASE.md`: le tue regole comuni (c'è un esempio corto: riscrivilo con le tue);
- `destinazioni.txt`: un file per riga;
- `distribuisci_regole.py`.

Poi scegli quando farlo girare:
- a mano, dopo aver cambiato `REGOLE-BASE.md`;
- ogni ora, con l'Utilità di pianificazione (Windows) o cron/launchd (Mac);
- oppure a ogni sessione, con un hook `SessionStart` che lancia
  `python3 "$HOME/.claude/regole-base/distribuisci_regole.py"`.

**Come si prova (su dati finti).**
1. Crea una cartella di prova con un file `agente.md` qualsiasi.
2. Scrivi il suo percorso in `destinazioni.txt` e lancia lo script: deve dire `aggiornata`.
3. Apri `agente.md`: in cima c'è il blocco fra `<!-- regole-base: inizio … -->` e `<!-- regole-base: fine -->`.
4. Cambia una parola dentro il blocco, lancia `--verifica`: deve dire `DIVERSA`. Rilancia senza
   `--verifica`: la parola torna com'era.

Io l'ho provato così, su file finti, il 27/11/2026.

**Limiti onesti.**
- Sul PC la protezione è solo «torna com'era al giro dopo». Se vuoi che un agente non possa
  proprio cambiare la fonte, serve un utente separato o un server, come faccio io.
- Tutto quello che metti in `REGOLE-BASE.md` entra in ogni agente e occupa contesto: tienilo corto.

**Come si toglie.** Ferma l'attività pianificata o l'hook. Nei file resta l'ultimo blocco:
cancellalo a mano fra i due segni, se non lo vuoi più.

## English

One source file of shared rules (`REGOLE-BASE.md`) copied by a script, between two markers, into every instruction file you list (sub-agents, AGENTS.md, other tools). Outside the markers nothing is touched; if someone edits the block in a copy, the next run restores it.

Install: copy the three files into a folder (for example `~/.claude/regole-base/`), write your rules in `REGOLE-BASE.md` and the target files in `destinazioni.txt`, then run `distribuisci_regole.py` by hand, every hour, or from a SessionStart hook.
