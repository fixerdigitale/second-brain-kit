---
slug: ricerca-inventario-notturno
title: "Inventory of what's really there"
area: ricerca
where_it_runs: PC
level: basic
cost: "€0. 10 minutes to copy it and set up the hook. Regenerating it takes less than a second."
package: "pacchetti/ricerca-inventario-notturno/"
status: "PC version of mine"
---

# Inventory of what's really there

**The problem.** Claude Code starts every session without knowing what I have installed. It concluded "I don't have it" about tools that were there (a Google client, a subdomain, some modules), and sometimes started rebuilding one from scratch.

**How I solved it.** On my side a script regenerates an INVENTARIO.md file every night: connected accounts, subdomains, containers, agents, MCP servers, skills, programs, services and only the names of the keys, never the values. CLAUDE.md says to read it before saying something isn't there or building a tool. If a section can't be read, a warning line takes its place and the others stay. For the PC I wrote a minimal version: skills, agents, commands, hooks, MCP servers, useful programs and key names in the .env files you point it to.

**Why this way.** Writing the map once a day costs less than letting the assistant rebuild it by trial and error every session, or remake something that exists. Only the key names, because the file is read by a model and could end up in a log. On a PC the nightly update works badly (it's off at night), so the script regenerates at session start if it's more than 20 hours old.

**When you need it.** When you've piled up skills, MCP servers and tools and no longer remember what's there. Also when several people or assistants work on the same PC or project.

**When you DON'T need it.** If you have a few skills and two MCP servers: you know them by heart and Claude sees them by itself (`/mcp`, the skill list), the inventory would be one more file to maintain. It's also not needed on a single project with no external tools.

**How to get it.** Copy `genera_inventario.py` into `~/.claude/strumenti/` and run it with `--progetto <your-project>` (and `--env <file.env>` if you want the key names). To keep it updated, the SessionStart hook from the package guide with `--se-vecchio 20`. In CLAUDE.md: "Before saying a tool isn't there, read INVENTARIO.md".

Step-by-step instructions: [package guide](../../pacchetti/ricerca-inventario-notturno/LEGGIMI.md).
