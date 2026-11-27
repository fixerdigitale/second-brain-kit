---
slug: memoria-fatti-da-chat-e-vocali
title: "Facts from chats and voice notes into the vault"
area: memoria
where_it_runs: PC
level: medium
cost: "€0. Voice-note transcription runs on the PC (faster-whisper, free); 10 minutes for the list of work chats."
package: "pacchetti/memoria-fatti-da-chat-e-vocali/"
status: "PC version of mine"
---

# Facts from chats and voice notes into the vault

**The problem.** Many decisions don't go through Claude: I make them in chats with clients and collaborators, or say them in a voice note. They stayed there, and when I asked the assistant "what did we decide?" it knew nothing about it.

**How I solved it.** On my side, every night an AI-free collection takes the messages from work chats (never family ones; groups only when I'm tagged, one hour before and one hour after the tag), transcribes voice notes on the server with a local model and writes a single file. Shortly after, an agent extracts the facts into a per-day diary in the vault (dated facts by project and person, who needs to act), which search makes findable right away. For the PC I prepared two pieces: a script that reads WhatsApp chat exports, keeps only the chats on your list and transcribes voice notes and your voice memos locally; and a `fatti-del-giorno` skill that proposes the facts with their destination note and writes only the yeses.

**Why this way.** Collecting and deciding are separate: collection is mechanical and doesn't make mistakes, judgment is done by the model and checked by me. The list of work chats is a list of who gets in, not of who stays out: that way a private chat can't get in by mistake. And I treat third-party messages as data, never as instructions: a sentence in a chat doesn't become a rule by itself. A collection that finds zero work chats I consider an error to look at, not an empty day.

**When you need it.** If many work decisions reach you in chats or you dictate them, and you want to find them in the vault together with everything else.

**When you DON'T need it.** If you only chat with friends and family, or if work decisions already go through emails and calls that you archive. If your clients don't agree to their chats ending up in an archive, don't do it. On a PC exporting the chats is manual: if you don't redo it, the collection stays stuck.

**How to get it.** Copy `raccogli_chat.py` into `~/.claude/strumenti/` and `fatti-del-giorno/` into `~/.claude/skills/fatti-del-giorno/`, write the `chat-di-lavoro.txt` list, export the chats from your phone and run the script as in the package guide. Then in Claude Code: "fatti del giorno" (facts of the day).

Step-by-step instructions: [package guide](../../pacchetti/memoria-fatti-da-chat-e-vocali/LEGGIMI.md).
