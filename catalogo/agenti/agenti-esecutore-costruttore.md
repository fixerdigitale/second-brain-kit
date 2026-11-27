---
slug: agenti-esecutore-costruttore
titolo: "Due sotto-agenti economici: esecutore e costruttore"
area: agenti
dove_gira: PC
livello: base
costo: "0 € in più: modelli già compresi nell'abbonamento Claude. Installazione: 2 minuti."
pacchetto: "pacchetti/agenti-esecutore-costruttore/"
stato: "lo uso"
---

# Due sotto-agenti economici: esecutore e costruttore

**Il problema.** Usavo il modello più caro anche per lavori meccanici: cercare un file, leggere un log, contare righe, applicare una correzione già decisa. La quota finiva su cose che non chiedevano ragionamento.

**Come l'ho risolto.** Ho creato due sotto-agenti di Claude Code. L'esecutore gira su Haiku e fa solo lavori meccanici, senza interpretare: se serve una scelta si ferma e fa la domanda. Il costruttore gira su Sonnet e scrive codice già deciso, segue lo stile che trova e si ferma se la decisione non regge. La sessione principale decide e rivede.

**Perché così.** Per me il ragionamento costoso serve a decidere e controllare, non a eseguire. Separando i ruoli la quota dura di più. E un agente che si ferma davanti a una scelta evita che un modello piccolo decida al posto mio.

**Quando ti serve.** Se fai spesso ricerche nei file, riassunti di log, rinomine o giri di piccole correzioni, e a volte arrivi al limite d'uso del piano.

**Quando non ti serve.** Se il tuo piano non ti fa mai arrivare al limite, o fai quasi solo lavori di ragionamento (strategia, testi): la differenza di consumo non la noti e aggiungi solo un passaggio.

**Come prenderlo.** Copia i due file `.md` in `~/.claude/agents/` (o nella cartella `.claude/agents/` del progetto) e controlla con `/agents` che compaiano. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/agenti-esecutore-costruttore/LEGGIMI.md).
