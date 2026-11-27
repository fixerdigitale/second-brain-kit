---
slug: ricerca-call-trascritte
title: "Transcribed calls: searchable, with no commitments lost"
area: ricerca
where_it_runs: PC
level: medium
cost: "€0 extra with a call recorder you already use. 10 minutes to copy script and skill; then a few seconds per run."
package: "pacchetti/ricerca-call-trascritte/"
status: "PC version of mine"
---

# Transcribed calls: searchable, with no commitments lost

**The problem.** Call transcripts arrived as text files with no title, date or participants, and search found them poorly: a decision said in a call was as good as unsaid. And commitments got lost from the recorder's automatic summary: one afternoon it had extracted six and I had picked up two, almost always the very ones to delegate.

**How I solved it.** Two pieces. The first is mechanical: every hour a script takes the transcripts saved by the recorder (I use Fathom) and writes one markdown note per call, with title, date, who's speaking, link to the recording and the full transcript; the calls folder is indexed together with the vault, so search finds them like any other note. The second is judgment: when a call ends, my main assistant sorts each point into work requested now (it becomes a draft task, with its source), an idea for the future (it stays in the note) or an agreement (it goes into the client's note); every action item from the recorder either becomes a task or has a written reason why not; then it prepares the recap for the client, which goes out only after my yes. For the PC I made both halves without depending on Fathom: a script that turns a folder of .txt, .vtt or .srt files into notes, and a `scheda-call` skill that makes the call note from a pasted transcript or one already in the vault.

**Why this way.** Calls are the source of decisions with clients: I use them to check a fact before building on it ("did we say X in the call?"). Full transcript and not summary, because the summary loses exactly the detail you need later, and it often writes "start working on…" even when nobody asked for it. Separating work, ideas and agreements avoids invented tasks. A recap prepared but not sent lets me align the client in a minute, without risk.

**When you need it.** If you have several calls a week with clients or partners, already record them with a tool that gives you the transcript, and commitments come out of them.

**When you DON'T need it.** If you have few calls, don't record them, or clients don't agree to being recorded. If you already take good notes by hand, the skill costs you more time than it saves. If your recorder already has good search and you don't need to cross it with your notes, it's a duplicate. And if the vault goes to GitHub or Drive, the clients' words go with it: keep it private and skip sensitive calls.

**How to get it.** Copy `call_in_markdown.py` into `~/.claude/strumenti/` and `scheda-call/` into `~/.claude/skills/scheda-call/`. Download the transcripts to a folder and run `python3 call_in_markdown.py <transcripts-folder> <vault-folder>/Call`; then in Claude Code "make me the call note". The version that starts by itself at the end of a call needs a server.

Step-by-step instructions: [package guide](../../pacchetti/ricerca-call-trascritte/LEGGIMI.md).
