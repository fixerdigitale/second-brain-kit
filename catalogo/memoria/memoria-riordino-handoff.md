---
slug: memoria-riordino-handoff
titolo: "Riordino: dai diari di lavoro alla scheda dei fatti"
area: memoria
dove_gira: PC
livello: medio
costo: "0 € in più con l'abbonamento Claude. Lo script gira in un secondo."
pacchetto: pacchetti/memoria-riordino-handoff/
stato: versione per PC del mio
---

# Riordino: dai diari di lavoro alla scheda dei fatti

**Il problema.** Anche con HANDOFF e SISTEMA separati, nessuno si ricordava di portare i fatti stabili nella scheda, e gli HANDOFF tornavano a gonfiarsi.

**Come l'ho risolto.** Da me ogni notte alle 4:40 un servizio sul server legge le sezioni nuove degli HANDOFF, chiede a Sonnet quali sono fatti stabili e cambia al massimo 12 righe di SISTEMA.md: copia prima di ogni modifica, segreti tolti prima di passare il testo al modello, ogni riga marcata «riordino gg/mm». Poi, se un HANDOFF supera 80 KB, sposta le sezioni più vecchie in un archivio mensile finché torna a 60 KB, controllando che nessuna riga si perda. Nel pacchetto ci sono le due metà in forma da PC: il prompt da usare come comando `/riordino` (mostra le modifiche e aspetta l'ok) e uno script Python che fa l'archivio meccanico, a secco finché non scrivi `--applica`.

**Perché così.** La parte di giudizio (cosa è stabile) la fa bene un modello, ma deve cambiare righe singole e mai inventare: per questo il prompt è stretto. La parte meccanica non ha bisogno di AI, e uno script che conta le righe mi dà più sicurezza di un modello che riscrive un file di 100 KB.

**Quando ti serve.** Se usi HANDOFF.md e SISTEMA.md su progetti lunghi e vedi gli HANDOFF crescere oltre le decine di KB.

**Quando non ti serve.** Se hai pochi progetti e li tieni in ordine a mano, o se i tuoi HANDOFF restano corti: lo script risponderebbe sempre «niente da fare». La versione automatica notturna ha senso solo con un server acceso.

**Come prenderlo.** Salva `prompt-riordino.md` come `~/.claude/commands/riordino.md` e usa `/riordino` nella cartella del progetto. Lancia `python3 archivia_handoff.py <cartella-progetto>` (a secco), poi con `--applica`.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-riordino-handoff/LEGGIMI.md).
