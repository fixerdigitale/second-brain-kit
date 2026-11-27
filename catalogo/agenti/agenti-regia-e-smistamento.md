---
slug: agenti-regia-e-smistamento
titolo: "Regia e smistamento: chi fa il lavoro, e chi lo controlla"
area: agenti
dove_gira: PC
livello: medio
costo: "0 €. 10 minuti per adattare la tabella; ogni controllo aggiunge qualche minuto di lavoro di Claude per delega."
pacchetto: "pacchetti/agenti-regia-e-smistamento/"
stato: "versione per PC del mio"
---

# Regia e smistamento: chi fa il lavoro, e chi lo controlla

**Il problema.** Avere i sotto-agenti non bastava. Claude se li dimenticava e faceva tutto col modello principale, oppure delegava cose che faceva prima a fare lui. E quando delegava, a volte l'agente rispondeva «fatto» e non era vero: file non scritti, pagine rotte sul telefono, richieste sparite fra un giro di correzioni e l'altro.

**Come l'ho risolto.** Claude Code fa da regista con due regole scritte in skill. La prima è una tabella per taglia: meno di 2 minuti lo fa la sessione; il lavoro meccanico va all'esecutore (Haiku); il codice già deciso al costruttore (Sonnet); il lavoro lungo (oltre 15 minuti circa o molti file) a un agente per lavori lunghi su ChatGPT; architettura, sicurezza e revisione finale restano al modello principale. Claude dice in una riga a chi passa il lavoro. La seconda è il modo di delegare: un brief corto (obiettivo, file da toccare e da non toccare, vincoli, stato da leggere, criteri di «fatto quando», formato della consegna), una sessione nuova per ogni giro, e prima di scrivermi Claude legge i file toccati e spunta i criteri. Massimo 2 giri di correzione: al terzo difetto ripetuto me lo dice invece di insistere. Da me le due regole sono nelle istruzioni sempre caricate, e un hook le ricorda quando un messaggio sembra un lavoro.

**Perché così.** Una regola scritta in un posto che Claude legge sempre funziona; una detta in chat si perde alla sessione dopo. La riga «lo passo a X» mi lascia correggere subito. Per me chi fa e chi controlla non sono mai lo stesso agente, e i criteri scritti prima evitano di discutere dopo su cosa voleva dire «fatto». La sessione nuova per ogni giro tiene il contesto dell'agente pulito.

**Quando ti serve.** Se hai già i sotto-agenti (scheda esecutore e costruttore) e vuoi che vengano usati davvero, o se ti è capitato di trovare errori dopo un «fatto».

**Quando non ti serve.** Se lavori quasi sempre su richieste brevi e conversazionali, o deleghi raramente e solo cose che controlli a occhio in un minuto: la riga di smistamento e il brief costano più del lavoro.

**Come prenderlo.** Copia le due skill (`smistamento` e `delega-con-controllo`) in `~/.claude/skills/` e aggiungi una riga al tuo `CLAUDE.md` che le richiama. Sono la versione generale delle mie, senza i nostri agenti e percorsi. Il promemoria al momento giusto è nella scheda [hook smistatore](../automazioni/hook-smistatore-procedure.md). Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/agenti-regia-e-smistamento/LEGGIMI.md).
