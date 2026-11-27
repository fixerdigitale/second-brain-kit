---
slug: impara-regole-base-uniche
title: "One set of base rules for all agents, copied automatically"
area: impara
where_it_runs: PC
level: medium
cost: "€0. 15 minutes, plus the time to write your shared rules."
package: "pacchetti/impara-regole-base-uniche/"
status: "PC version of mine"
---

# One set of base rules for all agents, copied automatically

**The problem.** Each agent had its own instructions file, and the rules that applied to all of them (how to write, how to verify, what never goes out) were copied by hand into each one. Over time the copies drifted apart, and an agent sometimes changed its own.

**How I solved it.** The shared rules live in a single file. A script copies them, between two markers, into each agent's file; outside the markers it touches nothing. If someone changes the block in a copy, on the next run it goes back to matching the source. A rule is changed in one place only, and applies to everyone. On my side the source is a file the agents can't modify, it's copied every hour, and new rules only get in with my ok (card [rules proposed with my ok](impara-regole-proposte-con-ok.md)).

**Why this way.** A rule copied by hand into ten places is, for me, ten different rules after a month. A single source that regenerates itself takes away the work and the doubt about which version applies.

**When you need it.** If you have at least two or three different instruction files: Claude Code sub-agents, an AGENTS.md for Codex, the rules of another tool.

**When you DON'T need it.** If you only use Claude Code with a CLAUDE.md: it already reads that every session, and an extra script adds nothing. On a PC the only protection is "it goes back to how it was on the next run": to really prevent changes you need a separate user or a server.

**How to get it.** Copy the three files into a folder (for example `~/.claude/regole-base/`), write your rules in `REGOLE-BASE.md` and the files to update in `destinazioni.txt`, then run the script by hand, every hour, or with a SessionStart hook. Step-by-step instructions: [package guide](../../pacchetti/impara-regole-base-uniche/LEGGIMI.md).
