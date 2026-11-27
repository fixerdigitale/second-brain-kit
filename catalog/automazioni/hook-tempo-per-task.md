---
slug: hook-tempo-per-task
title: "Time per task, counted by hooks"
area: automazioni
where_it_runs: PC
level: medium
cost: "€0. 10 minutes for the PC version."
package: "pacchetti/hook-tempo-per-task/"
status: "PC version of mine"
---

# Time per task, counted by hooks

**The problem.** Whoever coordinates the work with me needed to see which task I was working on and which one the AI was, and how long they took. Manual timers I never started.

**How I solved it.** I tied each Claude Code session to a task on the board: the UserPromptSubmit, PostToolUse and Stop hooks mark who's active and add up the minutes on the task (pauses over 15 minutes don't count, two sessions on the same task don't double up), and the board shows which tasks are "live" right now. That version writes to a database on a server. For the PC I wrote the minimal version: write "#task name" in the message (or assign a task to a folder), the same three hooks write time, folder and task to a file, and a command produces the summary by day and task.

**Why this way.** Time only gets counted if it counts itself. Using the task as the key, not the folder, tells me what each job really costs, even when several jobs live in the same folder.

**When you need it.** If you bill by the hour, estimate jobs and want to compare the estimate with the real time, or someone needs to see what you're working on.

**When you DON'T need it.** If you don't need to know the time. It only counts time with Claude active: calls and work outside Claude aren't there, so it isn't a complete timesheet. The version with a "live" board for a collaborator needs an always-on server and a database.

**How to get it.** Copy `registro_tempo.py` into `~/.claude/hooks/` and the three blocks from `settings-esempio.json` into `~/.claude/settings.json`. Summary: `python3 ~/.claude/hooks/registro_tempo.py riepilogo 30`. Step-by-step instructions: [package guide](../../pacchetti/hook-tempo-per-task/LEGGIMI.md).
