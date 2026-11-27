---
slug: sicurezza-aggiornamenti-mensili
title: "Updates never automatic: a check once a month, then I decide"
area: sicurezza
where_it_runs: PC on
level: basic
cost: "€0. 10 minutes to set up, then a few minutes a month to read the note."
package: "pacchetti/sicurezza-aggiornamenti-mensili/"
status: "PC version of mine"
---

# Updates never automatic: a check once a month, then I decide

**The problem.** Skills and tools taken from GitHub change upstream. An automatic update can bring in a new hook, a different install script or a setting I've never read, and the security check I did at install time no longer holds.

**How I solved it.** For third-party tools, no automatic updates. Once a month a check looks at what changed upstream and writes me a note: how many new commits, which sensitive files were touched (hooks, scripts, settings, files that run commands). It updates nothing. Then I decide: if sensitive parts changed I redo the security check, make a copy, and update one thing at a time. For the PC I wrote the same idea: it checks skills installed with git and global npm packages.

**Why this way.** This way every update goes through the same eyes as the installation. Once a month is enough not to fall too far behind, and rare enough to read the note carefully.

**When you need it.** If you've installed skills, MCPs or tools from third-party repositories, especially if they contain scripts or hooks.

**When you DON'T need it.** For Claude Code itself and for official plugins I keep normal updates. For urgent security fixes to a program you use every day, waiting a month may be too long: there I update right away, after reading what changes. If you have nothing taken from outside, you don't need it.

**How to get it.** Change the notes folder in `controlla_aggiornamenti.py` and schedule it for the first of the month. Instructions: [package guide](../../pacchetti/sicurezza-aggiornamenti-mensili/LEGGIMI.md). The security check to redo is in the [Check before installing](sicurezza-scan-prima-di-installare.md) card.
