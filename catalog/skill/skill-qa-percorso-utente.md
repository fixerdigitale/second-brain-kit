---
slug: skill-qa-percorso-utente
title: "Testing the page the way a real user uses it"
area: skill
where_it_runs: PC
level: medium
cost: "€0; a run on a landing page takes 10-20 minutes"
package: "pacchetti/skill-qa-percorso-utente/"
status: "I use it"
---

# Testing the page the way a real user uses it

**The problem.** "The page responds" doesn't mean it works. Forms that don't submit, broken thank-you pages, tracking that doesn't fire, a messed-up phone version: I found out afterwards, from the client.

**How I solved it.** A skill that replays a user's path in a browser, at 1440 px and at 393 px. It clicks, fills in, submits, watches console and network, and opens the linked pages too. Every defect has evidence. After the fix it redoes the whole path from the start, at most 3 rounds. It ends with a score: below 8 I don't deliver.

**Why this way.** Reproducing before touching the code avoids random fixes. Redoing the whole path after the fix uncovers what the fix broke elsewhere. The idea comes from gstack's /qa loop (see the card on suites taken from outside); I had the text rewritten from scratch, shorter.

**When you need it.** Before delivering landing pages, forms, checkouts, client areas; when someone reports an error.

**When you DON'T need it.** For a text change on a page that already works it's too much. It needs a browser Claude can drive: without one, the skill has no hands.

**How to get it.** Copy `qa-percorso-utente/` into `~/.claude/skills/` and add Chrome DevTools MCP (https://github.com/ChromeDevTools/chrome-devtools-mcp, needs Node.js). Step-by-step instructions: [package guide](../../pacchetti/skill-qa-percorso-utente/LEGGIMI.md).
