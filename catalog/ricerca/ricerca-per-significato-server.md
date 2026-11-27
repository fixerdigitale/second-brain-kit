---
slug: ricerca-per-significato-server
title: "Search by meaning across the whole memory"
area: ricerca
where_it_runs: server
level: advanced
cost: "€0 extra if you already have a server: Ollama and nomic-embed-text are free and the model weighs 274 MB. Without a server, a VPS starts at a few euros a month, plus a few hours to install and connect everything."
package: "none: idea only"
status: "I use it"
---

# Search by meaning across the whole memory

**The problem.** The vault grew past 2,000 notes, more than 100 call transcripts. Searching by exact words I couldn't find things: I had written "price" and was searching for "quote", or a decision was told in words different from the ones I remembered. The agents answered "I have no information" about things written weeks before.

**How I solved it.** On the server the agents (I use OpenClaw) have a memory search tool that indexes the vault and the calls folder. Each piece of a note becomes a vector computed locally by Ollama with the nomic-embed-text model, so search finds notes that talk about the same thing even in different words. Claude Code reaches it through the same tool, with an MCP connection to the agents. Everything runs on the server: no note goes out to external services to be indexed.

**Why this way.** The value of a vault, for me, is in finding more than in writing. I chose a local embedding model because the notes contain clients, money and calls: I didn't want to send them to an external service just to index them, and this way the cost is zero. It lives on the server because there the agents answer at night and from the phone too.

**When you need it.** When the vault goes past a few hundred notes, when you write freely (dictation, call notes) and when several people or agents write with different words. Also if you want an always-on assistant to answer from your notes while the PC is off.

**When you DON'T need it.** If the vault is small or you keep it tidy with clear titles: Claude Code's word search is enough and you have nothing to maintain. If you only work from the PC, this server version is overkill: see the "Search by meaning on the PC with QMD" card. And if you don't already have a server with agents, it isn't worth setting one up just for this.

**How to get it.** Idea only: it needs a server with an agent system that has memory search, set up to use a local embedding model (Ollama) and the extra folders to index. For the PC the ready option is in the "Search by meaning on the PC with QMD" card.
