---
slug: sicurezza-copia-settimanale
title: "One copy a week outside the computer, no software needed"
area: sicurezza
where_it_runs: PC
level: basic
cost: "€0. 5 minutes the first time, 2 minutes a week."
package: "none: idea only"
status: "what I did at the start, before the nightly backup"
---

# One copy a week outside the computer, no software needed

**The problem.** At the start all my work with Claude lived in a single folder on the laptop. No copy: if the disk broke or the computer went missing, I'd lose instructions, notes and templates. An automatic backup felt like something for technical people, and I switched the laptop off every evening.

**How I solved it.** On a fixed day each week I copied the whole work folder to a place outside the computer: an online drive (Google Drive, OneDrive, iCloud) or a USB stick I kept somewhere else. A new folder each time, with the date in the name (`work-2026-11-27`), the last four kept, the older ones removed. A calendar reminder told me the day.

**Why this way.** Nothing to install, and it works even with the computer off: you make the copy when you turn it on. The date in the name tells you right away which one is the latest. Keeping four copies also covers a file that got damaged without me noticing. Every now and then I opened a copy from another device to see that the files really opened.

**When you need it.** If today you have no copy of your work outside the computer, and you want the simplest thing that protects you from a broken disk or a lost computer.

**When you DON'T need it.** If the folder is already inside OneDrive, iCloud or Google Drive with sync on, an online copy already exists: this card only adds protection against a deletion that syncs too (with the dated folder you get it back). If you already have git with a private online copy, or an automatic backup that works, you don't need it. When the manual copy starts to feel heavy, I moved on to the [nightly backup](sicurezza-backup-notturno.md).

**How to get it.** No package: ask Claude "copy this folder to <place> with today's date in the name" and set a weekly reminder. The first time, try to reopen the copy with the [restore test](sicurezza-prova-ripristino.md). Don't put password or key files in the online copy: if there are any, first the card [No passwords in chat or notes](sicurezza-niente-password-in-chat.md).
