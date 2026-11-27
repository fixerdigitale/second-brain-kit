---
slug: skill-qa-percorso-utente
titolo: "Prova della pagina come la usa un utente vero"
area: skill
dove_gira: PC
livello: medio
costo: "0 €; un giro su una landing richiede 10-20 minuti"
pacchetto: "pacchetti/skill-qa-percorso-utente/"
stato: "lo uso"
---
# Prova della pagina come la usa un utente vero

**Il problema.** «La pagina risponde» non vuol dire che funziona. Moduli che non inviano, pagine di ringraziamento rotte, tracciamento che non parte, versione telefono sballata: li scoprivo dopo, dal cliente.

**Come l'ho risolto.** Una skill che rifà il percorso di un utente in un browser, a 1440 px e a 393 px. Clicca, compila, invia, guarda console e rete, apre anche le pagine collegate. Ogni difetto ha una prova. Dopo la correzione rifà tutto il percorso dall'inizio, al massimo 3 giri. Chiude con un voto: sotto 8 non consegno.

**Perché così.** Riprodurre prima di toccare il codice evita le correzioni a caso. Rifare tutto il percorso dopo la correzione scopre quello che la correzione ha rotto altrove. L'idea viene dal ciclo /qa di gstack (vedi la scheda sulle suite prese da fuori); il testo l'ho fatto riscrivere da zero, più corto.

**Quando ti serve.** Prima di consegnare landing, moduli, checkout, aree clienti; quando qualcuno segnala un errore.

**Quando non ti serve.** Per una modifica di testo su una pagina che già funziona è troppo. Serve un browser comandabile da Claude: senza, la skill non ha mani.

**Come prenderlo.** Copia `qa-percorso-utente/` in `~/.claude/skills/` e aggiungi Chrome DevTools MCP (https://github.com/ChromeDevTools/chrome-devtools-mcp, serve Node.js). Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/skill-qa-percorso-utente/LEGGIMI.md).
