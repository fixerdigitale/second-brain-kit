---
slug: sicurezza-permessi-deny-ask
title: "Permissions: what passes by itself, what never does, and an \"ask\" level to try"
area: sicurezza
where_it_runs: PC
level: basic
cost: "€0. 10 minutes."
package: "pacchetti/sicurezza-permessi-deny-ask/"
status: "PC version of mine"
---

# Permissions: what passes by itself, what never does, and an \"ask\" level to try

**The problem.** Claude asked me for permission even for an ls, and by dint of clicking "yes" I'd have approved the wrong thing too. Conversely, there were actions I never wanted it to take, not even on a distracted request of mine: reading the keys file, the SSH keys.

**How I solved it.** In Claude Code's settings.json I use two lists. Allow: read-only commands (ls, grep, git status, log) pass without asking. Deny: reading the secrets file, the credentials folder and the SSH keys, always blocked. On my side there are only these two. In the PC template I added a third list, ask, for actions that are hard to undo (push, deletions, installs, downloads): it's a new proposal, I don't use it this way, and I mark it as such.

**Why this way.** Fewer useless prompts means more attention on the real ones. Deny is a safety net that doesn't depend on how tired I am that day.

**When you need it.** As soon as you use Claude Code on folders with real data, key files or repos connected to GitHub.

**When you DON'T need it.** If you work in the mode that asks for everything and clicking doesn't bother you, the allow list is of little use; deny is still worth it in my view. Deny stops Claude's tools, not every possible shell command: a `cat` from the shell can read a file that deny blocks for the read tool. Secrets are better kept outside work folders. The ask list you can also remove, if normal mode is enough for you.

**How to get it.** Copy the `permissions` block from `settings.json` into `~/.claude/settings.json` (all projects) or into `<your-project>/.claude/settings.json`, add your secrets folder to deny if you have one, and check with `/permissions`. Instructions: [package guide](../../pacchetti/sicurezza-permessi-deny-ask/LEGGIMI.md).
