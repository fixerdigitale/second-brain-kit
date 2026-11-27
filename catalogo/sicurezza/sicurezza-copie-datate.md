---
slug: sicurezza-copie-datate
titolo: Copia datata prima di toccare un file importante
area: sicurezza
dove_gira: PC
livello: base
costo: 0 €. 5 minuti.
pacchetto: pacchetti/sicurezza-copie-datate/
stato: lo uso
---
# Copia datata prima di toccare un file importante

**Il problema.** Una modifica a un file di configurazione andava storta e non avevo la versione di prima. Le copie .bak senza data si sovrascrivevano a vicenda e non sapevo più quale fosse quella buona.

**Come l'ho risolto.** Prima di modificare un file importante che non sta sotto git, Claude fa una copia accanto con data e motivo, per esempio `settings.json.bak-20261127-permessi`. Non sovrascrive mai una copia esistente, ne aggiunge una nuova. Poi mi scrive il nome della copia, così so da dove tornare indietro. Nella cartella della configurazione principale dei miei agenti ce ne sono un centinaio: si legge la storia di ogni cambio.

**Perché così.** Tornare indietro diventa un comando di copia, senza dover ricordare cosa c'era. La data e la nota dicono subito quale copia è quella giusta.

**Quando ti serve.** Per file fuori da git: configurazioni di Claude Code, file di automazioni, configurazioni di un server, documenti esportati.

**Quando non ti serve.** Dentro una cartella già sotto git basta un commit prima della modifica: lì le copie .bak fanno solo disordine. Se le copie si accumulano, ogni tanto cancello quelle vecchie di mesi.

**Come prenderlo.** Incolla `regola-claude-md.md` nel tuo `CLAUDE.md`; lo script `copia_datata.py` è facoltativo, serve per fare la copia con un comando sempre uguale. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-copie-datate/LEGGIMI.md).
