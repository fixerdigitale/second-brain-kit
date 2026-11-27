---
slug: memoria-raccolta-sessioni
title: "Collecting the requests made in other sessions"
area: memoria
where_it_runs: PC on
level: medium
cost: "€0. The script runs in a few seconds."
package: "pacchetti/memoria-raccolta-sessioni/"
status: "PC version of mine"
---

# Collecting the requests made in other sessions

**The problem.** I work with many sessions in parallel, from the phone too. I'd say "as I asked you yesterday" and the new session knew nothing about it.

**How I solved it.** On my side an AI-free service, three times a day (7:40, 13:05, 19:05), collects into a single file my requests from the latest Claude Code sessions, plus recorded calls, tasks and calendar, and puts it where both Claude and the agents read it. It takes only my messages, not the replies. CLAUDE.md says: if I talk about a job you don't see here, read that file. The package has the part that works on a PC: a Python script that reads Claude Code sessions in `~/.claude/projects` and writes a markdown with only your messages, by project and by session, masking anything that looks like a key.

**Why this way.** Collecting needs no intelligence, so no model: it costs nothing and doesn't make mistakes. A compact file reads in a moment; digging through session files each time costs context. Only my messages, because they're the ones that say what I want, and they keep the file short and less sensitive.

**When you need it.** If you open many sessions on the same projects in the same day, or work from several places.

**When you DON'T need it.** If you use one session per project and carry it on until it's finished: the context is already there. On a PC it runs only while the PC is on, and it doesn't see sessions from other devices. If your vault goes to GitHub or Drive, the file contains your requests: exclude it if there's client material in it.

**How to get it.** Copy `raccogli_sessioni.py` outside the vault and run it with `python3 raccogli_sessioni.py --ore 24 --out <vault-folder>/Fonti/raccolta/ultima.md`. Optional: schedule it three times a day (Task Scheduler on Windows, crontab on Mac) and add the line for CLAUDE.md from the package guide.

Step-by-step instructions: [package guide](../../pacchetti/memoria-raccolta-sessioni/LEGGIMI.md).
