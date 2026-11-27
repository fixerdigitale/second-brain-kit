---
slug: skill-cerca-strumento
title: "Evaluating a tool before installing it"
area: skill
where_it_runs: PC
level: medium
cost: "€0; 5-15 minutes of session per evaluation"
package: "pacchetti/skill-cerca-strumento/"
status: "I use it"
---

# Evaluating a tool before installing it

**The problem.** People kept sending me links to "super useful" skills, MCPs and repos. Installing them on the spot means running strangers' code next to my keys and client data. And sometimes I did the same evaluation twice.

**How I solved it.** A skill that first looks at what I already have, then searches the right registries (the official MCP registry, PulseMCP, Glama, Smithery, GitHub). It compares at most three candidates: whether it's alive, who maintains it, what it touches, license, code actually read and not just the README. It ends with a three-line verdict: INSTALL, TRY ISOLATED or LEAVE IT. Every verdict, the noes too, goes into `valutati.md`.

**Why this way.** In 2026 there were campaigns of malicious skills in open registries, with names almost identical to the real ones. A static scanner (I use NVIDIA's SkillSpector) helps, but it gives many false positives: without reading the code by hand I don't decide. Separating searching from installing saves me from impulse installs.

**When you need it.** If you often install skills, plugins or MCPs taken from outside.

**When you DON'T need it.** If you only use Anthropic's official skills or those of a provider you know, it's too much.

**How to get it.** Copy `cerca-strumento/` (with `valutati.md`) into `~/.claude/skills/`. Optional scanner, needs Docker: https://github.com/NVIDIA/SkillSpector. Step-by-step instructions: [package guide](../../pacchetti/skill-cerca-strumento/LEGGIMI.md).
