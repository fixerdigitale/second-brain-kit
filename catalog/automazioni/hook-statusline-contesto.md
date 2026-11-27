---
slug: hook-statusline-contesto
title: "Status line with model, context and limits"
area: automazioni
where_it_runs: PC
level: basic
cost: "€0. 5 minutes."
package: "pacchetti/hook-statusline-contesto/"
status: "new proposal, I don't use it this way"
---

# Status line with model, context and limits

**The problem.** I never knew at a glance which model I was working on, how full the session was, and how much of the 5-hour window and the week I had already used. I found out when the limit hit.

**How I solved it.** I have an always-visible counter above the prompt, but it's a desktop-app mod. For the kit I wrote a version with Claude Code's standard status line (statusLine): a Python script that prints "Opus · context 84k/200k 42% · 5 hours 31% · week 12% · folder", reading the data Claude Code itself passes to it. I don't use this version myself: you're the first to try it.

**Why this way.** For me a number always in front of my eyes changes habits more than a rule: I see when it's worth opening a new session or delegating, without asking Claude anything and without spending tokens.

**When you need it.** If you use Claude Code from the terminal (including VS Code's integrated one) with a Pro or Max subscription and want to keep an eye on context and limits.

**When you DON'T need it.** If you only use the VS Code extension's graphical panel: the status line may not appear there, and there's already a context indicator. The 5-hour and weekly limits only show up if your version passes them (I verified it on 2.1.330).

**How to get it.** Copy `statusline.py` into `~/.claude/` and the `statusLine` key from `settings-esempio.json` into `~/.claude/settings.json`. If you also want the usage traffic light, see the [usage traffic light](automazioni-semaforo-consumi.md) card: the two scripts can be chained. Step-by-step instructions: [package guide](../../pacchetti/hook-statusline-contesto/LEGGIMI.md).
