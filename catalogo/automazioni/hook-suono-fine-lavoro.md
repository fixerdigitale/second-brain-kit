---
slug: hook-suono-fine-lavoro
titolo: "Suono quando Claude ha finito o aspetta me"
area: automazioni
dove_gira: PC
livello: base
costo: "0 €. 5 minuti."
pacchetto: "pacchetti/hook-suono-fine-lavoro/"
stato: "versione per PC del mio"
---

# Suono quando Claude ha finito o aspetta me

**Il problema.** Lanciavo un lavoro, passavo ad altro e scoprivo dopo mezz'ora che Claude aspettava un mio sì dal primo minuto.

**Come l'ho risolto.** Io non ho un suono sul PC: ho un piccolo display fisico sulla scrivania che, a fine turno, fa un bip e un'animazione, comandato da una mod dell'app desktop. Questa scheda è la versione per PC, che chiunque può avere: un hook Stop suona quando Claude ha finito, e un hook Notification suona (e su Mac mostra una notifica) quando aspetta un permesso o una risposta.

**Perché così.** Il tempo perso non è quello di Claude, è il mio quando non mi accorgo che ha finito. Un segnale diverso per «finito» e «aspetta te» mi basta a non controllare la finestra ogni due minuti.

**Quando ti serve.** Se lanci lavori da più di qualche minuto e nel frattempo fai altro.

**Quando non ti serve.** Se resti sempre davanti alla finestra di Claude, o lavori in posti dove i suoni danno fastidio. A volte bastano già le notifiche dell'editor.

**Come prenderlo.** Copia `fine_lavoro.py` in `~/.claude/hooks/` e i due blocchi di `settings-esempio.json` in `~/.claude/settings.json`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-suono-fine-lavoro/LEGGIMI.md).
