---
slug: memoria-riordino-handoff
title: "Tidy-up: from work diaries to the facts sheet"
area: memoria
where_it_runs: PC
level: medium
cost: "€0 extra with the Claude subscription. The script runs in a second."
package: "pacchetti/memoria-riordino-handoff/"
status: "PC version of mine"
---

# Tidy-up: from work diaries to the facts sheet

**The problem.** Even with HANDOFF and SISTEMA separated, nobody remembered to move the stable facts into the sheet, and the HANDOFFs swelled up again.

**How I solved it.** On my side, every night at 4:40 a service on the server reads the new sections of the HANDOFFs, asks Sonnet which ones are stable facts and changes at most 12 lines of SISTEMA.md: a copy before every change, secrets removed before passing the text to the model, every line marked "riordino dd/mm". Then, if a HANDOFF goes over 80 KB, it moves the oldest sections into a monthly archive until it's back to 60 KB, checking that no line gets lost. The package has both halves in PC form: the prompt to use as a `/riordino` command (it shows the changes and waits for the ok) and a Python script that does the mechanical archiving, as a dry run until you add `--applica`.

**Why this way.** The judgment part (what's stable) a model does well, but it must change single lines and never invent: that's why the prompt is tight. The mechanical part needs no AI, and a script that counts lines gives me more confidence than a model rewriting a 100 KB file.

**When you need it.** If you use HANDOFF.md and SISTEMA.md on long projects and see the HANDOFFs grow beyond tens of KB.

**When you DON'T need it.** If you have few projects and keep them tidy by hand, or if your HANDOFFs stay short: the script would always answer "nothing to do". The automatic nightly version only makes sense with a server that's on.

**How to get it.** Save `prompt-riordino.md` as `~/.claude/commands/riordino.md` and use `/riordino` in the project folder. Run `python3 archivia_handoff.py <project-folder>` (dry run), then with `--applica`.

Step-by-step instructions: [package guide](../../pacchetti/memoria-riordino-handoff/LEGGIMI.md).
