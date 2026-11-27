---
slug: skill-roadmap-lavoro
title: "Roadmap: who, when, where we stand"
area: skill
where_it_runs: PC
level: medium
cost: "€0 extra; an average roadmap costs 5-10 minutes of session"
package: "pacchetti/skill-roadmap-lavoro/"
status: "I use it"
---

# Roadmap: who, when, where we stand

**The problem.** After "we know what to do", the how and the when were always missing. Estimates were "a bit of work", the points where I was needed stayed hidden in the middle, and "where are we?" had vague answers.

**How I solved it.** A skill that breaks down a job starting from outcomes, not activities, on at most three levels. Each task has who does it, an estimate in minutes, what it depends on, whether my ok is needed, the proof of "done" and who checks it (never whoever did it). Without proof the task isn't closed. The status report fits on one page and its first line says: on time, at risk or late.

**Why this way.** I took the ideas I needed from four project management tools (planning-with-files, claude-task-master, Marcus, agent-almanac) without installing any of them: I needed the rules, not another program. If there's a pipeline, it wins; the roadmap only adds times and checks.

**When you need it.** Jobs lasting several days, with several people or agents, or with real deadlines.

**When you DON'T need it.** For a one-hour job it's bureaucracy. If you already use a project manager with its own rules, you risk two systems contradicting each other.

**How to get it.** Copy `roadmap-lavoro/` into `~/.claude/skills/`. Without a task manager the roadmap lives in `<your-project>/ROADMAP.md`; with the board from `pacchetti/canali-board-task/` the tasks end up there. Step-by-step instructions: [package guide](../../pacchetti/skill-roadmap-lavoro/LEGGIMI.md).
