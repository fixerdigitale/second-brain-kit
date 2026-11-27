---
name: soluzioni
description: >-
  Archivio delle soluzioni: cosa si e' rotto, perche' e come si e' aggiustato.
  Cerca qui PRIMA di diagnosticare un problema tecnico (bug, sito che non carica, servizio
  che non risponde, integrazione rotta, deploy fallito, comportamento intermittente), e
  scrivi una scheda DOPO averne risolto uno non banale. Usala quando un problema sembra
  gia' visto, quando qualcuno chiede "com'era che si risolveva", e ogni volta che una
  diagnosi e' costata piu' di mezz'ora.
---

# Archivio soluzioni

Lo stesso problema torna. Ogni soluzione trovata si scrive una volta e si rilegge molte:
la volta dopo si parte dalla causa gia' trovata e dai vicoli ciechi gia' esplorati.

L'archivio sta in `<cartella-vault>/soluzioni/`, una scheda markdown per problema.
Il modello della scheda e' in `modello-scheda.md` accanto a questo file.

## Prima di diagnosticare: cerca

```bash
python3 ~/.claude/skills/soluzioni/soluzioni.py cerca <parole>
```

Cerca con le parole del **sintomo**, non con la causa che sospetti: la causa e' proprio
quello che stai cercando. Due o tre parole bastano ("form tagliato", "502 nginx",
"timeout webhook").

Altri comandi:

```bash
python3 ~/.claude/skills/soluzioni/soluzioni.py elenco          # tutte, dalla piu' recente
python3 ~/.claude/skills/soluzioni/soluzioni.py elenco <tag>    # filtrate per tag
python3 ~/.claude/skills/soluzioni/soluzioni.py mostra <slug>   # la scheda intera
```

Se lo script non c'e', basta cercare nella cartella con Grep: le schede sono testo.

Se non trovi niente, procedi normalmente, ma allora la scheda la scrivi tu alla fine.

## Dopo aver risolto: scrivi la scheda

Scrivi quando la diagnosi e' costata piu' di mezz'ora, quando la causa non era quella che
sembrava, o quando il problema puo' ripresentarsi su un altro progetto. Le cose ovvie e le
correzioni da un minuto non vanno in archivio: lo diluiscono e basta.

```bash
python3 ~/.claude/skills/soluzioni/soluzioni.py nuova <slug-parlante>   # crea dal modello
# compilala
python3 ~/.claude/skills/soluzioni/soluzioni.py indice                  # rigenera INDICE.md
```

Lo slug descrive il sintomo, non il cliente: `iframe-vuoto-o-tagliato`, non `fix-sito-x`.

## Come si scrive una scheda che serve davvero

Il modello ha sette sezioni. Le tre che fanno risparmiare tempo:

- **Sintomo**: con le parole di chi l'ha segnalato, compresi i sintomi fuorvianti. Sono
  quelli che fanno sbagliare strada la volta dopo.
- **Come si riconosce**: il test piu' veloce per distinguere questo problema da uno simile.
  Un comando o un controllo concreto, non una descrizione.
- **Vicoli ciechi**: cosa hai provato che NON ha funzionato, e perche'. Vale quanto la
  soluzione: e' la parte che non si ricostruisce leggendo il codice.

Regole di scrittura:

- numeri, percorsi, comandi e stringhe di errore esatti, mai parafrasati;
- la causa vera, non il primo sospetto: se hai cambiato idea a meta' strada, il primo
  sospetto va nei vicoli ciechi;
- come hai verificato che funziona, con i numeri;
- in fondo, per cosa e' riusabile: quali altri casi ricadono nello stesso meccanismo;
- mai password, chiavi o token nella scheda: scrivi il nome della variabile, non il valore.
