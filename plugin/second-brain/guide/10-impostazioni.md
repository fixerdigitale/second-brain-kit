# 10 · Le impostazioni consigliate

`/second-brain:installa` ti propone queste impostazioni **una per una**: ti dice cosa fa ognuna, come si toglie, e aspetta il tuo sì. Puoi dire no a tutte e il pacchetto funziona lo stesso. Qui le trovi spiegate, se vuoi rivederle o cambiarle dopo.

Le impostazioni di Claude Code stanno nel file `settings.json` della cartella `.claude` del tuo utente (su Windows `C:\Users\<nome>\.claude\settings.json`, su Mac `~/.claude/settings.json`). Prima di cambiarlo Claude ne fa una copia con la data, e **aggiunge** le righe senza cancellare quelle che ci sono. Dopo, riapri Claude Code.

## 1. Regole di blocco (consigliata)

Sono una rete di sicurezza che vale anche quando Claude si dimentica una regola:

- **bloccati**: cancellare con `rm`, usare comandi da amministratore (`sudo`), leggere i file delle chiavi (`.env`);
- **sempre con domanda**: mandare il lavoro online (`git push`), installare pacchetti, scaricare da internet.

Controllo: il comando `/permissions` mostra le regole attive. Le regole fermano i comandi scritti in quel modo: un comando scritto diversamente può passare. Sono una rete in più, non tolgono il bisogno delle copie.

Come si toglie: «togli le regole di blocco del second brain dalle impostazioni», oppure si rimette la copia di `settings.json`.

## 2. Barra di stato con contesto e consumi (facoltativa)

Una riga sotto il campo di scrittura che mostra, mentre lavori, quanto contesto hai usato e quanta quota delle 5 ore e della settimana. Così vedi in anticipo quando conviene aprire una sessione nuova o rimandare un lavoro pesante.

Claude Code la permette ufficialmente (impostazione `statusLine`: code.claude.com/docs/en/statusline). Nella versione 0.1 del pacchetto non è ancora inclusa: arriverà con un aggiornamento, provata su Windows e su Mac. Intanto i consumi li vedi con `/usage`.

## 3. Compressione del contesto prima del limite (facoltativa)

Di serie Claude Code comprime la conversazione quando il contesto è quasi pieno. Se il tuo modello ha il contesto da 1 milione, molti si trovano meglio a farlo comprimere prima, verso la metà: le risposte restano più precise.

L'impostazione è `autoCompactWindow` (per esempio `480000`, cioè compressione intorno ai 480.000 token). Attenzione: questa chiave **non è nella documentazione ufficiale**; funziona sulle versioni recenti di Claude Code. Se un giorno sparisce, non succede niente di male: Claude Code torna al comportamento di serie.

Ha senso solo se il tuo piano e il tuo modello hanno il contesto da 1 milione. Se non lo sai, chiedi a Claude di controllare prima di attivarla.

## 4. Modalità di lavoro (consigliata)

Resta sulla modalità normale, quella che chiede il permesso. L'approvazione automatica delle modifiche ai file va bene solo in una cartella con git. Mai le modalità che approvano tutto da sole (guida 05).

## 5. Git nella cartella di lavoro (consigliata)

Git salva le versioni dei file, così puoi tornare a com'era ieri. Se non è installato, Claude ti dice come installarlo (su Windows di solito c'è già, perché Claude Code lo usa). Poi un primo salvataggio: «metti la cartella sotto git e fai il primo salvataggio».

## Prova adesso (2 minuti)

Scrivi `/permissions` e guarda quali regole sono attive.
