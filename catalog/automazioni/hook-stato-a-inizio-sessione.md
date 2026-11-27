---
slug: hook-stato-a-inizio-sessione
title: "Real state in the context at session start"
area: automazioni
where_it_runs: PC
level: basic
cost: "€0. 10 minutes."
package: "pacchetti/hook-stato-a-inizio-sessione/"
status: "PC version of mine"
---

# Real state in the context at session start

**The problem.** Memory is a snapshot of the past. One day an old note said one of my agents ran on a certain model, while it had been using another one for days, and Claude advised me on a wrong basis.

**How I solved it.** I added a SessionStart hook that, at every session, reads the agents' configuration live and puts each one's model and fallback into the context, with the sentence "this counts more than memory". For the PC I wrote the general version: today's date and time plus the first lines of the state files you choose (ongoing projects, what's active), with their modification date.

**Why this way.** The real state has to arrive by itself, like memory does, otherwise memory wins. And today's date avoids mistakes about "yesterday" and "next Friday".

**When you need it.** If you have a file that says what the situation is right now and you really keep it updated, or if Claude often gets dates wrong.

**When you DON'T need it.** If you don't have an up-to-date state file: putting in an old one makes things worse. Everything you list enters every session and takes up context: keep it short.

**How to get it.** Copy `stato_inizio.py` and `stato_file.txt` into `~/.claude/hooks/`, write your paths in the `.txt` and the block from `settings-esempio.json` into `~/.claude/settings.json`. Step-by-step instructions: [package guide](../../pacchetti/hook-stato-a-inizio-sessione/LEGGIMI.md).
