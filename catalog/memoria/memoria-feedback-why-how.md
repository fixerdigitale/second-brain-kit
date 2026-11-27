---
slug: memoria-feedback-why-how
title: "Correction files with Why and How to apply"
area: memoria
where_it_runs: PC
level: basic
cost: "€0. Two minutes per correction, or zero if you ask Claude to do it."
package: "pacchetti/memoria-feedback-why-how/"
status: "I use it"
---

# Correction files with Why and How to apply

**The problem.** Corrections saved as a bare sentence ("don't do X") were applied literally and got the neighboring cases wrong. And I didn't know which corrections came back most often.

**How I solved it.** Each correction is a `feedback_<name>.md` file with three parts: what happened (date and exact words), **Why** (the concrete damage the rule prevents), **How to apply** (what to do in practice, with the exceptions). In the frontmatter there's a one-sentence description: that's what Claude reads to decide whether to open the file. When the correction comes back, I add "Update of dd/mm" at the bottom: counting them tells me which rules deserve to move up.

**Why this way.** With the why, Claude generalizes to cases the rule doesn't name. A good description gets the file opened at the right moment. The updates at the bottom are the evidence of how many times I had to repeat the thing, and they become the criterion for promoting it to the Golden Rules.

**When you need it.** If you often correct Claude on the same kind of thing and want the correction to stick.

**When you DON'T need it.** If your corrections are few and simple: a line in CLAUDE.md does the same job with fewer files.

**How to get it.** Copy `feedback_esempio.md` into your memory folder as a template, or write in CLAUDE.md: "save corrections as feedback_<name>.md with Why and How to apply parts".

Step-by-step instructions: [package guide](../../pacchetti/memoria-feedback-why-how/LEGGIMI.md).
