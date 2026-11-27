---
slug: agenti-esecutore-costruttore
title: "Two cheap sub-agents: executor and builder"
area: agenti
where_it_runs: PC
level: basic
cost: "€0 extra: the models are already included in the Claude subscription. Setup: 2 minutes."
package: "pacchetti/agenti-esecutore-costruttore/"
status: "I use it"
---

# Two cheap sub-agents: executor and builder

**The problem.** I was using the most expensive model even for mechanical work: finding a file, reading a log, counting lines, applying a fix I had already decided on. My quota went on things that needed no reasoning.

**How I solved it.** I created two Claude Code sub-agents. The executor runs on Haiku and only does mechanical work, without interpreting: if a choice is needed, it stops and asks. The builder runs on Sonnet and writes code that has already been decided, follows the style it finds, and stops if the decision doesn't hold up. The main session decides and reviews.

**Why this way.** For me, expensive reasoning is for deciding and checking, not for executing. Splitting the roles makes the quota last longer. And an agent that stops in front of a choice keeps a small model from deciding in my place.

**When you need it.** If you often search files, summarize logs, rename things or do rounds of small fixes, and you sometimes hit your plan's usage limit.

**When you DON'T need it.** If your plan never gets you to the limit, or you do almost only reasoning work (strategy, writing): you won't notice the difference in usage and you just add a step.

**How to get it.** Copy the two `.md` files into `~/.claude/agents/` (or into the project's `.claude/agents/` folder) and check with `/agents` that they show up. Step-by-step instructions: [package guide](../../pacchetti/agenti-esecutore-costruttore/LEGGIMI.md).
