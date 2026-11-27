---
slug: sicurezza-controlli-salute
title: "Health checks that alert only when the state changes"
area: sicurezza
where_it_runs: PC on
level: medium
cost: "€0. 20 minutes to write the checks."
package: "pacchetti/sicurezza-controlli-salute/"
status: "PC version of mine"
---

# Health checks that alert only when the state changes

**The problem.** When things run by themselves, the risk that worries me most is that they break silently: an automation that writes "all ok" without doing anything, a site that responds but stays blank because a file went missing, a backup stuck for days. And at the opposite end, a check that alerts me on every run ends up unread.

**How I solved it.** On the server I have automatic checks that look at the result, not at whether something started: public pages read the way a browser reads them (page plus scripts, css and fonts), server memory, night jobs that must have produced something, backups that must be recent. Each one saves its state and writes to me only when it changes: once when it breaks, once when it's back. If it stays broken, no reminder on every run. Before telling anyone "it works" I also do a manual, read-only check. For the PC I wrote a small version: a file with the list of checks (addresses, files that must be recent, commands that must succeed) and a system notification only on changes.

**Why this way.** An alert that arrives only when something changes is one I read. And looking at the outcome instead of the start is the only way I know to notice an automation that is confidently lying.

**When you need it.** When you have at least one thing that runs by itself and costs you if it stops: a backup, a site, a nightly script, an automation for a client.

**When you DON'T need it.** If nothing runs by itself, there's nothing to check. The PC version only checks while the PC is on: for a site that must stay up at night too you need an external monitoring service or a server. And if a service already has reliable alerts of its own, I don't duplicate them.

**How to get it.** Write your checks in `controlli.json`, test them with `--prova`, then schedule `controlli.py` every hour. Instructions: [package guide](../../pacchetti/sicurezza-controlli-salute/LEGGIMI.md).
