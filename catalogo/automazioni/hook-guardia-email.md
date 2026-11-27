---
slug: hook-guardia-email
titolo: "Guardia che non fa uscire la mia email verso siti terzi"
area: automazioni
dove_gira: PC
livello: base
costo: "0 €. 10 minuti."
pacchetto: "pacchetti/hook-guardia-email/"
stato: "lo uso"
---

# Guardia che non fa uscire la mia email verso siti terzi

**Il problema.** Claude vede l'email del mio account nelle istruzioni di partenza e a volte la mette da sola in un User-Agent o in un URL quando chiama un sito. Mi è successo verso un sito pubblico: la mia email finita nei log di qualcun altro.

**Come l'ho risolto.** Ho messo un hook PreToolUse su Bash, WebFetch, WebSearch e sugli strumenti che aprono pagine: se l'indirizzo compare (anche codificato in un URL o in base64) e la destinazione non è un mio servizio, ferma la richiesta o mi chiede conferma. Gli indirizzi stanno in un file a parte, nel codice non ce n'è nessuno.

**Perché così.** È un errore piccolo ma ripetibile, e nessun permesso standard lo copre: i permessi guardano il comando, non cosa c'è dentro.

**Quando ti serve.** Se fai fare a Claude ricerche, scraping o chiamate a siti pubblici dal tuo PC.

**Quando non ti serve.** Se Claude non va mai su internet per te. Non protegge da tutto: copre gli strumenti elencati, non un programma che Claude scrive e lancia dopo.

**Come prenderlo.** Copia `guardia_email.py` e `indirizzi_email.txt` in `~/.claude/hooks/`, scrivi i tuoi indirizzi nel `.txt` e i tuoi domini in `HOST_AMMESSI`, poi il blocco di `settings-esempio.json`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-guardia-email/LEGGIMI.md).
