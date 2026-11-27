---
slug: memoria-handoff-e-sistema
title: "HANDOFF.md and SISTEMA.md for every long-running client"
area: memoria
where_it_runs: PC
level: basic
cost: "€0. 20-40 minutes for a client's first SISTEMA.md, then a few minutes per session."
package: "pacchetti/memoria-handoff-e-sistema/"
status: "I use it"
---

# HANDOFF.md and SISTEMA.md for every long-running client

**The problem.** On a client with months of work the HANDOFF had become a diary of hundreds of KB, always written at the bottom. The stable facts were buried in it, and sessions redid maps that already existed instead of reading them.

**How I solved it.** Every long-running client or project has two files. SISTEMA.md (the system sheet) holds the stable facts: who's who (with namesakes highlighted), how data flows, what we can see and what we can't, settled decisions, mistakes already made, tools to reuse. It's corrected in place, every line with its date. HANDOFF.md holds only open work: a fixed "Open risks" section and, under "## Lavori" (Jobs), the new sections at the top, with goal, state, files touched, decisions and next step. When I discover a stable fact I write a line "For SISTEMA.md: …". CLAUDE.md says: if a job gets interrupted, update the HANDOFF first; before mapping a system or attributing an account, read SISTEMA.md.

**Why this way.** They're two different timescales: stable facts get read first and must fit in a few pages; open work changes every day. Mixing them makes the former disappear. With the HANDOFF up to date, a new session or another assistant restarts from the next step without asking me for context.

**When you need it.** On clients or projects that last weeks, with several people and systems, and when you work in sessions that get interrupted (usage limit, full context).

**When you DON'T need it.** On jobs that close in one or two sessions: the file would be longer than the work. For a simple client, its note in the vault is enough.

**How to get it.** Copy `SISTEMA.md` and `HANDOFF.md` into the client's or project's folder and add to CLAUDE.md the two lines written in the package guide.

Step-by-step instructions: [package guide](../../pacchetti/memoria-handoff-e-sistema/LEGGIMI.md).
