---
slug: automazioni-pulizia-sessioni-ferme
titolo: "Pulizia automatica delle sessioni ferme"
area: automazioni
dove_gira: PC acceso
livello: base
costo: "0 €. 10 minuti."
pacchetto: "pacchetti/automazioni-pulizia-sessioni-ferme/"
stato: "versione per PC del mio"
---

# Pulizia automatica delle sessioni ferme

**Il problema.** Ogni chat di Claude Code aperta e dimenticata tiene acceso un processo con i suoi server MCP: da me circa 500 MB ciascuna fra memoria e swap. Con dieci chat aperte il computer rallentava, e io non le chiudevo mai a mano.

**Come l'ho risolto.** Un giro automatico chiude il processo delle sessioni che non lavorano e non aspettano niente da 30 minuti. Non ne chiude una se la conversazione è cambiata da poco, se ha un comando in corso, se aspetta la risposta di uno strumento o un mio permesso, o se l'ho messa nella lista «tieni». La conversazione resta salvata su disco e si riprende riaprendo la chat o con `claude --resume`. Da me gira su un server ogni 5 minuti e riconosce anche i lavori in background; la versione per PC è più semplice, e nel dubbio lascia stare.

**Perché così.** Le chat aperte non costano niente finché non le chiudo io, e io non le chiudo. Chiuderle da sole, solo quando sono davvero ferme, mi ridà la memoria senza perdere niente.

**Quando ti serve.** Se tieni aperte molte sessioni di Claude Code (app o terminali) e il computer ha poca memoria.

**Quando non ti serve.** Se apri una sessione alla volta e la chiudi quando hai finito. In un terminale, chiudere il processo vuol dire che `claude` esce: se scrivi in un terminale lasciato fermo, prima va rilanciato con `--resume`.

**Come prenderlo.** Copia `ferma_sessioni.py` in `~/.claude/strumenti/`. Prima lancialo senza argomenti (mostra cosa farebbe), poi pianifica `ferma_sessioni.py ferma` ogni 10-15 minuti. Su Windows serve `pip install psutil`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/automazioni-pulizia-sessioni-ferme/LEGGIMI.md).
