---
slug: ricerca-qmd-sul-pc
title: "Search by meaning on the PC with QMD"
area: ricerca
where_it_runs: PC
level: medium
cost: "€0. About 15-30 minutes to install and do the first indexing, plus the space for the local models (I haven't measured it: it depends on the version)."
package: "pacchetti/ricerca-qmd-sul-pc/"
status: "new proposal, I don't use it this way"
---

# Search by meaning on the PC with QMD

**The problem.** If the vault lives on the PC and you use it with Claude Code, search only finds exact words. A note that talks about the same thing in other words stays invisible, and Claude concludes the information isn't there.

**How I solved it.** I'll say it up front: I haven't installed QMD, because on the server I already have search by meaning (card "Search by meaning across the whole memory"). On a PC without search it's the option I'd try first. QMD (github.com/tobi/qmd) is a local search engine over markdown folders: it combines keyword search (BM25), search by meaning (vectors) and a re-ranking of the results done by a small model, all on the PC. It has an MCP server, so Claude Code uses it like a tool. The package has the entry for `.mcp.json` and the lines for CLAUDE.md that tell Claude to search there before saying "it's not there".

**Why this way.** Among the options I looked at, it's the closest to what I use on the server, but without a server: the notes stay on the PC, the models run locally and there's nothing to pay. I prefer it to the alternatives because it indexes markdown folders as they are, without asking you to change the vault's format or structure. From what I've read it's maintained: in 2026 several versions came out (up to 2.5.3 at the end of May). I haven't tried it on Windows.

**When you need it.** When the vault has a few hundred notes or more, when you write free-form or dictated notes, when you often ask Claude "what had I decided about…".

**When you DON'T need it.** If the notes are few and well titled: word search is enough. If the PC is old or short on space: the first indexing downloads local models and keeps the processor busy for a while. If you already have search by meaning (like me on the server), it's a duplicate. If you want a memory Claude writes by itself, see the Basic Memory card. And remember that the index updates when you rerun it.

**How to get it.** Official source: https://github.com/tobi/qmd (npm package `@tobilu/qmd`; there are forks with the same name, install only from tobi/qmd). In the package: the steps in the package guide, the entry for `.mcp.json` and the lines for CLAUDE.md. The commands come from the November 2026 documentation: if they change, the README wins.

Step-by-step instructions: [package guide](../../pacchetti/ricerca-qmd-sul-pc/LEGGIMI.md).
