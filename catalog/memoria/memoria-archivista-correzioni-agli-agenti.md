---
slug: memoria-archivista-correzioni-agli-agenti
title: "The archivist brings corrections to the agents"
area: memoria
where_it_runs: server
level: advanced
cost: "€0 extra with the Claude subscription, but it needs a server with an agent platform (I use OpenClaw)."
package: "none: idea only"
status: "I use it"
---

# The archivist brings corrections to the agents

**The problem.** I have several AI agents (copy, graphics, code, research). A correction given to one of them, or to Claude Code, often applied to all of them, but it stayed where it had been said.

**How I solved it.** Every night, after the reviewer, an Archivist agent (Sonnet) reads the day's corrections: those given to the agents and Claude Code's correction memories, which a small bridge puts in its queue. It writes them into the instruction files of the right agents and keeps a history of what it took where. Rules that would apply to everyone it doesn't apply: it proposes them as cards, and they get in only if I approve.

**Why this way.** A correction must be written where the agent always reads it, that is, in its instruction files. Doing it by hand across ten agents doesn't hold up. Shared rules go through my ok because they change everyone's behavior, and because the archivist also reads messages from other people: I don't want a sentence written in a chat to become a rule by itself.

**When you need it.** Only if you have several AI agents, with separate instruction files, working for you autonomously.

**When you DON'T need it.** If you use Claude Code on its own, even with subagents in `.claude/agents/`: you put corrections in CLAUDE.md or in memory and they already apply to everyone. On a PC the equivalent is the "Nightly session reviewer" card in its end-of-day archivist version.

**How to get it.** Idea only: it needs a server with several always-on agents. On a PC: a repeated correction goes into CLAUDE.md, which subagents read too.
