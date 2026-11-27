---
slug: sicurezza-segreti-file-unico
title: "Keys in a single file, loaded only when needed"
area: sicurezza
where_it_runs: PC
level: medium
cost: "€0. About 30 minutes to move the keys."
package: "none: idea only"
status: "PC version of mine"
---

# Keys in a single file, loaded only when needed

**The problem.** API keys ended up everywhere: in scripts, in each project's .env files, sometimes in notes. When one had to be changed I no longer knew where it was, and every copy was one more place it could leak from.

**How I solved it.** I keep all the keys in a single file, outside the folders Claude works on, and programs don't read it directly. A small launcher opens the file, takes only the keys written in a list of allowed names and runs the command with those variables. It doesn't execute the file as a script, so an odd line placed in there doesn't run. In notes I only write what a key is called and where it lives, never the value. On a PC the simple version is the same idea without a launcher: a file outside the vault, excluded from git and put in the permissions deny list.

**Why this way.** One place means only one place to protect and update. The list of allowed names keeps a sensitive variable (for example PATH) from changing what runs. And Claude can use a key without seeing it.

**When you need it.** When you have more than two or three API keys used by different scripts, or when Claude runs scripts that call paid services.

**When you DON'T need it.** If you use one or two keys in a single project, for me a .env file excluded from git and put in the permissions deny list is enough. The launcher with the list of names really matters on a server where the agents and the administrator are different users.

**How to get it.** There's no package: it's a way of arranging things. Move the keys into a file outside the vault (for example `~/.chiavi/chiavi.env`), exclude it from git and put it in the permissions deny list (card [Permissions](sicurezza-permessi-deny-ask.md)). On Mac and Windows an alternative is the system keychain or a password manager with a command line (1Password CLI, Bitwarden CLI).
