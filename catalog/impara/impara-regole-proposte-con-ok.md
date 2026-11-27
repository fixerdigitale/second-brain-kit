---
slug: impara-regole-proposte-con-ok
title: "Rules proposed overnight, made permanent only after my ok"
area: impara
where_it_runs: PC on
level: medium
cost: "€0: no model, just a script. 15 minutes."
package: "pacchetti/impara-regole-proposte-con-ok/"
status: "PC version of mine"
---

# Rules proposed overnight, made permanent only after my ok

**The problem.** The corrections I gave several times deserved to become permanent rules, the ones Claude always reads. But if it promoted them on its own, sooner or later a wrong rule would get in, or a sentence written by someone else would become law. And if it was up to me to remember, it never happened.

**How I solved it.** Every night a run looks at the corrections saved in memory and finds the ones that came back at least twice. It doesn't apply them: it proposes them to me, one by one, as a "make it permanent?" question. In the morning I answer yes or no. Another run applies only the yeses, with a dated copy of the file before writing, and keeps a history of the decisions. A no is remembered, so the same proposal doesn't come back. The cap of 20 Golden Rules applies here too: when the cap is full, a yes waits until I remove one. On my side the question arrives as a card on my phone, and the same run also covers the rules shared by all agents. On the PC the card is a line in a file: put [x] or [-].

**Why this way.** The machine is good at counting how many times a correction came back; deciding what becomes a rule forever stays with me. Separating "propose" from "apply" gives me a moment to read, and the dated copy makes every yes reversible.

**When you need it.** If you save corrections in memory (card [corrections with Why and How](../memoria/memoria-feedback-why-how.md)) and keep the Golden Rules at the top of the index (card [index and Golden Rules](../memoria/memoria-indice-e-regole-doro.md)).

**When you DON'T need it.** If you have few corrections: with fewer than about twenty memory files you can reread them yourself in five minutes. And if you already do the end-of-day review (card [nightly reviewer](../memoria/memoria-revisore-notturno.md)), which also proposes Golden Rules: this is the automatic, model-free run, and one of the two is enough.

**How to get it.** Copy `regole_doro.py` and schedule `proponi` at night and `applica` in the morning, with the path of your memory folder. Step-by-step instructions: [package guide](../../pacchetti/impara-regole-proposte-con-ok/LEGGIMI.md).
