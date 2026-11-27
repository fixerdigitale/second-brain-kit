---
slug: memoria-vault-etichette-alla-nascita
title: "A vault with fixed folders and labels at birth"
area: memoria
where_it_runs: PC
level: medium
cost: "€0 for the manual version. The automatic one, on my side, uses a model for the second check: a few cents a day, but it needs a server."
package: "pacchetti/memoria-vault-etichette-alla-nascita/"
status: "PC version of mine"
---

# A vault with fixed folders and labels at birth

**The problem.** The vault grew without order: I no longer knew which notes concerned a client, which were financial or personal. When I wanted to let a collaborator read the vault, I had no way to filter what she could see.

**How I solved it.** The vault has fixed folders (Clients, Projects, Decisions, Resources, Facts by month, Sources for raw material). Every note is born with a frontmatter of labels: `entita` (which client or project it refers to), `livello` (operational, financial, personal) and `visibile_a` (who can read it). On my side a service on the server looks at new notes every 15 minutes and adds the labels by itself, with a model and a second check; the same labels are the ones that filter per-person search (card "Search filtered by person"): it's one system. The package has the manual version: a note template, the folder scheme and a script that lists notes without labels.

**Why this way.** Adding labels when the note is born costs a few seconds; adding them later to hundreds of notes costs days, and a label added after the fact is more likely to be wrong. With `entita` I find everything about a client; with `livello` and `visibile_a` I can give someone access without showing them the financial or personal things.

**When you need it.** If the vault already has dozens of notes on different clients, or if you're thinking of letting a partner, a collaborator or an agent with permissions different from yours read it.

**When you DON'T need it.** If you're the only one reading the vault and you search it by text: clear folders and names are enough, labels would be extra work. Automatic labeling only makes sense with several readers and an always-on server.

**How to get it.** Copy `CARTELLE.md` and `nota-modello.md` into the root of the vault (in Obsidian you can use `nota-modello.md` as a template). Run `python3 controlla_etichette.py <vault-folder>` to see the notes without labels: it's read-only.

Step-by-step instructions: [package guide](../../pacchetti/memoria-vault-etichette-alla-nascita/LEGGIMI.md).
