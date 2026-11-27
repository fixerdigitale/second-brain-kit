---
slug: canali-lavori-in-background
title: "Long jobs in the background, with a notice at the end"
area: canali
where_it_runs: PC on
level: medium
cost: "€0 extra, same Claude subscription; 10 minutes to install"
package: "pacchetti/canali-lavori-in-background/"
status: "PC version of mine"
---

# Long jobs in the background, with a notice at the end

**The problem.** A long job (a research task, a reorganization of notes, a big draft) kept my chat busy: either I waited, or I opened another window and then forgot to go and look.

**How I solved it.** When a request takes more than a couple of minutes, my assistant doesn't keep me hanging: it launches a new Claude Code session in the background with a complete brief (goal, files, what to deliver), tells me right away it has started and, when the job ends, I get "✅ title: …" or "❌ …". At most 3 jobs at once. The package has the PC version: a script that launches `claude -p` in the background, writes the result to a markdown file and sends a desktop notification (Windows, Mac, Linux).

**Difference from night work.** You launch this yourself, now, during the day, one job at a time, while you keep working in chat; it finishes in minutes and you look at the result right away. The night queue ([card](canali-lavoro-notte.md)) is a list prepared in the evening, runs when you're not there (on my server it checks plan usage before each job; the PC script stops at a fixed time) and leaves everything "to review" in the morning.

**Why this way.** Separating "asking" from "waiting" lets me keep thinking. The brief written for a session starting from zero also forces me to clarify what I want, and the result file stays as a trace.

**When you need it.** If you often launch 10-30 minute jobs and want to do something else with Claude in the meantime.

**When you DON'T need it.** If your jobs take a minute, or you prefer to follow what Claude does step by step: in the background you can't approve commands one by one, so those that ask for permission are denied.

**How to get it.** Copy `lavora.py` wherever you like (for example `<vault-folder>/strumenti/`), change `CARTELLA_PREDEFINITA` if you want the results in the vault and try it with a dummy job. Step-by-step instructions: [package guide](../../pacchetti/canali-lavori-in-background/LEGGIMI.md).
