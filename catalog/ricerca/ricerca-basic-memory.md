---
slug: ricerca-basic-memory
title: "Alternative: Basic Memory, a memory Claude writes and rereads"
area: ricerca
where_it_runs: PC
level: medium
cost: "€0 in the local version (open source, AGPL v3). About 20 minutes to install and connect it."
package: "none: idea only"
status: "new proposal, I don't use it this way"
---

# Alternative: Basic Memory, a memory Claude writes and rereads

**The problem.** QMD searches the notes you write. If instead you want Claude, during conversations, to write and link notes and find them again later, you need a tool designed for that.

**How I solved it.** Basic Memory (github.com/basicmachines-co/basic-memory) is a local MCP server: it keeps knowledge in normal markdown files (they also open in Obsidian, with double-bracket links) and uses a SQLite database for the index and search. Claude reads, writes and links notes through its tools. I don't use it: I evaluated it as an alternative for the PC.

**Why this way.** I listed it as a second choice for two reasons. First, it wants to organize the notes itself (entities, relations, its own structure), while an established vault, in my view, works better with a tool that searches on top of what's there. Second, it's still moving: version 1.0 at the end of October 2026 removed some MCP tools and changed commands and configuration.

**When you need it.** If you're starting from zero or nearly, and want Claude to build the memory while you work, with notes linked to each other.

**When you DON'T need it.** If you already have a vault structured your own way and just want to find things better: QMD is lighter and doesn't touch the notes. If you don't want an assistant writing in the vault without you rereading. If the AGPL v3 license is a problem for use inside a product you sell, read it first.

**How to get it.** Official source: https://github.com/basicmachines-co/basic-memory (documentation and changelog at https://docs.basicmemory.com). It installs with uv (`uv tool install basic-memory`) or Homebrew and connects to Claude Code as an MCP server. Before installing it, read the changelog of the current version.
