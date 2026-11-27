# What I tried and let go

🇮🇹 [Italiano](../catalogo/scartati.md)

This is the part of the catalog people don't usually talk about: tools and ways of working that I tried, or looked at carefully, and then set aside. They aren't absolute verdicts. They're choices made for the way I work: a single server, two subscriptions (Claude Max and ChatGPT) and a rule of paying as little as possible per use. For each entry I also write when, in my view, it might still be useful to you.

The entries are grouped by area, like the catalog cards. The dates are when I made the decision.

---

## Memory

### Agent memory systems as an alternative to a vault of notes (Mem0, Letta, Graphiti, Cognee, LightRAG, claude-mem and similar)
- **What it promised.** Automatic long-term memory for agents, with fact extraction and smart search.
- **Why I tried it.** My curated notes were getting buried in search results, and I was looking for something smarter.
- **Why I let it go.** Almost all of them need a model to extract facts (slow without a graphics card, or pay-per-use), they create a second source of truth next to mine, and the accuracy numbers are the vendor's own claims. One depended on an archived library; another would have replaced the whole agent engine. The real problem, once I measured it, was simpler: raw session transcripts in the index were drowning out the good notes.
- **What I use instead.** A vault of Markdown notes as the single memory: I took the raw transcripts out of the index and I measure search quality with a fixed set of questions. I'll only look at a more powerful search engine if this stops being enough.
- **When it might suit you.** If you're starting from zero, you don't have an archive of notes and paying per use is fine with you: a ready-made memory saves you time.
- **When.** November 2026.

### Hindsight (shared memory across coding assistants)
- **What it promised.** One memory shared by Claude Code, Codex and Cursor, installable with a single command.
- **Why I tried it.** I liked the idea of my assistants remembering the same things.
- **Why I let it go.** Evaluated, not installed. As an OpenClaw plugin it replaced the built-in memory and, because of a bug that was open at the time, switched off the agents' memory search. It works best inside a git repository, and my working folder isn't one. By default it sends data to its cloud; the self-hosted version, as I found it, started without authentication. And local summarization needed RAM I didn't have free.
- **What I use instead.** An overnight session reviewer that carries corrections into memory, with the vault as the only source.
- **When it might suit you.** If you work in a single git repository with several coding assistants and don't have a memory of your own yet. In that case I'd keep it local (127.0.0.1) and without automatic updates.
- **When.** September 2026.

### OpenClaw Dreaming (memory that tidies itself overnight)
- **What it promised.** Every night the agent goes back over its conversations and saves what matters.
- **Why I tried it.** It was on by default.
- **Why I let it go.** It rarely saved anything, and once it put an old task list into my main assistant's memory.
- **What I use instead.** My own overnight run that gathers facts into the vault, plus a session reviewer.
- **When it might suit you.** If you have few agents and no memory system of your own, as a starting point.
- **When.** October 2026.

### Automatically importing every agent's memory into the vault ("bridge" mode of a wiki plugin)
- **What it promised.** Copying all the agents' memories into the vault, to have them in one place.
- **Why I tried it.** It was switched on together with the wiki plugin.
- **Why I let it go.** It filled the vault with nearly empty copies, mostly overnight reports with no content. Those copies ended up in the agents' search and drowned out the real notes. On top of that, it kicked in even when I just checked the status with a command. I archived the copies (not deleted) and turned the import off.
- **What I use instead.** A bridge that copies only the curated notes.
- **When it might suit you.** With few agents and the dreaming feature off, the noise is much lower.
- **When.** October 2026.

---

## Search

### Self-hosted Firecrawl (reading web pages)
- **What it promised.** A web page turned into clean text, several pages at once too.
- **Why I tried it.** It was my agents' first way of reading the web.
- **Why I let it go.** I switched it off and then removed it completely (container, images, data). Starting from a free lightweight browser was enough for the agents. I didn't write down a more detailed reason.
- **What I use instead.** Lightpanda (a lightweight browser) first, then a full browser, then a paid service only when it's really needed.
- **When it might suit you.** If you read lots of pages in bulk and have RAM to spare for it.
- **When.** October 2026.

### Direct page fetching (web fetch) as the agents' default route
- **What it promised.** The simplest way to read a page.
- **Why I tried it.** It's the agents' built-in tool.
- **Why I let it go.** With direct fetch available, the agents never used the lightweight browser, even though in testing it handled the vast majority of reads. I removed it to see whether a problem shows up: it's an experiment, with the rollback ready.
- **What I use instead.** Lightpanda first.
- **When it might suit you.** For simple pages it works perfectly well. Removing it only makes sense if you want to push the agents toward a method that reads better.
- **When.** November 2026.

### Context7, codebase-memory-mcp, Design DNA, QMD (strong candidates, not installed)
- **What it promised.** Up-to-date library docs, code memory, style taken from reference sites, local search across notes.
- **Why I tried it.** They were the strongest candidates in a tools plan I put together with many agents working in parallel.
- **Why I let it go.** None of them made it onto my server, because the conditions weren't there. For Context7 I had a single case of a library mistake, already caught by my checks. For codebase-memory-mcp the evidence was weak and the savings were only claimed by the vendor. I didn't need Design DNA at the time. QMD is on hold: it goes in only if memory search stays below a threshold I measure.
- **What I use instead.** The tools I have, measured before I change them. For people working on a PC, I still suggest QMD in a separate card in the Search area.
- **When it might suit you.** Context7 if your assistant often gets library APIs wrong; Design DNA if you often rebuild pages borrowing the style from a site.
- **When.** November 2026.

### Automatically fixing who's speaking in call transcripts
- **What it promised.** Transcripts with the right name on every line.
- **Why I tried it.** The call recorder I use often attributes short replies to the person who spoke just before.
- **Why I let it go.** Dead end: the service's API doesn't provide the audio, so there's no way to re-transcribe it with a model that separates voices. An automatic rule like "whoever says their own name" found at most one case per call.
- **What I use instead.** I read transcripts knowing the attribution may be wrong.
- **When it might suit you.** If you have the call audio, re-transcribing with speaker separation solves it.
- **When.** September 2026.

---

## Agents and models

### Pay-per-use models as the base for everything (OpenRouter and a cheap fallback model)
- **What it promised.** Every model with a single key, paying only for what you use, and a cheap model always ready as a fallback when the subscription runs out.
- **Why I tried it.** It was my starting setup: a cheap pay-per-use model as the default and fallback for every agent, and a few scripts moved there for convenience.
- **Why I let it go.** I want a single spending channel: the subscriptions I already pay for. Pay-per-use APIs for everyday work were extra money I didn't see coming. And I found out that small top-ups are expensive: a fixed minimum fee and VAT weigh a lot below 15 dollars.
- **What I use instead.** Claude Max and ChatGPT subscriptions, with rules on which job goes to which model, and fallbacks inside the subscription (smaller models from the same family). Pay-per-use stays only for a few cases: video, bulk analysis with data retention switched off, and as the last resort if the subscriptions don't respond.
- **When it might suit you.** If you don't have subscriptions, work at low and irregular volumes, or need a model the subscriptions don't offer, pay-per-use can cost less than a flat plan. If you top up, larger amounts work out better.
- **When.** October 2026, adjusted in November for video.

### OmniRoute (a router to the free tiers of many providers)
- **What it promised.** Loads of free tokens by stacking the trial plans of many providers, through a single endpoint.
- **Why I tried it.** I wanted to have many days of transcripts read without using up my subscription.
- **Why I let it go.** Providers' free tiers may use your data to train their models: with client data, that's a risk I won't take. It reaches providers through unofficial access, and it goes against my rule of using the subscriptions I pay for. The "free tokens" were just the sum of the trial quotas. When I did switch it on, it sat for weeks with no providers connected and no requests: it only took up memory. I removed it from the server, with a copy archived.
- **What I use instead.** The subscriptions; for large volumes of client data, a pay-per-use service with data retention switched off.
- **When it might suit you.** For personal experiments on public content, with no client data, if you accept the risk to your account and don't have subscriptions.
- **When.** Stopped in October 2026, removed in November 2026.

### A pay-per-use service as the main route for images and video (MuAPI)
- **What it promised.** Lots of image and video models in one place, paying per generation.
- **Why I tried it.** It was my first route for media.
- **Why I let it go.** For images I was already paying for ChatGPT and that subscription sat idle, while the service charged for every image. For video the price was almost the same as on OpenRouter, where I still had budget. It also deletes files after 30 days, so they always have to be copied elsewhere.
- **What I use instead.** Images generated with the ChatGPT subscription; video on OpenRouter with a spending cap per video; the pay-per-use service only for music, sound effects, lipsync, background removal and little else.
- **When it might suit you.** If you don't have a ChatGPT subscription, or need a particular image model, it's a good pay-per-use storefront with a single bill.
- **When.** October 2026.

### My first team of agents with personal names (one agent per type of job, many agents)
- **What it promised.** A specialized agent for every task, each with its own personality and name.
- **Why I tried it.** It was my first team.
- **Why I let it go.** I compared the old team with a new one organized by roles, across about 30 tests: same tasks, three models. With the role-based team my main assistant delegated more and better (research to the one who's good at it, the right reviewer), and it was faster on multi-step jobs. Neither team finished a landing page on its own. On top of that, every delegation costs context and every extra agent needs maintaining. The rule I came away with: a role becomes an agent only if it needs different permissions, a different model, fresh eyes to check the work, or parallel work. Everything else I do with pipelines and skills.
- **What I use instead.** Agents named after their job (PM, Designer, Engineer, Researcher, Archivist…).
- **When it might suit you.** If the agent talks to clients or to your team as a recognizable figure, a personal name helps. The point, for me, is not to multiply them.
- **When.** October 2026.

### A dedicated agent for each collaborator or client
- **What it promised.** Everyone gets their own assistant, with its own memory and permissions.
- **Why I tried it.** It was the most natural route when I gave other people access to the agents.
- **Why I let it go.** Multiplying agents costs RAM and maintenance, and to me permissions don't belong inside the agent but in a table.
- **What I use instead.** Shared role-based agents, separate sessions per channel, an access table and a single memory with search filtered by person.
- **When it might suit you.** If you have two or three people with very different needs who don't share data, one agent each can be simpler to understand.
- **When.** October 2026.

### Alternative agent frameworks (Claude Agent SDK, Mastra, LangGraph, CrewAI, Inngest, Temporal, Archon, n8n as the engine)
- **What it promised.** More structured orchestration, durable workflows, more control.
- **Why I tried it.** I evaluated them when I reorganized agents, skills and pipelines.
- **Why I let it go.** For a micro-agency on a single server, none of them was worth more than what I had. The value is in my files (rules, memory, skills, pipelines in standard formats), not in the engine: that way the engine stays replaceable without rewriting everything.
- **What I use instead.** OpenClaw as the engine (channels, sessions, cron, model calls), without touching its code, plus a small adapter of my own; n8n only for approvals from people.
- **When it might suit you.** With a technical team, several servers, or workflows that need to survive long restarts, a framework like Temporal or LangGraph can be worth the effort.
- **When.** October 2026.

### A fast model that routes requests before the main assistant
- **What it promised.** Faster answers: a small, almost free model decides where each request goes.
- **Why I tried it.** My main assistant was slow to respond.
- **Why I let it go.** The model really was fast and cheap, but the slowness came from the huge context the assistant reloads every turn, not from deciding where to send the request. And the "confidence" a model reports about its choices isn't measured accuracy. A classifier picks between given options: it isn't a memory.
- **What I use instead.** Work on the context (fewer skills loaded, cleaner memory) and a keyword-based router.
- **When it might suit you.** If you have lots of repetitive requests of a few clearly distinct types, a classifier up front can save money, as long as you measure its accuracy on 100-200 real labeled cases.
- **When.** October 2026, confirmed in November.

### Leaving the uncertain cases to the cheap model too
- **What it promised.** Finishing a whole analysis automatically, at almost zero cost.
- **Why I tried it.** In a bulk analysis of many messages, the cheap model had left hundreds of cases marked "unclear".
- **Why I let it go.** With little context, a small model leaves a lot of cases uncertain. Reread by a strong model with more context, the unclear ones dropped from 580 to 26: they were bot replies, automatic summaries, approval threads. A careful read finds patterns the cheap model doesn't see.
- **What I use instead.** Fixed rules first, then the cheap model only on large volumes, then a strong model on what's left; every decision becomes a rule that can be rerun, with the reason written down.
- **When it might suit you.** If the uncertain cases are few or a mistake costs little, leaving them to the cheap model is perfectly fine.
- **When.** October 2026.

### Delegating to the other subscription's models through the most convenient route
- **What it promised.** Sending long jobs to ChatGPT with a single call, straight from the chat with the assistant.
- **Why I tried it.** It was the most convenient way to delegate.
- **Why I let it go.** Launched that way, the agents started without access to the command line and got stuck, or fell back to the default model and used up the other subscription. The result: my ChatGPT limit stayed almost untouched while I was paying for it. Rules written as reminders weren't enough, so I put in a block with no exceptions.
- **What I use instead.** Launching from the command line with the model named explicitly, a hook that stops any other kind of launch, and a check that the session really runs on the subscription plan.
- **When it might suit you.** If your platform gives the same tools to the convenient route too, it can work. I'd still check that the work really ends up on the model and plan you think it does.
- **When.** October 2026.

### Laya (open-source decision model)
- **What it promised.** A model that picks between options or says yes/no with a confidence percentage, free and local.
- **Why I tried it.** I wanted to route support requests automatically without paying for a large model.
- **Why I let it go.** Parked. Without training it guessed worse than chance, it would have needed thousands of labeled examples to be useful, and without a graphics card it took almost a minute per decision.
- **What I use instead.** The paid version of the same kind of model, only to filter a small queue.
- **When it might suit you.** If you already have thousands of labeled examples and a GPU, and want a fully in-house classifier.
- **When.** October 2026.

### A dedicated agent to watch model usage
- **What it promised.** An agent that decides which model to use and keeps tokens under control.
- **Why I tried it.** A single agent was using a large share of the most expensive model's tokens, with huge contexts.
- **Why I let it go.** I followed the advice not to add an agent: a mandatory check and shared rules apply to the whole system, while an extra agent is one more piece to watch over.
- **What I use instead.** Cheap sub-agents for mechanical jobs, automatic warnings when the context grows, rules on which job goes to which model.
- **When it might suit you.** If lots of people launch jobs without shared rules, a central controller can make sense.
- **When.** October 2026.

---

## Automations

### Checking chats and channels on a fixed schedule
- **What it promised.** Simple to build: every so many minutes, look whether something has arrived.
- **Why I tried it.** Some of my checks on chats and channels started out that way.
- **Why I let it go.** I want memory and alerts to update almost in real time, without pointless rounds and calls. Even when the cost of a scheduled check is negligible, my rule stays the same: everything starts from an event.
- **What I use instead.** Triggers: a service that receives events in real time for Slack, a webhook for WhatsApp. The timer stays only as a slow backup, every few hours, for missed events.
- **When it might suit you.** If the service doesn't send events or one update a day is enough for you, a scheduled check is simpler and works fine.
- **When.** November 2026.

### Transcribing voice notes with my own Whisper as the first choice
- **What it promised.** Transcripts under my control, always available.
- **Why I tried it.** It was the route already in place for voice notes and videos.
- **Why I let it go.** Some chat services already do their own transcription: redoing it uses resources for a job the service gives you for free, and two pieces of logic for the same thing is double the work. To be fair, on the voice notes I checked, the service's transcript was ready for only a small share: mine is still needed as a backup.
- **What I use instead.** The service's transcription via API first, Whisper only where it's missing.
- **When it might suit you.** If your service doesn't transcribe, or does it badly in your language, Whisper as the first choice is the right route.
- **When.** November 2026.

### Letting an AI's free judgment decide when a check goes "red"
- **What it promised.** An AI looks at screenshots of a landing page and flags the problems.
- **Why I tried it.** It was the automatic check for my landing pages.
- **Why I let it go.** A single word in the model's free-form sentence was enough to trigger the serious alarm, and the screenshot was taken before the page had finished rendering. I learned something else too: handing the whole fix to an agent as one long task doesn't work; small steps and a check of the files at the end work better.
- **What I use instead.** Deterministic checks for red; the AI's judgment only as a note to read.
- **When it might suit you.** An AI's judgment works fine as a note to read, not as an alarm.
- **When.** September 2026.

### Connecting n8n to Google with the OAuth app left in "Testing"
- **What it promised.** Hooking automations up to Google in a few minutes.
- **Why I tried it.** It's the setup you get by default.
- **Why I let it go.** With the app in "Testing", Google expires the connection every 7 days and the automations stop, often at night. Dead ends: a Desktop-type client gives a redirect error, and rerunning without reconnecting fails at the same point.
- **What I use instead.** A Web-type OAuth client with the consent screen published.
- **When it might suit you.** Only for a test lasting a few days.
- **When.** September 2026.

### Letting the AI work inside my browser to operate business tools
- **What it promised.** Doing any operation even where there's no API, clicking the way I would.
- **Why I tried it.** On some business tools (online courses, CRM, email) the AI had started using the browser.
- **Why I let it go.** It's slow, it uses my session, and I don't want my browser being driven. Often the API was there, or there was already a tool that read the data: I just had to look for it first.
- **What I use instead.** Official APIs or tools that read via API; where the API doesn't reach, the AI prepares the text and steps for me and I do the operation myself.
- **When it might suit you.** If you use a system with no API and you're fine with the agent working in a browser profile separate from yours, it can save you hours.
- **When.** September 2026, reaffirmed in October.

### NocoDB as the operational database (tasks, contacts, projects)
- **What it promised.** A database with a spreadsheet-like interface and ready-made APIs.
- **Why I tried it.** For months it held tasks, contacts, projects and hours.
- **Why I let it go.** I measured it: in 30 days, no access from the browser, everything went through scripts, and its APIs were slow (over a second and a half to read all the tasks, against about a tenth of a second reading the database directly). Nobody was using the interface that justified it.
- **What I use instead.** Postgres directly, with a small adapter that speaks the same format as the old APIs: the programs only changed their call function. NocoDB is switched off, not deleted.
- **When it might suit you.** If you or your team really open the data by hand every day and you don't have a developer, it's a good way to get a database with a simple interface.
- **When.** November 2026.

---

## Security

### Tools that hold my subscription tokens or my account cookies
- **What it promised.** Using the Claude subscription from other programs, cross-reviews between models, access to social networks without an API (examples I evaluated: Claudex, claudexor, Agent Reach).
- **Why I tried it.** I looked at them when I added ChatGPT alongside Claude and was looking for ways to make them work together.
- **Why I let it go.** They hold the subscription's access tokens or the accounts' cookies: if something goes wrong I risk the account. One only did cross-review and the security scanner gave it the maximum risk score. Others send sessions outside.
- **What I use instead.** The official ChatGPT login in the tools that support it, and a security check (SkillSpector) before installing anything from outside.
- **When it might suit you.** On test accounts, with no real data and no subscriptions you care about, to experiment.
- **When.** October and November 2026.

### Pay-per-use services or ones that send data outside (cloud code reviewers, paid scraping and search, cloud agents)
- **What it promised.** Code review, web search, scraping and ready-made automations, without building anything (examples I evaluated: Strix, PR-Agent, CodeRabbit, Exa, Firecrawl cloud, Browserbase, Manus).
- **Why I tried it.** They showed up in the rankings and tips I collect.
- **Why I let it go.** They cost per use, or the data leaves my server. One of them also published its ports with Docker in a way that bypasses the firewall. I'd only reopen them with an explicit spending decision.
- **What I use instead.** Reviews done by a reviewer agent on the subscriptions, and web-reading tools I already have installed.
- **When it might suit you.** If you don't have your own server or subscriptions and your data isn't sensitive, they give you results right away, paying a little per use.
- **When.** November 2026.

### Plugins with administrator permissions to let the AI work on WordPress
- **What it promised.** Full AI access to the sites, code included.
- **Why I tried it.** I found it already installed on some WordPress sites.
- **Why I let it go.** With administrator permissions, whoever steals the key from the server can control every site.
- **What I use instead.** A dedicated plugin that only touches content, with one key per site that can be revoked.
- **When it might suit you.** For bugs and custom work done by a developer, not for an AI working on its own.
- **When.** November 2026.

### Blocking agents' tools with a "deny" list in the engine's configuration
- **What it promised.** Taking dangerous tools away from an agent with one line of configuration.
- **Why I tried it.** It's the documented way to restrict an agent.
- **Why I let it go.** Dead end, in my case: on agents running through the Claude command line on the subscription, that list didn't touch the native tools (shell, file reading, web). Another rule decided instead: without a sandbox everything allowed, with the sandbox everything denied.
- **What I use instead.** The sandbox and the agent engine's execution rules.
- **When it might suit you.** On agents that use models via API the list works. Either way, I'd test the block with a fake case before trusting it.
- **When.** October 2026.

### Trusting a "clean" scan without looking at what it read
- **What it promised.** The scanner says "no keys found": all good.
- **Why I tried it.** It was the security check on my repositories.
- **Why I let it go.** The scan had read zero commits: git refused the repositories owned by another user and the error was hidden. The "clean" result was false.
- **What I use instead.** I always check how many files or commits were read, and I don't throw away error messages.
- **When it might suit you.** It applies to any scanner: I verify an empty result before believing it.
- **When.** October 2026.

### find-skills and context-mode
- **What it promised.** Finding and installing skills on the fly; clever context management.
- **Why I tried it.** They showed up in the content I save to evaluate later.
- **Why I let it go.** find-skills installs skills with automatic confirmation, skipping the security check I run on everything that comes from outside. context-mode had an unclear license.
- **What I use instead.** A command of my own that only searches, without installing, then a security check and a read-through before every install.
- **When it might suit you.** find-skills on a test machine, with no sensitive data.
- **When.** October 2026.

### rtk (a command compressor to save tokens)
- **What it promised.** Fewer tokens used, by rewriting commands and compressing their output.
- **Why I tried it.** I was trying to cut usage.
- **Why I let it go.** Not installed: it rewrites every command and compresses the output, while I need the exact errors. It also changes Claude Code's settings, and the security scanner gave it the maximum risk score.
- **What I use instead.** Cheap sub-agents for mechanical jobs and a warning when the context grows too much.
- **When it might suit you.** If you use pay-per-use APIs and count every token, after a controlled test.
- **When.** October 2026.

---

## Channels

### The agent engine's built-in WhatsApp channel
- **What it promised.** Talking to my main assistant from WhatsApp, through the agent engine (OpenClaw).
- **Why I tried it.** It was how I talked to the assistant from my phone.
- **Why I let it go.** I preferred to talk on WhatsApp directly with Claude Code, which handles everything else. My main assistant stayed on the other channels.
- **What I use instead.** A small service of my own, built on OpenWA, connected to Claude Code, that only answers my number.
- **When it might suit you.** If you only use OpenClaw and not Claude Code, the built-in channel is the simplest route.
- **When.** October 2026.

### Open WebUI or a desktop app to talk to the assistant
- **What it promised.** A chat on my computer connected to the whole system.
- **Why I tried it.** I asked myself whether I needed an interface of my own on the PC.
- **Why I let it go.** Open WebUI can't use Claude Code without a bridge that reuses the login, and the terms of service don't allow that. With API keys I'd pay per use. Connected to the agents, it would have duplicated the assistant page I already have.
- **What I use instead.** Claude Code, the assistant page on my dashboard, WhatsApp.
- **When it might suit you.** If you use local models or API keys and want a single chat for your team.
- **When.** November 2026.

### A bot that joins Google Meet calls on its own
- **What it promised.** The assistant joins the call, records it, reads and writes in the chat.
- **Why I tried it.** Almost all my calls are on Meet and I didn't want to pay for an hourly service.
- **Why I let it go.** Google blocks the automated browser ("You can't join this video call"), and it doesn't depend on the IP address or on a fake webcam. I didn't want to get around the anti-bot check.
- **What I use instead.** A ready-made call recorder (Fathom).
- **When it might suit you.** If a service like Recall is fine for you (the bot is visible in the call), or a recording made from a participant's browser.
- **When.** November 2026.

### Remote access to team PCs with Tailscale
- **What it promised.** Getting into PCs remotely to set them up and run jobs on them.
- **Why I tried it.** I wanted to set up a laptop from a distance and connect a coding model on my PC.
- **Why I let it go.** For the laptop I'd have needed a paid plan for tags, and the PC had ended up on the wrong network. For my own PC I didn't need it: I already had another way to reach it.
- **What I use instead.** Claude Code installed on the laptop with a written brief.
- **When it might suit you.** If you manage many team PCs remotely, on an ongoing basis.
- **When.** November 2026.

---

## Skills and tools from outside

### A "condensed" design skill taking the best of four
- **What it promised.** Less text for the agent to read, design rules concentrated in a single file.
- **Why I tried it.** I wanted the agents to really use the skills, and the idea was to merge four into one of my own.
- **Why I let it go.** A/B test on a real landing page: the condensed version came out flat; the original skill used in full (scripts, guides, separate reviewer) gave it a lot more character. Condensing strips out exactly the details that make the difference.
- **What I use instead.** The design skills in full, all named in the briefs, plus a visual reference.
- **When it might suit you.** If your agent has little context or you make very simple pages, a short version may be enough: I'd test it against the original before deciding.
- **When.** October 2026.

### Mandatory automatic checks on every page draft (Lighthouse, axe, phone screenshots)
- **What it promised.** Page quality guaranteed by automatic scores.
- **Why I tried it.** They'd been suggested to me as a fix for flaws in deliveries.
- **Why I let it go.** They were already in the instructions of the agent that builds the pages, and they don't see the real flaws, which are matters of judgment (spacing, hierarchy, copy). And checking drafts on a phone goes against my order of work: first I approve the design on desktop, then the phone version gets done.
- **What I use instead.** A visual review by a separate agent and, as an experiment, a list of recurring flaws with a script that looks for them.
- **When it might suit you.** On sites that are already approved and live, for accessibility and speed, they're useful.
- **When.** November 2026.

### Using the copy and typographic style Stitch generates
- **What it promised.** Ready-made page sections, with layout and copy.
- **Why I tried it.** I use Stitch to explore section layouts.
- **Why I let it go.** I keep the layout (backgrounds, cards, visual hierarchy). I discard the copy and the numbers, because it makes them up, and its wide uppercase type, which I don't like: my font stays.
- **What I use instead.** Stitch only as a layout prompt, then adapted to my style, my font and my copy.
- **When it might suit you.** For a quick throwaway prototype, its copy works fine as a placeholder.
- **When.** November 2026.

### Slides for one-to-one training calls
- **What it promised.** A tidy presentation to explain a process.
- **Why I tried it.** While preparing a training call I wondered whether I needed them.
- **Why I let it go.** In a one-to-one call the goal is for the other person to learn to do it on their own; with slides, I'm the one talking. To lead a conversation I prefer a script with the sentences already written.
- **What I use instead.** A "one sentence at a time" page with a Next button, questions written out in full and backup lines always visible.
- **When it might suit you.** For a real presentation to several people, slides are still the right choice.
- **When.** November 2026.

### Suggesting a client a different tool from mine without a verified reason
- **What it promised.** A lighter login system (Authelia instead of Authentik, in the case I saw).
- **Why I tried it.** The AI had suggested it for a server without looking at its setup.
- **Why I let it go.** There was no good reason: the server had plenty of memory. An unjustified difference undermines trust in the proposal. What matters to me is that the tool is as functional and secure as possible, not which one it is.
- **What I use instead.** The same tool I use, unless there's a reason verified on the server and written into the proposal.
- **When it might suit you.** On a small server with little memory, a lighter login system can really be the right choice.
- **When.** Autumn 2026.

### Figma's official MCP inside OpenClaw agents
- **What it promised.** Agents read and write Figma files.
- **Why I tried it.** I wanted to review landing pages on Figma together with the agent that builds the pages.
- **Why I let it go.** Figma only accepts clients from its own catalog; OpenClaw shows up as a new client and gets rejected. The route through the plugin in a headless browser is blocked too, and changing the browser's identity would mean getting around a check: I didn't do it.
- **What I use instead.** Figma from an accepted client (Claude Code or Codex).
- **When it might suit you.** If you use Claude Code or Codex directly, the official MCP works.
- **When.** October 2026.

### mimik (click-through guides recorded automatically)
- **What it promised.** It records your clicks in the browser and produces a step-by-step guide with screenshots.
- **Why I tried it.** I wanted to make guides for clients faster. I tried it myself.
- **Why I let it go.** It works, but the text comes out in English and rough, the blurring only covers emails, phone numbers and cards, and it doesn't record Chrome's internal pages. The security scanner said "don't install", with many findings still to review, and I didn't have the number of guides that would have justified it. It isn't closed for good: it stays on the list for when I need a guide on a system I can't reach any other way.
- **What I use instead.** Written guides with maps and screenshots.
- **When it might suit you.** If you often make guides in English for simple web tools, with a separate browser profile and no sensitive data on screen.
- **When.** November 2026.

### Tools and offers with inflated promises (free GPUs, student plans, miracle prompts, fake extensions)
- **What it promised.** Free computing power, free premium models, guaranteed results with one prompt.
- **Why I tried it.** They come from reels and tips I save to evaluate.
- **Why I let it go.** When I checked, they were inflated, fake, or a way in to sell something else. One example: a supposed "powerful extension for Claude Code" was actually a chat for getting around the models' rules.
- **What I use instead.** A list of bookmarks to browse (public collections of APIs, MCP servers and apps), without installing anything.
- **When it might suit you.** Rarely. If one makes you curious, I'd look at who publishes it and what they sell afterwards, and read the code before trusting it.
- **When.** October and November 2026.

### Tools that redo what I already have (duplicates and stalled projects)
- **What it promised.** Alternative coding agents, workflow builders, scrapers, video downloaders, task management, ready-made agent teams (examples: OpenHands, Aider, langflow, open-flow, Scrapling, cobalt, TaskView, agency-agents).
- **Why I tried it.** I evaluated them during my tool-research rounds.
- **Why I let it go.** They redid things I already have: workflows with n8n, video downloads with yt-dlp, the task board. One turned out to be archived, so no longer maintained. Another browser tool only worked with Claude Code, and agents on other models couldn't see it. From agency-agents I only took a few ideas for roles, without installing it.
- **What I use instead.** The tools I already have installed, re-evaluated when a real job calls for them.
- **When it might suit you.** If you don't have anything equivalent yet, some of them are great starting points (langflow, for example, if you don't use n8n).
- **When.** October and November 2026.
