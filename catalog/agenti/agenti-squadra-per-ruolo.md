---
slug: agenti-squadra-per-ruolo
title: "A team of agents by role, with separate reviewers"
area: agenti
where_it_runs: server
level: advanced
cost: "A VPS at about €15-40/month plus a few hours of maintenance a week; the models stay within the Claude and ChatGPT subscriptions."
package: "none: idea only"
status: "I use it"
---

# A team of agents by role, with separate reviewers

**The problem.** A single assistant doing everything became, for me, mediocre at everything, and nobody checked it. And I had agents created for one person or one client, overlapping each other.

**How I solved it.** On the server I have a team on OpenClaw (open source agent software), one agent per role, not per person. My main assistant talks to me on WhatsApp and routes the work. Then there's a PM for projects and tasks, a Designer and a Developer on ChatGPT for pages and code, a Copywriter, Creative, Researcher, Analyst and Marketer on Sonnet, a Sysadmin for server and security, and an Archivist for memory and corrections. Whoever builds doesn't review: the Creative reviews visual work, the Sysadmin reviews code with three verdicts (approved, rejected, not verifiable), the Marketer reviews marketing. After the reviewers I still check myself, with Claude Code.

**Why this way.** Each role has short instructions and its own skills, so it works better. The separate reviewer has found errors that neither the author nor I had seen. The rule I set myself: a role becomes an agent only if it needs a different permission, a different model, fresh eyes for checking, or parallel work. Everything else I do with procedures and skills.

**When you need it.** If you want agents that work even when your PC is off, answer from WhatsApp or Slack, and run queues at night.

**When you DON'T need it.** Almost always, at the start. With Claude Code on the PC you get most of the value with sub-agents (executor, builder, reviewer, sysadmin) without a server to maintain. A team on a server costs real maintenance: updates, permissions, an always-on service to watch.

**How to get it.** Idea only, it needs a server. The PC version is the sub-agents in the other cards of this area. OpenClaw is a public project: evaluate it from its official documentation before installing it.
