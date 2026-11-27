---
slug: agenti-lavori-lunghi-codex
title: "Claude decides, ChatGPT (Codex) does the long jobs"
area: agenti
where_it_runs: PC
level: medium
cost: "€0 extra if you already have ChatGPT; otherwise the ChatGPT subscription. Installing Codex CLI: about 10 minutes."
package: "pacchetti/agenti-lavori-lunghi-codex/"
status: "PC version of mine"
---

# Claude decides, ChatGPT (Codex) does the long jobs

**The problem.** I pay for two subscriptions, Claude and ChatGPT, but I was only using Claude. Pages and long scripts ate the quota I needed for deciding and reviewing.

**How I solved it.** I hand long jobs (pages, components, graphics, long code, integrations) to Codex with the ChatGPT subscription. Claude writes the brief to a file, launches Codex from the command line, then checks the delivery as it does with any agent. On my side two agents on the server do this with the GPT model, and a hook checks that every launch really uses the right model (card [command guard](../automazioni/hook-guardia-comandi.md)). For the PC I wrote the simple version with `codex exec`.

**Why this way.** Using both subscriptions lets me get more work done without spending more. I find Claude more useful for deciding and checking; the long, repetitive work can be done by the other one. Control stays with Claude, so quality doesn't depend only on the model doing the work.

**When you need it.** If you already have a ChatGPT subscription (Plus or higher) and you sometimes run out of Claude quota on long jobs.

**When you DON'T need it.** If you don't have ChatGPT: buying it just for this only makes sense if you often hit Claude's limit. It isn't worth it for short jobs, where brief and check cost more than the work. And don't use it on client data you promised to keep with a single provider.

**How to get it.** Install Codex CLI (`npm install -g @openai/codex`), run `codex login` with your ChatGPT account and copy the skill into `~/.claude/skills/lavoro-lungo-codex/`. Step-by-step instructions: [package guide](../../pacchetti/agenti-lavori-lunghi-codex/LEGGIMI.md).
