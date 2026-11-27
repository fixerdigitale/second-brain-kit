---
slug: sicurezza-versioni-locali
title: "Local versions of pages and documents, without GitHub"
area: sicurezza
where_it_runs: PC on
level: medium
cost: "€0. 15 minutes."
package: "pacchetti/sicurezza-versioni-locali/"
status: "PC version of mine"
---

# Local versions of pages and documents, without GitHub

**The problem.** Pages, reports and work documents change often, and sometimes the good version was the one from three days earlier. Dated copies are fine for a configuration file, not for dozens of pages. But putting everything on GitHub meant sending client data off the PC too, just to have the history.

**How I solved it.** I decided GitHub is for code that runs. For pages and documents I keep versions locally: every night, shortly before the backup, a commit records what changed. No remote, no push. The .git lives outside the folder, so it never ends up in a published site or in the cloud sync. Only text files under 5 MB go in. After an important publication I also make a manual commit with a message. The history then goes into the nightly backup. For the PC I wrote the same thing as a script, with two commands to see a file's versions and recover an old one next to the original.

**Why this way.** Going back to yesterday's version becomes a command, and the data stays where it is. Doing it before the backup, the history is protected like everything else.

**When you need it.** If you work on HTML pages, reports or Markdown documents that change often and aren't already under git.

**When you DON'T need it.** If the folder is already a git repo (the vault, a code project), it already has its history. For Word files, Google Docs or PDFs the service's own history works better: git only compares text well. For a single file now and then, dated copies are enough.

**How to get it.** Write the folders in `versioni_locali.py`, run it once, then schedule it a quarter of an hour before the backup. Instructions: [package guide](../../pacchetti/sicurezza-versioni-locali/LEGGIMI.md).
