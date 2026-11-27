---
slug: automazioni-pulizia-sessioni-ferme
title: "Automatic cleanup of idle sessions"
area: automazioni
where_it_runs: PC on
level: basic
cost: "€0. 10 minutes."
package: "pacchetti/automazioni-pulizia-sessioni-ferme/"
status: "PC version of mine"
---

# Automatic cleanup of idle sessions

**The problem.** Every Claude Code chat left open and forgotten keeps a process running with its MCP servers: for me about 500 MB each between memory and swap. With ten chats open the computer slowed down, and I never closed them by hand.

**How I solved it.** An automatic run closes the process of sessions that have been neither working nor waiting for anything for 30 minutes. It doesn't close one if the conversation changed recently, if it has a command running, if it's waiting for a tool's answer or for my permission, or if I put it on the "keep" list. The conversation stays saved on disk and you resume it by reopening the chat or with `claude --resume`. On my side it runs on a server every 5 minutes and also recognizes background jobs; the PC version is simpler, and when in doubt it leaves things alone.

**Why this way.** Open chats cost nothing until I close them, and I don't close them. Having them close themselves, only when they're really idle, gives me the memory back without losing anything.

**When you need it.** If you keep many Claude Code sessions open (app or terminals) and your computer is short on memory.

**When you DON'T need it.** If you open one session at a time and close it when you're done. In a terminal, closing the process means `claude` exits: if you type into a terminal left idle, you first have to relaunch it with `--resume`.

**How to get it.** Copy `ferma_sessioni.py` into `~/.claude/strumenti/`. First run it with no arguments (it shows what it would do), then schedule `ferma_sessioni.py ferma` every 10-15 minutes. On Windows you need `pip install psutil`. Step-by-step instructions: [package guide](../../pacchetti/automazioni-pulizia-sessioni-ferme/LEGGIMI.md).
