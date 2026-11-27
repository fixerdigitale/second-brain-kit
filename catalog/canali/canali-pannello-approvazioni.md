---
slug: canali-pannello-approvazioni
title: "Requests for my ok in one place"
area: canali
where_it_runs: PC
level: medium
cost: "€0 for the file version; my control panel is a custom application, weeks of work"
package: "pacchetti/canali-pannello-approvazioni/"
status: "PC version of mine"
---

# Requests for my ok in one place

**The problem.** Agents and automations asked me for confirmations everywhere: in chat, on Slack, on WhatsApp. I forgot what I had approved, and some requests stayed stuck for days without my knowing.

**How I solved it.** In my control panel, next to the task board, there's the Approvals page: one card per request with topic, what's being asked, link to the work and three actions (Approve, Reply with the correction, Stop) plus comments. I only get a message with the link to the card. Requests that touch the server also require the 6-digit code from my login; after a correct code I have 5 minutes in which the others can be approved with one tap. Every status change stays in a log that can't be deleted. Tasks born from calls also come in as drafts, and whoever plans with me evaluates them before they end up in my day. The package has the vault version: a `DA-APPROVARE.md` file with the cards and a rule for CLAUDE.md.

**Why this way.** One place means I always know what's waiting for me. "Reply with the correction" avoids the "no" → "so how then?" round trip. And the log tells me who approved what and when.

**When you need it.** If you let Claude or other agents work while you're away and want them to stop before sensitive actions (emails to clients, publications, deletions).

**When you DON'T need it.** If you work with Claude only in chat, in front of the screen: confirmations in chat are enough. The file doesn't send notifications: if you don't open it, the cards wait.

**How to get it.** Copy `DA-APPROVARE.md` into the root of the vault and paste `regola-per-CLAUDE.md` into your CLAUDE.md. The panel with buttons, code and notifications remains an idea: it needs a server. Step-by-step instructions: [package guide](../../pacchetti/canali-pannello-approvazioni/LEGGIMI.md).
