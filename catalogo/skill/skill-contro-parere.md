---
slug: skill-contro-parere
titolo: "Un Claude che non mi dà ragione per forza"
area: skill
dove_gira: PC
livello: base
costo: "0 € in più; circa 10 minuti per adattare la tabella delle fonti"
pacchetto: "pacchetti/skill-contro-parere/"
stato: "lo uso"
---
# Un Claude che non mi dà ragione per forza

**Il problema.** I modelli tendono a darmi ragione. Se in una call ricordavo male un budget, Claude ci costruiva sopra il preventivo. E se insistevo, cedeva anche quando i fatti stavano dalla sua parte.

**Come l'ho risolto.** Ho scritto una skill che controlla sulla fonte i fatti che riporto (trascrizione della call, note, email) prima di usarli. Sulle scelte importanti scrive prima il suo parere partendo solo dalle fonti, poi lo confronta con il mio. Quando non siamo d'accordo risponde in tre forme sole: TENGO (il fatto, più cosa gli farebbe cambiare idea), CAMBIO (fatto nuovo e ragionamento rifatto da capo), VERIFICO (come lo controlla, e lo fa). «Esegui e basta» la spegne per quel messaggio. Io non la richiamo mai a mano: la tengo sempre attiva con una riga nel mio CLAUDE.md, e la skill ha `disable-model-invocation: true`, così non si accende o spegne a caso.

**Perché così.** Mi serve qualcuno che migliori le decisioni, non uno che le applaude. Il tono e l'insistenza non sono prove: questa regola lo mette nero su bianco. Un'obiezione sola, con il costo concreto di sbagliare; su un'istruzione chiara la dice una volta e poi esegue. Così non diventa opposizione sistematica.

**Quando ti serve.** Se decidi spesso su soldi, clienti o cose difficili da annullare, e ti capita di riportare a memoria cose dette in call o in chat.

**Quando non ti serve.** Se usi Claude solo per scrivere codice o testi su istruzioni precise, ti rallenta e basta. Se le tue fonti (call, note) non stanno dove Claude può leggerle, il controllo dei fatti si riduce a «non trovo la fonte, vado sulla tua parola».

**Come prenderlo.** Copia la cartella `contro-parere/` in `~/.claude/skills/` e aggiungi al tuo `CLAUDE.md` la riga del LEGGIMI per tenerla sempre accesa. Prima sistema la tabella delle fonti con le tue. Idea presa da talhapythoneer/anti-sycophancy-prompt e HimanshuJ16/frank (MIT), testo riscritto. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/skill-contro-parere/LEGGIMI.md).
