---
slug: skill-sicurezza-codice
title: "Security checks on code and sites"
area: skill
where_it_runs: PC
level: advanced
cost: "€0; a full review of a medium project uses quite a lot of context"
package: "none: third-party skill from the source"
status: "I use it"
---

# Security checks on code and sites

**The problem.** When I have the AI build tools with access, keys or other people's data, I need a second look that searches for holes, not just bugs.

**How I solved it.** I have two third-party skills. security-audit (by Cloudflare) guides a code review by attack class: authentication, data isolation, supply chain, AI and prompts, with validators for the report. security-scanner is a kit of commands for port and vulnerability scans with nmap and nuclei, only on authorized targets.

**Why this way.** I use security-audit on sensitive code: it reasons by attack class instead of producing a generic list. security-scanner I keep as a command reminder: I haven't installed nmap and nuclei, so in practice I don't use it.

**When you need it.** Before putting online a tool with login, keys or third-party data; when someone asks you to check their site (with written authorization).

**When you DON'T need it.** For brochure sites with no forms or logins. Port scans must never be run on systems that aren't yours or that you have no authorization for.

**How to get it.** Third-party skills, from the source: security-audit from https://github.com/cloudflare/security-audit-skill; security-scanner from the ClawHub registry (https://clawhub.ai/dmx64/security-scanner), which is open: read it first. nmap and nuclei are installed separately.
