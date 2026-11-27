---
slug: hook-contesto-avviso-e-compressione
title: "Context warning and automatic compaction"
area: automazioni
where_it_runs: PC
level: basic
cost: "€0. 15 minutes to copy and try it."
package: "pacchetti/hook-contesto-avviso-e-compressione/"
status: "I use it"
---

# Context warning and automatic compaction

**The problem.** A long session rereads the whole context on every message. I noticed late: I had sessions above 500k tokens per message, and out of about 11,500 logged checks more than 5,000 were above 250k. It cost subscription quota and made Claude slower and more confused. Before, I used to block messages above a threshold myself and open a new session: it interrupted the work.

**How I solved it.** Two pieces together. A UserPromptSubmit hook reads the tail of the conversation and, above a first threshold, adds a warning just once, which Claude reports to me in one line ("I'll delegate reading and searching to a sub-agent"); above the high threshold it asks Claude, every turn, to update the HANDOFF. Then compaction starts by itself, without stopping me: with the setting `autoCompactWindow: 480000` my version compacts around 447k (window minus about 33k), and idle-session compaction compacts sessions while I'm not using them. Before every compaction the HANDOFF save runs. On my side there's also a desktop-app mod that acts as a safety net if automatic compaction is off: that one isn't in the package.

**Why this way.** I don't have to remember: the number arrives when it matters, and the context manages itself while I work. Warning only once is deliberate: it stays in the history, and repeating it every turn would waste more context. The high threshold keeps as much detail as possible before compacting; the HANDOFF avoids losing it.

**When you need it.** If you run long sessions (hours on the same job), use a model with a large window, or find yourself running out of limits earlier than expected or seeing Claude forget things said at the start.

**When you DON'T need it.** If you open a new session for each job and rarely go past a few tens of thousands of tokens. With the standard 200k window `autoCompactWindow` changes nothing. Don't use automatic compaction without a state save (card [HANDOFF saved at compaction](hook-handoff-prima-compressione.md)). I verified the setting names on version 2.1.330: on another version they might not exist.

**How to get it.** Copy `avviso_contesto.py` into `~/.claude/hooks/` and, from `settings-esempio.json`, the two keys and the hook block into `~/.claude/settings.json`. The thresholds are at the top of the file. Step-by-step instructions: [package guide](../../pacchetti/hook-contesto-avviso-e-compressione/LEGGIMI.md).
