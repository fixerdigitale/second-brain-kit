---
slug: skill-pipeline-di-lavoro
title: "Work pipelines: corrections don't get lost anymore"
area: skill
where_it_runs: PC
level: medium
cost: "€0 extra; about 30 minutes for the first pass of the document"
package: "pacchetti/skill-pipeline-di-lavoro/"
status: "I use it"
---

# Work pipelines: corrections don't get lost anymore

**The problem.** I repeated the same corrections on every landing page and every quote. When the session ended, Claude forgot them. And I didn't distinguish the rules that apply to everyone from those of a single client.

**How I solved it.** One document, `PIPELINE-LAVORO.md`: types of work, reusable pieces (safety copy, test, client's copy, phone check), Directives for each client and type × client pipelines. Plus a skill that, on every request, figures out whether it's information or a job. For a job it finds the pipeline, states it in one line and follows it one step at a time: before, "shall I do X?", after, "I did this, is it ok?". Every correction of mine it writes into the piece, if it applies to everyone, or into the client's Directives, plus a line in the HISTORY. The rule I follow: the first time I record the steps, the second time the pipeline is born, the third time I optimize it.

**Why this way.** I built it after counting two months of tasks and sessions: the real jobs were 14 types, always the same ones. Written once, I don't explain them again. The check before and after each step leaves the decisions with me, while the AI does the work.

**When you need it.** If you do similar jobs for several clients (pages, quotes, reports, technical problems) and each client has their quirks.

**When you DON'T need it.** If you do a different job every time, or work for a single client with few rules: your CLAUDE.md is enough. The check at every step slows things down: for 10-minute jobs it's too much.

**How to get it.** Copy the skill into `~/.claude/skills/pipeline-lavoro/` and the two templates into `<vault-folder>/pipeline-lavoro/`, then replace the path placeholder. At the start the document is almost empty, and that's as it should be. Step-by-step instructions: [package guide](../../pacchetti/skill-pipeline-di-lavoro/LEGGIMI.md).
