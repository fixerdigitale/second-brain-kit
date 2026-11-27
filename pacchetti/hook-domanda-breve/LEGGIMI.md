# Domanda breve: risposta, non lavoro

Capita di chiedere "ma la newsletter parte da sola?" e vedere Claude aprire dieci file, lanciare
un sotto-agente e cambiare qualcosa. Questo hook riconosce le domande brevi (finiscono con "?" o
cominciano con "come", "cosa", "perché"…, e non hanno verbi di lavoro come "fai" o "sistema") e
ricorda a Claude di rispondere in poche righe. Se serve lavoro, te lo propone e aspetta il tuo ok.

## Dove si copia

1. `domanda_breve.py` in `~/.claude/hooks/`.
2. Il blocco di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`.
   Windows: `python` al posto di `python3`, o il percorso completo.
3. Se scrivi in un'altra lingua, cambia le due liste `INTERROGATIVE` e `LAVORO` in cima al file.

## Come si prova

    echo '{"prompt":"come funziona il backup?"}' | python3 domanda_breve.py      # stampa l'avviso
    echo '{"prompt":"sistemami il backup"}' | python3 domanda_breve.py           # non stampa niente

## Come si toglie

Togli il blocco da `settings.json` e cancella il file.

## English

A UserPromptSubmit hook that recognizes short questions (no work verbs like "do", "fix", "create") and reminds Claude to answer in a few lines, with at most 3 reads, and to propose any work instead of starting it. It reads no files and blocks nothing.

Install: copy `domanda_breve.py` into `~/.claude/hooks/` and the block from `settings-esempio.json` into `~/.claude/settings.json` under `"hooks"` (on Windows use `python` instead of `python3`). The `INTERROGATIVE` and `LAVORO` word lists at the top of the file are Italian: replace them with words in your language.
