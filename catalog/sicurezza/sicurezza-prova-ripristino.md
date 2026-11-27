---
slug: sicurezza-prova-ripristino
title: "Restore test: actually reopening the backup"
area: sicurezza
where_it_runs: PC
level: basic
cost: "€0. About 15 minutes a month."
package: "pacchetti/sicurezza-prova-ripristino/"
status: "I use it"
---

# Restore test: actually reopening the backup

**The problem.** A backup that says "succeeded" says it started, not what it contains. A folder or a database excluded by mistake only shows up when you reopen the copy, and you usually find out at the worst moment.

**How I solved it.** I do the test in a separate folder, never on top of the original: I download the copy again from the cloud as if the computer were lost, decrypt it, extract it and check specific things. The files are there, the main memory file is identical, the important folders are all there, the configuration opens. I turned the steps into a checklist to fill in, which I repeat once a month and after every change to the backup script.

**Why this way.** For me it's the only way to know the backup works. You do the real restore under stress, so it's worth having done it once calmly, including the question "can I find the password even without this PC?".

**When you need it.** Once right after setting up the backup, then every month or after every change to the script.

**When you DON'T need it.** If your only backup is GitHub and you often clone the repo on another PC, you're effectively testing it already: just check now and then that the clone is complete.

**How to get it.** Copy the checklist into the vault and fill in a dated copy at every test; the first time you can have Claude Code walk you through it. Instructions: [package guide](../../pacchetti/sicurezza-prova-ripristino/LEGGIMI.md).
