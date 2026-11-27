---
slug: memoria-claude-md-a-sezioni
titolo: "Un CLAUDE.md a sezioni fisse"
area: memoria
dove_gira: PC
livello: base
costo: "0 €. Circa 30 minuti per riempire il modello la prima volta."
pacchetto: pacchetti/memoria-claude-md-a-sezioni/
stato: lo uso
---

# Un CLAUDE.md a sezioni fisse

**Il problema.** Ogni sessione di Claude Code parte da zero. Mi ritrovavo a rispiegare come voglio le risposte, dove stanno i progetti, cosa non si tocca e dove si salvano le cose. Le istruzioni che avevo già dato si perdevano da una sessione all'altra.

**Come l'ho risolto.** Ho un CLAUDE.md, che Claude legge a ogni messaggio, diviso in sezioni sempre uguali: come rispondermi (lo stile scritto per intero, non un rimando a una skill), dove operare (cartelle dei progetti, cosa non toccare, dove stanno i segreti: solo il percorso), «prima di dire non ce l'ho leggi l'inventario», dove va la memoria (fatti nel vault, correzioni nella memoria di Claude), passaggio di consegne con HANDOFF e SISTEMA, e una sezione Regole con le correzioni che ho dovuto ripetere, ognuna con la data.

**Perché così.** CLAUDE.md è l'unico posto che viene letto sempre. Una skill si apre solo se sembra pertinente, un file di memoria solo se il titolo combacia. Quando ripeto una regola per la seconda volta la sposto qui: è il modo che ho trovato perché non si perda. Le sezioni fisse mi servono a ritrovarla e a correggerla sul posto, invece di aggiungere sempre in fondo.

**Quando ti serve.** Se usi Claude Code tutti i giorni su più progetti e ti capita di ripetere le stesse istruzioni, o di vedere Claude ricostruire uno strumento che hai già.

**Quando non ti serve.** Se apri Claude Code ogni tanto per un compito singolo: cinque righe bastano. E occhio al peso: il mio è arrivato a circa 270 righe (23 KB) e si carica a ogni messaggio, consumando contesto. Quando cresce così, conviene spostare i dettagli in file a parte e lasciare qui solo la regola con il percorso.

**Come prenderlo.** Copia `CLAUDE.md` del pacchetto in `~/.claude/CLAUDE.md` (vale per tutti i progetti) oppure nella cartella del progetto. Sostituisci i segnaposto `<...>` e cancella le sezioni che non ti servono.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-claude-md-a-sezioni/LEGGIMI.md).
