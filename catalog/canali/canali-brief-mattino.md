---
slug: canali-brief-mattino
title: "The morning brief"
area: canali
where_it_runs: PC on
level: basic
cost: "€0 extra; a few minutes to adapt the paths"
package: "pacchetti/canali-brief-mattino/"
status: "PC version of mine"
---

# The morning brief

**The problem.** In the morning I spent half an hour rebuilding where I'd left off: tasks, mail, who was waiting, what had come out of calls. And I often noticed too late the person who'd been stuck for a week.

**How I solved it.** At 08:00, Monday to Friday, a script checks the tasks against their sources, estimates times, plans the calendar and collects the state. Then my main assistant writes a single WhatsApp message in four parts: the most important thing today; who's waiting, for how many days, with the draft reply already ready for the first two; the two or three delays that really do damage; the decisions that need me. At most five pending items, each with three possible answers: done, drop, postpone until when. At the third postponement it only offers done or drop. Every fact carries its source and date. The package has the PC skill, which reads the vault instead of the server.

**Why this way.** A fact on its own isn't news; a fact that crosses another one is (a close date with no preparation, a decision from a call that didn't become a task, a person with no reply). The brief does these crossings for me. "Done, drop, postpone" removes the "I'll think about it" option, which is how things stay stuck for weeks.

**When you need it.** If every morning you lose time figuring out where to start, or people waiting slip through the cracks.

**When you DON'T need it.** If your tasks and the people waiting for you fit in a ten-line list: you'll read it faster yourself. And if the vault doesn't have tasks written down somewhere, the brief has nothing to cross.

**How to get it.** Copy `brief-mattino/` into `~/.claude/skills/brief-mattino/` and adapt the vault paths. Run it with `/brief-mattino`; automatically at 8 with Task Scheduler (Windows) or cron (Mac), only while the PC is on. Step-by-step instructions: [package guide](../../pacchetti/canali-brief-mattino/LEGGIMI.md).
