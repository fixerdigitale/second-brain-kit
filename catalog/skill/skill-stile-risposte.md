---
slug: skill-stile-risposte
title: "Short, tidy answers (caveman + i-have-adhd in Italian)"
area: skill
where_it_runs: PC
level: basic
cost: "€0; 5 minutes"
package: "pacchetti/skill-stile-risposte/"
status: "I use it"
---

# Short, tidy answers (caveman + i-have-adhd in Italian)

**The problem.** Answers were long, with the context before the thing to do. Between one message and the next I lost track of where we were.

**How I solved it.** I always keep two third-party skills on: caveman (filler gone, one idea per sentence) and i-have-adhd (first line = action, numbered steps, state recapped every turn, closing with a single short action). I never invoke them: in my system both skills have `disable-model-invocation: true` and the rules sit directly in CLAUDE.md, so they apply in every session. My piece is that CLAUDE.md block, which adapts them to Italian: lite level, with articles and full sentences, and a list of things that are never compressed (numbers, paths, commands, negations, uncertainties, security warnings).

**Why this way.** caveman's more aggressive levels were made for English: in Italian, without articles, it reads badly. Cutting a "not" flips the meaning, so negations always stay. The style applies only in chat: code, documents and messages to others are written normally.

**When you need it.** If you read answers in a hurry, on the phone, or jump from one job to another and need to find your place again.

**When you DON'T need it.** If you like discursive explanations or use Claude to learn a new subject: compression removes the reasoning you need.

**How to get it.** Install the skills from the sources: https://github.com/JuliusBrussee/caveman and https://github.com/ayghri/i-have-adhd (MIT). Then paste the package's block into your `CLAUDE.md`. If you work in English, you can use caveman's own levels directly and skip the Italian adaptation. Step-by-step instructions: [package guide](../../pacchetti/skill-stile-risposte/LEGGIMI.md).
