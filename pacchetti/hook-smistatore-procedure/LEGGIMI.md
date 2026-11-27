# Smistatore: la procedura giusta per ogni tipo di lavoro

Se hai scritto delle procedure (come si fa una landing, un report, una proposta), questo hook
le ricorda a Claude quando il tuo messaggio ne parla. Esempio: scrivi "fammi la landing per il
corso" e Claude riceve "procedura possibile: Landing page, <cartella-vault>/procedure/landing.md".
La legge, ti dice in una riga che la segue, e parte.

Indovina dalle parole, quindi sbaglia ogni tanto: per questo l'avviso dice "da verificare" e
compare una sola volta per sessione e per procedura.

## Dove si copia

1. `smistatore.py` e `procedure.json` insieme in `~/.claude/hooks/`.
2. In `procedure.json` metti le tue procedure: nome, parole che la fanno scattare, percorso del
   file (assoluto, per esempio `C:/Users/<tuo-utente>/<cartella-vault>/procedure/landing.md`).
   Parole troppo comuni ("pagina", "sito") fanno scattare spesso: tienile specifiche.
3. Il blocco di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`.
   Windows: `python` al posto di `python3`, o il percorso completo.
4. Facoltativo: `promemoria.txt` accanto allo script. Se c'è, quando il messaggio sembra un
   lavoro (fai, crea, sistema…) l'hook aggiunge anche quel testo, una volta per sessione. Io lo
   uso per ricordare la regia: «prima di cominciare decidi chi fa il lavoro» (pacchetto
   `agenti-regia-e-smistamento`). Se non ti serve, cancella il file.

## Come si prova

    echo '{"prompt":"fammi un preventivo per il nuovo cliente","session_id":"prova1"}' | python3 smistatore.py

Deve stampare l'avviso con "Proposta commerciale". Rilanciato con lo stesso `session_id` non
stampa niente (avviso già dato).

## Come si toglie

Togli il blocco da `settings.json`. I segni "già detto" stanno nella cartella temporanea del
sistema (`claude-smistatore`).

## English

A UserPromptSubmit hook that recognizes the type of job from the words in your message and adds, once per session, "possible procedure: X, in file Y, to be verified". When the message looks like a job it can also add a direction reminder (decide who does it before starting).

Install: copy `smistatore.py`, `procedure.json` and, optionally, `promemoria.txt` into `~/.claude/hooks/`. Put your procedures in the JSON (name, trigger words, absolute path of the file) and add the block from `settings-esempio.json` to `~/.claude/settings.json`. The sample trigger words are Italian.
