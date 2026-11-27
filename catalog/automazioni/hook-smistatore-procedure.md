---
slug: hook-smistatore-procedure
title: "Routing hook: the right procedure at the right moment"
area: automazioni
where_it_runs: PC
level: medium
cost: "€0. 15 minutes, plus the time to write the procedures."
package: "pacchetti/hook-smistatore-procedure/"
status: "PC version of mine"
---

# Routing hook: the right procedure at the right moment

**The problem.** I wrote procedures for the jobs I repeat (landing pages, reports, proposals), and the direction rules for deciding who does what. But Claude didn't open them unless I reminded it: it started from scratch and repeated mistakes already corrected.

**How I solved it.** I added a UserPromptSubmit hook that recognizes the type of job from the words in my message and adds for Claude, once per session, "possible procedure: X, in file Y, to be verified". When the message looks like a job, it also adds a direction reminder: before starting, decide who does it. On my side it also brings up the stable-facts sheet when I name a client. In the PC version the procedures live in a JSON file (name, words, file path) and the reminder in an optional text file.

**Why this way.** Procedures are only worth something if they get read. This way they show up when they're needed, and Claude tells me in one line which one it's following: if it's wrong I see it right away. "To be verified" is deliberate: it guesses from the words and sometimes gets it wrong.

**When you need it.** If you already have (or are writing) procedures in files for recurring jobs, or use the skills in the [direction and routing](../agenti/agenti-regia-e-smistamento.md) card.

**When you DON'T need it.** If you have no written procedures: the hook has nothing to remind, so start with those. With few procedures, always the same ones, a line in CLAUDE.md is enough.

**How to get it.** Copy `smistatore.py`, `procedure.json` and, if you want the direction reminder, `promemoria.txt` into `~/.claude/hooks/`. Put your procedures in the JSON (absolute paths) and the block from `settings-esempio.json` into `~/.claude/settings.json`. Step-by-step instructions: [package guide](../../pacchetti/hook-smistatore-procedure/LEGGIMI.md).
