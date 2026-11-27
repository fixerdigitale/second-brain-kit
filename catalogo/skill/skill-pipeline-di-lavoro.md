---
slug: skill-pipeline-di-lavoro
titolo: "Pipeline di lavoro: le correzioni non si perdono più"
area: skill
dove_gira: PC
livello: medio
costo: "0 € in più; circa 30 minuti per il primo giro del documento"
pacchetto: "pacchetti/skill-pipeline-di-lavoro/"
stato: "lo uso"
---
# Pipeline di lavoro: le correzioni non si perdono più

**Il problema.** Ripetevo le stesse correzioni a ogni landing e a ogni preventivo. Finita la sessione, Claude se ne dimenticava. E non distinguevo le regole che valgono per tutti da quelle di un cliente solo.

**Come l'ho risolto.** Un documento, `PIPELINE-LAVORO.md`: tipi di lavoro, pezzi riutilizzabili (copia di sicurezza, prova, copy del cliente, controllo su telefono), Direttive per ogni cliente e pipeline tipo × cliente. Più una skill che a ogni richiesta capisce se è un'informazione o un lavoro. Per un lavoro trova la pipeline, la dice in una riga e la segue un passo alla volta: prima «faccio X?», dopo «ho fatto questo, va bene?». Ogni mia correzione la scrive nel pezzo, se vale per tutti, o nelle Direttive del cliente, più una riga nello STORICO. La regola che seguo: la prima volta registro i passi, la seconda nasce la pipeline, la terza la ottimizzo.

**Perché così.** L'ho costruita dopo aver contato due mesi di task e di sessioni: i lavori veri erano 14 tipi, sempre quelli. Scritti una volta, non li rispiego più. Il check prima e dopo ogni passo mi lascia le decisioni, mentre l'AI fa il lavoro.

**Quando ti serve.** Se fai lavori simili per più clienti (pagine, preventivi, report, problemi tecnici) e ogni cliente ha le sue fisse.

**Quando non ti serve.** Se fai un lavoro diverso ogni volta, o lavori per un solo cliente con poche regole: ti basta il CLAUDE.md. Il check a ogni passo rallenta: per lavori da 10 minuti è troppo.

**Come prenderlo.** Copia la skill in `~/.claude/skills/pipeline-lavoro/` e i due modelli in `<cartella-vault>/pipeline-lavoro/`, poi sostituisci il segnaposto del percorso. All'inizio il documento è quasi vuoto, ed è giusto così. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/skill-pipeline-di-lavoro/LEGGIMI.md).
