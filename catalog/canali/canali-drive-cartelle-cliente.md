---
slug: canali-drive-cartelle-cliente
title: "Shared Drive with the same folders for every client"
area: canali
where_it_runs: PC
level: basic
cost: "€0 if you already have Google Workspace; ten minutes"
package: "pacchetti/canali-drive-cartelle-cliente/"
status: "PC version of mine"
---

# Shared Drive with the same folders for every client

**The problem.** Documents created by the AI were born in my personal Drive, each in a different place. The people working with me couldn't see them, and every time I had to share them by hand.

**How I solved it.** Every file is born in the studio's shared Drive, visible to the people working with me and to my main assistant's account. Each client always has the same five folders: 01 Initial documents, 02 Materials, 03 For requests, 04 Deliveries, 05 Internal work. A command gives Claude the right folder for client and type, so the file is born in its place. Drafts and checks go into "Internal work", into "Deliveries" only what goes to the client. Never in the shared Drive: credentials, contracts, invoices and banking, candidate data, personal things. In the package: a script that creates the structure in a folder synced with Drive for desktop, and the rule for CLAUDE.md.

**Why this way.** The same structure for everyone means neither I nor the AI has to decide each time where to put a file. The list of what never goes in protects the things that mustn't circulate.

**When you need it.** If you work with a partner, an assistant or a collaborator who needs to see client files.

**When you DON'T need it.** If you work alone and don't share anything: the structure in the vault is enough. If your Google Workspace doesn't have shared drives, you can use a normal shared folder, but files remain owned by whoever creates them.

**How to get it.** Copy `cartella_cliente.py`, set `RADICE` to the local path of the shared Drive's Clients folder and paste `regola-per-CLAUDE.md` into your CLAUDE.md. The script only creates folders: it never deletes or moves anything. The folder names in the script are Italian; rename them if you like. Step-by-step instructions: [package guide](../../pacchetti/canali-drive-cartelle-cliente/LEGGIMI.md).
