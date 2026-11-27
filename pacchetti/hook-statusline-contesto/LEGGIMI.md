# Riga di stato: modello e contesto

> **Proposta nuova, non la uso così.** Io ho un contatore simile sopra il prompt, ma è una mod
> dell'app desktop. Questa riga di stato standard l'ho scritta per il kit: la provi tu per primo.

Una riga sempre visibile sotto il prompt:

    Opus 4 · contesto 84k/200k 42% · 5 ore 31% · settimana 12% · second-brain

Ti dice su che modello sei, quanto è piena la sessione e quanto hai consumato dei limiti
dell'abbonamento (finestra di 5 ore e settimana), senza chiedere niente a Claude.
I limiti compaiono solo se la tua versione di Claude Code li passa (abbonamento Pro/Max).

## Dove si copia

1. `statusline.py` in `~/.claude/`.
2. Il blocco di `settings-esempio.json` in `~/.claude/settings.json` (chiave `statusLine`, allo
   stesso livello di `hooks`). Windows: `python` al posto di `python3`, o il percorso completo.

Nota per Visual Studio Code: la riga di stato si vede quando usi Claude Code nel terminale
integrato (comando `claude`). Il pannello grafico dell'estensione ha un suo indicatore e può
non mostrarla.

## Come si prova

A mano, senza Claude Code:

    echo '{"model":{"display_name":"Opus"},"context_window":{"total_input_tokens":84000,"context_window_size":200000,"used_percentage":42},"workspace":{"current_dir":"/tmp/prova"}}' | python3 statusline.py

Deve stampare `Opus · contesto 84k/200k 42% · prova`. Poi apri `claude` nel terminale: la riga
compare dopo la prima risposta.

## Come si toglie

Togli la chiave `statusLine` da `settings.json` e cancella il file.

## English

A status line script for Claude Code that prints model, context used, 5-hour and weekly limits and folder, for example "Opus · context 84k/200k 42% · 5 hours 31% · week 12% · folder", from the data Claude Code itself passes in. A new proposal: I don't use this exact version myself.

Install: copy `statusline.py` into `~/.claude/` and the `statusLine` key from `settings-esempio.json` into `~/.claude/settings.json`. The limits appear only if your Claude Code version passes them (verified on 2.1.330). Labels are printed in Italian; change them in the script if you like.
