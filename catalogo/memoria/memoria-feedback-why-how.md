---
slug: memoria-feedback-why-how
titolo: "File di correzione con Why e How to apply"
area: memoria
dove_gira: PC
livello: base
costo: "0 €. Due minuti per correzione, o zero se lo chiedi a Claude."
pacchetto: pacchetti/memoria-feedback-why-how/
stato: lo uso
---

# File di correzione con Why e How to apply

**Il problema.** Le correzioni salvate come una frase secca («non fare X») venivano applicate alla lettera e sbagliate sui casi vicini. E non sapevo quali correzioni tornavano più spesso.

**Come l'ho risolto.** Ogni correzione è un file `feedback_<nome>.md` con tre parti: cosa è successo (data e parole esatte), **Why** (il danno concreto che la regola evita), **How to apply** (cosa fare in pratica, con le eccezioni). Nel frontmatter c'è una description di una frase: è quello che Claude legge per decidere se aprire il file. Quando la correzione torna, aggiungo in fondo «Aggiornamento del gg/mm»: contarli mi dice quali regole meritano di salire.

**Perché così.** Con il perché Claude generalizza ai casi che la regola non nomina. Una description buona fa aprire il file al momento giusto. Gli aggiornamenti in fondo sono la prova di quante volte ho dovuto ripetere la cosa, e diventano il criterio per promuoverla fra le Regole d'oro.

**Quando ti serve.** Se correggi Claude spesso sullo stesso tipo di cose e vuoi che la correzione resti.

**Quando non ti serve.** Se le tue correzioni sono poche e semplici: una riga in CLAUDE.md fa lo stesso lavoro con meno file.

**Come prenderlo.** Copia `feedback_esempio.md` nella cartella della memoria come modello, oppure scrivi in CLAUDE.md: «le correzioni salvale come feedback_<nome>.md con le parti Why e How to apply».

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-feedback-why-how/LEGGIMI.md).
