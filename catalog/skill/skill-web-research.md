---
slug: skill-web-research
title: "Web research with the sources alongside"
area: skill
where_it_runs: PC
level: basic
cost: "€0 with search and direct reading; paid scraping optional, about $0.002-0.01 per page"
package: "pacchetti/skill-web-research/"
status: "PC version of mine"
---

# Web research with the sources alongside

**The problem.** The AI's research mixed facts and opinions, with no dates and no links. Pages that wouldn't open disappeared silently.

**How I solved it.** A skill that searches first and reads afterwards: 2-4 real sources, a ladder of ways to open a page (direct reading, then a light browser that runs JavaScript, then a real browser, paid only as a last resort). For prices it starts from comparison sites. For videos it downloads them and reads the frames. It always comes out with a short answer, every claim with its link, and an "Uncertainties" section with the pages that didn't open. From my version I removed the commands that depend on my server.

**Why this way.** I need research to decide: without links I can't verify it. A figure found on a single source gets written as "according to X". If a page is blocked I'd rather know, instead of reading an invented summary.

**When you need it.** Comparisons of prices and tools, competitors, fact checks, opening a link or a video someone sent you.

**When you DON'T need it.** For questions that don't depend on recent information, just ask. For long market studies you need deeper research, with more rounds.

**How to get it.** Copy `web-research/` into `~/.claude/skills/`. Optional: yt-dlp and ffmpeg for videos, Lightpanda (https://github.com/lightpanda-io/browser) or a browser MCP. Step-by-step instructions: [package guide](../../pacchetti/skill-web-research/LEGGIMI.md).
