---
slug: hook-stato-a-inizio-sessione
titolo: "Stato vero nel contesto a inizio sessione"
area: automazioni
dove_gira: PC
livello: base
costo: "0 €. 10 minuti."
pacchetto: "pacchetti/hook-stato-a-inizio-sessione/"
stato: "versione per PC del mio"
---

# Stato vero nel contesto a inizio sessione

**Il problema.** La memoria è una fotografia del passato. Un giorno una nota vecchia diceva che un mio agente girava su un modello, mentre da giorni ne usava un altro, e Claude mi ha consigliato su una base sbagliata.

**Come l'ho risolto.** Ho messo un hook SessionStart che a ogni sessione legge in diretta la configurazione degli agenti e mette nel contesto modello e riserva di ciascuno, con la frase «questo vale più della memoria». Per il PC ho scritto la versione generale: data e ora di oggi più le prime righe dei file di stato che scegli tu (progetti in corso, cosa è attivo), con la data di modifica.

**Perché così.** Lo stato vero deve arrivare da solo, come la memoria, altrimenti vince la memoria. E la data di oggi evita errori su «ieri» e «venerdì prossimo».

**Quando ti serve.** Se hai un file che dice com'è la situazione adesso e lo aggiorni davvero, o se Claude sbaglia spesso le date.

**Quando non ti serve.** Se non hai un file di stato aggiornato: metterci un file vecchio peggiora le cose. Tutto quello che elenchi entra in ogni sessione e occupa contesto: tienilo corto.

**Come prenderlo.** Copia `stato_inizio.py` e `stato_file.txt` in `~/.claude/hooks/`, scrivi i tuoi percorsi nel `.txt` e il blocco di `settings-esempio.json` in `~/.claude/settings.json`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-stato-a-inizio-sessione/LEGGIMI.md).
