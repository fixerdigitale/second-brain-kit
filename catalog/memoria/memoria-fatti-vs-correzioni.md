---
slug: memoria-fatti-vs-correzioni
title: "Facts in the vault, corrections in memory"
area: memoria
where_it_runs: PC
level: basic
cost: "€0. 10 minutes to copy the skill and the line in CLAUDE.md."
package: "pacchetti/memoria-fatti-vs-correzioni/"
status: "I use it"
---

# Facts in the vault, corrections in memory

**The problem.** I had two memories and things ended up at random: the outcome of a call in Claude Code's memory instead of the vault, duplicates in both places, and the other tools that read the vault didn't see the facts.

**How I solved it.** I split the jobs. Facts (clients, projects, decisions, people, agreements) go only into the vault, into the right note, at the end of the "## Dalle sessioni" (From the sessions) section, with Goal, Done and Open. Claude Code's memory keeps only corrections about how to work. When I say "save to memory" it means the vault, always, with no copy in the other one. I wrote this in CLAUDE.md and in a small skill that decides where to put the note.

**Why this way.** Something in only one place can't contradict itself. Everything reads the vault (Obsidian, the agents, search), Claude Code's memory doesn't get read that way. And a "save to memory" said in a hurry or out loud doesn't force me to specify where every time.

**When you need it.** If you already have a notes vault and also use Claude Code's automatic memory: it's the typical case where the two overlap.

**When you DON'T need it.** If you don't have a vault and Claude Code's memory is enough for you: this split isn't needed.

**How to get it.** Copy the `salva-in-memoria/` folder into `~/.claude/skills/salva-in-memoria/` and replace `<cartella-vault>` in SKILL.md. The optional line for CLAUDE.md is in the package guide.

Step-by-step instructions: [package guide](../../pacchetti/memoria-fatti-vs-correzioni/LEGGIMI.md).
