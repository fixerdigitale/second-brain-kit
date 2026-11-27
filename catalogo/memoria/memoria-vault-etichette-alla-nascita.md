---
slug: memoria-vault-etichette-alla-nascita
titolo: "Vault con cartelle fisse ed etichette alla nascita"
area: memoria
dove_gira: PC
livello: medio
costo: "0 € la versione manuale. Quella automatica, da me, usa un modello per il secondo controllo: pochi centesimi al giorno, ma serve un server."
pacchetto: pacchetti/memoria-vault-etichette-alla-nascita/
stato: versione per PC del mio
---

# Vault con cartelle fisse ed etichette alla nascita

**Il problema.** Il vault cresceva senza ordine: non sapevo più quali note riguardavano un cliente, quali erano economiche o personali. Quando ho voluto far leggere il vault a una collaboratrice, non avevo modo di filtrare cosa poteva vedere.

**Come l'ho risolto.** Il vault ha cartelle fisse (Clienti, Progetti, Decisioni, Risorse, Fatti per mese, Fonti per il materiale grezzo). Ogni nota nasce con un frontmatter di etichette: `entita` (a quale cliente o progetto si riferisce), `livello` (operativo, economico, personale) e `visibile_a` (chi può leggerla). Da me un servizio sul server guarda le note nuove ogni 15 minuti e mette le etichette da solo, con un modello e un secondo controllo; le stesse etichette sono quelle che filtrano la ricerca per persona (scheda «Ricerca filtrata per persona»): è un sistema unico. Nel pacchetto c'è la versione manuale: modello di nota, schema delle cartelle e uno script che elenca le note senza etichette.

**Perché così.** Mettere le etichette quando la nota nasce costa pochi secondi; rimetterle dopo su centinaia di note costa giorni, e un'etichetta messa a posteriori sbaglia più facilmente. Con `entita` trovo tutto di un cliente; con `livello` e `visibile_a` posso dare accesso a qualcuno senza mostrargli le cose economiche o personali.

**Quando ti serve.** Se il vault ha già decine di note su clienti diversi, o se pensi di farlo leggere a un socio, a un collaboratore o a un agente con permessi diversi dai tuoi.

**Quando non ti serve.** Se il vault lo leggi solo tu e lo cerchi per testo: cartelle e nomi chiari bastano, le etichette sarebbero lavoro in più. L'etichettatura automatica ha senso solo con più lettori e un server sempre acceso.

**Come prenderlo.** Copia `CARTELLE.md` e `nota-modello.md` nella radice del vault (in Obsidian puoi usare `nota-modello.md` come template). Lancia `python3 controlla_etichette.py <cartella-vault>` per vedere le note senza etichette: è in sola lettura.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-vault-etichette-alla-nascita/LEGGIMI.md).
