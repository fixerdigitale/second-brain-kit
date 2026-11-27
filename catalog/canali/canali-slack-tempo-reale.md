---
slug: canali-slack-tempo-reale
title: "Slack and WhatsApp by events, not on a schedule"
area: canali
where_it_runs: server
level: advanced
cost: "€0 for the filter (rules only, no model); the run that updates tasks uses the subscription; always-on server"
package: "none: idea only"
status: "I use it"
---

# Slack and WhatsApp by events, not on a schedule

**The problem.** Following Slack and work WhatsApp groups with scheduled checks meant either too many notifications or replies hours late. And an important tag got lost among a hundred messages.

**How I solved it.** A service stays connected to the Slack workspaces in real time (Socket Mode); for WhatsApp the same with a webhook. A direct message or a tag for me triggers, after a moment of quiet, a run that updates the tasks. If the text says "urgent" I get a WhatsApp right away, and if I don't answer a phone call starts. In the evening and at night only new high-priority tasks get through. Some "followed" channels start a specific job on every message. Message text never ends up in the logs. A scheduled check remains only as a slow backup, every few hours, for missed events.

**Why this way.** An event that arrives when it happens costs less than a hundred checks that find nothing, and gets answered sooner. The filter (direct messages, tags, urgent) decides what deserves my attention, not the clock. One thing I learned: only one connection per Slack app, because two split the events between them.

**When you need it.** If you're in many work channels and the real requests are few and scattered.

**When you DON'T need it.** If you use Slack with few people: the native notifications on tags already do the job. And without an always-on computer a real-time connection doesn't hold up.

**How to get it.** No package: it's just the idea, it needs a server. On a PC: turn on the official Slack connector in claude.ai and ask when you need it "what did I miss in channels X since yesterday, only where I was tagged"; for the rest, Slack's native notifications on tags and keywords (for example "urgent").
