---
slug: hook-suono-fine-lavoro
title: "A sound when Claude is done or waiting for me"
area: automazioni
where_it_runs: PC
level: basic
cost: "€0. 5 minutes."
package: "pacchetti/hook-suono-fine-lavoro/"
status: "PC version of mine"
---

# A sound when Claude is done or waiting for me

**The problem.** I'd launch a job, move on to something else, and find out half an hour later that Claude had been waiting for my yes since the first minute.

**How I solved it.** I don't have a sound on the PC: I have a small physical display on my desk that beeps and plays an animation at the end of each turn, driven by a desktop-app mod. This card is the PC version anyone can have: a Stop hook plays a sound when Claude is done, and a Notification hook plays a sound (and on a Mac shows a notification) when it's waiting for a permission or an answer.

**Why this way.** The time lost isn't Claude's, it's mine when I don't notice it's finished. A different signal for "done" and "waiting for you" is enough for me not to check the window every two minutes.

**When you need it.** If you launch jobs that take more than a few minutes and do something else in the meantime.

**When you DON'T need it.** If you always stay in front of the Claude window, or work in places where sounds are a nuisance. Sometimes your editor's notifications are already enough.

**How to get it.** Copy `fine_lavoro.py` into `~/.claude/hooks/` and the two blocks from `settings-esempio.json` into `~/.claude/settings.json`. Step-by-step instructions: [package guide](../../pacchetti/hook-suono-fine-lavoro/LEGGIMI.md).
