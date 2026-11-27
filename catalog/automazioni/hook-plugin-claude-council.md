---
slug: hook-plugin-claude-council
title: "claude-council plugin: a second opinion from other models"
area: automazioni
where_it_runs: PC
level: medium
cost: "€0 extra with the CLIs of subscriptions you already pay for; with API keys, the usage cost of each question."
package: "none: third-party plugin from the source"
status: "I use it"
---

# claude-council plugin: a second opinion from other models

**The problem.** On important technical choices (architecture, a bug that won't show itself, security) a single model can be confidently wrong, and I don't always have the expertise to notice.

**How I solved it.** I installed claude-council, a public third-party plugin: with one command it sends the same question to several models (for example Codex with the ChatGPT subscription, or Gemini) and shows the answers side by side, with a summary of where they agree and where they don't.

**Why this way.** When two different models reach the same answer I trust it more; when they diverge, I know where to look. Using the CLIs of subscriptions I already pay for, it costs me nothing extra.

**When you need it.** Before technical decisions that are hard to undo, or when a problem has resisted for hours.

**When you DON'T need it.** For everyday work: it multiplies time and usage. If you don't have another subscription or CLI (Codex, Gemini…), you need pay-per-use API keys.

**How to get it.** From the original source: https://github.com/hex/claude-council (in Claude Code: `/plugin marketplace add hex/claude-marketplace`, then `/plugin install claude-council`). Before installing it, read the README and the security section, and run it through a check like the one in the [tool finder](../skill/skill-cerca-strumento.md) card.
