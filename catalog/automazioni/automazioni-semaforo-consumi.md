---
slug: automazioni-semaforo-consumi
title: "Usage traffic light: long jobs stop by themselves"
area: automazioni
where_it_runs: PC on
level: medium
cost: "€0 extra: it uses subscription quota that would otherwise be lost. Setup: 20 minutes."
package: "pacchetti/automazioni-semaforo-consumi/"
status: "PC version of mine"
---

# Usage traffic light: long jobs stop by themselves

**The problem.** With a subscription there are two opposite risks. A long job or a night queue can burn the quota right before the day I need it. And the week's quota I don't use before the reset is lost.

**How I solved it.** I have a traffic light: it reads how much of the 5-hour window and of the week I've used, and says green, stop or "I don't know". The thresholds rise as the reset gets closer: four days before the reset long jobs stop at 50% of the week, on the last day at 90%. Every long job, every night queue and every restart asks the traffic light before starting. On top of that there's a free shift: every 15 minutes it checks whether I've been idle for 45 minutes and whether there's quota left in the week that would be lost; if so, it does one job from the queue and leaves it for review. On my side the usage reading comes from a service on the server every 5 minutes. On the PC it comes from Claude Code's status line, which receives the subscription limits, and from the jobs themselves.

**Why this way.** I don't want to have to watch usage: it has to stop by itself. Thresholds rising toward the reset protect the days I work, and let me spend what's left when it would be lost anyway. One job per run means the traffic light is asked again before each one.

**When you need it.** If you have a Pro or Max subscription, run long jobs or queues without watching them, and have hit the limit at the wrong moment or seen leftover quota at the end of the week.

**When you DON'T need it.** If you only use Claude when you're at the PC and never hit the limits. On a PC, without a recently opened session, the reading gets stale and the traffic light says "I don't know": the free shift then does at most one job a day. It only works while the PC is on and awake.

**How to get it.** Copy the three scripts into `~/.claude/semaforo/`, set `registra_limiti.py` as the status line and schedule `turno_libero.py` every 15 minutes. It goes well with the queue in the [night work](../canali/canali-lavoro-notte.md) card. Step-by-step instructions: [package guide](../../pacchetti/automazioni-semaforo-consumi/LEGGIMI.md).
