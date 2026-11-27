---
slug: sicurezza-copie-datate
title: "A dated copy before touching an important file"
area: sicurezza
where_it_runs: PC
level: basic
cost: "€0. 5 minutes."
package: "pacchetti/sicurezza-copie-datate/"
status: "I use it"
---

# A dated copy before touching an important file

**The problem.** A change to a configuration file went wrong and I didn't have the previous version. Undated .bak copies overwrote each other and I no longer knew which one was the good one.

**How I solved it.** Before modifying an important file that isn't under git, Claude makes a copy next to it with date and reason, for example `settings.json.bak-20261127-permessi`. It never overwrites an existing copy, it adds a new one. Then it writes me the name of the copy, so I know where to go back to. In the folder of my agents' main configuration there are about a hundred: you can read the history of every change.

**Why this way.** Going back becomes a copy command, without having to remember what was there. The date and the note say right away which copy is the right one.

**When you need it.** For files outside git: Claude Code configurations, automation files, server configurations, exported documents.

**When you DON'T need it.** Inside a folder already under git, a commit before the change is enough: there .bak copies just make a mess. If copies pile up, every so often I delete the ones that are months old.

**How to get it.** Paste `regola-claude-md.md` into your `CLAUDE.md`; the `copia_datata.py` script is optional, it's for making the copy with an always-identical command. Instructions: [package guide](../../pacchetti/sicurezza-copie-datate/LEGGIMI.md).
