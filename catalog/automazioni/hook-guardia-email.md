---
slug: hook-guardia-email
title: "A guard that keeps my email from leaking to third-party sites"
area: automazioni
where_it_runs: PC
level: basic
cost: "€0. 10 minutes."
package: "pacchetti/hook-guardia-email/"
status: "I use it"
---

# A guard that keeps my email from leaking to third-party sites

**The problem.** Claude sees my account email in its startup instructions and sometimes puts it, on its own initiative, into a User-Agent or a URL when it calls a site. It happened to me with a public site: my email ended up in someone else's logs.

**How I solved it.** I added a PreToolUse hook on Bash, WebFetch, WebSearch and the tools that open pages: if the address appears (even encoded in a URL or in base64) and the destination isn't one of my services, it blocks the request or asks me for confirmation. The addresses live in a separate file; there are none in the code.

**Why this way.** It's a small but repeatable mistake, and no standard permission covers it: permissions look at the command, not at what's inside it.

**When you need it.** If you have Claude do research, scraping or calls to public sites from your PC.

**When you DON'T need it.** If Claude never goes on the internet for you. It doesn't protect against everything: it covers the listed tools, not a program Claude writes and runs afterwards.

**How to get it.** Copy `guardia_email.py` and `indirizzi_email.txt` into `~/.claude/hooks/`, write your addresses in the `.txt` and your domains in `HOST_AMMESSI`, then add the block from `settings-esempio.json`. Step-by-step instructions: [package guide](../../pacchetti/hook-guardia-email/LEGGIMI.md).
