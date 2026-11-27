---
slug: hook-domanda-breve
title: "Short question: an answer, not a job"
area: automazioni
where_it_runs: PC
level: basic
cost: "€0. 5 minutes."
package: "pacchetti/hook-domanda-breve/"
status: "I use it"
---

# Short question: an answer, not a job

**The problem.** I'd ask a quick question ("does the email go out by itself?") and Claude would start reading files, spawning sub-agents and sometimes making changes. I wanted an answer and found a job underway.

**How I solved it.** I added a UserPromptSubmit hook that decides from the text alone: if the message is short, is a question and has no work verbs (do, create, fix…), it adds for Claude "answer in a few lines, at most 3 reads; if work is needed, propose it and wait for the ok". For me it has fired about 450 times.

**Why this way.** Telling a question from an order is easy for a person and less so for an eager model. A fixed rule on the text costs nothing, and the work verbs switch it off when it shouldn't fire.

**When you need it.** If you also use Claude for quick questions in the same session where you work.

**When you DON'T need it.** If Claude already answers your questions briefly. If you dictate a lot or write long sentences, the length filter makes it fire rarely.

**How to get it.** Copy `domanda_breve.py` into `~/.claude/hooks/` and the block from `settings-esempio.json` into `~/.claude/settings.json`. Note: the work verbs in the script are Italian; replace them with your own language's. Step-by-step instructions: [package guide](../../pacchetti/hook-domanda-breve/LEGGIMI.md).
