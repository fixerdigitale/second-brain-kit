---
slug: hook-smistatore-procedure
titolo: "Hook smistatore: la procedura giusta al momento giusto"
area: automazioni
dove_gira: PC
livello: medio
costo: "0 €. 15 minuti, più il tempo per scrivere le procedure."
pacchetto: "pacchetti/hook-smistatore-procedure/"
stato: "versione per PC del mio"
---

# Hook smistatore: la procedura giusta al momento giusto

**Il problema.** Ho scritto le procedure per i lavori che ripeto (landing, report, proposte), e le regole di regia per decidere chi fa cosa. Ma Claude non le apriva se non glielo ricordavo io: partiva da zero e rifaceva errori già corretti.

**Come l'ho risolto.** Ho messo un hook UserPromptSubmit che riconosce dalle parole del mio messaggio il tipo di lavoro e aggiunge a Claude, una volta per sessione, «procedura possibile: X, nel file Y, da verificare». Quando il messaggio sembra un lavoro, aggiunge anche un promemoria di regia: prima di cominciare, decidi chi lo fa. Da me ricorda pure la scheda dei fatti stabili quando nomino un cliente. Nella versione per PC le procedure stanno in un JSON (nome, parole, percorso del file) e il promemoria in un file di testo facoltativo.

**Perché così.** Le procedure valgono solo se si leggono. Così arrivano nel momento in cui servono, e Claude mi dice in una riga quale sta seguendo: se sbaglia lo vedo subito. «Da verificare» è voluto: indovina dalle parole e ogni tanto sbaglia.

**Quando ti serve.** Se hai già (o stai scrivendo) procedure in file per i lavori ricorrenti, o usi le skill della scheda [regia e smistamento](../agenti/agenti-regia-e-smistamento.md).

**Quando non ti serve.** Se non hai procedure scritte: l'hook non ha niente da ricordare, comincia da quelle. Con poche procedure, sempre le stesse, basta una riga in CLAUDE.md.

**Come prenderlo.** Copia `smistatore.py`, `procedure.json` e, se vuoi il promemoria di regia, `promemoria.txt` in `~/.claude/hooks/`. Metti le tue procedure nel JSON (percorsi assoluti) e il blocco di `settings-esempio.json` in `~/.claude/settings.json`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-smistatore-procedure/LEGGIMI.md).
