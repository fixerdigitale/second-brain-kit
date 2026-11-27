---
slug: memoria-indice-e-regole-doro
title: "File-based memory, compact index and Golden Rules"
area: memoria
where_it_runs: PC
level: basic
cost: "€0. An hour to reorganize an index you already have."
package: "pacchetti/memoria-indice-e-regole-doro/"
status: "I use it"
---

# File-based memory, compact index and Golden Rules

**The problem.** Claude Code's automatic memory loads only the beginning of MEMORY.md (about 200 lines or 25 KB). With a "one line per file" index, once the files went past 200 the corrections at the bottom disappeared without any warning: they showed as saved, but Claude no longer read them.

**How I solved it.** Each correction lives in its own file (today I have more than 440). MEMORY.md is compact and has two parts. "Golden Rules": the text of the rule is written in the index, with a cap of 20, so Claude always reads them. "By topic": only the file names grouped by subject, which Claude opens when the topic is relevant. New corrections go into a "To sort" group. A correction moves up to the Golden Rules only if it came back at least twice, and only with my ok.

**Why this way.** Text in the index is always read, a file is opened only if its name looks right: the most repeated rules deserve the guaranteed spot. The cap is there because if every rule is golden, none is. For me it's the hardest part to keep: I tend to exceed it, and every so often I thin it out by moving the least used ones to CLAUDE.md or to their topic.

**When you need it.** When automatic memory goes past a few dozen files, or when you notice Claude forgetting a correction you know is saved.

**When you DON'T need it.** With fewer than 50 memory files a simple index works fine. If the really important rules are few, you can put them straight into CLAUDE.md and skip the Golden Rules.

**How to get it.** Copy the structure of the package's `MEMORY.md` into your project's memory folder (`~/.claude/projects/<project-folder-name>/memory/`). If you already have a MEMORY.md, make a copy and reorganize it by hand.

Step-by-step instructions: [package guide](../../pacchetti/memoria-indice-e-regole-doro/LEGGIMI.md).
