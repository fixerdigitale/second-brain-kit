---
slug: canali-whatsapp-assistente
title: "WhatsApp with my assistant, voice notes included"
area: canali
where_it_runs: server
level: advanced
cost: "€0 extra for the model; free transcription; a second SIM and the always-on server (about €15/month, shared)"
package: "none: idea only"
status: "I use it"
---

# WhatsApp with my assistant, voice notes included

**The problem.** Ideas and requests come to me when I'm not at the PC: in the car, between calls. Opening the computer to say "remind me to…" or "send the report to…" meant not doing it.

**How I solved it.** My main assistant has its own WhatsApp number. I write to it or send it a voice note as I would to a person. A service on the server receives the message, puts 👀 right away, waits 6 seconds of silence to join split messages, transcribes voice notes (Whisper on the server, free; a paid service only as a backup) and passes everything to Claude Code, which works with my same memory. Replies arrive in pieces while it works; at the end 👀 becomes ✅ (or ❌). Each message carries its time, so if I write three in a row it answers all of them starting from the oldest. If a job takes more than a couple of minutes, it launches it in the background and the result reaches me by itself. Automatic notices (brief, failures, pending questions) go out from the same number and the assistant sees them: if I just reply "ok", it knows which notice I mean. Before each turn it checks plan usage: if it's at the limit it tells me instead of going silent. It writes to other numbers only if I've asked it explicitly.

**Why this way.** The channel I already use all day is WhatsApp: no new app to open. A separate number keeps my personal messages distinct from those to the assistant, and a single channel for notices means a "yes" from me always has a context.

**When you need it.** If you give many instructions on the move, think better by talking than by writing, or want notices where you already look.

**When you DON'T need it.** If you almost always work at the PC, or the Claude app on your phone is enough, which already has dictation. And keep in mind that connecting WhatsApp to a program goes through unofficial tools: WhatsApp can ban the number, which is why I use a dedicated number and not my own.

**How to get it.** No package: it's just the idea, because the bridge has to answer even with the PC off. Without a server: the Claude app on the phone, with the official connectors; if your version of Claude Code has remote control, you continue from the phone a session open on the PC while it's on. If you really want a chat, Telegram has an official bot API and you don't risk a ban, but you still need something always on.
