---
slug: skill-stile-risposte
titolo: "Risposte corte e ordinate (caveman + i-have-adhd in italiano)"
area: skill
dove_gira: PC
livello: base
costo: "0 €; 5 minuti"
pacchetto: "pacchetti/skill-stile-risposte/"
stato: "lo uso"
---
# Risposte corte e ordinate (caveman + i-have-adhd in italiano)

**Il problema.** Le risposte erano lunghe, con il contesto prima della cosa da fare. Fra un messaggio e l'altro perdevo il filo di dove eravamo.

**Come l'ho risolto.** Tengo sempre accese due skill di terzi: caveman (via i riempitivi, una idea per frase) e i-have-adhd (prima riga = azione, passi numerati, stato ricapitolato a ogni turno, chiusura con una sola azione breve). Non le richiamo mai: nel mio sistema le due skill hanno `disable-model-invocation: true` e le regole stanno direttamente nel CLAUDE.md, quindi valgono in ogni sessione. Il pezzo mio è quel blocco di CLAUDE.md, che le adatta all'italiano: livello lite, con articoli e frasi intere, e una lista di cose che non si comprimono mai (numeri, percorsi, comandi, negazioni, incertezze, avvisi di sicurezza).

**Perché così.** I livelli più spinti di caveman nascono per l'inglese: in italiano senza articoli si legge male. Tagliare un «non» ribalta il senso, quindi le negazioni restano sempre. Lo stile vale solo in chat: codice, documenti e messaggi ad altri si scrivono normali.

**Quando ti serve.** Se leggi le risposte di fretta, dal telefono, o salti da un lavoro all'altro e ti serve ritrovare il punto.

**Quando non ti serve.** Se ti piacciono le spiegazioni discorsive o usi Claude per imparare un argomento nuovo: la compressione toglie il ragionamento che ti serve.

**Come prenderlo.** Installa le skill dalle fonti: https://github.com/JuliusBrussee/caveman e https://github.com/ayghri/i-have-adhd (MIT). Poi incolla il blocco del pacchetto nel tuo `CLAUDE.md`. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/skill-stile-risposte/LEGGIMI.md).
