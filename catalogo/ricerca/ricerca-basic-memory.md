---
slug: ricerca-basic-memory
titolo: "Alternativa: Basic Memory, memoria che Claude scrive e rilegge"
area: ricerca
dove_gira: PC
livello: medio
costo: "0 € nella versione locale (open source, AGPL v3). Circa 20 minuti per installarlo e collegarlo."
pacchetto: "nessuno: solo idea"
stato: proposta nuova, non la uso così
---

# Alternativa: Basic Memory, memoria che Claude scrive e rilegge

**Il problema.** QMD cerca nelle note che scrivi tu. Se invece vuoi che sia Claude, durante le conversazioni, a scrivere e collegare le note e a ritrovarle dopo, ti serve uno strumento pensato per questo.

**Come l'ho risolto.** Basic Memory (github.com/basicmachines-co/basic-memory) è un server MCP locale: tiene la conoscenza in file markdown normali (si aprono anche con Obsidian, con i link a doppia parentesi) e usa un database SQLite per l'indice e la ricerca. Claude legge, scrive e collega note attraverso i suoi strumenti. Io non lo uso: l'ho valutato come alternativa per il PC.

**Perché così.** L'ho messo come seconda scelta per due motivi. Primo, vuole organizzare lui le note (entità, relazioni, una sua struttura), mentre un vault già avviato secondo me funziona meglio con uno strumento che cerca sopra quello che c'è. Secondo, è in movimento: la versione 1.0 di fine ottobre 2026 ha tolto alcuni strumenti MCP e cambiato comandi e configurazione.

**Quando ti serve.** Se parti da zero o quasi, e vuoi che sia Claude a costruire la memoria mentre lavori, con note collegate fra loro.

**Quando non ti serve.** Se hai già un vault strutturato a modo tuo e vuoi solo ritrovare meglio: QMD è più leggero e non tocca le note. Se non vuoi che un assistente scriva nel vault senza che tu rilegga. Se la licenza AGPL v3 ti crea problemi per un uso dentro un prodotto che vendi, leggila prima.

**Come prenderlo.** Fonte ufficiale: https://github.com/basicmachines-co/basic-memory (documentazione e changelog su https://docs.basicmemory.com). Si installa con uv (`uv tool install basic-memory`) o Homebrew e si collega a Claude Code come server MCP. Prima di installarlo, leggi il changelog della versione corrente.
