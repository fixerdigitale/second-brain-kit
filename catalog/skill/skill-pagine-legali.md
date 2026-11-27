---
slug: skill-pagine-legali
title: "Legal pages written from what the site really does"
area: skill
where_it_runs: PC
level: advanced
cost: "€0 in tools; 1-2 hours per site; the professional's review is separate"
package: "pacchetti/skill-pagine-legali/"
status: "I use it"
---

# Legal pages written from what the site really does

**The problem.** Privacy and cookie policies copied from generic templates said false things: tools the site doesn't use, while the ones it does use were missing (pixels, calendars, forms). And the cookie banner often loaded trackers before the choice.

**How I solved it.** I adapted a public skill (Apache 2.0 license) into Italian. First it scans the site's code or HTML and tests the banner in the browser: what fires before the choice, after "Reject", after "Accept". Then it collects the facts from the client and writes privacy policy, cookie policy, terms of service, a notice on AI use and the banner texts. Whatever has no source stays as a placeholder and goes into a list to verify. When I need to cite an article from the law in force I also turn on the legal-it plugin from mcp-legal-it (public, Apache 2.0), which reads Normattiva, EUR-Lex and Brocardi; by default I keep it off, because every session starts its own server and I don't need it for normal work.

**Why this way.** First you look at the site, then you write: never the other way around. No invented data and no laws cited from memory: only those verified on a primary source, with the date. It isn't legal advice: these are drafts to give a professional, who then reviews instead of writing from scratch.

**When you need it.** A landing page going live, a site adding trackers or forms, a check of existing legal pages.

**When you DON'T need it.** If you already have a privacy consultant looking after the site, or if the site handles sensitive data (health, minors): there you need the professional from the start. The drafts shouldn't be published without review. The adaptation is for Italian/EU sites; for other jurisdictions start from the original skill.

**How to get it.** Copy `pagine-legali/` into `~/.claude/skills/` keeping LICENSE and NOTICE. You need Python 3 and, for the banner test, Node.js with Playwright and Chromium. Original: https://github.com/gricyk/claude-skill-eu-web-compliance. Optional plugin: https://github.com/capazme/mcp-legal-it. Step-by-step instructions: [package guide](../../pacchetti/skill-pagine-legali/LEGGIMI.md).
