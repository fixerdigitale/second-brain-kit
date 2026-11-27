---
slug: sicurezza-scan-prima-di-installare
title: "A security check before installing skills and MCPs from outside"
area: sicurezza
where_it_runs: PC
level: medium
cost: "€0. You need Docker (free); about 20 minutes the first time, then a minute per check."
package: "none: idea only"
status: "I use it"
---

# A security check before installing skills and MCPs from outside

**The problem.** The skills and MCP servers I find on GitHub are instructions and code that Claude runs with my permissions. A skill can tell Claude to send files somewhere, a script can do things the README doesn't mention. Reading them all by hand isn't realistic for me.

**How I solved it.** Before installing any skill, MCP, plugin or agent repo taken from outside, even when I've already decided to take it, I run it through NVIDIA's SkillSpector (open source, Apache-2.0) in static analysis only: the code is not executed. It gives a score from 0 to 100. From 21 to 49 I read the findings before installing; from 50 up I read every finding and don't install if one of them is real. I run it in a Docker container with no secrets mounted, read-only and without privileges.

**Why this way.** It costs me a minute and catches things I don't see by eye: hidden commands, instructions telling Claude to ignore the rules, dependencies with known vulnerabilities. A low score doesn't mean "safe": it means the tool didn't find anything, and I treat it that way.

**When you need it.** When you install a skill or an MCP from an author you don't know, or a repo with scripts.

**When you DON'T need it.** For skills you write yourself or for Anthropic's official plugins I don't need it. If you install something only now and then, an alternative without Docker is to open the files and ask Claude to read them looking for network commands, key access and odd instructions: it's less thorough, but it's something.

**How to get it.** Third-party tool, not copied here: [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector), with the instructions in the README. I run it in Docker with no secrets mounted and with the `--no-llm` option for static-only analysis. To recheck updates of things already installed: the [Updates never automatic](sicurezza-aggiornamenti-mensili.md) card.
