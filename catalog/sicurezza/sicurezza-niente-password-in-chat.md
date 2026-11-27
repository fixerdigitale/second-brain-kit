---
slug: sicurezza-niente-password-in-chat
title: "No passwords in chat or in notes"
area: sicurezza
where_it_runs: PC
level: basic
cost: "€0. 5 minutes."
package: "pacchetti/sicurezza-niente-password-in-chat/"
status: "I use it"
---

# No passwords in chat or in notes

**The problem.** Chats, emails and client messages sometimes contain credentials they wrote themselves. By saving notes into the vault I risked carrying them along. And even just checking whether a password was there made it appear in the session logs.

**How I solved it.** Fixed rule: no password, PIN or token in clear text, neither in answers nor in notes, not even a part of one. Not even masked with a regex: if the regex is wrong, the rest of the value stays in the logs. To know whether a secret is there, Claude counts lines or gives the line number, never the text. If I paste a password by mistake, Claude tells me once with the remedy (change it) and then doesn't repeat it. For the kit I also wrote a small check that flags suspicious files and lines in the vault without ever showing the value.

**Why this way.** Everything that goes through chat stays in session logs, and logs end up in backups and sometimes in memory. For me the safest place for a secret is a single one, outside the vault.

**When you need it.** If notes from chats, emails or calls with other people end up in the vault, or if the vault goes to GitHub, even a private repo.

**When you DON'T need it.** If the vault contains only your own work notes and you never copy other people's texts into it, the rule is enough: the script adds little. The script only finds the common forms, not a password written alone on a line.

**How to get it.** Paste `regola-claude-md.md` into your `CLAUDE.md`; run `cerca_segreti.py` on the vault before a push or when you import notes from others. Instructions: [package guide](../../pacchetti/sicurezza-niente-password-in-chat/LEGGIMI.md).
