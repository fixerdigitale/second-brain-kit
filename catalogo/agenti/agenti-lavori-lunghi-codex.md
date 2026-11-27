---
slug: agenti-lavori-lunghi-codex
titolo: "Claude decide, ChatGPT (Codex) esegue i lavori lunghi"
area: agenti
dove_gira: PC
livello: medio
costo: "0 € in più se hai già ChatGPT; altrimenti l'abbonamento ChatGPT. Installazione di Codex CLI: circa 10 minuti."
pacchetto: "pacchetti/agenti-lavori-lunghi-codex/"
stato: "versione per PC del mio"
---

# Claude decide, ChatGPT (Codex) esegue i lavori lunghi

**Il problema.** Pago due abbonamenti, Claude e ChatGPT, ma usavo solo Claude. Le pagine e gli script lunghi consumavano la quota che mi serviva per decidere e rivedere.

**Come l'ho risolto.** I lavori lunghi (pagine, componenti, grafica, codice lungo, integrazioni) li passo a Codex con l'abbonamento ChatGPT. Claude scrive il brief in un file, lancia Codex dalla riga di comando, poi controlla la consegna come fa con ogni agente. Da me lo fanno due agenti sul server con il modello GPT, e un hook controlla che ogni lancio usi davvero il modello giusto (scheda [guardia dei comandi](../automazioni/hook-guardia-comandi.md)). Per il PC ho scritto la versione semplice con `codex exec`.

**Perché così.** Usare tutti e due gli abbonamenti mi permette di fare più lavoro senza spendere di più. A me Claude torna più utile per decidere e controllare; il lavoro lungo e ripetitivo lo può fare l'altro. Il controllo resta a Claude, quindi la qualità non dipende solo dal modello che esegue.

**Quando ti serve.** Se hai già un abbonamento ChatGPT (Plus o superiore) e ti capita di finire la quota di Claude su lavori lunghi.

**Quando non ti serve.** Se non hai ChatGPT: comprarlo solo per questo ha senso solo se arrivi spesso al limite di Claude. Non serve per lavori brevi, dove brief e controllo costano più del lavoro. E non usarlo su dati di clienti che hai promesso di tenere presso un solo fornitore.

**Come prenderlo.** Installa Codex CLI (`npm install -g @openai/codex`), fai `codex login` con il tuo account ChatGPT e copia la skill in `~/.claude/skills/lavoro-lungo-codex/`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/agenti-lavori-lunghi-codex/LEGGIMI.md).
