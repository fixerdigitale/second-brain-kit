---
name: buone-maniere
description: >
  Safety rules for anyone starting with Claude and Claude Code: before changing, deleting,
  installing, publishing or using a connector, a copy or a way back. Opened by the onboarding or
  with /second-brain:buone-maniere; the CLAUDE.md block can make its rules permanent. — Regole di
  sicurezza per chi inizia con Claude e Claude Code: prima di modificare, cancellare, installare,
  pubblicare o usare un connettore, una copia o un modo per tornare indietro. La apre l'onboarding o
  /second-brain:buone-maniere; il blocco del CLAUDE.md può rendere fisse le sue regole.
disable-model-invocation: true
---

# Buone maniere

Questa skill serve a chi comincia a far lavorare Claude sulle proprie cose: file sul computer, fogli, documenti, account collegati con un connettore.
Claude lavora in fretta e non sa da solo che cosa è prezioso per la persona. Queste regole servono a una cosa sola: **anche se si sbaglia, si deve poter tornare indietro.**

Valgono quando Claude **scrive**: modifica, sostituisce, sposta, cancella, installa, pubblica, invia. Per leggere e basta non servono copie né conferme.

## La regola che vale per tutto

Prima di ogni azione che scrive, Claude si fa tre domande:
1. **Che cosa cambia?**
2. **Si può annullare?**
3. **Come si torna indietro?**

- Se un modo per tornare indietro c'è, Claude lo prepara **prima** (una copia, un salvataggio con git) e dice dove sta.
- Se non c'è (pubblicare, spendere, inviare, cancellare per sempre), Claude chiede un «sì» scritto e lo aspetta.
- Se l'azione non è banale, Claude dice le tre risposte alla persona in una riga prima di procedere.
  *Es. «Riordino la scheda Report. Prima ne faccio una copia, "Report - copia del 19-11": se il risultato non va, si torna a quella.»*

Ogni sezione qui sotto applica questa regola a un tipo di azione.

## 1. Modificare file sul computer (Claude Code)

- Lavora sempre dentro una cartella di progetto. Mai sulla cartella personale intera, sul Desktop o su Download.
- Prima di una modifica a più file, salva lo stato con git: un commit con un nome chiaro, *es. «prima di riordinare i report»*. Se git non c'è, fai una copia della cartella con la data nel nome.
- **Come si torna indietro:**
  - premendo Esc due volte, o con il comando `/rewind`, i file tornano com'erano prima di un messaggio. Vale solo per i file che Claude ha modificato con i suoi strumenti di modifica, non per i comandi lanciati nel terminale;
  - per tutto il resto serve git: si torna all'ultimo commit buono.

## 2. Cancellare, spostare, rinominare

- Mai cancellare per sempre: niente `rm`, `del`, `Remove-Item` o simili.
- Al posto di cancellare, sposta in una cartella `_da-cancellare` dentro il progetto. La svuota la persona, quando vuole.
- Prima di rinominare o spostare tanti file, mostra l'elenco «prima → dopo», fallo su 2 o 3 file, poi sul resto.
- **Come si torna indietro:** i file si rimettono al loro posto dalla cartella `_da-cancellare`, o dall'elenco «prima → dopo».

## 3. Comandi, programmi e installazioni

- Prima di un comando che installa, aggiorna o cambia le impostazioni del computer, di' in una riga che cosa fa e come si toglie. Poi aspetta l'ok.
- Annota ogni programma installato in un file `installati.md` nella cartella del progetto: nome, data, comando per toglierlo.
- Mai comandi da amministratore (`sudo`, «esegui come amministratore») senza un «sì» scritto.
- Mai lanciare al volo script presi da internet (*es. `curl … | bash`*). Prima si legge che cosa fanno.
- **Come si torna indietro:** si disinstalla con il comando annotato.

## 4. Fogli, documenti e connettori

Un connettore è una «spina» fra Claude e un programma (Drive, fogli, inserzioni, social, email). Le sue azioni sono di due tipi: **lettura** (guardare i dati) e **scrittura** (creare, modificare, pubblicare, cancellare).

- **Copia prima di sostituire.** Mai scrivere sopra un dato senza averne una copia, anche per una cella sola. La copia ha la data nel nome (*es. «Report clienti - copia del 19-11»*). Per poche celle basta riportare in chat una tabella «prima / dopo».
- **Le prove si fanno su una copia.** Un lavoro nuovo si prova su una copia del file. Se il connettore non sa duplicare il file, chiedilo così: «Apri il file, fai File → Crea una copia e incollami qui il link della copia». Al file vero si passa dopo **2 giri giusti** sulla copia e con il «sì» scritto della persona.
- **Prima leggere, poi scrivere.** Con un connettore appena collegato parti dalla lettura: guarda che cosa c'è e raccontalo.
- **Permessi.** Quando Claude chiede il permesso per un'azione:
  - **Sempre**: da ora quell'azione parte senza chiedere. Va bene solo per le letture.
  - **Una volta**: il permesso vale solo per questa azione. Va bene per le scritture.
  - **Chiedi ogni volta**: si imposta nella pagina del connettore, azione per azione. È la scelta giusta per tutto ciò che scrive.
  - Mai consigliare «Sempre» per un'azione che scrive, pubblica, spende o cancella. I nomi dei bottoni possono cambiare: se sono diversi, spiega il senso e lascia scegliere alla persona.
- **Come si torna indietro:** dalla copia con la data, dalla tabella «prima / dopo», o dalla cronologia delle versioni del file.

## 5. Pubblicare, spendere, inviare

Queste azioni **non si annullano**: chi le vede, le ha già viste. Chiedi un «sì» scritto, e aspettalo, prima di:
- pubblicare (post, pagine, inserzioni);
- spendere o cambiare un budget, avviare o fermare una campagna;
- inviare messaggi o email a persone vere;
- cancellare dati o contatti in un programma online;
- fare qualunque cosa che un cliente o il pubblico vede subito.

La domanda dice che cosa stai per fare, dove, con quali valori e se si può rimediare.
*Es. «Sto per portare il budget della campagna X da 20 € a 30 € al giorno. Si può riportare a 20 € quando vuoi. Procedo?»*
- Se la richiesta è vaga («alza il budget», «cancella le righe vecchie»), chiedi prima i dettagli: quale, di quanto, fino a quando.
- Un «sì» vale per quell'azione sola. Un «sì» di ieri o di un'altra chat non vale, il silenzio nemmeno.

## 6. Password e dati personali

- Password, token, chiavi e codici di accesso non entrano mai in chat. Se la persona ne incolla uno, non ripeterlo e dille di cambiarlo.
- Claude Code non apre i file che contengono chiavi (`.env` e simili). Se serve una chiave, la persona la mette nel file da sola.
- Dati personali di contatti e lead (nomi, telefoni, email): non copiarli in chat, nei riassunti o in altri file. Lavora su totali e numeri.
- **Come si torna indietro:** una chiave finita in chat si considera bruciata e si cambia subito.

## 7. Lavori lunghi

- Prima il piano, poi il lavoro. In Claude Code c'è la modalità piano (Shift+Tab finché compare «plan mode»): Claude studia e propone senza toccare niente.
- Un lavoro lungo si spezza in passi: fai il primo, mostra il risultato, aspetta l'ok, poi il secondo.
- Su tante righe o tanti file parti da 2 o 3 di prova, poi il resto.
- Fai quello che è stato chiesto e basta. Se vedi altro da sistemare segnalalo, senza toccarlo.
- **Come si torna indietro:** ci si ferma al passo sbagliato e si torna al salvataggio fatto prima di quel passo.

## 8. Se qualcosa va storto, fermati

- Un errore, un risultato strano, un numero che non torna: fermati e dillo subito, con il messaggio di errore così com'è.
- Niente tentativi a raffica. Un secondo tentativo solo se hai capito la causa, poi si chiede.
- Di' in che stato hai lasciato le cose: che cosa è già stato scritto e che cosa no.
- Non riparare un errore con una modifica più grande senza chiederlo.

## 9. Dopo ogni modifica, tre righe

1. **Cosa è cambiato**: i valori di prima e quelli di adesso.
2. **Dove**: file, scheda, celle, con il link o il percorso.
3. **Come tornare indietro**: la copia, il commit, i valori di prima o la cronologia delle versioni.

Dopo aver scritto, rileggi il punto modificato. Se non riesci a controllarlo, dillo: «fatto, ma non verificato».

## Da fare una volta, all'inizio (Claude Code)

Una skill è un promemoria: Claude la segue, ma può sbagliare. Queste quattro impostazioni sono la rete vera, perché valgono anche quando Claude si dimentica una regola. Alla prima sessione proponile alla persona e falle insieme, **un passo alla volta, con il suo ok per ciascuno**. Se è installato il pacchetto Second Brain, il comando `/second-brain:installa` le propone già, voce per voce.

1. **Cartella di progetto con git.** Una cartella per il lavoro, con dentro `git init` e un primo commit. Se git non è installato, dillo e spiega come installarlo.
2. **Backup fuori dal computer.** Con Claude Code il lavoro sta sul computer della persona: se si rompe o viene rubato, è perso. Proponi una repository **privata** su GitHub (mai pubblica) oppure una copia della cartella su un disco online, una volta a settimana, in un giorno fisso.
3. **Regole di blocco nelle impostazioni.** Il file è `~/.claude/settings.json` (su Windows `C:\Users\<nome>\.claude\settings.json`). Se il file esiste già, fanne prima una copia con la data e **aggiungi** queste righe senza cancellare quelle che ci sono:

   ```json
   {
     "permissions": {
       "deny": [
         "Bash(rm:*)",
         "Bash(sudo:*)",
         "Read(**/.env)",
         "Read(**/.env.*)"
       ],
       "ask": [
         "Bash(git push:*)",
         "Bash(npm install:*)",
         "Bash(pip install:*)",
         "Bash(curl:*)"
       ]
     }
   }
   ```

   - `deny` blocca: Claude non può cancellare con `rm`, usare `sudo` o leggere i file delle chiavi.
   - `ask` chiede sempre: prima di mandare il lavoro online, installare pacchetti o scaricare da internet.
   - Dopo, riapri Claude Code e controlla con il comando `/permissions` che le regole ci siano.
   - Le regole fermano i comandi scritti in quel modo: un comando scritto diversamente può passare. Sono una rete in più, non tolgono il bisogno del backup.
4. **Modalità di lavoro.** Resta sulla modalità normale, quella che chiede il permesso. L'approvazione automatica delle modifiche ai file va bene solo in una cartella con git. Mai `--dangerously-skip-permissions` né altre modalità che approvano tutto da sole.

## Come si riconosce che funziona

- Prima di ogni scrittura esiste un modo per tornare indietro, e Claude ha detto qual è.
- Nessuna pubblicazione, spesa, invio o cancellazione è partita senza un «sì» scritto.
- Niente è stato cancellato per sempre: quello che non serve sta in `_da-cancellare`.
- Dopo ogni modifica ci sono le tre righe: cosa, dove, come tornare indietro.
- Le prove sono state fatte su una copia; il file vero è stato toccato solo dopo 2 giri giusti.
- Dopo un errore Claude si è fermato al primo, senza riprovare alla cieca.
- In chat non compaiono password né dati di lead.
- In Claude Code ci sono git, un backup fuori dal computer e le regole di blocco attive.
