---
slug: skill-media
title: "Images, video and voice: what I use and what it costs"
area: skill
where_it_runs: PC
level: medium
cost: "images €0 extra with the ChatGPT subscription; video and voice pay-per-use (about $0.15-0.45 per 5 seconds of video as of October 2026)"
package: "pacchetti/skill-media/"
status: "PC version of mine"
---

# Images, video and voice: what I use and what it costs

**The problem.** For images, video and audio there were dozens of services, each with its own credits and its own key. I was paying per image even though I had a ChatGPT subscription sitting idle.

**How I solved it.** I set a fixed order. Images (new or edited from a photo) I make with OpenAI's Codex, that is with the ChatGPT subscription: in my system it goes through a bridge on the server that stops by itself when weekly usage passes 70%, without silently switching to a paid service. Videos from text or from an image I make with OpenRouter's video API; those written as code (animated titles, motion graphics) with HyperFrames, which is free. Music, effects, upscaling, background removal and lipsync go through MuAPI. For transcription I use Whisper, free; for voice-over ElevenLabs or Fish Audio, which let you control emotion. For videos I also have two skills of my own (directing a video made in code, and an illustrated video starting from a voice note) that I don't put in the kit, because they're tied to my way of working.

**Why this way.** The subscription I already pay for covers what I do most often, images. The rest I pay for only when I need it. For voice I learned that perfect pronunciation isn't enough: in a video what matters is the delivery, so I choose engines where you mark the emotion in the text.

**When you need it.** If you often produce images for pages, posts or presentations and already have a ChatGPT plan; if now and then you need a short video or a voice.

**When you DON'T need it.** If you need few images a month, the ChatGPT app does the same without scripts. If the material belongs to clients with confidential data, first check each service's data terms: not all of them delete what you upload. And don't generate on behalf of others with your personal subscription.

**How to get it.** The package has `immagine.py` (Codex from the command line, tested only with a fake Codex) and the table of services with the public sources: Codex https://github.com/openai/codex, OpenRouter https://openrouter.ai, HyperFrames https://github.com/heygen-com/hyperframes, MuAPI https://muapi.ai/docs, ElevenLabs skills https://github.com/elevenlabs/skills, Whisper https://github.com/openai/whisper. Step-by-step instructions: [package guide](../../pacchetti/skill-media/LEGGIMI.md).
