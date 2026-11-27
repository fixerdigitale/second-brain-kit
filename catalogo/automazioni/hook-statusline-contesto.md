---
slug: hook-statusline-contesto
titolo: "Riga di stato con modello, contesto e limiti"
area: automazioni
dove_gira: PC
livello: base
costo: "0 €. 5 minuti."
pacchetto: "pacchetti/hook-statusline-contesto/"
stato: "proposta nuova, non la uso così"
---

# Riga di stato con modello, contesto e limiti

**Il problema.** Non sapevo mai, a colpo d'occhio, su che modello stavo lavorando, quanto era piena la sessione e quanto avevo già consumato della finestra di 5 ore e della settimana. Lo scoprivo quando arrivava il limite.

**Come l'ho risolto.** Io ho un contatore sempre visibile sopra il prompt, ma è una mod dell'app desktop. Per il kit ho scritto una versione con la riga di stato standard di Claude Code (statusLine): uno script Python che stampa «Opus · contesto 84k/200k 42% · 5 ore 31% · settimana 12% · cartella», leggendo i dati che Claude Code stesso gli passa. Questa versione non la uso io: la provi tu per primo.

**Perché così.** Per me un numero sempre davanti agli occhi cambia le abitudini più di una regola: vedo quando conviene aprire una sessione nuova o delegare, senza chiedere niente a Claude e senza spendere token.

**Quando ti serve.** Se usi Claude Code dal terminale (anche quello integrato di VS Code) con un abbonamento Pro o Max e vuoi tenere d'occhio contesto e limiti.

**Quando non ti serve.** Se usi solo il pannello grafico dell'estensione di VS Code: lì la riga di stato può non comparire, e c'è già un indicatore del contesto. I limiti di 5 ore e settimana compaiono solo se la tua versione li passa (io l'ho verificato sulla 2.1.330).

**Come prenderlo.** Copia `statusline.py` in `~/.claude/` e la chiave `statusLine` di `settings-esempio.json` in `~/.claude/settings.json`. Se vuoi anche il semaforo dei consumi, guarda la scheda [semaforo dei consumi](automazioni-semaforo-consumi.md): i due script si mettono in fila. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-statusline-contesto/LEGGIMI.md).
