---
slug: sicurezza-chiave-finita-online
title: "If a key ends up in an online copy: what I'd do"
area: sicurezza
where_it_runs: PC
level: basic
cost: "€0. 15-20 minutes, mostly on the website of the service that issued the key."
package: "none: idea only"
status: "new proposal, it hasn't happened to me: I'd do it this way"
---

# If a key ends up in an online copy: what I'd do

**The problem.** An access key for a service can end up in a notes file. If that folder is saved to GitHub, or sits inside a folder synced to the cloud, removing the line from the file isn't enough: the key stays in the old saves and in the online copy. It hasn't happened to me; this is the sequence I'd follow.

**How I'd solve it.** In this order: 1) I'd **change the key at the source**, on the website of the service that issued it ("revoke" or "regenerate"): from then on the old one is worthless, wherever it ended up; 2) I'd put the new key in a `.env` file outside the notes; 3) I'd add `.env` to `.gitignore`; 4) if the file with the key is already saved in git, I'd remove it from the tracked files with `git rm --cached <file>` (the file stays on disk, git stops saving it); 5) I'd make a new save and run `cerca-segreti` again to see it's clean. For a synced folder I'd also check the cloud service's trash and previous versions.

**Why this way.** The first step is the only one that really closes the risk: git history and cloud versions keep the old key even after you remove it from the file, and rewriting history is long and easy to get wrong. Once the key is changed, the old one is just useless text.

**When you need it.** If `cerca-segreti` finds a key in a file saved in git with an online copy, or sitting in a synced folder (OneDrive, iCloud, Dropbox, Google Drive).

**When you DON'T need it.** If the key is only on your computer, in a folder that isn't synced and was never saved in git: moving it to a `.env` is enough (card [One secrets file](sicurezza-segreti-file-unico.md)). If the value found is a fake example or an already expired key, there's nothing to change.

**How to get it.** No package: it's a sequence to do calmly. The part on the service's website is done by the person, because it needs their login; Claude prepares `.env`, `.gitignore` and the `git rm --cached` command, and runs them only after a yes. Old git history can also be rewritten (`git filter-repo`), but I wouldn't do it once the key has been changed.
