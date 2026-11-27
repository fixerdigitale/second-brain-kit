# Niente password in chat né nelle note

- `regola-claude-md.md`: la regola da incollare nel `CLAUDE.md`.
- `cerca_segreti.py`: controlla una cartella e dice dove ci sono righe che sembrano password o chiavi, **senza stamparle**.

## Dove si copia

- La regola: in `~/.claude/CLAUDE.md`.
- Lo script: per esempio `<cartella-vault>/strumenti/cerca_segreti.py`.

## Come si prova

```
python3 cerca_segreti.py <cartella-vault>
```
Prova prima su una cartella con un file finto: un `prova.md` con una riga come `password` seguita da due punti e da un valore inventato di almeno 8 caratteri con lettere e cifre. Deve segnalare `prova.md:1:password`, cioè file, riga e nome, senza mostrare il valore. Poi sposta il file di prova fuori dal vault (o nel cestino tu, a mano).

È lo stesso script che usa il plugin `second-brain` (`plugin/second-brain/scripts/cerca_segreti.py`): una sola versione, le stesse forme. Legge anche il testo dei `.docx`, `.xlsx` e `.pptx`; i PDF no, e alla fine dice quanti ne ha saltati. Riga 0 vuol dire che è il **nome** del file a far pensare a credenziali (`password.txt`, `accessi.docx`). Codici di uscita: 0 pulito, 1 trovato qualcosa, 2 errore.

Puoi lanciarlo prima di ogni push su GitHub, o chiedere a Claude di farlo prima di salvare note che vengono da chat con clienti.

## Limiti

Trova solo le forme comuni. Una password scritta da sola su una riga, senza una parola come «password», «pass», «pwd» o «wifi» vicino, sfugge. Non sostituisce la regola: la aiuta.

## Come si toglie

Togli il paragrafo dal `CLAUDE.md` e cancella lo script.

## English

A CLAUDE.md rule that keeps passwords, PINs and tokens out of answers and notes, not even partially or masked; to check whether a secret exists Claude reports line numbers, never text. `cerca_segreti.py` flags suspicious files and lines in the vault without ever printing the value.

Install: paste `regola-claude-md.md` into your `CLAUDE.md`; run `python3 cerca_segreti.py <vault-folder>` before a push or after importing notes from others. It finds common patterns only.
