🇮🇹 [Italiano](README.it.md)

# Second Brain Kit

**My second brain with Claude Code: what I use, what I dropped, and an onboarding that looks at your setup before suggesting anything.**

[![License: MIT](https://img.shields.io/badge/license-MIT-informational)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0.0-informational)](CHANGELOG.md)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-informational)](docs/INSTALL.md)
[![Language](https://img.shields.io/badge/language-English%20%7C%20italiano-informational)](README.it.md)

[Italiano](README.it.md) · [Install](docs/INSTALL.md) · [Catalog](catalog/README.md) · [What I dropped](catalog/discarded.md)

![The second brain loop: capture, organize, find, use, learn, around a memory made of notes](docs/loop.svg)

## Why I'm sharing this

I work with Claude Code every day, together with a small group of agents. I built myself a setup so I don't have to re-explain everything at every session, and a few people asked me how it works.
This is my way of doing it, limits included: it isn't a method and it isn't the only right one. Take what helps you and leave the rest.

## Get started in 2 minutes

1. Download the repo as a zip (**Code → Download ZIP**) or clone it:
   ```bash
   git clone https://github.com/fixerdigitale/second-brain-kit.git
   ```
2. Open the folder in Claude Code: from the terminal with `cd second-brain-kit && claude`, or from VS Code or the desktop app.
3. Type **"start the onboarding"**, or `/second-brain:onboarding` if you installed the plugin.

The other ways in (plugin from the marketplace, catalog only, Mac, Windows, Linux) are in [docs/INSTALL.md](docs/INSTALL.md).

## What's inside

| Part | What it does | Where |
|---|---|---|
| **Onboarding** | First it looks at what you already have (names and counts only, with your permission), gives you a first concrete result in about 15 minutes, then a map of your setup and a plan of at most 3 steps. After 14 days it takes the same measurements again. | [plugin/second-brain/](plugin/second-brain/) |
| **Catalog** | 88 cards on what I use, in 8 areas: memory, search, learning, automations, agents, channels, skills, security. Each card covers the problem, how I solved it, why I did it that way, and when you **don't** need it. | [catalog/](catalog/README.md) |
| **Discarded** | 45 tools and ideas I tried or evaluated and then set aside, with the reason and when they might still be useful to you. | [catalog/discarded.md](catalog/discarded.md) |
| **Packages** | Ready-to-copy files for 64 cards: skills, hooks, scripts, note templates. Each one has a LEGGIMI (read-me) explaining what it does, where it goes and how to remove it. | [pacchetti/](pacchetti/) |

The cards and the package read-mes are in Italian for now. Claude Code reads them fine, and you can ask it to explain or translate any of them as you go.

## Who it's for

- **If you're starting from zero.** The onboarding avoids jargon, asks one question at a time and runs the commands for you. The first result is a real task you do often, done better.
- **If you already have some files and a CLAUDE.md.** It shows you where your setup is leaking (memory, corrections, backups) and suggests the smallest steps to close the gaps.
- **If you already have a vault, your own skills, hooks and agents.** It goes through your setup area by area and talks to you as a peer. Your system is probably better than mine in places: for you the catalog works more as a comparison than as a list of things to install.

It doesn't ask for your level: it reads it from your files, area by area. You can be advanced on memory and at zero on backups, and that's normal.

## My day with AI

How these pieces work together, from the morning brief to the overnight work: [My day with AI](catalogo/canali/canali-giornata-con-ai.md) (in Italian).
I run a lot of this on a server. All of it can also run on a PC: the difference is that a PC isn't always on, and a server is. Each card says where it runs.

## What I dropped

People usually only talk about what works. I also kept a list of what I tried and let go: memory systems for agents, search engines, automation platforms, channels. These aren't verdicts: they're choices made for the way I work. [Read what I dropped](catalog/discarded.md).

## Safety

The onboarding works read-only until you say yes. In particular, it never does any of these things on its own:

- read outside the folders you've allowed, or open your browser, email or chats;
- print, copy or store in memory the values of passwords, keys and tokens;
- write, move, rename or delete without a yes for each item (it makes a dated copy first, and instead of deleting it moves things to `_da-cancellare/`, "to delete");
- push, create repositories or share anything;
- install skills, MCP servers or plugins from outside without a check and a yes;
- turn on hooks, broad permissions or auto mode without explaining what they do;
- send anything outside: no telemetry, the map and the plan stay on your computer.

Never paste passwords or keys into the chat, not even here.

## Honest limits

- It's one person's setup, shaped by my work (a small digital studio) and my subscriptions (Claude Max and ChatGPT). Some choices only make sense there.
- Cards marked "server" describe how I do it: on a PC they need adapting, and some have no package.
- The PC versions are adaptations of my originals: I've used them for much less time.
- Claude Code changes often. Some commands or settings may already be different by the time you read this.
- Everything was written in Italian first; the English version is a translation.
- This isn't professional advice: on backups, permissions and other people's data, you decide, with your own judgment.

## Contributing

What I'd most like to hear is what didn't work for you: open an issue with your operating system, your Claude Code version and what happened.
If you have a better way to do something that's in the catalog, a pull request with a new card or a fix is welcome. Keep the same structure as the other cards, including the "Quando non ti serve" ("When you don't need it") section, and no names of people, clients or real data.

## License

[MIT](LICENSE) © 2026 Daniel Martines / Fixer Digitale. Use it, change it, pass it on: if it helped you, I'd be glad to hear about it.
