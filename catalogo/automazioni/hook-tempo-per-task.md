---
slug: hook-tempo-per-task
titolo: "Tempo per task, contato dagli hook"
area: automazioni
dove_gira: PC
livello: medio
costo: "0 €. 10 minuti per la versione PC."
pacchetto: "pacchetti/hook-tempo-per-task/"
stato: "versione per PC del mio"
---

# Tempo per task, contato dagli hook

**Il problema.** Chi coordina il lavoro con me doveva vedere su quale task stavo lavorando io e su quale l'AI, e quanto tempo prendevano. I cronometri a mano non li avviavo mai.

**Come l'ho risolto.** Ho legato ogni sessione di Claude Code a una task della board: gli hook UserPromptSubmit, PostToolUse e Stop segnano chi è attivo e sommano i minuti sulla task (le pause oltre 15 minuti non contano, due sessioni sulla stessa task non raddoppiano), e la board mostra le task «live» adesso. Quella versione scrive su un database su un server. Per il PC ho scritto la versione minima: scrivi «#task nome» nel messaggio (o assegni una task a una cartella), gli stessi tre hook scrivono ora, cartella e task in un file, e un comando fa il riepilogo per giorno e task.

**Perché così.** Il tempo si conta solo se si conta da solo. Tenere la task come chiave, e non la cartella, mi dice quanto costa davvero ogni lavoro, anche quando più lavori stanno nella stessa cartella.

**Quando ti serve.** Se fatturi a ore, stimi i lavori e vuoi confrontare la stima col tempo vero, o qualcuno deve vedere su cosa stai lavorando.

**Quando non ti serve.** Se non ti serve sapere il tempo. Conta solo il tempo con Claude attivo: call e lavoro fuori da Claude non ci sono, quindi non è un registro completo delle ore. La versione con board «live» per un collaboratore richiede un server sempre acceso e un database.

**Come prenderlo.** Copia `registro_tempo.py` in `~/.claude/hooks/` e i tre blocchi di `settings-esempio.json` in `~/.claude/settings.json`. Riepilogo: `python3 ~/.claude/hooks/registro_tempo.py riepilogo 30`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-tempo-per-task/LEGGIMI.md).
