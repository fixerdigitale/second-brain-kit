# Copy in italiano

**Cosa fa.** `copy-italia` è una skill corta che si legge prima delle skill di copy americane: dice cosa cambiare per l'Italia (tono, leve vietate dal Codice del Consumo, garanzie, prezzi barrati). Da sola non scrive copy: fa da filtro alle altre.

**Le skill di metodo si prendono dalla fonte** (non sono nostre):
- Hormozi (offerta, prezzi, hook, obiezioni): https://github.com/alexsmedile/hormozi-skills (MIT)
- Cialdini, Kennedy, Schwartz, Whitman, Halbert, Ogilvy, Hopkins: https://github.com/rowantonkin-ai/copy-skills (MIT)
- Italiano senza tic da AI: https://github.com/mario-montanari/italiano-scrittura-anti-ai
- `copywriting-pro` (procedura generale: avatar, voce del cliente, livelli di consapevolezza): registro ClawHub, slug `copywriting-pro`; autore da verificare prima di installarla.

**Dove si copia.** `copy-italia/` in `~/.claude/skills/copy-italia/`, accanto alle skill di copy che installi dalle fonti.

**Come si prova.** Chiedi «scrivimi l'offerta per un corso, usa hormozi-offer». In testa al testo deve comparire cosa è stato adattato all'Italia, e niente «solo 3 posti» se non gliel'hai detto tu.

**Come si toglie.** Cancella `~/.claude/skills/copy-italia/`.

## English

`copy-italia`, a short skill that sits in front of American copywriting method skills and adapts them to the Italian market: concrete B2B tone, urgency and scarcity only when real (Italian consumer law), guarantees only if the seller can keep them, no inflated values. At the top of each text it lists what it adapted.

Install: copy `copy-italia/` into `~/.claude/skills/`, and install the method skills from their sources (listed above). Useful as a model if you want the same filter for another country.
