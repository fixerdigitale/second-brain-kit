---
slug: sicurezza-registro-modifiche
title: "A change log on systems where several people work"
area: sicurezza
where_it_runs: server
level: basic
cost: "€0. Two minutes per change."
package: "pacchetti/sicurezza-registro-modifiche/"
status: "I use it"
---

# A change log on systems where several people work

**The problem.** On clients' servers and systems several of us work, each with our own Claude. One person changed a configuration, the other didn't know and overwrote it, or lost an hour figuring out why something behaved differently.

**How I solved it.** On the system itself there's a REGISTRO-MODIFICHE.md file (change log) with the most recent entries at the top. After every change an entry is written: UTC date, who, what, why, how to roll back, what was verified. Never secrets: you write where something is, not what it contains. Before touching a service, Claude reads the latest entries. On top of that I leave a comment on the job's task.

**Why this way.** The log lives where everyone works, not on my PC: whoever comes in later sees right away what changed and how to undo it, even if they're not part of my team.

**When you need it.** When several people or several agents work on a server, a CRM or an automation system.

**When you DON'T need it.** If you're the only one touching the system, git commits or the project notes are enough for me. For a site on managed hosting with no file access, the log can live in a document shared with the client instead of on the server.

**How to get it.** Copy `REGISTRO-MODIFICHE.md` onto the system, in a folder everyone can see, and paste `regola-claude-md.md` into the project's `CLAUDE.md`. Instructions: [package guide](../../pacchetti/sicurezza-registro-modifiche/LEGGIMI.md).
