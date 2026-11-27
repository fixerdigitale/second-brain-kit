---
slug: canali-report-pagine
title: "How I deliver pages and reports"
area: canali
where_it_runs: PC
level: basic
cost: "€0 on the PC; a site with login needs a server and days of setup"
package: "pacchetti/canali-report-pagine/"
status: "PC version of mine"
---

# How I deliver pages and reports

**The problem.** The AI's results reached me as markdown or file paths. From the phone I didn't open them, and I couldn't forward them to a client like that. And when I did send them, attachments and public links circulated without control and I no longer knew who had what.

**How I solved it.** Every document meant to be read becomes a web page in my fixed style: conclusion at the top, table of contents, numbered sections. Fixed rule: I always get a link, never a file path. The command that publishes it won't run unless I say which client, project and task it's for, and the same page published twice gets updated instead of being duplicated. In my system the pages live on a site of mine behind a login with a second factor; a public folder exists only for the few pages that must be open, with no listing; clients only get what I mark as external (see the catalog, [card](canali-catalogo-elementi.md)). The package has the PC version: a skill that makes a single HTML page, which opens with a double click, and three ways to get it to someone.

**Why this way.** A page with the conclusion at the top can be read in two minutes on the phone; a file in a folder nobody opens. Having to say who it's for avoids orphan reports. And one place with controlled access is worth more than attachments scattered between mail and chat.

**When you need it.** If you often send analyses, summaries or proposals to clients or partners, or want to reread results from your phone.

**When you DON'T need it.** If you're the only one reading the results, in VS Code, right away: markdown is enough. If you already send Google Docs to clients, stick with those. And a site of your own with a login only makes sense if you deliver often to several clients: it's a service to update and keep secure, and for a few files a month a Drive shared with specific people does the same job.

**How to get it.** Copy `report-pagina/` (`SKILL.md` and `template.html`) into `~/.claude/skills/report-pagina/` and change the colors at the top of the template if you want your own. The package guide explains the three ways to deliver it: Drive, a private claude.ai page, your own site with login. Step-by-step instructions: [package guide](../../pacchetti/canali-report-pagine/LEGGIMI.md).
