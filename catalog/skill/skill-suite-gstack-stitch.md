---
slug: skill-suite-gstack-stitch
title: "Skill suites taken from outside: gstack and Stitch"
area: skill
where_it_runs: PC
level: advanced
cost: "€0 for gstack (MIT); Stitch is a Google service with its own usage limits, to check on your account"
package: "none: third-party skill from the source"
status: "I use it"
---

# Skill suites taken from outside: gstack and Stitch

**The problem.** Big suites promise "a whole team" in one folder: dozens of skills, commands, hooks. Installing them whole means a lot of other people's code and a lot of context; taking random pieces means losing the reason they work together.

**How I solved it.** I use two. Garry Tan's gstack (more than 40 skills: plan review, design review, QA in a real browser, code review, release) I installed whole, after scanning and reading it, with automatic updates turned off: a monthly check tells me if there's a new version and I decide. The ones I really use are few: design-review and qa (the "reproduce, fix, re-verify" loop, from which I took the skill in the card on testing the user path), office-hours and plan-ceo-review to stress-test an idea, design-shotgun to get several variants. Stitch's skills (Google Labs, 7 skills) I use only to explore the layout of a section: one call per section, I pass screenshots, fonts, logo and colors, and I take background and hierarchy from it, never texts or numbers, because it invents them.

**Why this way.** From gstack I take the method of the checks, which is the strong part; the skills I don't use cost me nothing until I open them. Stitch gives composition ideas that pages made only from text lack, but it stays a starting point, not the final page.

**When you need it.** gstack, if you build products or tools of your own and want reviews and QA with a fixed method. Stitch, if you make landing pages and need a second visual direction before building.

**When you DON'T need it.** If you write little code or few pages: for one person 40 skills are a lot, and the method skills in the other cards are enough. gstack has parts that want a browser without a sandbox, install scripts and hooks: if you don't have time to read them, don't install it whole. Stitch's skills do nothing without a Stitch account and its key.

**How to get it.** No package: take them from the source. gstack: https://github.com/garrytan/gstack (MIT; read the setup script before running it). Stitch: https://github.com/google-labs-code/stitch-skills and the service https://stitch.withgoogle.com. The Stitch key goes in an environment variable, not in the skill text or on the command line. Before installing them, `pacchetti/skill-cerca-strumento/`.
