# Prova di ripristino — checklist

Una volta al mese (e dopo ogni cambio allo script di backup). Durata: circa 15 minuti.
Si ripristina sempre in una cartella a parte, mai sopra l'originale.

Data della prova: ____________   Fatta da: ____________

## 1. Scegli cosa ripristinare
- [ ] Una copia di almeno 2 giorni fa (non quella di stanotte)
- [ ] Scrivi qui il nome: ____________

## 2. Scarica e apri in una cartella a parte
- [ ] Crea una cartella vuota, per esempio `~/ripristino-prova-AAAAMMGG`
- [ ] Copia della cartella cloud: scarica lo zip dal sito di Drive (dal browser, come se il PC fosse perso) ed estrailo lì
- [ ] Copia GitHub: `git clone <url-repo-privato> ~/ripristino-prova-AAAAMMGG/da-github`
- [ ] Se usi restic: `restic -r <repo> restore latest --target ~/ripristino-prova-AAAAMMGG` (serve la password: la trovi senza il PC?)

## 3. Controlla che sia davvero tutto
- [ ] Numero di file simile all'originale (differenza: ____)
- [ ] Apri 3 note a caso, una recente, una vecchia, una con immagini: si leggono?
- [ ] Il file di memoria / regole principale (`CLAUDE.md`, indice) è identico all'originale
- [ ] Le cartelle importanti ci sono tutte: ____________
- [ ] Mancano cose che pensavi fossero dentro? Scrivile: ____________

## 4. Esito
- [ ] OK: cancella la cartella di prova
- [ ] Problema trovato: scrivi qui cosa e correggi lo script prima della prossima notte

Perché la faccio: un backup che dice «riuscito» dice che è partito, non cosa contiene. Una cartella o un database esclusi per errore si vedono solo riaprendolo.
