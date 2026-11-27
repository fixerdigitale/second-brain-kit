---
slug: canali-connettore-telefono
title: "My system inside claude.ai, from the phone"
area: canali
where_it_runs: server
level: advanced
cost: "€0 extra for the model; an always-on server (about €15/month, shared); days of work on security"
package: "none: idea only"
status: "I use it"
---

# My system inside claude.ai, from the phone

**The problem.** In claude.ai on the phone Claude knew nothing about me: not my notes, not the morning's work sessions, not what was running on the server.

**How I solved it.** I have a personal MCP connector (an address I add in claude.ai as a connector) with OAuth login and password. Through it Claude on the phone reads my Claude Code sessions and memory, looks at server files and logs read-only with secrets masked, searches my main assistant's memory and, with a dedicated tool, has Claude Code work on the server as if I were at the PC. Those sessions stay separate from the VS Code ones, but they're saved and I can find them.

**Why this way.** The phone becomes a real terminal of my system, not a chat that starts from zero. I use it to check where a job stands or to start something small without opening the PC.

**When you need it.** If your vault and your work live on an always-on machine and you want to reach them from claude.ai.

**When you DON'T need it.** If the vault is on your PC and on Drive: the official connectors are enough and you don't have to maintain anything. A home-made connector is an entrance into your system from the internet: if you're not ready to look after its security (login, attempt limits, read-only), don't do it.

**How to get it.** No package: it's just the idea, it needs a server. On a PC you get close like this: 1) in claude.ai turn on the official connectors (Google Drive, Gmail, Calendar): if the vault is synced to Drive, Claude reads it from the phone even with the PC off; 2) in Claude Desktop add an MCP server for local files pointed at the vault folder (only while the PC is on); 3) if your version of Claude Code has remote control, follow a session open on the PC from your phone.
