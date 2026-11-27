---
name: smistamento
description: Decide chi fa un lavoro in base alla sua taglia (la sessione stessa, un sotto-agente economico, un agente per lavori lunghi) prima di cominciare. Usala all'inizio di ogni richiesta che non si chiude in pochi minuti.
---

# Smistamento per taglia

Prima di cominciare un lavoro, guardane la taglia e scegli chi lo fa. Dillo in una riga («Lo passo al costruttore: è codice già deciso»), poi procedi.

| Taglia del lavoro | Chi | Modello |
|---|---|---|
| Meno di 2 minuti: una lettura, una risposta | la sessione stessa | quello della sessione |
| Meccanico: cercare, leggere log, contare, modifiche già decise | sotto-agente `esecutore` | Haiku |
| Codice già deciso, script brevi, giri di correzioni | sotto-agente `costruttore` | Sonnet |
| Lungo (oltre ~15 minuti o molti file): pagine, script grossi, integrazioni | agente per lavori lunghi, se c'è (es. Codex con l'abbonamento ChatGPT) | quello dell'abbonamento |
| Scelta di architettura, sicurezza, accessi, revisione finale | la sessione principale | il modello migliore che hai |

Regole:
- Non delegare quello che fai prima tu che a scrivere il brief.
- Il lavoro delegato torna sempre alla sessione principale, che lo controlla prima di dire «fatto».
- Se una delega fallisce due volte sulla stessa cosa, fermati e chiedi alla persona invece di insistere.
