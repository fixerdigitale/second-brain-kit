---
slug: skill-grilling
title: "Grilling: the interview before hard choices"
area: skill
where_it_runs: PC
level: basic
cost: "€0; an interview takes 10-30 minutes"
package: "none: third-party skill from the source"
status: "I use it"
---

# Grilling: the interview before hard choices

**The problem.** On big choices (an architecture, a contract, a new system) I started with half the decisions not made. I discovered them with the work underway, when redoing cost a lot.

**How I solved it.** I use grilling: Claude interviews me in rounds. Each round is a numbered list of the decisions that can be made now, each with its recommended answer. I answer, and the next round goes down into the decisions that depend on them. I don't keep it on: Claude proposes it before choices that are hard to undo, or I ask for it.

**Why this way.** The recommended answer next to each question lets me answer quickly ("yes, yes, not number 3"). The rounds follow the decision tree, so it doesn't ask me things that depend on answers not yet given.

**When you need it.** Before new projects, systems to build, choices about money or clients.

**When you DON'T need it.** For small or already decided jobs it's a pointless interrogation. Keeping it on by default gets tiring fast.

**How to get it.** Third-party skill, from the source: https://github.com/mattpocock/skills (grilling; grill-me calls it). It installs in `~/.claude/skills/`.
