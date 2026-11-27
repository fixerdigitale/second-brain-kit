---
slug: skill-contro-parere
title: "A Claude that doesn't just agree with me"
area: skill
where_it_runs: PC
level: basic
cost: "€0 extra; about 10 minutes to adapt the sources table"
package: "pacchetti/skill-contro-parere/"
status: "I use it"
---

# A Claude that doesn't just agree with me

**The problem.** Models tend to agree with me. If I misremembered a budget from a call, Claude built the quote on top of it. And if I insisted, it gave in even when the facts were on its side.

**How I solved it.** I wrote a skill that checks the facts I report against the source (call transcript, notes, email) before using them. On important choices it first writes its own opinion starting only from the sources, then compares it with mine. When we disagree it answers in only three forms: I HOLD (the fact, plus what would change its mind), I CHANGE (new fact and reasoning redone from scratch), I VERIFY (how it checks, and it does). "Just do it" switches it off for that message. I never invoke it by hand: I keep it always on with a line in my CLAUDE.md, and the skill has `disable-model-invocation: true`, so it doesn't switch on or off at random.

**Why this way.** I need someone who improves decisions, not someone who applauds them. Tone and insistence aren't evidence: this rule puts that in black and white. A single objection, with the concrete cost of getting it wrong; on a clear instruction it says it once and then executes. That way it doesn't turn into systematic opposition.

**When you need it.** If you often decide about money, clients or things that are hard to undo, and you find yourself reporting from memory things said in calls or chats.

**When you DON'T need it.** If you only use Claude to write code or texts on precise instructions, it just slows you down. If your sources (calls, notes) aren't where Claude can read them, fact checking boils down to "I can't find the source, I'll take your word for it".

**How to get it.** Copy the `contro-parere/` folder into `~/.claude/skills/` and add to your `CLAUDE.md` the line from the package guide to keep it always on. First adapt the sources table to yours. Idea taken from talhapythoneer/anti-sycophancy-prompt and HimanshuJ16/frank (MIT), text rewritten. The skill text is in Italian. Step-by-step instructions: [package guide](../../pacchetti/skill-contro-parere/LEGGIMI.md).
