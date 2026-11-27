# Catalogo «Cosa uso io» — elenco da cui si sceglie

File generato da `scripts/genera_indice_catalogo.py`: non modificarlo a mano, rilancia lo script.
Formato: `slug` (dove gira, livello, tono minimo): titolo. La scheda intera sta in `catalogo/<famiglia>/<slug>.md`
della repo del kit; il pacchetto, quando c'e', in `pacchetti/<slug>/LEGGIMI.md`.

Dove gira: **PC** = sono file, funziona anche a PC spento; **PC acceso** = gira solo quando il PC è acceso;
**server** = serve un computer sempre acceso (per queste c'è solo l'idea, niente pacchetto).

## Contesto
- `hook-contesto-avviso-e-compressione` (PC, base, T0): Avviso di contesto e compressione automatica
- `hook-handoff-prima-compressione` (PC, medio, T1): HANDOFF salvato quando la sessione viene compressa
- `hook-stato-a-inizio-sessione` (PC, base, T0): Stato vero nel contesto a inizio sessione
- `hook-statusline-contesto` (PC, base, T0): Riga di stato con modello, contesto e limiti
- `memoria-claude-md-a-sezioni` (PC, base, T0): Un CLAUDE.md a sezioni fisse
- `memoria-handoff-e-sistema` (PC, base, T0): HANDOFF.md e SISTEMA.md per ogni cliente lungo

## Memoria
- `memoria-fatti-da-chat-e-vocali` (PC, medio, T1): Fatti da chat e vocali verso il vault
- `memoria-fatti-vs-correzioni` (PC, base, T0): Fatti nel vault, correzioni nella memoria
- `memoria-raccolta-sessioni` (PC acceso, medio, T1): Raccolta delle richieste fatte nelle altre sessioni
- `memoria-riordino-handoff` (PC, medio, T1): Riordino: dai diari di lavoro alla scheda dei fatti
- `memoria-vault-etichette-alla-nascita` (PC, medio, T1): Vault con cartelle fisse ed etichette alla nascita

## Correzioni
- `impara-regole-base-uniche` (PC, medio, T1): Regole base uniche per tutti gli agenti, ricopiate da sole
- `impara-regole-proposte-con-ok` (PC acceso, medio, T1): Regole proposte di notte, fisse solo dopo il mio ok
- `impara-skill-migliorate-dalle-sessioni` (PC acceso, avanzato, T2): Skill che migliorano leggendo le sessioni, adottate da me
- `memoria-archivista-correzioni-agli-agenti` (server, avanzato, T3): L'archivista porta le correzioni agli agenti — senza pacchetto (nessuno: solo idea)
- `memoria-feedback-why-how` (PC, base, T0): File di correzione con Why e How to apply
- `memoria-indice-e-regole-doro` (PC, base, T0): Memoria a file, indice compatto e Regole d'oro
- `memoria-revisore-notturno` (PC, medio, T1): Revisore notturno delle sessioni

## Metodo
- `agenti-esecutore-costruttore` (PC, base, T0): Due sotto-agenti economici: esecutore e costruttore
- `agenti-lavori-lunghi-codex` (PC, medio, T1): Claude decide, ChatGPT (Codex) esegue i lavori lunghi
- `agenti-regia-e-smistamento` (PC, medio, T1): Regia e smistamento: chi fa il lavoro, e chi lo controlla
- `agenti-revisore-prima-di-mandare` (PC, base, T0): Revisore con occhi puliti prima di pubblicare o mandare
- `agenti-sistemista-settimanale` (PC acceso, medio, T1): Sistemista settimanale in sola lettura
- `agenti-squadra-per-ruolo` (server, avanzato, T3): Una squadra di agenti per ruolo, con revisori separati — senza pacchetto (nessuno: solo idea)
- `hook-domanda-breve` (PC, base, T0): Domanda breve: risposta, non lavoro
- `hook-plugin-claude-council` (PC, medio, T1): Plugin claude-council: secondo parere da altri modelli — senza pacchetto (nessuno: plugin di terzi dalla fonte)
- `hook-smistatore-procedure` (PC, medio, T1): Hook smistatore: la procedura giusta al momento giusto
- `canali-board-task` (PC, base, T0): Ogni lavoro è una task: stima, tempo vero, chi ci lavora adesso
- `skill-contro-parere` (PC, base, T0): Un Claude che non mi dà ragione per forza
- `skill-grilling` (PC, base, T0): Grilling: l'intervista prima delle scelte difficili — senza pacchetto (nessuno: skill di terzi dalla fonte)
- `skill-pipeline-di-lavoro` (PC, medio, T1): Pipeline di lavoro: le correzioni non si perdono più
- `skill-roadmap-lavoro` (PC, medio, T1): Roadmap: chi, quando, a che punto siamo
- `skill-stile-risposte` (PC, base, T0): Risposte corte e ordinate (caveman + i-have-adhd in italiano)
- `skill-triage` (PC, base, T0): Triage: cosa faccio prima quando è tutto urgente — senza pacchetto (nessuno: skill di terzi dalla fonte)

## Mestiere
- `skill-animazioni` (PC, medio, T1): Animazioni che si sentono giuste — senza pacchetto (nessuno: skill di terzi dalla fonte)
- `skill-arena` (PC, avanzato, T2): Arena: tante versioni di Claude in gara sullo stesso compito — senza pacchetto (nessuno: skill di terzi dalla fonte)
- `skill-book-to-skill` (PC, medio, T1): Da un libro a una skill — senza pacchetto (nessuno: skill di terzi dalla fonte)
- `skill-brand-e-logo` (PC, base, T0): Brand, voce e logo con metodo — senza pacchetto (nessuno: skill di terzi dalla fonte)
- `skill-copy-italiano` (PC, base, T0): Copy persuasivo, ma in italiano e in regola
- `skill-design-dodici` (PC, medio, T1): Le 12 skill di design e il brief che le nomina tutte
- `skill-media` (PC, medio, T1): Immagini, video e voce: cosa uso e quanto costa
- `skill-pagine-legali` (PC, avanzato, T2): Pagine legali scritte su quello che il sito fa davvero
- `skill-qa-percorso-utente` (PC, medio, T1): Prova della pagina come la usa un utente vero
- `skill-segnalazioni` (server, avanzato, T3): Segnalazioni dal browser con la foto della pagina — senza pacchetto (nessuno: solo idea)
- `skill-suite-gstack-stitch` (PC, avanzato, T2): Suite di skill prese da fuori: gstack e Stitch — senza pacchetto (nessuno: skill di terzi dalla fonte)

## Ricerca
- `ricerca-archivio-soluzioni` (PC, base, T0): Archivio delle soluzioni
- `ricerca-basic-memory` (PC, medio, T1): Alternativa: Basic Memory, memoria che Claude scrive e rilegge — senza pacchetto (nessuno: solo idea)
- `ricerca-call-trascritte` (PC, medio, T1): Call trascritte: ricercabili e senza impegni persi
- `ricerca-filtrata-per-persona` (server, avanzato, T3): Ricerca filtrata per persona — senza pacchetto (nessuno: solo idea)
- `ricerca-inventario-notturno` (PC, base, T0): Inventario di cosa c'è davvero
- `ricerca-per-significato-server` (server, avanzato, T3): Ricerca per significato in tutta la memoria — senza pacchetto (nessuno: solo idea)
- `ricerca-qmd-sul-pc` (PC, medio, T1): Ricerca per significato sul PC con QMD
- `skill-web-research` (PC, base, T0): Ricerche sul web con le fonti accanto

## Automazioni e canali
- `automazioni-ok-dal-telefono` (PC acceso, avanzato, T2): Il lavoro lungo chiede l'ok sul telefono e riparte da solo
- `automazioni-pulizia-sessioni-ferme` (PC acceso, base, T0): Pulizia automatica delle sessioni ferme
- `automazioni-semaforo-consumi` (PC acceso, medio, T1): Semaforo dei consumi: i lavori lunghi si fermano da soli
- `hook-suono-fine-lavoro` (PC, base, T0): Suono quando Claude ha finito o aspetta me
- `hook-tempo-per-task` (PC, medio, T1): Tempo per task, contato dagli hook
- `canali-brief-mattino` (PC acceso, base, T0): Il brief del mattino
- `canali-catalogo-elementi` (PC, base, T0): Un catalogo di tutto quello che produco
- `canali-connettore-telefono` (server, avanzato, T3): Il mio sistema dentro claude.ai, dal telefono — senza pacchetto (nessuno: solo idea)
- `canali-drive-cartelle-cliente` (PC, base, T0): Drive condiviso con le stesse cartelle per ogni cliente
- `canali-giornata-con-ai` (server, avanzato, T3): La mia giornata con l'AI — senza pacchetto (nessuno: solo idea)
- `canali-lavori-in-background` (PC acceso, medio, T1): Lavori lunghi in background, con avviso alla fine
- `canali-lavoro-notte` (PC acceso, medio, T1): Il lavoro della notte, da rivedere al mattino
- `canali-pannello-approvazioni` (PC, medio, T1): Le richieste di ok in un posto solo
- `canali-report-pagine` (PC, base, T0): Come consegno pagine e report
- `canali-slack-tempo-reale` (server, avanzato, T3): Slack e WhatsApp a eventi, non a orario — senza pacchetto (nessuno: solo idea)
- `canali-whatsapp-assistente` (server, avanzato, T3): WhatsApp con il mio assistente, anche a vocali — senza pacchetto (nessuno: solo idea)

## Sicurezza e ripristino
- `hook-guardia-comandi` (PC, medio, T1): Guardia che ferma i comandi sbagliati e spiega quelli giusti
- `hook-guardia-email` (PC, base, T0): Guardia che non fa uscire la mia email verso siti terzi
- `sicurezza-aggiornamenti-mensili` (PC acceso, base, T0): Aggiornamenti mai automatici: un controllo al mese, poi decido io
- `sicurezza-backup-notturno` (PC acceso, medio, T1): Backup notturno con la regola 3-2-1: tre copie, due posti, una fuori casa
- `sicurezza-chiave-finita-online` (PC, base, T0): Se una chiave finisce in una copia online: cosa farei — senza pacchetto (nessuno: solo idea)
- `sicurezza-classificatore-permessi` (PC, base, T0): Quando Claude viene bloccato, si ferma e chiede
- `sicurezza-controlli-salute` (PC acceso, medio, T1): Controlli di salute che avvisano solo quando lo stato cambia
- `sicurezza-copia-settimanale` (PC, base, T0): Una copia a settimana fuori dal computer, senza programmi — senza pacchetto (nessuno: solo idea)
- `sicurezza-copie-datate` (PC, base, T0): Copia datata prima di toccare un file importante
- `sicurezza-niente-password-in-chat` (PC, base, T0): Niente password in chat né nelle note
- `sicurezza-permessi-deny-ask` (PC, base, T0): Permessi: cosa passa da solo, cosa mai, e un livello «chiedi» da provare
- `sicurezza-prova-ripristino` (PC, base, T0): Prova di ripristino: riaprire davvero il backup
- `sicurezza-registro-modifiche` (server, base, T3): Registro delle modifiche sui sistemi dove lavorano più persone
- `sicurezza-scan-prima-di-installare` (PC, medio, T1): Controllo di sicurezza prima di installare skill e MCP presi da fuori — senza pacchetto (nessuno: solo idea)
- `sicurezza-segreti-file-unico` (PC, medio, T1): Le chiavi in un file solo, caricate solo quando servono — senza pacchetto (nessuno: solo idea)
- `sicurezza-utente-separato-agenti` (server, avanzato, T3): Gli agenti lavorano con un utente separato e pochi permessi — senza pacchetto (nessuno: solo idea)
- `sicurezza-versioni-locali` (PC acceso, medio, T1): Versioni locali di pagine e documenti, senza GitHub
- `skill-cerca-strumento` (PC, medio, T1): Valutare uno strumento prima di installarlo
- `skill-sicurezza-codice` (PC, avanzato, T2): Controlli di sicurezza su codice e siti — senza pacchetto (nessuno: skill di terzi dalla fonte)

## Segnale → scheda (scorciatoia)

| Cosa vedi o senti | Scheda da considerare |
|---|---|
| Nessuna copia fuori dal PC, chi inizia o spegne il PC | `sicurezza-copia-settimanale` |
| Nessun remoto git, ultimo salvataggio vecchio, una sola copia | `sicurezza-backup-notturno` |
| Una chiave in un file salvato online (git con remoto, cartella sincronizzata) | `sicurezza-chiave-finita-online` |
| Backup mai riaperto | `sicurezza-prova-ripristino` |
| Chiavi o password dentro le note | `sicurezza-niente-password-in-chat`, `sicurezza-segreti-file-unico` |
| Permessi tutti liberi o tutti da chiedere | `sicurezza-permessi-deny-ask` |
| Modifiche fatte senza una copia prima | `sicurezza-copie-datate`, `sicurezza-versioni-locali` |
| «Glielo ripeto ogni volta» | `memoria-indice-e-regole-doro`, `memoria-feedback-why-how` |
| Correzioni dette tante volte ma mai fissate | `impara-regole-proposte-con-ok`, `memoria-revisore-notturno` |
| CLAUDE.md lungo, disordinato o contraddittorio | `memoria-claude-md-a-sezioni` |
| Fatti e correzioni mescolati, memoria che cresce senza ordine | `memoria-fatti-vs-correzioni` |
| Lavori lunghi rispiegati a ogni sessione | `memoria-handoff-e-sistema`, `hook-handoff-prima-compressione` |
| HANDOFF enormi, fatti stabili sepolti | `memoria-riordino-handoff` |
| «Non trovo più quella nota» | `memoria-vault-etichette-alla-nascita`, `ricerca-qmd-sul-pc` |
| Lo stesso problema tecnico risolto due volte | `ricerca-archivio-soluzioni` |
| «Non ce l'ho» detto su cose che ci sono | `ricerca-inventario-notturno` |
| Impegni presi in call e persi | `ricerca-call-trascritte` |
| Smistamento personale/azienda che sbaglia cartella | `memoria-vault-etichette-alla-nascita`, `hook-smistatore-procedure` |
| Sessioni lunghe che si perdono | `hook-contesto-avviso-e-compressione`, `hook-statusline-contesto` |
| Claude dà sempre ragione | `skill-contro-parere` |
| Risposte troppo lunghe | `skill-stile-risposte` |
| Consumi alti per lavori semplici | `agenti-esecutore-costruttore`, `agenti-regia-e-smistamento` |
| Correzioni che si perdono fra un lavoro e l'altro | `skill-pipeline-di-lavoro` |

Quello che ho provato e lasciato, con il motivo: `catalogo/scartati.md`.
