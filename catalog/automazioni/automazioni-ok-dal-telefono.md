---
slug: automazioni-ok-dal-telefono
title: "The long job asks for my ok on the phone and restarts by itself"
area: automazioni
where_it_runs: PC on
level: advanced
cost: "€0: the ntfy app is free. Setup: 30 minutes."
package: "pacchetti/automazioni-ok-dal-telefono/"
status: "PC version of mine"
---

# The long job asks for my ok on the phone and restarts by itself

**The problem.** I often work from my phone. A long job would reach a point where it needed my ok, and there it sat until I got back to the computer, sometimes for hours.

**How I solved it.** When a job reaches a checkpoint, Claude updates the HANDOFF, sends the question to my phone with what happens on a yes and on a no, and stops. When I answer, a run every 2 minutes reads the reply and restarts Claude Code by itself, in the project folder, with the answer in the prompt (by default, from the phone, only yes or no from the buttons). One restart at a time, and only if the usage traffic light is green. On my side the question arrives on WhatsApp, and a service on the server collects the reply. For the PC I chose push notifications from the ntfy app, with Yes and No buttons: no account or server needed.

**Why this way.** The work shouldn't have to wait for me to get back to the computer, but the decisions stay mine. The HANDOFF written before stopping means whoever restarts doesn't need the old conversation. The question is marked "restarting" before the launch, so the same answer can't start the job twice.

**When you need it.** If you launch long multi-step jobs and then step away from the computer, and want to approve from your phone without reopening anything.

**When you DON'T need it.** If your version of Claude Code already lets you follow and control the session from your phone (remote control or the official app's notifications): that's simpler. Don't use it for questions with sensitive data: they go through a notification service, and on ntfy.sh anyone who knows the topic name can read them. The question code matches the reply to the question, it doesn't protect it.

**How to get it.** Copy `ponte_telefono.py` into `~/.claude/ponte/` and the `chiedi-ok.md` command into `~/.claude/commands/`, run `configura`, subscribe to the topic in the ntfy app and schedule `giro` every 2 minutes. Step-by-step instructions: [package guide](../../pacchetti/automazioni-ok-dal-telefono/LEGGIMI.md).
