# Report in pagina (skill)

**Cosa fa.** Quando un risultato va letto (da te dal telefono, da un socio, da un cliente), Claude
lo scrive come pagina HTML unica: titolo, indice, sezioni numerate con la conclusione in cima,
tema chiaro e scuro, nessuna libreria esterna. La salva in `<cartella-vault>/report/<slug>.html`
e, se c'è, aggiunge una riga in `ELEMENTI.md`.

**Dove si copia.** La cartella `report-pagina/` (con `SKILL.md` e `template.html`) in
`~/.claude/skills/report-pagina/`. Se hai colori o logo tuoi, cambia le variabili in cima a
`template.html` (`--accento`, `--sfondo`...).

**Come si prova.** In Claude Code: «fammi un report-pagina sulle note di questa settimana».
Apri il file con un doppio clic, poi dal telefono (se il vault è su Drive o simili).

**Differenza con il mio sistema.** Io pubblico i report su un sito mio dietro login, con un
catalogo di tutti i documenti: quello vuole un server. Qui la pagina è un file: per farla vedere a
qualcuno la carichi su Drive o la mandi.

**Come si toglie.** Cancella `~/.claude/skills/report-pagina/`.

**Se la pagina deve arrivare a qualcuno.** Tre strade, dalla più semplice:
1. La carichi nella cartella «Consegne» del cliente su Drive, condivisa solo con le persone giuste
   (vedi `pacchetti/canali-drive-cartelle-cliente/`). Drive non mostra l'HTML come pagina: chi la
   riceve la scarica e la apre.
2. La pubblichi come pagina privata di claude.ai, se il tuo piano lo offre, e condividi il link
   solo quando decidi tu.
3. Un sito tuo dietro login, come il mio: serve un server, un sistema di accesso con secondo fattore
   e qualcuno che lo aggiorni. Ha senso solo se consegni spesso a più clienti.

## English

A `report-pagina` skill that turns any document into a single self-contained HTML page with a fixed style: conclusion at the top, table of contents, numbered sections. It opens with a double click and reads well on a phone. This guide also explains three ways to deliver it: Drive, a private claude.ai page, or your own site with login.

Install: copy `report-pagina/` (`SKILL.md` and `template.html`) into `~/.claude/skills/report-pagina/` and change the colors at the top of the template if you want your own.
