---
slug: agenti-revisore-prima-di-mandare
title: "A fresh-eyed reviewer before publishing or sending"
area: agenti
where_it_runs: PC
level: basic
cost: "€0 extra (model included in the subscription; you can put it on Sonnet). Second opinion with Codex: €0 if you already have ChatGPT."
package: "pacchetti/agenti-revisore-prima-di-mandare/"
status: "PC version of mine"
---

# A fresh-eyed reviewer before publishing or sending

**The problem.** Things I sent out contained errors I no longer saw when rereading: a wrong signature, a date, an internal link. Whoever wrote a text reads what they meant to write, not what's there.

**How I solved it.** Before every send or publication that matters, the work goes to a reviewer who didn't write it and doesn't fix it. It rereads the original request, checks facts, numbers and links, what the recipient will see, data that must not go out, and in code the error paths. It returns APPROVED, REJECTED with the list, or NOT VERIFIABLE, and writes its verdict before reading my opinion. If I have ChatGPT, I can also ask Codex for a read-only second opinion. On the server the team's reviewers do this; this is the PC version.

**Why this way.** A reviewer who fixes becomes an author, and nobody checks them anymore. Two different models make mistakes in different ways: where they agree I trust it more, where they disagree I look myself. It costs me a few minutes; an error sent to a client would cost me much more.

**When you need it.** Before emails to clients, quotes, published pages, code that writes to real data.

**When you DON'T need it.** For internal notes, drafts for yourself, short messages to people you know: the review slows you down without reducing a real risk.

**How to get it.** Copy `revisore.md` into `~/.claude/agents/`. For a ready-made second opinion there is the codex skill from the public gstack collection (https://github.com/garrytan/gstack): run a security check on it first. Step-by-step instructions: [package guide](../../pacchetti/agenti-revisore-prima-di-mandare/LEGGIMI.md).
