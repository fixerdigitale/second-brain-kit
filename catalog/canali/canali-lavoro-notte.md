---
slug: canali-lavoro-notte
title: "Night work, to review in the morning"
area: canali
where_it_runs: PC on
level: medium
cost: "€0 extra: it uses the plan you already pay for that would otherwise be lost; a bit of electricity if you leave the PC on"
package: "pacchetti/canali-lavoro-notte/"
status: "PC version of mine"
---

# Night work, to review in the morning

**The problem.** The Claude subscription has a weekly limit: what I don't use before the reset is lost. Meanwhile I had a queue of jobs that could move forward without me, but only if I was there to launch them.

**How I solved it.** In the evening I write into a queue the preparatory jobs that can move forward on their own (tidy-ups, drafts, research). At night they run one after another, and before each one usage is checked: if the 5-hour window is at 90% it waits for the reset, if the week is at 85% the queue stops. During the day there's also a shift that turns itself on: every 15 minutes a check looks at whether I've been idle for at least 45 minutes and whether there's capacity that would be lost. And long daytime jobs go through a traffic light with thresholds that rise as the reset approaches: four days before the reset they stop at 50% of the week, on the last day at 90%. In the morning I find the deliveries with a yes/no each, and the tasks stay "to review" until I look at them. At night things get prepared, nothing gets sent to anyone. In the package: a PC script that reads `CODA.md` from the vault, runs the jobs in a row and writes `DA-RIVEDERE.md`.

**Difference from background jobs.** Those ([card](canali-lavori-in-background.md)) I launch myself, during the day, one at a time, and look at as soon as they finish. This is a queue prepared beforehand, which runs when I'm not there, stops by itself at the usage thresholds and closes nothing without my yes.

**Why this way.** Capacity already paid for, work that moves forward while I sleep, and me deciding in the morning instead of executing. "To review" exists because a job done autonomously isn't finished until I've looked at it. The thresholds are there so I don't wake up with the plan used up on exactly the day I need it.

**When you need it.** If at the end of the week you have plan left over and clear preparatory jobs you can describe in a brief.

**When you DON'T need it.** If you already use up the whole plan during the day, or if your jobs always need your decisions halfway. On a PC it only runs if the PC stays on and doesn't go to sleep. And the package script doesn't read plan usage: it only stops at a fixed time (7 am), so keeping the queue short is up to you.

**How to get it.** Copy `coda.py`, set `VAULT` to the vault path, write the jobs in `CODA.md` (a "## title" and the brief below it) and schedule it at night with Task Scheduler (Windows, with "Wake the computer to run this task") or cron (Mac). The shift that turns itself on when you're idle remains a server idea. Step-by-step instructions: [package guide](../../pacchetti/canali-lavoro-notte/LEGGIMI.md).
