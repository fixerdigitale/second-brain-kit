---
slug: canali-report-pagine
titolo: "Come consegno pagine e report"
area: canali
dove_gira: PC
livello: base
costo: "0 € sul PC; un sito con login vuole un server e giorni di configurazione"
pacchetto: "pacchetti/canali-report-pagine/"
stato: "versione per PC del mio"
---
# Come consegno pagine e report

**Il problema.** I risultati dell'AI mi arrivavano come markdown o percorsi di file. Dal telefono non li aprivo, e a un cliente non potevo girarli così. Quando poi li mandavo, allegati e link pubblici giravano senza controllo e non sapevo più chi aveva cosa.

**Come l'ho risolto.** Ogni documento da leggere diventa una pagina web con il mio stile fisso: conclusione in cima, indice, sezioni numerate. Regola fissa: a me arriva sempre un link, mai un percorso di file. Il comando che la pubblica non parte se non dico per quale cliente, progetto e task è, e la stessa pagina pubblicata due volte si aggiorna invece di nascere doppia. Nel mio sistema le pagine stanno su un sito mio dietro login con secondo fattore; una cartella pubblica c'è solo per le poche pagine che devono essere aperte, senza elenco; ai clienti arriva solo quello che segno come esterno (vedi il catalogo, [scheda](canali-catalogo-elementi.md)). Nel pacchetto c'è la versione per PC: una skill che fa una pagina HTML unica, che si apre con un doppio clic, e tre strade per farla arrivare a qualcuno.

**Perché così.** Una pagina con la conclusione in cima si legge in due minuti dal telefono; un file in una cartella non lo apre nessuno. L'obbligo di dire per chi è evita report orfani. E un posto solo con gli accessi controllati vale più di allegati sparsi fra posta e chat.

**Quando ti serve.** Se mandi spesso analisi, riepiloghi o proposte a clienti o soci, o vuoi rileggere i risultati dal telefono.

**Quando non ti serve.** Se i risultati li leggi solo tu, in VS Code, subito: il markdown basta. Se ai clienti mandi già Google Docs, resta su quelli. E un sito tuo con login ha senso solo se consegni spesso a più clienti: è un servizio da aggiornare e da tenere sicuro, e per pochi file al mese Drive condiviso con persone precise fa lo stesso.

**Come prenderlo.** Copia `report-pagina/` (`SKILL.md` e `template.html`) in `~/.claude/skills/report-pagina/` e cambia i colori in cima al template se vuoi i tuoi. Il LEGGIMI spiega le tre strade per consegnarla: Drive, pagina privata di claude.ai, sito tuo con login. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/canali-report-pagine/LEGGIMI.md).
