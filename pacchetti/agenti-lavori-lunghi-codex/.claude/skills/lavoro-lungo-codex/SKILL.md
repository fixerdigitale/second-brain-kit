---
name: lavoro-lungo-codex
description: Passa un lavoro lungo (più di ~15 minuti o molti file: pagine, script grossi, integrazioni) a Codex con l'abbonamento ChatGPT, invece di consumare la quota di Claude. Claude scrive il brief e controlla la consegna. Usala quando lo smistamento indica un lavoro lungo e Codex è installato.
---

# Lavoro lungo su Codex

Claude decide e controlla; Codex esegue il lavoro lungo con l'abbonamento ChatGPT.

1. Controlla che Codex ci sia: `codex --version`. Se manca, fai il lavoro qui o col sotto-agente `costruttore`, e dillo.
2. Scrivi il brief in un file `BRIEF-<lavoro>-<data>.md` nella cartella del progetto: obiettivo, file da toccare e da non toccare, vincoli, criteri di «fatto quando», «a fine lavoro scrivi CONSEGNA.md con i file toccati e cosa hai verificato».
3. Lancia, dalla cartella del progetto:
   ```
   codex exec --sandbox workspace-write -C <tuo-progetto> -o <tuo-progetto>/.esito-codex.txt "Leggi BRIEF-<lavoro>-<data>.md e fai il lavoro. Lavora solo dentro questa cartella."
   ```
   Per lavori lunghi lancialo in background e aspetta la fine del processo.
4. Controlla: leggi `CONSEGNA.md` e i file toccati (`git diff` se è un repo), spunta ogni criterio, guarda il risultato a schermo se è una pagina. Un'uscita senza errori non prova che il lavoro sia giusto.
5. Difetti: un nuovo `codex exec` con la sola lista dei difetti. Massimo 2 giri, poi riferisci alla persona.

Non passare a Codex dati di clienti o file con credenziali senza dirlo alla persona: escono dall'abbonamento Claude.
