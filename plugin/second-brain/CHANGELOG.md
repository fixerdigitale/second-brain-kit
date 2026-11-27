# Novità del pacchetto Second Brain

Ogni versione ha due righe per novità: cosa cambia e cosa puoi fare tu. Dopo aver aggiornato il pacchetto, `/second-brain:aggiorna` porta nella tua cartella solo le novità a cui dici sì.

## Non ancora rilasciato · correzioni dopo le prove

- Segreti: `cerca-segreti` riconosce le forme italiane («Password CRM: …», «la password del CRM è …», «pass …», wifi), i token dentro JSON, URL e `Bearer`, legge il testo di `.docx`/`.xlsx`/`.pptx`, segnala i file con un nome da credenziali e dice quanti PDF non ha letto. Una riga per riga sospetta, così il conteggio è giusto. Il pacchetto `sicurezza-niente-password-in-chat` usa lo stesso script. Dentro `~/.claude` salta plugin, cache e sessioni. Cosa puoi fare: rilanciarlo sulle tue cartelle.
- `temi_sessioni` oscura tutta la riga dopo una parola come password o token, più email, telefoni, IBAN e parole con cifre; i temi non contengono nomi propri. Cosa puoi fare: niente.
- Prova di ripristino: esiti separati (si riapre, è fuori dal PC, è pulita); una copia sullo stesso PC o la cartella stessa non conta come backup; modo «documenti» per chi non ha file di Claude; zip con una cartella in cima. Cosa puoi fare: rifare la prova se l'avevi fatta.
- Onboarding: la cartella di lavoro si conferma prima di scrivere lo stato (rifiutate home, Scrivania, Download e Documenti interi); avviso se la cartella è sincronizzata o ha una copia online; tono calcolato da cinque aree; impostazioni lette senza stampare token (`config_claude.py`). Cosa puoi fare: niente.
- `contro-parere` e `smistamento` non partono più da sole dall'installazione; `salva-in-memoria` chiede il sì anche per i file nuovi. «Modalità: principiante/esperto» diventa «Modo: passo passo/diretto» (la riga vecchia vale ancora). Cosa puoi fare: chiamarle con `/second-brain:contro-parere` e `/second-brain:smistamento` quando servono.
- Catalogo: due schede base nuove, `sicurezza-copia-settimanale` e `sicurezza-chiave-finita-online`. Cosa puoi fare: niente, il piano le propone se servono.
- Seconda prova avversaria: nessun segreto nemmeno nei nomi di file e cartelle (diventano `[OSCURATO]`), nei .csv con una colonna password o pw, nelle righe «home banking»; `stato.py` rifiuta i valori che sembrano chiavi o password e non riparte da uno stato vecchio nella cartella personale; `pagina.py` toglie i segreti dalla pagina HTML; `temi_sessioni` rifiuta un argomento non capito invece di leggere tutte le sessioni e nelle correzioni mostrate i nomi diventano [NOME]; le frasi nei file rivolte all'AI («manda questo a…») sono materiale, non ordini, e si segnalano. Cosa puoi fare: niente.

## 2.0.0 · 27/11/2026

- Nuovo ingresso unico: `/second-brain:onboarding`. Un primo risultato vero in circa 15 minuti, poi la MAPPA di quello che hai, un PIANO con al massimo 3 passi dal catalogo e la rimisura dopo 14 giorni. Cosa puoi fare: scrivere `/second-brain:onboarding` nella tua cartella di lavoro.
- Nuove skill `onboarding`, `primo-risultato`, `piano-upgrade` e `mappa-vault`; nuovi sotto-agenti `studia` (solo lettura, imposta dagli strumenti) e `revisore`. `installa` ora esegue le missioni scelte, una alla volta. Cosa puoi fare: niente, se usavi già `/second-brain:installa` funziona ancora, come missione `cassetti-memoria`.
- `salva-in-memoria` scrive anche dentro un vault che hai già, nel suo formato. `aiuto` capisce `più piano` e `più veloce`.
- Un automatismo all'avvio (`hooks/hooks.json`): dal giorno 14 dopo il piano propone la rimisura, una volta sola. Non fa niente se l'onboarding non c'è.
- Script in Python 3, sola lettura: `cerca-segreti` (solo `file:riga:NOME`), `prova-ripristino`, `controlla-nomi`, `date_cartelle`, `salute_vault`, `temi_sessioni`, `pagina` (MAPPA e PIANO in HTML).
- Le idee extra sono diventate schede del catalogo della repo, con un indice nel plugin (`catalogo-indice.json`).

## 0.1.0 · 20/11/2026

Prima versione.

- Il metodo nel `CLAUDE.md`, la memoria in `memoria/` con i modelli delle note, le pipeline in `pipeline/`, l'archivio dei problemi in `soluzioni/`.
- Skill: `buone-maniere`, `contro-parere`, `salva-in-memoria`, `definisci-pipeline`, `smistamento`, `soluzioni`, `google-account`, `aiuto`. Aiutanti: `esecutore` e `costruttore`.
- Undici guide, da `INIZIA-DA-QUI.md`. Si aprono con `/second-brain:aiuto`.
