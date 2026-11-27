---
slug: sicurezza-utente-separato-agenti
title: "Agents work as a separate user with few permissions"
area: sicurezza
where_it_runs: server
level: advanced
cost: "€0. A few hours of setup on a Linux server, plus the discipline not to bypass it."
package: "none: idea only"
status: "I use it"
---

# Agents work as a separate user with few permissions

**The problem.** On the server there are AI agents running (with OpenClaw, in my case) that receive messages from outside: chats, emails, web pages. A message written on purpose could convince an agent to do something it shouldn't. If the agent had administrator permissions, the damage would have no limit.

**How I solved it.** The agents run as their own system user, not an administrator. They can run as administrator only a few specific commands, written one by one in the sudo list (for example sending me an alert). I work with Claude Code as administrator, but I never run files that live in the agents' folders, because an agent could have changed them. I don't load their secrets file as a script. When I need to write into their files I use a dedicated little program that doesn't follow links they created.

**Why this way.** If an agent gets tricked, the damage stays inside its folder. It's the same principle as Claude Code's permissions: everyone has only what they need.

**When you need it.** When you have agents running by themselves on a server and reading text written by others.

**When you DON'T need it.** On a PC where you're the only one using Claude Code a separate user doesn't seem useful to me: permissions (card [Permissions](sicurezza-permessi-deny-ask.md)) and keeping secrets outside work folders are enough. It's an idea that only makes sense with a server.

**How to get it.** There's no package: it needs a server. The idea in three steps: create a Linux user dedicated to the agents, don't put it in the sudo group, and if it needs an administrator action grant in `/etc/sudoers` only that precise command, with the full path.
