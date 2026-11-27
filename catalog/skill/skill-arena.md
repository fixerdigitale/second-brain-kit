---
slug: skill-arena
title: "Arena: many versions of Claude competing on the same task"
area: skill
where_it_runs: PC
level: advanced
cost: "€0 extra, but very high quota usage; better to use --quick (16 agents)"
package: "none: third-party skill from the source"
status: "I use it"
---

# Arena: many versions of Claude competing on the same task

**The problem.** On some important answers the first version doesn't convince me, and "try again" gives a variant of the same idea.

**How I solved it.** Arena launches many sub-agents (100 by default, 16 with --quick) on the same task, each with a different strategy. Then it pits them against each other in a knockout bracket: they attack each other's solutions, defend them, and a judge scores them on a written rubric until one is left. My copy asks for confirmation before starting.

**Why this way.** It forces exploring different paths instead of polishing the first one. I keep it for the rare cases where the quality of the answer is worth much more than the usage; I've used it only a few times.

**When you need it.** A very important text or choice, where the first answer isn't enough.

**When you DON'T need it.** Almost always. 100 sub-agents plus the judging can burn a large share of the weekly limit in one go. For normal use, the counter-opinion skill and a second review are enough.

**How to get it.** Third-party skill, source to be verified: my copy has no author or link. If you find it, run it through the method in `pacchetti/skill-cerca-strumento/` first.
