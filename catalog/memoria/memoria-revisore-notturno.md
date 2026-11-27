---
slug: memoria-revisore-notturno
title: "Nightly session reviewer"
area: memoria
where_it_runs: PC
level: medium
cost: "€0 extra with the Claude subscription (one run on Sonnet). 3-5 minutes a day to approve."
package: "pacchetti/memoria-revisore-notturno/"
status: "PC version of mine"
---

# Nightly session reviewer

**The problem.** Decisions made during the day, in different sessions, didn't end up in memory unless I asked explicitly. The vault got stale, with outdated notes and duplicates. And repeated corrections never moved up in importance.

**How I solved it.** On my side a reviewer runs every night at 4:00 on a server. It reads all the sessions of the last hours (Claude Code, Codex, agents, calls, work chats); a single Sonnet call decides item by item what to save, where, and what to discard with the reason; then it writes into the vault (Goal, Request, Done, Open) and into memory. If a correction came back at least twice, it proposes making it a Golden Rule with a card I approve. The principle: information isn't cut, it's organized. For the PC I made a version called "end-of-day archivist": you write "fine giornata" (end of day), a sub-agent reads today's requests and the notes that changed, and proposes up to 15 items (fact to save, correction, outdated note, duplicate, Golden Rule candidate), each with its source. It writes nothing: a skill shows them to you one at a time and applies only the yeses.

**Why this way.** Asking "save" at every decision doesn't work: I forget. A single run sees everything together and finds the duplicates. Counting repetitions makes what becomes a Golden Rule objective. On the server I let it write by itself because I read the reports; on the PC I preferred it to ask for the ok, because at night the PC is usually off and an error saved to memory stays for weeks.

**When you need it.** If you work many hours a day with Claude, make decisions in different sessions and use the vault every day.

**When you DON'T need it.** If you use Claude for short, unrelated tasks, or if saying "save to memory" when needed is enough. If you write in the vault a few times a week, 15 proposals a day become noise: below 5-10 changed notes a week, rereading them yourself is enough.

**How to get it.** Copy `.claude/agents/archivista.md` into `~/.claude/agents/` and `.claude/skills/fine-giornata/` into `~/.claude/skills/fine-giornata/`, replace the placeholders, then write "fine giornata" in Claude Code. It works best together with the `pacchetti/memoria-raccolta-sessioni/` package.

Step-by-step instructions: [package guide](../../pacchetti/memoria-revisore-notturno/LEGGIMI.md).
