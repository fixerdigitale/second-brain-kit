---
slug: hook-handoff-prima-compressione
title: "HANDOFF saved when the session gets compacted"
area: automazioni
where_it_runs: PC
level: medium
cost: "€0. 15 minutes to install it and test it with a /compact."
package: "pacchetti/hook-handoff-prima-compressione/"
status: "PC version of mine"
---

# HANDOFF saved when the session gets compacted

**The problem.** When the session fills up, Claude Code compacts it and keeps only a summary. The conversation stays on disk, but the session forgets the details: decisions, files touched, what was missing. And if the project's HANDOFF.md is stale, whoever picks up (me, another session, another agent) starts from an old state.

**How I solved it.** I use a mod of the Claude Code desktop app, not a settings.json hook: a moment before compaction it asks a copy of the session what to save and writes it into the project's HANDOFF.md, in a dated section, plus the corrections about me into memory. For a normal PC I wrote a version with the standard hooks: PreCompact saves your last 15 requests (with passwords and keys masked), and SessionStart with the "compact" matcher tells Claude to reread HANDOFF.md, compare it with those requests and update it before continuing. There's also the /salva-handoff command to do it by hand.

**Why this way.** The weak moment of long sessions is compaction: that's where you lose the thread. Hooking the save to that event means it always happens, even when I don't think about it. The hook version is less precise than mine (it updates the HANDOFF right after, not before, because during PreCompact the model doesn't answer), but it covers the gap with the saved requests.

**When you need it.** If you work on projects that last several days, keep (or want to keep) a HANDOFF.md per project, and have found that after a compaction Claude no longer knew where you were.

**When you DON'T need it.** If your sessions are short and never reach compaction. If you don't keep a HANDOFF per project, you need that first (card [HANDOFF and SISTEMA](../memoria/memoria-handoff-e-sistema.md)): the hook on its own creates files nobody reads.

**How to get it.** Copy `handoff_compressione.py` into `~/.claude/hooks/`, `commands/salva-handoff.md` into `~/.claude/commands/` and the two blocks from `settings-esempio.json` into `~/.claude/settings.json`. Step-by-step instructions: [package guide](../../pacchetti/hook-handoff-prima-compressione/LEGGIMI.md).
