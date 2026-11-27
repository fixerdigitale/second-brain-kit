---
slug: canali-board-task
title: "Every job is a task: estimate, real time, who's on it now"
area: canali
where_it_runs: PC
level: basic
cost: "€0; ten minutes"
package: "pacchetti/canali-board-task/"
status: "PC version of mine"
---

# Every job is a task: estimate, real time, who's on it now

**The problem.** Jobs lived in chats, in messages and in my head. I didn't know what a type of job really cost me, who was doing it at that moment (me, the AI or a collaborator), and which "in progress" jobs had been stuck for days.

**How I solved it.** Every job that takes more than a few minutes is a task on a board, with the source it came from (a call, a message, a link). Each task has two separate times: the estimate, decided beforehand, and the real time, counted while working. In my system the real time is counted by Claude Code hooks: when a session works on a task the board shows it "live" on the avatar of whoever is working on it, adds up the minutes (long pauses don't count, two sessions on the same task don't double up) and flags in-progress tasks that aren't moving. Whoever plans with me sees everything without asking "where are you at?". When I talk about a task I always write its link. The package has the file version: `board.py` keeps estimate, real time, who's on it now and source, and writes a `TASK.md` view readable from the phone too.

**Why this way.** If real time is written by hand, you end up copying the estimate, and then it teaches nothing: that's why the system counts it and the estimate isn't touched. The difference between estimate and real time is what makes me improve later estimates and quotes. And "who's on it now" stops two people, or two agents, from doing the same thing.

**When you need it.** If you work with several clients or with a collaborator, if you bill by the hour or by project and want to know what a job really costs you, or if you let the AI work autonomously and want to see what it's doing.

**When you DON'T need it.** If you have few jobs at a time and keep them well in mind. If you already use a task manager (Trello, Asana, Linear) with time tracking, stick with that: two boards quickly contradict each other. The file version is for one person or a small group: no notifications, no simultaneous writing.

**How to get it.** Copy `board.py` into the vault, choose the board folder and paste `regola-per-CLAUDE.md` into your CLAUDE.md. To count time automatically, pair it with the `pacchetti/hook-tempo-per-task/` package; to break a big job into tasks, `pacchetti/skill-roadmap-lavoro/`. Step-by-step instructions: [package guide](../../pacchetti/canali-board-task/LEGGIMI.md).
