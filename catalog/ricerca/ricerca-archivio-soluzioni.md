---
slug: ricerca-archivio-soluzioni
title: "Archive of solutions"
area: ricerca
where_it_runs: PC
level: basic
cost: "€0. 5 minutes to copy it; then about 10 minutes per entry, only when a problem cost you more than half an hour."
package: "pacchetti/ricerca-archivio-soluzioni/"
status: "I use it"
---

# Archive of solutions

**The problem.** The same failures kept coming back: an iframe that gets cut off, a webhook timing out, a login going round in circles. Each time the diagnosis was redone from scratch, and the same wrong paths were tried again, because nobody remembered what hadn't worked the time before.

**How I solved it.** A folder with one markdown entry for each solved problem (today I have about 180). Each entry has seven sections: symptom (in the words of whoever reported it), real cause, how to recognize it (the fastest test), solution, verification with numbers, dead ends, what it's reusable for. A `soluzioni` command does search, show, list, new and index. A skill tells Claude Code to search there before diagnosing and to write an entry after solving something that cost more than half an hour. The agents and Codex read and write the same folder.

**Why this way.** The part that saves me the most time is the dead ends: that's what you can't rebuild by reading the code. You search with the words of the symptom, not of the cause, because the cause is exactly what you don't know yet. One-minute fixes don't go in: they would dilute the archive, and then nobody reads it anymore.

**When you need it.** If you use Claude Code to fix sites, automations, servers or integrations, and you catch yourself thinking "I've seen this before". Also if you work with other people or other assistants who run into the same problems.

**When you DON'T need it.** If you use Claude Code mostly for writing or strategy and technical problems are rare: the folder stays empty. Also if every project is different and failures don't repeat. And if after a month you have 50 one-minute entries, the archive stops being useful.

**How to get it.** Copy `SKILL.md`, `modello-scheda.md` and `soluzioni.py` into `~/.claude/skills/soluzioni/`, create `<vault-folder>/soluzioni/` and set `VAULT_DIR` or `SOLUZIONI_DIR`. The script is optional: without it, Claude searches the folder with its own tools.

Step-by-step instructions: [package guide](../../pacchetti/ricerca-archivio-soluzioni/LEGGIMI.md).
