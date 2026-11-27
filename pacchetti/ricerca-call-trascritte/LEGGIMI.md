# Call trascritte: ricercabili e senza impegni persi

Due pezzi che si usano anche separati.
- `call_in_markdown.py` (meccanico): trasforma le trascrizioni in note markdown nel vault, con titolo, data e
  chi parla in testa. Così la ricerca (Grep, QMD o quello che usi) le trova come tutte le altre note, e a Claude
  puoi chiedere «cosa avevamo detto sul preventivo nella call di martedì?».
- La skill `scheda-call` (giudizio): da una trascrizione scrive la scheda della call, cioè decisioni, lavori
  chiesti adesso separati dalle idee per il futuro, controllo uno per uno degli action item del registratore,
  dubbi, e una bozza di recap per l'altra persona che non parte da sola.

## Cosa c'è

- `call_in_markdown.py`: prende una cartella di trascrizioni `.txt`, `.vtt` o `.srt` e scrive una nota per call
  in `<cartella-vault>/Call/`. Non tocca gli originali, non riscrive le note già fatte. Solo libreria standard,
  Python 3.9 o più recente.
- `scheda-call/SKILL.md`: la skill. Se la nota della call esiste già, mette la scheda sopra la trascrizione.

## Dove si copia

1. Lo script in `~/.claude/strumenti/` (o dove vuoi).
2. La cartella `scheda-call/` in `~/.claude/skills/scheda-call/`. Nel `SKILL.md` cambia `<cartella-vault>` e il
   nome del file dei task con quelli tuoi.
3. Scarica le trascrizioni dal tuo strumento di registrazione (Fathom, Meet, Zoom, Teams…) in una cartella, per
   esempio `~/Downloads/trascrizioni/`. Se il nome del file contiene la data (`2026-11-24-...`) la nota la usa;
   altrimenti prende la data del file.
4. Lancia: `python3 ~/.claude/strumenti/call_in_markdown.py ~/Downloads/trascrizioni <cartella-vault>/Call`
5. Per la scheda: in Claude Code «fammi la scheda della call del 24/11», oppure incolla la trascrizione.

Se il tuo registratore ha un connettore ufficiale per Claude (Fathom ne ha uno MCP), puoi attivarlo e Claude
legge la call da lì: verifica sul sito del registratore cosa offre il tuo piano. Se le trascrizioni arrivano da
sole in una cartella (API o Drive), puoi lanciare lo script a ogni sessione con un hook `SessionStart`. Gira solo
a PC acceso.

## Come si prova

- Script: metti in una cartella un file `2026-11-24-prova-call.txt` con due righe tipo `Mario: ciao` e
  `Anna: ciao a te`, lancia lo script e apri la nota: dovrebbe avere data 24/11/2026 e «Parlano: Mario, Anna».
- Skill: dalle la trascrizione di una call vecchia di cui ricordi bene gli impegni, e controlla che li trovi
  tutti e che non trasformi in task le idee buttate lì.

## Come si toglie

Cancella lo script e `~/.claude/skills/scheda-call/`. Le note restano nel vault: se non le vuoi, cancella la
cartella `Call/`.

## Attenzione

Le trascrizioni contengono quello che dicono clienti e collaboratori. Se il vault va su GitHub o Drive, quelle
frasi ci vanno con lui: tienilo privato, e se una call è delicata non importarla.

## Differenza con il mio

Da me, quando una call finisce il registratore avvisa il server, il mio assistente principale fa la scheda e
prepara il recap, e ogni ora uno script scrive le note delle call nella cartella che la ricerca per significato
indicizza insieme al vault. Le registrazioni le copio anche su una libreria video mia, così l'archivio non dipende
dall'account del registratore. Sul PC la parte automatica non c'è: scarichi tu le trascrizioni.

## English

Makes call transcripts searchable and actionable. `call_in_markdown.py` turns a folder of .txt, .vtt or .srt transcripts into one markdown note per call (title, date, speakers, full transcript). The `scheda-call` skill sorts each point into work, idea or agreement and drafts a recap that is never sent without your yes.

Install: copy `call_in_markdown.py` into `~/.claude/strumenti/` and `scheda-call/` into `~/.claude/skills/scheda-call/`. Run `python3 call_in_markdown.py <transcripts-folder> <vault-folder>/Call`, then ask Claude for the call note. Keep the vault private if it holds clients' words.
