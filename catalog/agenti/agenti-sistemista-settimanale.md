---
slug: agenti-sistemista-settimanale
title: "Read-only weekly sysadmin"
area: agenti
where_it_runs: PC on
level: medium
cost: "€0 extra. About 5 minutes of run time per week. Optional and free: gh and gitleaks."
package: "pacchetti/agenti-sistemista-settimanale/"
status: "PC version of mine"
---

# Read-only weekly sysadmin

**The problem.** I thought I had backups. But a backup I've never tried to restore is just a hope, and a key that ended up in a commit by mistake stays invisible until it does damage.

**How I solved it.** On the server, the Sysadmin keeps everything running and checks the others' work with attached evidence. For the PC I wrote a sub-agent that once a week checks, without touching anything: vault saved to GitHub and in sync, private repo, Drive folder up to date, a restore test in a temporary folder, suspicious words (passwords, tokens, keys) in the commit history without ever showing their value, files that shouldn't be in the repo, very old programs. Each item comes back OK, PROBLEM or NOT VERIFIABLE.

**Why this way.** The one who checks doesn't fix: if it fixes, nobody checks it anymore. And keeping "not verifiable" separate from "ok" stops me from mistaking a skipped check for a passed one.

**When you need it.** If your vault is on GitHub or Drive and holds things you don't want to lose, or if you've ever pasted a key into it.

**When you DON'T need it.** If your vault is small and you copy it by hand every week to a disk you control. Honest note: read-only is guaranteed by the instructions, not by a technical block, because the sub-agent uses Bash; if you want a real block, remove Bash from its tools and you lose the git checks.

**How to get it.** Copy `sistemista.md` into `~/.claude/agents/` and replace the placeholders (vault, repo, Drive). Run it by hand once a week or with a scheduled task that runs `claude -p`. Step-by-step instructions: [package guide](../../pacchetti/agenti-sistemista-settimanale/LEGGIMI.md).
