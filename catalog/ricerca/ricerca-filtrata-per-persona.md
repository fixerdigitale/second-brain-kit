---
slug: ricerca-filtrata-per-persona
title: "Search filtered by person"
area: ricerca
where_it_runs: server
level: advanced
cost: "€0 extra on the server I already had. Development and testing: a few days of work."
package: "none: idea only"
status: "I use it"
---

# Search filtered by person

**The problem.** I wanted a collaborator to be able to ask the assistant about the state of her projects without seeing money, other clients or personal things that live in the same vault. Making a vault or an agent for each person doesn't hold up: everything gets duplicated.

**How I solved it.** One vault, and one system with the labels from the "A vault with fixed folders and labels at birth" card: every note is born with `livello` (operational, financial, personal), the clients it talks about and who can see it. From those labels an index containing only the labeled pieces of notes is regenerated every 15 minutes. The agent that talks to the collaborator doesn't read the files: it has a single search tool, where the person is fixed in the configuration and doesn't come from the chat. A piece comes out only if it's in the index, with the same text, and with a level and clients allowed for that person. A piece changed after labeling doesn't come out until it's relabeled.

**Why this way.** The rule I set myself is "one agent per role, not per person". The filter lives in the tool, not in the instructions to the model: a model can be persuaded, a script can't. And I add the labels when the note is born because that's when it's best known what's in it: redoing them later across the whole vault is slower and less precise.

**When you need it.** When several people (collaborators, clients) query the same memory and not everyone may see everything.

**When you DON'T need it.** If you're the only one using the vault, or with partners who see everything: it's pure complexity. It isn't a PC thing, because it has to answer when the others write. If you just want to share something with a collaborator, a separate shared folder is simpler and safer.

**How to get it.** Idea only: it needs a server with an agent locked in a separate environment and a custom search tool. The piece you can take right away is labels at birth: package `pacchetti/memoria-vault-etichette-alla-nascita/`.
