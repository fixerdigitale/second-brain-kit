# Le 12 skill di design e il brief che le nomina

**Cosa fa.** Le dodici skill sono tutte di terzi e si prendono dalla fonte. Il pezzo nostro è il modello di brief (`modello-brief-design.md`): le nomina tutte, chiede una riga per skill nella consegna e una revisione alla cieca. Senza il brief, gli agenti ne aprono due o tre e dicono di averle usate.

**Fonti delle skill** (installale in `~/.claude/skills/<nome>/` seguendo ciascuna repo):

| Skill | Fonte | A cosa serve |
|---|---|---|
| impeccable | https://github.com/pbakaus/impeccable | costruire la pagina con un sistema di regole e controlli |
| design-critic | fonte da verificare | voto su 6 dimensioni e proposte di correzione |
| design-taste-frontend | ClawHub, `akdira/design-taste-frontend` (derivata da https://github.com/Leonxlnx/taste-skill, da verificare) | evitare le scelte da «template AI» |
| refactoring-ui | https://github.com/edisonmbli/refactoring-ui-skill | contrasti, spaziature, gerarchia (dal libro Refactoring UI) |
| critique-visual-hierarchy | https://github.com/Owl-Listener/designer-skills (solo quel file) | dove cade l'occhio, cosa si ruba l'attenzione |
| better-layout, better-interface, better-typography, better-colors, better-ui | https://github.com/jakubkrehel/skills | spazi, interfaccia, caratteri, colori, dettagli |
| ui-ux-pro-max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | catalogo di stili, palette e regole (solo i testi) |
| hallmark-riferimenti | https://github.com/Nutlope/hallmark (solo i testi su layout e macrostrutture) | strutture di pagina di riferimento |

Prima di installarle, passale da una scansione o leggile (vedi il pacchetto «cerca strumento»): alcune hanno script.

**Dove si copia il modello.** `modello-brief-design.md` dove tieni i modelli, per esempio `<cartella-vault>/modelli/`. Se vuoi che Claude lo usi da solo, nel `CLAUDE.md`: «Ogni brief di design usa `<cartella-vault>/modelli/modello-brief-design.md`».

**Come si prova.** Chiedi una sezione «chi siamo» con il modello. Nella consegna devono esserci 12 righe, ognuna con sì/no e una modifica concreta.

**Come si toglie.** Togli la riga dal `CLAUDE.md` e cancella le skill che non usi.

## English

A design brief template (`modello-brief-design.md`) that names all 12 third-party design skills I kept after comparing them, asks for a starting visual reference, and requires one line per skill in the delivery (opened yes/no, what it changed), followed by a blind review.

Install: get the skills from the sources listed above, then copy `modello-brief-design.md` into your vault and use it for every page or interface brief.
