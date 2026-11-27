---
slug: hook-guardia-comandi
title: "A guard that stops wrong commands and explains the right ones"
area: automazioni
where_it_runs: PC
level: medium
cost: "€0. 20 minutes to write and test the first rules."
package: "pacchetti/hook-guardia-comandi/"
status: "PC version of mine"
---

# A guard that stops wrong commands and explains the right ones

**The problem.** I had a clear rule: two specialist agents are launched only on ChatGPT, with a specific command. It was written in the instructions, in the skills and in memory, and Claude still got it wrong now and then.

**How I solved it.** I added a PreToolUse hook that reads every command before it runs: if it's the wrong launch it blocks it, and in the reason it writes the right command, ready to use. Claude reads it and corrects itself. On my side it also logs every launch: out of 774 it stopped 7. For the PC I wrote a general version: the rules live in a JSON file (tool, pattern to look for, exception, "block" or "ask for confirmation", message with the right way). There are three examples: force pushes, recursive deletes, writes to .env files.

**Why this way.** A rule that depends on Claude's memory gets broken sooner or later; a rule in a hook doesn't depend on its memory. It's a reminder, not a barrier: the regular expressions cover the forms I foresaw; to actually block something I use `permissions.deny`. What makes it work, for me, is the message: if it also says how to do it right, Claude doesn't retry the same thing, it corrects itself.

**When you need it.** When you have a rule you've repeated several times that Claude keeps getting wrong: dangerous commands, a specific way to deploy, files not to touch.

**When you DON'T need it.** If Claude already follows your rules. To just block, without explaining, the permissions in settings.json are enough (card [permissions](../sicurezza/sicurezza-permessi-deny-ask.md)). Regular expressions need testing: a badly written one blocks harmless commands.

**How to get it.** Copy `guardia_comandi.py` and `regole_comandi.json` into `~/.claude/hooks/`, the block from `settings-esempio.json` into `~/.claude/settings.json`, then rewrite the rules with your own. Step-by-step instructions: [package guide](../../pacchetti/hook-guardia-comandi/LEGGIMI.md).
