# Example map (invented data)

Everything in this folder is made up. "Alex" is a generic freelance designer, the vault,
the projects and the numbers do not belong to anyone. I use it only to show what the
onboarding produces, without showing a real setup.

- `make_example_vault.py` builds the invented Obsidian-style vault (143 notes).
- `MAPPA.md` is the map written for it in English, following `plugin/second-brain/modelli/en/MAPPA.md`;
  `MAPPA.it.md` is the same map in Italian. The vault numbers come from `salute_vault.py` and
  `cerca_segreti.py` run on that vault; the time estimates are invented like the rest.
- `social-preview.html` is the layout of `docs/social-preview.png`; it expects a `card.png`
  next to it, cut from the "8 areas" table of the rendered map.

How the images were made:

```bash
python3 docs/esempio/make_example_vault.py <empty-folder>
python3 plugin/second-brain/scripts/salute_vault.py <empty-folder>/Notes
python3 plugin/second-brain/scripts/pagina.py docs/esempio/MAPPA.md MAPPA.html --lingua en
# then a browser screenshot of MAPPA.html: top part -> docs/mappa-esempio.png
```

---

# Mappa d'esempio (dati inventati)

Tutto quello che c'è in questa cartella è inventato. «Alex» è un designer freelance generico:
il vault, i progetti e i numeri non sono di nessuno. Mi serve solo a mostrare cosa produce
l'onboarding, senza mostrare un sistema vero.

- `make_example_vault.py` crea il vault inventato, in stile Obsidian (143 note).
- `MAPPA.md` è la mappa scritta per quel vault in inglese, dal modello `plugin/second-brain/modelli/en/MAPPA.md`;
  `MAPPA.it.md` è la stessa mappa in italiano. I numeri del vault vengono da `salute_vault.py` e
  `cerca_segreti.py` lanciati su quel vault; le stime di tempo sono inventate come il resto.
- `social-preview.html` è l'impaginazione di `docs/social-preview.png`; si aspetta un `card.png`
  accanto, ritagliato dalla tabella «Le 8 aree» della mappa.

Come sono fatte le immagini: gli stessi comandi qui sopra, poi uno screenshot del browser
della parte alta di `MAPPA.html` → `docs/mappa-esempio.png`.
