# Suono a fine lavoro

> **Versione per PC del mio.** Io non ho un suono sul PC: ho un piccolo display fisico sulla
> scrivania che fa un bip e un'animazione a fine turno, comandato da una mod dell'app desktop.
> Questa è la versione che chiunque può avere con gli hook standard e le casse del computer.

Lanci un lavoro lungo, passi ad altro, e ti accorgi dopo venti minuti che Claude aspettava un
tuo "sì" dal primo minuto. Questo hook suona:

- quando Claude ha finito il turno (evento `Stop`);
- quando aspetta te: un permesso o una risposta (evento `Notification`). Su Mac compare anche
  una notifica.

## Dove si copia

1. `fine_lavoro.py` in `~/.claude/hooks/`.
2. Il blocco di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`.
   Windows: `python` al posto di `python3`, o il percorso completo.
3. Suoni diversi: su Mac cambia i file in `MAC_SUONI` (quelli in `/System/Library/Sounds/`).

## Come si prova

    echo '{}' | python3 fine_lavoro.py fine
    echo '{}' | python3 fine_lavoro.py attesa

Devi sentire due suoni diversi. Poi chiedi a Claude una cosa qualsiasi: alla fine suona.

## Come si toglie

Togli i due blocchi da `settings.json` e cancella il file.

## English

Two hooks that play a sound: Stop when Claude has finished, Notification (with a desktop notification on Mac) when it's waiting for a permission or an answer. Different signals for "done" and "waiting for you".

Install: copy `fine_lavoro.py` into `~/.claude/hooks/` and the two blocks from `settings-esempio.json` into `~/.claude/settings.json`.
