---
slug: impara-skill-migliorate-dalle-sessioni
title: "Skills that improve by reading sessions, adopted by me"
area: impara
where_it_runs: PC on
level: advanced
cost: "€0 extra with the Claude subscription, but it uses quota at night (I have a cap of 150,000 tokens per night). Setup: 30-60 minutes."
package: "pacchetti/impara-skill-migliorate-dalle-sessioni/"
status: "I use it"
---

# Skills that improve by reading sessions, adopted by me

**The problem.** I wrote my skills once and then they stayed as they were, even when I saw Claude stumble on the same steps session after session. Rewriting them by hand, going through dozens of sessions, was something I never did.

**How I solved it.** I use SkillOpt-Sleep, part of Microsoft's open source SkillOpt project. At night it reads recent sessions, finds the jobs I repeat, replays them with and without a change to the skill, and proposes the change only if it improves on held-out tasks. I configured it with the Claude subscription, never with pay-per-use keys, and with automatic adoption turned off: every proposal comes to me for approval, along with the rules it must not contradict. Over 7 nights since I started approving them: 1 adopted, 1 rejected by me, 2 with no proposal because the check didn't pass, the others withdrawn or pending.

**Why this way.** Sessions already contain the evidence of what works and what doesn't; a tool can read them better than I can. But a skill changes the behavior of every session after it, so the last word stays with me.

**When you need it.** If you have skills you use every day on repeated jobs, and your PC can stay on at night.

**When you DON'T need it.** If you have few skills or your work is always different: there are no recurring tasks to replay, and the run uses quota for nothing. Don't use it on projects with data you promised not to let out: pieces of the sessions go to the model provider, and the documentation says that secret redaction is not a guarantee. I run it on the server: I haven't tried it on a PC.

**How to get it.** From the source: https://github.com/microsoft/SkillOpt (`pip install skillopt`). The package has my example configuration, with automatic adoption turned off, and the steps to try it first without writing anything. Step-by-step instructions: [package guide](../../pacchetti/impara-skill-migliorate-dalle-sessioni/LEGGIMI.md).
