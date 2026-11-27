---
slug: ricerca-qmd-sul-pc
titolo: "Ricerca per significato sul PC con QMD"
area: ricerca
dove_gira: PC
livello: medio
costo: "0 €. Circa 15-30 minuti per installare e fare la prima indicizzazione, più lo spazio dei modelli locali (non l'ho misurato: dipende dalla versione)."
pacchetto: pacchetti/ricerca-qmd-sul-pc/
stato: proposta nuova, non la uso così
---

# Ricerca per significato sul PC con QMD

**Il problema.** Se il vault vive sul PC e lo usi con Claude Code, la ricerca trova solo le parole esatte. Una nota che parla della stessa cosa con altre parole resta invisibile, e Claude conclude che l'informazione non c'è.

**Come l'ho risolto.** Lo dico subito: io QMD non l'ho installato, perché sul server ho già la ricerca per significato (scheda «Ricerca per significato in tutta la memoria»). Su un PC senza ricerca è l'opzione che proverei per prima. QMD (github.com/tobi/qmd) è un motore di ricerca locale sopra le cartelle markdown: unisce ricerca per parole (BM25), ricerca per significato (vettori) e un riordino dei risultati fatto da un piccolo modello, tutto sul PC. Ha un server MCP, quindi Claude Code lo usa come uno strumento. Nel pacchetto ci sono la voce per `.mcp.json` e le righe per CLAUDE.md che dicono a Claude di cercare lì prima di dire «non c'è».

**Perché così.** Fra le opzioni che ho guardato è la più vicina a quello che uso sul server, ma senza server: le note restano sul PC, i modelli girano in locale e non c'è niente da pagare. La preferisco alle alternative perché indicizza le cartelle markdown così come sono, senza chiederti di cambiare formato o struttura del vault. Da quello che ho letto è mantenuto: nel 2026 sono uscite più versioni (fino alla 2.5.3 di fine maggio). Non l'ho provato su Windows.

**Quando ti serve.** Quando il vault ha qualche centinaio di note o più, quando scrivi appunti liberi o dettati, quando chiedi spesso a Claude «cosa avevo deciso su…».

**Quando non ti serve.** Se le note sono poche e ben titolate: la ricerca per parole basta. Se il PC è vecchio o con poco spazio: la prima indicizzazione scarica modelli locali e impegna il processore per un po'. Se hai già una ricerca per significato (come me sul server), è un doppione. Se vuoi una memoria che Claude scrive da solo, guarda la scheda su Basic Memory. E ricorda che l'indice si aggiorna quando lo rilanci.

**Come prenderlo.** Fonte ufficiale: https://github.com/tobi/qmd (pacchetto npm `@tobilu/qmd`; esistono fork con lo stesso nome, installa solo da tobi/qmd). Nel pacchetto: i passi nel LEGGIMI, la voce per `.mcp.json` e le righe per CLAUDE.md. I comandi vengono dalla documentazione di novembre 2026: se cambiano, vale il README.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/ricerca-qmd-sul-pc/LEGGIMI.md).
