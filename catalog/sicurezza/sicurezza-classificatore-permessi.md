---
slug: sicurezza-classificatore-permessi
title: "When Claude gets blocked, it stops and asks"
area: sicurezza
where_it_runs: PC
level: basic
cost: "€0. 2 minutes."
package: "pacchetti/sicurezza-classificatore-permessi/"
status: "I use it"
---

# When Claude gets blocked, it stops and asks

**The problem.** In auto mode Claude Code has a check that sometimes denies a risky action, for example a production release, a permanent timer or a write to another server, even when I've already said yes in chat. The temptation, for Claude, is to find another route to do the same thing.

**How I solved it.** I have a fixed rule. If an action is denied, Claude stops and tells me what it wanted to do and why. If I give a written ok naming the precise action, not a generic "yes", it retries the identical command once. If it's denied again, it proposes a permission rule or gives me the command to run myself. No workarounds: another tool, a split command, a renamed file. On top of that it keeps actions that change something in a separate command from reads, so if it's denied it's clear why.

**Why this way.** The block is a second pair of eyes, and getting around it means switching it off. I've seen that an ok naming the exact action usually passes, while a generic ok to a list of suggestions doesn't.

**When you need it.** If you use auto mode or let Claude work alone for a long time on things that touch production or clients.

**When you DON'T need it.** If you always work with manual permission prompts, you approve every step yourself and the rule adds little.

**How to get it.** Paste `regola-claude-md.md` into `~/.claude/CLAUDE.md`. Instructions: [package guide](../../pacchetti/sicurezza-classificatore-permessi/LEGGIMI.md).
