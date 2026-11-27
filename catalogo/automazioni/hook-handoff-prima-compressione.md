---
slug: hook-handoff-prima-compressione
titolo: "HANDOFF salvato quando la sessione viene compressa"
area: automazioni
dove_gira: PC
livello: medio
costo: "0 €. 15 minuti per installarlo e provarlo con un /compact."
pacchetto: "pacchetti/hook-handoff-prima-compressione/"
stato: "versione per PC del mio"
---

# HANDOFF salvato quando la sessione viene compressa

**Il problema.** Quando la sessione si riempie, Claude Code la comprime e tiene solo un riassunto. La conversazione resta su disco, ma la sessione dimentica i dettagli: decisioni, file toccati, cosa mancava. E se l'HANDOFF.md del progetto è fermo, chi riprende (io, un'altra sessione, un altro agente) riparte da uno stato vecchio.

**Come l'ho risolto.** Io uso una mod dell'app desktop di Claude Code, non un hook di settings.json: un attimo prima della compressione chiede a una copia della sessione cosa salvare e lo scrive nell'HANDOFF.md del progetto, in una sezione datata, più le correzioni su di me in memoria. Per un PC normale ho scritto una versione con gli hook standard: PreCompact salva le tue ultime 15 richieste (con password e chiavi oscurate), e SessionStart con matcher «compact» dice a Claude di rileggere HANDOFF.md, confrontarlo con quelle richieste e aggiornarlo prima di continuare. C'è anche il comando /salva-handoff per farlo a mano.

**Perché così.** Il momento debole delle sessioni lunghe è la compressione: lì si perde il filo. Agganciare il salvataggio a quell'evento vuol dire che succede sempre, anche quando non ci penso. La versione con gli hook è meno precisa della mia (aggiorna l'HANDOFF subito dopo, non prima, perché durante PreCompact il modello non risponde), ma copre il buco con le richieste salvate.

**Quando ti serve.** Se lavori su progetti che durano più giorni, tieni (o vuoi tenere) un HANDOFF.md per progetto, e ti è capitato che dopo una compressione Claude non sapesse più a che punto eravate.

**Quando non ti serve.** Se le tue sessioni sono corte e non arrivano mai alla compressione. Se non tieni un HANDOFF per progetto, prima serve quello (scheda [HANDOFF e SISTEMA](../memoria/memoria-handoff-e-sistema.md)): l'hook da solo crea file che poi nessuno legge.

**Come prenderlo.** Copia `handoff_compressione.py` in `~/.claude/hooks/`, `commands/salva-handoff.md` in `~/.claude/commands/` e i due blocchi di `settings-esempio.json` in `~/.claude/settings.json`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-handoff-prima-compressione/LEGGIMI.md).
