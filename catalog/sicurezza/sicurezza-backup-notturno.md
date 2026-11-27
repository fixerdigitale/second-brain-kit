---
slug: sicurezza-backup-notturno
title: "Nightly backup with the 3-2-1 rule: three copies, two places, one off-site"
area: sicurezza
where_it_runs: PC on
level: medium
cost: "€0 if you already have GitHub and a cloud (Drive, OneDrive, iCloud); restic is free. A few hundred MB for 7 zips of a notes vault. 20 minutes of setup."
package: "pacchetti/sicurezza-backup-notturno/"
status: "PC version of mine"
---

# Nightly backup with the 3-2-1 rule: three copies, two places, one off-site

**The problem.** I thought GitHub was already a backup. But if I delete a folder by mistake and push, the deletion arrives there too; if I lose access to the account, I lose everything at once. And a backup on the same disk or the same server disappears with it.

**How I solved it.** I follow the classic 3-2-1 rule: 3 copies, on 2 different media, 1 off-site. On the server I do it with restic: every night an encrypted, deduplicated backup (7 daily copies, 4 weekly, 6 monthly, an integrity check once a week), plus an encrypted archive of the essential part on a different cloud. An automatic check turns red if either one fails or is older than 30 hours. The password lives outside the server: without it the backup can't be opened. For a vault on a PC I wrote a minimal version: commit and push to a private GitHub repo, plus a dated zip in the cloud-synced folder, keeping the last 7 copies. The script stops if one of the files to save looks like a key, or if the repo turns out to be public.

**Why this way.** Each copy protects against a different failure: broken disk, my mistake, blocked account. The dated zips cover the deletion that propagates. And a backup that fails silently is, for me, worse than no backup, because it makes you feel safe: that's why every run writes its outcome to a file that can be checked.

**When you need it.** As soon as the vault contains things you don't want to rewrite: memory, procedures, work notes. The PC script is useful if today you push to GitHub by hand or only now and then.

**When you DON'T need it.** If the vault is already under git with automatic push and the cloud syncs it in real time, you already have two copies: the zip only adds protection against a deletion that propagates. A fourth copy (external disk, NAS) isn't needed in my view if the three are there and the restore test passes. The restic version with database dumps is only for a server with databases. The zip isn't encrypted: with client data I use restic.

**How to get it.** Change the two lines in `backup_vault.py`, run it by hand, then schedule it with launchd (Mac) or Task Scheduler (Windows). Instructions, restic commands and caveats: [package guide](../../pacchetti/sicurezza-backup-notturno/LEGGIMI.md). The `ultimo-backup.txt` file it writes can be checked by the [Health checks](sicurezza-controlli-salute.md) card.
