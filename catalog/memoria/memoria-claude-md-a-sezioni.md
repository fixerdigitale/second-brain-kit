---
slug: memoria-claude-md-a-sezioni
title: "A CLAUDE.md with fixed sections"
area: memoria
where_it_runs: PC
level: basic
cost: "€0. About 30 minutes to fill in the template the first time."
package: "pacchetti/memoria-claude-md-a-sezioni/"
status: "I use it"
---

# A CLAUDE.md with fixed sections

**The problem.** Every Claude Code session starts from zero. I kept re-explaining how I want answers, where the projects are, what not to touch and where things get saved. Instructions I had already given got lost from one session to the next.

**How I solved it.** I have a CLAUDE.md, which Claude reads with every message, divided into sections that are always the same: how to answer me (the style written out in full, not a pointer to a skill), where to operate (project folders, what not to touch, where the secrets are: only the path), "before saying I don't have it, read the inventory", where memory goes (facts in the vault, corrections in Claude's memory), handover with HANDOFF and SISTEMA, and a Rules section with the corrections I had to repeat, each with its date.

**Why this way.** CLAUDE.md is the only place that is always read. A skill opens only if it seems relevant, a memory file only if its title matches. When I repeat a rule for the second time I move it here: it's the way I found to keep it from getting lost. The fixed sections help me find it and correct it in place, instead of always adding at the bottom.

**When you need it.** If you use Claude Code every day on several projects and find yourself repeating the same instructions, or seeing Claude rebuild a tool you already have.

**When you DON'T need it.** If you open Claude Code now and then for a single task: five lines are enough. And watch the weight: mine reached about 270 lines (23 KB) and it loads with every message, using up context. When it grows that much, it's worth moving the details into separate files and leaving here only the rule with the path.

**How to get it.** Copy the package's `CLAUDE.md` to `~/.claude/CLAUDE.md` (it applies to all projects) or into the project folder. Replace the `<...>` placeholders and delete the sections you don't need. The template is in Italian: translate the headings if you prefer.

Step-by-step instructions: [package guide](../../pacchetti/memoria-claude-md-a-sezioni/LEGGIMI.md).
