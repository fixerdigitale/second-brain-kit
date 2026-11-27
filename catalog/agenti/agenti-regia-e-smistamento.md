---
slug: agenti-regia-e-smistamento
title: "Direction and routing: who does the work, and who checks it"
area: agenti
where_it_runs: PC
level: medium
cost: "€0. 10 minutes to adapt the table; each check adds a few minutes of Claude work per delegation."
package: "pacchetti/agenti-regia-e-smistamento/"
status: "PC version of mine"
---

# Direction and routing: who does the work, and who checks it

**The problem.** Having sub-agents wasn't enough. Claude forgot about them and did everything with the main model, or it delegated things it could have done faster itself. And when it did delegate, sometimes the agent answered "done" and it wasn't true: files not written, pages broken on the phone, requests lost between one round of fixes and the next.

**How I solved it.** Claude Code acts as director, with two rules written as skills. The first is a table by size: under 2 minutes, the session does it; mechanical work goes to the executor (Haiku); already-decided code to the builder (Sonnet); long work (more than about 15 minutes or many files) to a long-jobs agent on ChatGPT; architecture, security and final review stay with the main model. Claude says in one line who it's handing the work to. The second is how to delegate: a short brief (goal, files to touch and not to touch, constraints, state to read, "done when" criteria, delivery format), a fresh session for each round, and before writing to me Claude reads the files that were touched and ticks off the criteria. At most 2 rounds of fixes: at the third repeated defect it tells me instead of insisting. On my side the two rules are in the always-loaded instructions, and a hook reminds Claude of them when a message looks like a job.

**Why this way.** A rule written somewhere Claude always reads works; a rule said in chat is lost by the next session. The "handing it to X" line lets me correct course right away. For me the one who does and the one who checks are never the same agent, and criteria written beforehand avoid arguing afterwards about what "done" meant. A fresh session for each round keeps the agent's context clean.

**When you need it.** If you already have sub-agents (executor and builder card) and want them actually used, or if you've found errors after a "done".

**When you DON'T need it.** If you almost always work on short, conversational requests, or you rarely delegate and only things you can check by eye in a minute: the routing line and the brief cost more than the work.

**How to get it.** Copy the two skills (`smistamento` and `delega-con-controllo`) into `~/.claude/skills/` and add a line to your `CLAUDE.md` that points to them. They are the general version of mine, without our agents and paths. The reminder at the right moment is in the [routing hook](../automazioni/hook-smistatore-procedure.md) card. Step-by-step instructions: [package guide](../../pacchetti/agenti-regia-e-smistamento/LEGGIMI.md).
