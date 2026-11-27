# Guardia email

Claude conosce l'email del tuo account Claude e ogni tanto la infila da solo dove non deve:
un User-Agent "contatto: tuo@indirizzo" in una chiamata a un sito pubblico, un parametro in un
URL. A me è successo davvero verso un sito pubblico di immagini. Questo hook lo ferma prima.

- `WebFetch` / `WebSearch` con il tuo indirizzo dentro (anche codificato): bloccato.
- `Bash` con il tuo indirizzo e un comando di rete verso un sito che non è nella lista degli
  ammessi: chiede conferma a te.

## Dove si copia

1. `guardia_email.py` e `indirizzi_email.txt` insieme in `~/.claude/hooks/`.
2. In `indirizzi_email.txt` scrivi i tuoi indirizzi, uno per riga. Il file resta sul tuo PC:
   non metterlo in un repository pubblico.
3. In `HOST_AMMESSI` (in cima allo script) aggiungi i tuoi domini e i servizi dove quell'email
   la usi davvero (es. il tuo CRM).
4. Il blocco di `settings-esempio.json` in `~/.claude/settings.json`, sotto `"hooks"`.
   Windows: `python` al posto di `python3`, o il percorso completo.

## Come si prova

Con `prova@esempio.it` scritto in `indirizzi_email.txt`:

    echo '{"tool_name":"WebFetch","tool_input":{"url":"https://sito-terzo.org/?from=prova%40esempio.it"}}' | python3 guardia_email.py

Deve stampare un JSON con `"permissionDecision": "deny"`. Poi togli l'indirizzo di prova.

## Come si toglie

Togli il blocco da `settings.json` e cancella i due file.

## English

A PreToolUse hook on Bash, WebFetch, WebSearch and page-opening tools that stops your email address from leaking to third-party sites (in a User-Agent, a URL, even URL-encoded or base64). Requests to your own domains pass. Addresses live in a separate file, none in the code.

Install: copy `guardia_email.py` and `indirizzi_email.txt` into `~/.claude/hooks/`, write your addresses in the `.txt` and your domains in `HOST_AMMESSI`, then add the block from `settings-esempio.json` to `~/.claude/settings.json`. It doesn't cover programs Claude writes and runs later.
