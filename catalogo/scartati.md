# Cosa ho provato e lasciato

🇬🇧 [English](../catalog/discarded.md)

Questa è la parte del catalogo che di solito non si racconta: strumenti e modi di lavorare che ho provato, o valutato con attenzione, e poi ho lasciato. Non sono bocciature assolute. Sono scelte fatte per il mio modo di lavorare: un solo server, due abbonamenti (Claude Max e ChatGPT) e la regola di pagare il meno possibile a consumo. Per ogni voce scrivo anche quando, secondo me, a te potrebbe servire lo stesso.

Le voci sono divise per area, come le schede del catalogo. Le date sono quelle della decisione.

---

## Memoria

### Sistemi di memoria per agenti alternativi a un vault di note (Mem0, Letta, Graphiti, Cognee, LightRAG, claude-mem e simili)
- **Cosa prometteva.** Una memoria a lungo termine automatica per gli agenti, con estrazione dei fatti e ricerca intelligente.
- **Perché l'ho provato.** Le note curate finivano sommerse nella ricerca, e cercavo un sistema più furbo.
- **Perché l'ho lasciato.** Quasi tutti chiedono un modello per estrarre i fatti (lento senza scheda grafica, oppure a consumo), creano una seconda fonte di verità accanto alla mia e i numeri di accuratezza sono quelli dichiarati dal produttore. Uno dipendeva da una libreria archiviata, un altro avrebbe sostituito tutto il motore degli agenti. Il problema vero, misurato, era più semplice: le trascrizioni grezze delle sessioni nell'indice coprivano le note buone.
- **Cosa uso invece.** Un vault di note Markdown come memoria unica: ho tolto dall'indice le trascrizioni grezze e misuro la ricerca con domande fisse. Un motore di ricerca più potente lo valuto solo se questo non basta.
- **Quando a te potrebbe servire.** Se parti da zero, non hai un archivio di note e un servizio a consumo ti va bene: una memoria pronta ti fa risparmiare tempo.
- **Quando.** Novembre 2026.

### Hindsight (memoria condivisa fra assistenti di codice)
- **Cosa prometteva.** Una memoria unica condivisa fra Claude Code, Codex e Cursor, installabile con un comando.
- **Perché l'ho provato.** Mi interessava che i miei assistenti ricordassero le stesse cose.
- **Perché l'ho lasciato.** Valutato e non installato. Come plugin di OpenClaw prendeva il posto della memoria di serie e, per un difetto aperto in quel momento, spegneva la ricerca in memoria degli agenti. Funziona meglio dentro un repository git, e la mia cartella di lavoro non lo è. Di serie manda i dati al suo cloud; la versione in casa, come l'ho trovata, partiva senza autenticazione. E per i riassunti in locale serviva RAM che non avevo libera.
- **Cosa uso invece.** Un revisore notturno delle sessioni che porta le correzioni nella memoria, con il vault come unica fonte.
- **Quando a te potrebbe servire.** Se lavori in un solo repository git con più assistenti di codice e non hai già una memoria tua. In quel caso lo terrei in locale (127.0.0.1) e senza aggiornamenti automatici.
- **Quando.** Settembre 2026.

### Dreaming di OpenClaw (la memoria che si riordina di notte)
- **Cosa prometteva.** Ogni notte l'agente ripassa le conversazioni e salva le cose importanti.
- **Perché l'ho provato.** Era acceso di serie.
- **Perché l'ho lasciato.** Salvava qualcosa di rado, e una volta ha messo nella memoria dell'assistente principale una lista di task vecchia.
- **Cosa uso invece.** Un giro notturno mio che raccoglie i fatti nel vault e un revisore delle sessioni.
- **Quando a te potrebbe servire.** Se hai pochi agenti e nessun sistema di memoria tuo, come punto di partenza.
- **Quando.** Ottobre 2026.

### Import automatico di tutte le memorie degli agenti nel vault (modalità «bridge» di un plugin wiki)
- **Cosa prometteva.** Copiare nel vault le memorie di tutti gli agenti, per averle in un posto solo.
- **Perché l'ho provato.** Era attivo insieme al plugin del wiki.
- **Perché l'ho lasciato.** Riempiva il vault di copie quasi vuote, per lo più report notturni senza contenuto. Quelle copie finivano nella ricerca degli agenti e coprivano le note vere. In più partiva anche solo controllando lo stato con un comando. Ho archiviato le copie (non cancellate) e spento l'import.
- **Cosa uso invece.** Un ponte che copia solo le note curate.
- **Quando a te potrebbe servire.** Con pochi agenti e la funzione dreaming spenta il rumore è molto minore.
- **Quando.** Ottobre 2026.

---

## Ricerca

### Firecrawl in casa (lettura di pagine web)
- **Cosa prometteva.** Una pagina web trasformata in testo pulito, anche più pagine insieme.
- **Perché l'ho provato.** Era il primo metodo dei miei agenti per leggere il web.
- **Perché l'ho lasciato.** L'ho spento e poi tolto del tutto (container, immagini, dati). Agli agenti bastava partire da un browser leggero gratuito. Un motivo più dettagliato non me lo sono scritto.
- **Cosa uso invece.** Lightpanda (browser leggero) come primo metodo, poi un browser completo, poi un servizio a pagamento solo quando serve davvero.
- **Quando a te potrebbe servire.** Se leggi molte pagine in blocco e hai RAM da dedicarci.
- **Quando.** Ottobre 2026.

### Lettura diretta delle pagine (web fetch) come strada di serie per gli agenti
- **Cosa prometteva.** Il modo più semplice per leggere una pagina.
- **Perché l'ho provato.** È lo strumento di serie degli agenti.
- **Perché l'ho lasciato.** Con il fetch diretto a disposizione gli agenti non usavano mai il browser leggero, anche se in prova quello riusciva nella grande maggioranza delle letture. L'ho tolto per vedere se nasce un problema: è una prova, con il ritorno indietro pronto.
- **Cosa uso invece.** Lightpanda come primo metodo.
- **Quando a te potrebbe servire.** Per pagine semplici va benissimo. Toglierlo ha senso solo se vuoi spingere gli agenti verso un metodo che legge meglio.
- **Quando.** Novembre 2026.

### Context7, codebase-memory-mcp, Design DNA, QMD (candidati forti, non installati)
- **Cosa prometteva.** Documentazione aggiornata delle librerie, memoria del codice, stile preso da siti di riferimento, ricerca locale nelle note.
- **Perché l'ho provato.** Erano i candidati più forti di un piano strumenti fatto con molti agenti in parallelo.
- **Perché l'ho lasciato.** Sul mio server nessuno è entrato, perché mancavano le condizioni. Per Context7 avevo un solo caso di errore sulle librerie, già fermato dai controlli. Per codebase-memory-mcp le prove erano deboli e i risparmi dichiarati solo dal produttore. Design DNA non mi serviva in quel momento. QMD lo tengo in attesa: entra solo se la ricerca nella memoria resta sotto una soglia che misuro.
- **Cosa uso invece.** Gli strumenti che ho, misurati prima di cambiarli. Per chi lavora sul PC, QMD lo propongo comunque in una scheda a parte dell'area Ricerca.
- **Quando a te potrebbe servire.** Context7 se il tuo assistente sbaglia spesso le API delle librerie; Design DNA se rifai spesso pagine prendendo lo stile da un sito.
- **Quando.** Novembre 2026.

### Correggere in automatico chi parla nelle trascrizioni delle call
- **Cosa prometteva.** Trascrizioni con il nome giusto su ogni frase.
- **Perché l'ho provato.** Il registratore di call che uso attribuisce spesso le risposte brevi alla persona che ha parlato prima.
- **Perché l'ho lasciato.** Vicolo cieco: le API del servizio non danno l'audio, quindi non si può ritrascrivere con un modello che separa le voci. Una regola automatica tipo «chi nomina sé stesso» trovava al massimo un caso per call.
- **Cosa uso invece.** Leggo le trascrizioni sapendo che l'attribuzione può essere sbagliata.
- **Quando a te potrebbe servire.** Se hai l'audio della call, una ritrascrizione con separazione delle voci risolve.
- **Quando.** Settembre 2026.

---

## Agenti e modelli

### Modelli a consumo come base di tutto (OpenRouter e un modello economico di riserva)
- **Cosa prometteva.** Tutti i modelli con una chiave sola, pagando solo quello che si usa, e un modello economico sempre pronto come riserva quando l'abbonamento finisce.
- **Perché l'ho provato.** Era la configurazione di partenza: un modello economico a consumo come modello di serie e riserva di tutti gli agenti, e qualche script spostato lì per comodità.
- **Perché l'ho lasciato.** Voglio un solo canale di spesa: gli abbonamenti che pago già. Le API a consumo per il lavoro di tutti i giorni erano soldi in più che non vedevo arrivare. E ho scoperto che le ricariche piccole costano care: commissione minima fissa e IVA pesano molto sotto i 15 dollari.
- **Cosa uso invece.** Claude Max e ChatGPT in abbonamento, con regole su quale lavoro va a quale modello e riserve dentro l'abbonamento (modelli più piccoli della stessa famiglia). Il consumo resta solo per pochi casi: i video, analisi di massa con la conservazione dei dati spenta, e l'ultima riserva se gli abbonamenti non rispondono.
- **Quando a te potrebbe servire.** Se non hai abbonamenti, lavori a volumi bassi e irregolari o ti serve un modello che gli abbonamenti non danno, il consumo può costare meno di un piano fisso. Se ricarichi, conviene farlo con importi più alti.
- **Quando.** Ottobre 2026, ritoccato a novembre per i video.

### OmniRoute (instradatore verso le quote gratuite di molti fornitori)
- **Cosa prometteva.** Tantissimi token gratis sommando i piani di prova di molti fornitori, passando da un punto solo.
- **Perché l'ho provato.** Volevo far leggere molti giorni di trascrizioni senza consumare l'abbonamento.
- **Perché l'ho lasciato.** I piani gratuiti dei fornitori possono usare i dati per addestrare i modelli: con dati di clienti è un rischio che non prendo. Passa dai fornitori con accessi non ufficiali, e va contro la mia regola di usare gli abbonamenti che pago. I «token gratis» erano solo la somma delle quote di prova. Quando l'ho acceso, è rimasto per settimane senza fornitori collegati e senza richieste: occupava solo memoria. L'ho tolto dal server, con una copia in archivio.
- **Cosa uso invece.** Gli abbonamenti; per grandi volumi di dati di clienti, un servizio a consumo con la conservazione dei dati spenta.
- **Quando a te potrebbe servire.** Per prove personali su contenuti pubblici, senza dati di clienti, se accetti il rischio sull'account e non hai abbonamenti.
- **Quando.** Fermato a ottobre 2026, tolto a novembre 2026.

### Un servizio a consumo come strada principale per immagini e video (MuAPI)
- **Cosa prometteva.** Tanti modelli di immagine e video in un posto, pagando a generazione.
- **Perché l'ho provato.** È stata la mia prima strada per i media.
- **Perché l'ho lasciato.** Per le immagini pagavo già ChatGPT e l'abbonamento restava fermo, mentre il servizio costava a ogni immagine. Per i video il prezzo era quasi uguale a quello di OpenRouter, dove avevo ancora budget. In più cancella i file dopo 30 giorni, quindi vanno sempre copiati altrove.
- **Cosa uso invece.** Immagini generate con l'abbonamento ChatGPT; video su OpenRouter con un tetto di spesa per video; il servizio a consumo solo per musica, effetti audio, lipsync, rimozione dello sfondo e poco altro.
- **Quando a te potrebbe servire.** Se non hai un abbonamento ChatGPT, o ti serve un modello di immagine particolare, è una buona vetrina a consumo con un conto solo.
- **Quando.** Ottobre 2026.

### La prima squadra di agenti con nomi propri (un agente per tipo di lavoro, tanti agenti)
- **Cosa prometteva.** Un agente specializzato per ogni compito, ognuno con la sua personalità e il suo nome.
- **Perché l'ho provato.** È stata la mia prima squadra.
- **Perché l'ho lasciato.** Ho messo a confronto la squadra vecchia e una nuova, organizzata per ruoli, con circa 30 prove: stessi compiti, tre modelli. Con la squadra per ruoli l'assistente principale delegava di più e meglio (la ricerca a chi la sa fare, il revisore giusto), ed era più veloce sui lavori in più passi. Nessuna delle due ha finito una landing da sola. In più ogni delega costa contesto e ogni agente in più va mantenuto. La regola che ne è uscita: un ruolo diventa un agente solo se serve un permesso diverso, un modello diverso, occhi puliti per controllare o lavoro in parallelo. Il resto lo faccio con pipeline e skill.
- **Cosa uso invece.** Agenti che si chiamano come il loro mestiere (PM, Designer, Tecnico, Ricercatore, Archivista…).
- **Quando a te potrebbe servire.** Se l'agente parla con clienti o con il team come una figura riconoscibile, un nome proprio aiuta. Il punto, per me, è non moltiplicarli.
- **Quando.** Ottobre 2026.

### Un agente dedicato per ogni collaboratore o cliente
- **Cosa prometteva.** Ognuno ha il suo assistente, con la sua memoria e i suoi permessi.
- **Perché l'ho provato.** Era la strada più naturale quando ho dato accesso agli agenti ad altre persone.
- **Perché l'ho lasciato.** Moltiplicare gli agenti costa RAM e manutenzione, e i permessi per me non devono stare dentro l'agente ma in una tabella.
- **Cosa uso invece.** Agenti per ruolo condivisi, sessioni separate per canale, una tabella degli accessi e una memoria unica con ricerca filtrata per persona.
- **Quando a te potrebbe servire.** Se hai due o tre persone con bisogni molto diversi che non condividono dati, un agente a testa può essere più semplice da capire.
- **Quando.** Ottobre 2026.

### Framework per agenti alternativi (Claude Agent SDK, Mastra, LangGraph, CrewAI, Inngest, Temporal, Archon, n8n come motore)
- **Cosa prometteva.** Orchestrazione più strutturata, flussi durevoli, più controllo.
- **Perché l'ho provato.** Li ho valutati quando ho riorganizzato agenti, skill e pipeline.
- **Perché l'ho lasciato.** Per una micro-agenzia con un solo server nessuno conveniva più di quello che avevo. Il valore sta nei miei file (regole, memoria, skill, pipeline in formati standard), non nel motore: così il motore resta sostituibile senza riscrivere tutto.
- **Cosa uso invece.** OpenClaw come motore (canali, sessioni, cron, chiamate ai modelli), senza toccarne il codice, con un piccolo adattatore mio; n8n solo per le approvazioni delle persone.
- **Quando a te potrebbe servire.** Con un team tecnico, più server o flussi che devono sopravvivere a riavvii lunghi, un framework come Temporal o LangGraph può valere lo sforzo.
- **Quando.** Ottobre 2026.

### Un modello veloce che smista le richieste prima dell'assistente principale
- **Cosa prometteva.** Risposte più rapide: un modello piccolo e quasi gratuito decide dove mandare ogni richiesta.
- **Perché l'ho provato.** Il mio assistente principale era lento a rispondere.
- **Perché l'ho lasciato.** Il modello era davvero veloce ed economico, ma la lentezza veniva dal contesto enorme che l'assistente ricarica a ogni turno, non dalla scelta di dove mandare la richiesta. E la «sicurezza» che un modello dichiara sulle sue scelte non è un'accuratezza misurata. Un classificatore sceglie fra opzioni date: non è una memoria.
- **Cosa uso invece.** Lavoro sul contesto (meno skill caricate, memoria più pulita) e uno smistatore a parole chiave.
- **Quando a te potrebbe servire.** Se hai tantissime richieste ripetitive di pochi tipi ben distinti, un classificatore davanti può far risparmiare, purché tu ne misuri l'accuratezza su 100-200 casi veri etichettati.
- **Quando.** Ottobre 2026, confermato a novembre.

### Lasciare al modello economico anche i casi incerti
- **Cosa prometteva.** Finire tutta un'analisi in automatico, a costo quasi zero.
- **Perché l'ho provato.** In un'analisi di massa su molti messaggi, il modello economico aveva lasciato centinaia di casi «non chiari».
- **Perché l'ho lasciato.** Con poco contesto un modello piccolo lascia molti incerti. Riletti da un modello forte con più contesto, i non chiari sono scesi da 580 a 26: erano risposte di bot, riepiloghi automatici, thread di approvazione. Una lettura attenta trova schemi che il modello economico non vede.
- **Cosa uso invece.** Prima regole fisse, poi il modello economico solo sui grandi volumi, poi un modello forte sui casi rimasti; ogni decisione diventa una regola rilanciabile, con il perché scritto.
- **Quando a te potrebbe servire.** Se i casi incerti sono pochi o l'errore costa poco, lasciarli al modello economico va benissimo.
- **Quando.** Ottobre 2026.

### Delegare ai modelli dell'altro abbonamento con la strada più comoda
- **Cosa prometteva.** Mandare i lavori lunghi a ChatGPT con una chiamata sola, direttamente dalla chat con l'assistente.
- **Perché l'ho provato.** Era il modo più comodo per delegare.
- **Perché l'ho lasciato.** Da quella strada gli agenti partivano senza poter usare la riga di comando e si bloccavano, oppure ricadevano sul modello di serie e consumavano l'altro abbonamento. Risultato: il limite di ChatGPT restava quasi intatto mentre lo pagavo. Le regole scritte come promemoria non sono bastate, quindi ho messo un blocco senza eccezioni.
- **Cosa uso invece.** Lancio dalla riga di comando con il modello indicato in modo esplicito, un hook che ferma ogni altro lancio, e il controllo che la sessione usi davvero il piano in abbonamento.
- **Quando a te potrebbe servire.** Se la tua piattaforma dà gli stessi strumenti anche alla strada comoda, può funzionare. Io controllerei comunque che il lavoro finisca davvero sul modello e sul piano che credi.
- **Quando.** Ottobre 2026.

### Laya (modello di decisione open source)
- **Cosa prometteva.** Un modello che sceglie fra opzioni o dice sì/no con una percentuale di sicurezza, gratis e in locale.
- **Perché l'ho provato.** Volevo smistare in automatico le richieste di assistenza senza pagare un modello grande.
- **Perché l'ho lasciato.** In parcheggio. Senza addestramento indovinava meno del caso, ci volevano migliaia di esempi etichettati per renderlo utile, e senza scheda grafica impiegava quasi un minuto a decisione.
- **Cosa uso invece.** La versione a pagamento dello stesso tipo di modello, solo per filtrare una coda piccola.
- **Quando a te potrebbe servire.** Se hai già migliaia di esempi etichettati e una GPU, e vuoi un classificatore tutto in casa.
- **Quando.** Ottobre 2026.

### Un agente dedicato a controllare il consumo dei modelli
- **Cosa prometteva.** Un agente che decide quale modello usare e tiene sotto controllo i token.
- **Perché l'ho provato.** Un solo agente consumava gran parte dei token del modello più caro, con contesti enormi.
- **Perché l'ho lasciato.** Ho seguito il consiglio di non aggiungere un agente: un controllo obbligatorio e regole comuni valgono per tutto il sistema, mentre un agente in più è un altro pezzo da sorvegliare.
- **Cosa uso invece.** Sotto-agenti economici per i lavori meccanici, avvisi automatici quando il contesto cresce, regole su quale lavoro va a quale modello.
- **Quando a te potrebbe servire.** Se molte persone lanciano lavori senza regole comuni, un controllore centrale può avere senso.
- **Quando.** Ottobre 2026.

---

## Automazioni

### Controllare chat e canali a orario fisso
- **Cosa prometteva.** Semplice da costruire: ogni tot minuti si guarda se è arrivato qualcosa.
- **Perché l'ho provato.** Alcuni miei controlli su chat e canali erano nati così.
- **Perché l'ho lasciato.** Voglio che memoria e avvisi si aggiornino quasi in tempo reale, senza giri e chiamate inutili. Anche quando il costo del controllo a orario è trascurabile, per me la regola resta: ogni cosa parte da un evento.
- **Cosa uso invece.** Trigger: un servizio che riceve gli eventi in tempo reale per Slack, un webhook per WhatsApp. Il timer resta solo come riserva lenta, a ore, per gli eventi persi.
- **Quando a te potrebbe servire.** Se il servizio non manda eventi o ti basta un aggiornamento al giorno, un controllo a orario è più semplice e va benissimo.
- **Quando.** Novembre 2026.

### Trascrivere i vocali con il mio Whisper come prima scelta
- **Cosa prometteva.** Trascrizioni sotto il mio controllo, sempre disponibili.
- **Perché l'ho provato.** Era la strada già pronta per vocali e video.
- **Perché l'ho lasciato.** Alcuni servizi di chat fanno già la loro trascrizione: rifarla consuma risorse per un lavoro che il servizio dà gratis, e due logiche per la stessa cosa sono doppio lavoro. Va detto che, sui vocali che ho controllato, la trascrizione del servizio era pronta solo per una piccola parte: la mia resta necessaria come riserva.
- **Cosa uso invece.** Prima la trascrizione del servizio via API, Whisper solo dove manca.
- **Quando a te potrebbe servire.** Se il tuo servizio non trascrive, o lo fa male in italiano, Whisper come prima scelta è la strada giusta.
- **Quando.** Novembre 2026.

### Far decidere il «rosso» di un controllo al giudizio libero di un'AI
- **Cosa prometteva.** Un'AI guarda gli screenshot di una landing e segnala i problemi.
- **Perché l'ho provato.** Era il controllo automatico delle mie landing.
- **Perché l'ho lasciato.** Bastava una parola nella frase libera del modello per far scattare l'allarme grave, e lo screenshot partiva prima che la pagina finisse di disegnarsi. Ho imparato anche un'altra cosa: affidare tutta la correzione a un agente in un compito unico e lungo non funziona, meglio passi piccoli e un controllo dei file alla fine.
- **Cosa uso invece.** Controlli deterministici per il rosso; il giudizio dell'AI solo come nota da leggere.
- **Quando a te potrebbe servire.** Il giudizio di un'AI va bene come segnalazione da leggere, non come allarme.
- **Quando.** Settembre 2026.

### Collegare n8n a Google con l'app OAuth lasciata in «Testing»
- **Cosa prometteva.** Collegare le automazioni a Google in pochi minuti.
- **Perché l'ho provato.** È la configurazione che si ottiene di serie.
- **Perché l'ho lasciato.** Con l'app in «Testing» Google fa scadere il collegamento ogni 7 giorni e le automazioni si fermano, spesso di notte. Vicoli ciechi: un client di tipo Desktop dà errore di redirect, e rilanciare senza ricollegare fallisce allo stesso punto.
- **Cosa uso invece.** Un client OAuth di tipo Web con la schermata di consenso pubblicata.
- **Quando a te potrebbe servire.** Va bene solo per una prova di pochi giorni.
- **Quando.** Settembre 2026.

### Far lavorare l'AI dentro il mio browser per operare sui gestionali
- **Cosa prometteva.** Fare qualsiasi operazione anche dove non c'è un'API, cliccando come farei io.
- **Perché l'ho provato.** Su alcuni gestionali (corsi online, CRM, email) l'AI aveva iniziato a usare il browser.
- **Perché l'ho lasciato.** È lento, usa la mia sessione, e non voglio che il mio browser venga pilotato. Spesso l'API c'era, o c'era già uno strumento che leggeva i dati: bastava cercarlo prima.
- **Cosa uso invece.** API ufficiali o strumenti che leggono via API; dove l'API non arriva, l'AI mi prepara testo e passi e l'operazione la faccio io.
- **Quando a te potrebbe servire.** Se usi un sistema senza API e accetti che l'agente lavori in un profilo del browser separato dal tuo, può farti risparmiare ore.
- **Quando.** Settembre 2026, ribadito a ottobre.

### NocoDB come database operativo (task, contatti, progetti)
- **Cosa prometteva.** Un database con interfaccia tipo foglio di calcolo e API pronte.
- **Perché l'ho provato.** Per mesi ci sono stati task, contatti, progetti e ore.
- **Perché l'ho lasciato.** Ho misurato: in 30 giorni nessun accesso dal browser, tutto passava dagli script, e le sue API erano lente (oltre un secondo e mezzo per leggere tutte le task, contro circa un decimo di secondo leggendo il database direttamente). L'interfaccia che lo giustificava non la usava nessuno.
- **Cosa uso invece.** Postgres diretto, con un piccolo adattatore che parla lo stesso formato delle vecchie API: i programmi hanno cambiato solo la funzione di chiamata. NocoDB è spento, non cancellato.
- **Quando a te potrebbe servire.** Se tu o il tuo team aprite davvero i dati a mano ogni giorno e non avete uno sviluppatore, è un buon modo per avere un database con un'interfaccia semplice.
- **Quando.** Novembre 2026.

---

## Sicurezza

### Strumenti che custodiscono i token del mio abbonamento o i cookie dei miei account
- **Cosa prometteva.** Usare l'abbonamento Claude da altri programmi, revisioni incrociate fra modelli, accesso ai social senza API (esempi valutati: Claudex, claudexor, Agent Reach).
- **Perché l'ho provato.** Li ho guardati quando ho affiancato ChatGPT a Claude e cercavo modi di farli lavorare insieme.
- **Perché l'ho lasciato.** Custodiscono i token di accesso dell'abbonamento o i cookie degli account: se qualcosa va storto rischio l'account. Uno faceva solo revisione incrociata e lo scanner di sicurezza gli dava il punteggio di rischio massimo. Altri mandano fuori le sessioni.
- **Cosa uso invece.** Il login ufficiale di ChatGPT negli strumenti che lo prevedono, e un controllo di sicurezza (SkillSpector) prima di installare qualunque cosa presa da fuori.
- **Quando a te potrebbe servire.** Su account di prova, senza dati veri e senza abbonamenti a cui tieni, per sperimentare.
- **Quando.** Ottobre e novembre 2026.

### Servizi a consumo o che mandano fuori i dati (revisori di codice in cloud, scraper e ricerca a pagamento, agenti in cloud)
- **Cosa prometteva.** Revisione del codice, ricerca sul web, scraping e automazioni pronte, senza costruire niente (esempi valutati: Strix, PR-Agent, CodeRabbit, Exa, Firecrawl cloud, Browserbase, Manus).
- **Perché l'ho provato.** Comparivano nelle classifiche e nelle segnalazioni che raccolgo.
- **Perché l'ho lasciato.** Costano a consumo, oppure i dati escono dal mio server. Uno, in più, pubblicava le porte con Docker in un modo che scavalca il firewall. Li riapro solo con una decisione di spesa esplicita.
- **Cosa uso invece.** Una revisione fatta da un agente revisore sugli abbonamenti e strumenti di lettura web già installati.
- **Quando a te potrebbe servire.** Se non hai un server tuo né abbonamenti e i tuoi dati non sono sensibili, ti danno risultati subito, pagando poco a uso.
- **Quando.** Novembre 2026.

### Plugin con permessi da amministratore per far lavorare l'AI su WordPress
- **Cosa prometteva.** Accesso completo dell'AI ai siti, codice compreso.
- **Perché l'ho provato.** L'ho trovato già installato su alcuni siti che seguo.
- **Perché l'ho lasciato.** Con permessi da amministratore, chi ruba la chiave dal server può comandare tutti i siti.
- **Cosa uso invece.** Un plugin dedicato che tocca solo i contenuti, con una chiave per sito che si stacca con un clic e aggiornamenti solo firmati.
- **Quando a te potrebbe servire.** Per bug e lavori su misura fatti da uno sviluppatore, non per un'AI che lavora da sola.
- **Quando.** Novembre 2026.

### Bloccare gli strumenti degli agenti con una lista «deny» nella configurazione del motore
- **Cosa prometteva.** Togliere a un agente gli strumenti pericolosi con una riga di configurazione.
- **Perché l'ho provato.** È il modo documentato per limitare un agente.
- **Perché l'ho lasciato.** Vicolo cieco, nel mio caso: sugli agenti che girano attraverso la riga di comando di Claude con l'abbonamento, quella lista non toccava gli strumenti nativi (shell, lettura file, web). Decideva un'altra regola: senza sandbox tutto permesso, con la sandbox tutto negato.
- **Cosa uso invece.** La sandbox e le regole di esecuzione del motore degli agenti.
- **Quando a te potrebbe servire.** Sugli agenti che usano i modelli via API la lista funziona. In ogni caso proverei il blocco con un caso finto prima di fidarmi.
- **Quando.** Ottobre 2026.

### Fidarsi di una scansione «pulita» senza guardare cosa ha letto
- **Cosa prometteva.** Lo scanner dice «nessuna chiave trovata»: tutto a posto.
- **Perché l'ho provato.** Era la verifica di sicurezza dei miei repository.
- **Perché l'ho lasciato.** La scansione aveva letto zero commit: git rifiutava i repository di un altro utente e l'errore finiva nascosto. Il «pulito» era falso.
- **Cosa uso invece.** Controllo sempre quanti file o commit sono stati letti e non butto via i messaggi d'errore.
- **Quando a te potrebbe servire.** Vale per qualunque scanner: un risultato vuoto lo verifico prima di crederci.
- **Quando.** Ottobre 2026.

### find-skills e context-mode
- **Cosa prometteva.** Trovare e installare skill al volo; gestione furba del contesto.
- **Perché l'ho provato.** Comparivano nei contenuti che salvo per valutarli.
- **Perché l'ho lasciato.** find-skills installa le skill con conferma automatica, saltando il controllo di sicurezza che faccio su tutto quello che arriva da fuori. context-mode aveva una licenza poco chiara.
- **Cosa uso invece.** Un mio comando che cerca soltanto, senza installare, poi controllo di sicurezza e lettura prima di ogni installazione.
- **Quando a te potrebbe servire.** find-skills su una macchina di prova, senza dati sensibili.
- **Quando.** Ottobre 2026.

### rtk (compressore dei comandi per risparmiare token)
- **Cosa prometteva.** Meno token consumati, riscrivendo i comandi e comprimendo l'output.
- **Perché l'ho provato.** Cercavo di ridurre il consumo.
- **Perché l'ho lasciato.** Non installato: riscrive tutti i comandi e comprime l'output, mentre a me servono gli errori esatti. In più modifica le impostazioni di Claude Code, e lo scanner di sicurezza gli dava il punteggio di rischio massimo.
- **Cosa uso invece.** Sotto-agenti economici per i lavori meccanici e un avviso quando il contesto cresce troppo.
- **Quando a te potrebbe servire.** Se usi le API a consumo e conti ogni token, dopo una prova controllata.
- **Quando.** Ottobre 2026.

---

## Canali

### Il canale WhatsApp di serie del motore degli agenti
- **Cosa prometteva.** Parlare con l'assistente principale da WhatsApp, passando dal motore degli agenti (OpenClaw).
- **Perché l'ho provato.** Era il modo in cui parlavo con l'assistente dal telefono.
- **Perché l'ho lasciato.** Ho preferito parlare su WhatsApp direttamente con Claude Code, che gestisce tutto il resto. L'assistente principale è rimasto sugli altri canali.
- **Cosa uso invece.** Un piccolo servizio mio, su OpenWA, collegato a Claude Code, che risponde solo al mio numero.
- **Quando a te potrebbe servire.** Se usi solo OpenClaw e non Claude Code, il canale di serie è la strada più semplice.
- **Quando.** Ottobre 2026.

### Open WebUI o un'app desktop per parlare con l'assistente
- **Cosa prometteva.** Una chat sul computer collegata a tutto il sistema.
- **Perché l'ho provato.** Mi sono chiesto se mi servisse un'interfaccia mia sul PC.
- **Perché l'ho lasciato.** Open WebUI non può usare Claude Code senza un ponte che riusa il login, e i termini del servizio non lo permettono. Con le chiavi API pagherei a consumo. Collegato agli agenti, sarebbe stato un doppione della pagina dell'assistente che ho già.
- **Cosa uso invece.** Claude Code, la pagina dell'assistente nella mia bacheca, WhatsApp.
- **Quando a te potrebbe servire.** Se usi modelli locali o chiavi API e vuoi una chat unica per il team.
- **Quando.** Novembre 2026.

### Un bot che entra da solo nelle call di Google Meet
- **Cosa prometteva.** L'assistente entra nella call, registra, legge e scrive in chat.
- **Perché l'ho provato.** Quasi tutte le mie call sono su Meet e non volevo pagare un servizio a ore.
- **Perché l'ho lasciato.** Google blocca il browser automatizzato («You can't join this video call»), e non dipende dall'indirizzo IP né dalla videocamera finta. Non ho voluto aggirare il controllo anti-bot.
- **Cosa uso invece.** Un registratore di call già pronto (Fathom).
- **Quando a te potrebbe servire.** Se ti va bene un servizio come Recall (il bot si vede in call) o una registrazione fatta dal browser di chi partecipa.
- **Quando.** Novembre 2026.

### Accesso remoto con Tailscale ai PC del team
- **Cosa prometteva.** Entrare da remoto nei PC per configurarli e lanciarci lavori.
- **Perché l'ho provato.** Volevo preparare un portatile a distanza e collegare un modello di codice sul mio PC.
- **Perché l'ho lasciato.** Per il portatile serviva un piano a pagamento per le etichette, e il PC era finito nella rete sbagliata. Per il mio PC non serviva: avevo già un accesso SSH a tempo.
- **Cosa uso invece.** Claude Code installato sul portatile con un brief scritto; SSH a tempo verso il mio PC.
- **Quando a te potrebbe servire.** Se gestisci da remoto molti PC del team, in modo stabile.
- **Quando.** Novembre 2026.

---

## Skill e strumenti presi da fuori

### Una skill di design «riassunta» che prende il meglio di quattro
- **Cosa prometteva.** Meno testo da leggere per l'agente, regole di design concentrate in un file solo.
- **Perché l'ho provato.** Volevo che gli agenti usassero davvero le skill, e l'idea era fonderne quattro in una mia.
- **Perché l'ho lasciato.** Prova A/B su una landing vera: la versione riassunta è uscita piatta; la skill originale usata intera (script, guide, revisore separato) ha dato molto più carattere. Riassumere toglie proprio i dettagli che fanno la differenza.
- **Cosa uso invece.** Le skill di design intere, nominate tutte nei brief, più un riferimento visivo.
- **Quando a te potrebbe servire.** Se il tuo agente ha poco contesto o fai pagine molto semplici, una versione corta può bastare: io la proverei contro l'originale prima di decidere.
- **Quando.** Ottobre 2026.

### Controlli automatici obbligatori su ogni bozza di pagina (Lighthouse, axe, screenshot da telefono)
- **Cosa prometteva.** Qualità delle pagine garantita da punteggi automatici.
- **Perché l'ho provato.** Me li avevano proposti come rimedio ai difetti delle consegne.
- **Perché l'ho lasciato.** Erano già nelle istruzioni dell'agente che fa le pagine e non vedono i difetti veri, che sono di giudizio (spazi, gerarchia, testi). E il controllo da telefono sulle bozze va contro il mio ordine di lavoro: prima approvo il design da desktop, poi si fa la versione per telefono.
- **Cosa uso invece.** Una revisione visiva fatta da un agente separato, e in prova una lista dei difetti ricorrenti con uno script che li cerca.
- **Quando a te potrebbe servire.** Su siti già approvati e online, per accessibilità e velocità, sono utili.
- **Quando.** Novembre 2026.

### Usare i testi e lo stile tipografico che genera Stitch
- **Cosa prometteva.** Sezioni di pagina pronte, con layout e testi.
- **Perché l'ho provato.** Uso Stitch per esplorare il layout delle sezioni.
- **Perché l'ho lasciato.** Il layout lo tengo (sfondi, card, gerarchia visiva). Scarto i testi e i numeri, perché li inventa, e il suo maiuscolo largo, che non mi piace: il mio font resta.
- **Cosa uso invece.** Stitch solo come spunto di layout, poi adattato al mio stile, al mio font e ai miei testi.
- **Quando a te potrebbe servire.** Per un prototipo veloce da buttare, i suoi testi vanno bene come segnaposto.
- **Quando.** Novembre 2026.

### Le slide per le call di formazione a due
- **Cosa prometteva.** Una presentazione ordinata per spiegare un processo.
- **Perché l'ho provato.** Preparando una call di formazione mi sono chiesto se servissero.
- **Perché l'ho lasciato.** In una call a due lo scopo è che l'altro impari a fare da solo; con le slide parlo io. E io mi perdo quando devo guidare una conversazione: mi serve una traccia con le frasi già scritte.
- **Cosa uso invece.** Una pagina «una frase alla volta» con il tasto Avanti, domande scritte per esteso e frasi di riserva sempre visibili.
- **Quando a te potrebbe servire.** Per una presentazione vera a più persone, le slide restano la scelta giusta.
- **Quando.** Novembre 2026.

### Proporre a un cliente uno strumento diverso dal mio senza un motivo verificato
- **Cosa prometteva.** Un sistema di login più leggero (Authelia invece di Authentik, nel caso che ho visto).
- **Perché l'ho provato.** L'AI l'aveva proposto per il server di un cliente senza guardare il server.
- **Perché l'ho lasciato.** Non c'era un motivo valido: il server aveva memoria in abbondanza. Una differenza non giustificata fa perdere fiducia nella proposta. A me interessa che lo strumento sia il più funzionale e sicuro possibile, non quale sia.
- **Cosa uso invece.** Lo stesso strumento che uso io, salvo un motivo verificato sul server e scritto nella proposta.
- **Quando a te potrebbe servire.** Su un server piccolo con poca memoria, un sistema di login più leggero può essere davvero la scelta giusta.
- **Quando.** Autunno 2026.

### L'MCP ufficiale di Figma dentro gli agenti di OpenClaw
- **Cosa prometteva.** Gli agenti leggono e scrivono i file Figma.
- **Perché l'ho provato.** Volevo rivedere le landing su Figma insieme all'agente che fa le pagine.
- **Perché l'ho lasciato.** Figma accetta solo i client del suo catalogo; OpenClaw si presenta come client nuovo e viene rifiutato. Anche la strada del plugin in un browser senza schermo è bloccata, e cambiare l'identità del browser vorrebbe dire aggirare un controllo: non l'ho fatto.
- **Cosa uso invece.** Figma da un client ammesso (Claude Code o Codex).
- **Quando a te potrebbe servire.** Se usi direttamente Claude Code o Codex, l'MCP ufficiale funziona.
- **Quando.** Ottobre 2026.

### mimik (guide a clic registrate in automatico)
- **Cosa prometteva.** Registra i clic nel browser e produce una guida passo passo con gli screenshot.
- **Perché l'ho provato.** Volevo fare guide per i clienti più in fretta. L'ho provato io.
- **Perché l'ho lasciato.** Funziona, ma i testi escono in inglese e grezzi, la sfocatura copre solo email, telefoni e carte, e non registra le pagine interne di Chrome. Lo scanner di sicurezza diceva «non installare», con molte segnalazioni ancora da rileggere, e il numero di guide che lo avrebbe giustificato non c'era. Non è chiuso per sempre: resta in lista per quando servirà una guida su un sistema che non raggiungo in altro modo.
- **Cosa uso invece.** Guide scritte con mappe e screenshot.
- **Quando a te potrebbe servire.** Se fai spesso guide in inglese su strumenti web semplici, con un profilo del browser separato e senza dati sensibili a schermo.
- **Quando.** Novembre 2026.

### Strumenti e offerte con promesse gonfiate (GPU gratis, piani studente, prompt miracolosi, finte estensioni)
- **Cosa prometteva.** Potenza di calcolo gratis, modelli premium gratis, risultati garantiti con un prompt.
- **Perché l'ho provato.** Arrivano da reel e segnalazioni che salvo per valutarli.
- **Perché l'ho lasciato.** Alla verifica erano gonfiati, falsi o porte d'ingresso per vendere altro. Un esempio: una presunta «estensione potente per Claude Code» era in realtà una chat per aggirare le regole dei modelli, usata per raccogliere follower.
- **Cosa uso invece.** Una lista di segnalibri da consultare (raccolte pubbliche di API, MCP e app), senza installare niente.
- **Quando a te potrebbe servire.** Raramente. Se uno ti incuriosisce, guarderei chi lo pubblica e cosa vende dopo, e leggerei il codice prima di fidarmi.
- **Quando.** Ottobre e novembre 2026.

### Strumenti che rifanno quello che ho già (doppioni e progetti fermi)
- **Cosa prometteva.** Agenti di codice alternativi, costruttori di flussi, scraper, scaricatori di video, gestione task, squadre di agenti pronte (esempi: OpenHands, Aider, langflow, open-flow, Scrapling, cobalt, TaskView, agency-agents).
- **Perché l'ho provato.** Li ho valutati nei giri di ricerca strumenti.
- **Perché l'ho lasciato.** Rifacevano cose che ho già: i flussi con n8n, i download video con yt-dlp, la bacheca delle task. Uno risultava archiviato, quindi non più mantenuto. Un altro strumento per il browser funzionava solo con Claude Code, e gli agenti su altri modelli non lo vedevano. Da agency-agents ho preso solo qualche spunto per i ruoli, senza installarlo.
- **Cosa uso invece.** Gli strumenti già installati, rivalutati quando c'è un lavoro vero che li richiede.
- **Quando a te potrebbe servire.** Se non hai ancora niente di equivalente, alcuni sono ottimi punti di partenza (per esempio langflow, se non usi n8n).
- **Quando.** Ottobre e novembre 2026.
