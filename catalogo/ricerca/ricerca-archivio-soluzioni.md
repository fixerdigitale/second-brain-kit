---
slug: ricerca-archivio-soluzioni
titolo: "Archivio delle soluzioni"
area: ricerca
dove_gira: PC
livello: base
costo: "0 €. 5 minuti per copiarlo; poi circa 10 minuti per scheda, solo quando un problema ti è costato più di mezz'ora."
pacchetto: pacchetti/ricerca-archivio-soluzioni/
stato: lo uso
---

# Archivio delle soluzioni

**Il problema.** Gli stessi guasti tornavano: un iframe che si taglia, un webhook in timeout, un login che gira in tondo. Ogni volta si rifaceva la diagnosi da zero, e si riprovavano le stesse strade sbagliate, perché nessuno si ricordava cosa non aveva funzionato la volta prima.

**Come l'ho risolto.** Una cartella con una scheda markdown per ogni problema risolto (oggi ne ho circa 180). Ogni scheda ha sette sezioni: sintomo (con le parole di chi l'ha segnalato), causa vera, come si riconosce (il test più veloce), soluzione, verifica con i numeri, vicoli ciechi, per cosa è riusabile. Un comando `soluzioni` fa cerca, mostra, elenco, nuova e indice. Una skill dice a Claude Code di cercare lì prima di diagnosticare e di scrivere una scheda dopo aver risolto qualcosa costato più di mezz'ora. La stessa cartella la leggono e la scrivono anche gli agenti e Codex.

**Perché così.** La parte che mi fa risparmiare più tempo sono i vicoli ciechi: è quella che non si ricostruisce leggendo il codice. Si cerca con le parole del sintomo, non della causa, perché la causa è proprio quello che non sai ancora. Le correzioni da un minuto non entrano: diluirebbero l'archivio, e poi non lo legge più nessuno.

**Quando ti serve.** Se con Claude Code sistemi siti, automazioni, server o integrazioni, e ti capita di pensare «questo l'avevo già visto». Anche se lavori con altre persone o altri assistenti che si scontrano con gli stessi problemi.

**Quando non ti serve.** Se usi Claude Code soprattutto per testi o strategia e i problemi tecnici sono rari: la cartella resta vuota. Anche se ogni progetto è diverso e i guasti non si ripetono. E se dopo un mese hai 50 schede da un minuto l'una, l'archivio smette di servire.

**Come prenderlo.** Copia `SKILL.md`, `modello-scheda.md` e `soluzioni.py` in `~/.claude/skills/soluzioni/`, crea `<cartella-vault>/soluzioni/` e imposta `VAULT_DIR` o `SOLUZIONI_DIR`. Lo script è facoltativo: senza, Claude cerca nella cartella con i suoi strumenti.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/ricerca-archivio-soluzioni/LEGGIMI.md).
