---
slug: memoria-handoff-e-sistema
titolo: "HANDOFF.md e SISTEMA.md per ogni cliente lungo"
area: memoria
dove_gira: PC
livello: base
costo: "0 €. 20-40 minuti per il primo SISTEMA.md di un cliente, poi qualche minuto a sessione."
pacchetto: pacchetti/memoria-handoff-e-sistema/
stato: lo uso
---

# HANDOFF.md e SISTEMA.md per ogni cliente lungo

**Il problema.** Su un cliente con mesi di lavoro l'HANDOFF era diventato un diario di centinaia di KB, scritto sempre in coda. I fatti stabili ci stavano sepolti dentro, e le sessioni rifacevano mappe già fatte invece di leggerle.

**Come l'ho risolto.** Ogni cliente o progetto lungo ha due file. SISTEMA.md tiene i fatti stabili: chi è chi (con le omonimie in evidenza), come passano i dati, cosa vediamo e cosa no, decisioni ferme, errori già fatti, strumenti da riusare. Si corregge sul posto, ogni riga con la data. HANDOFF.md tiene solo il lavoro aperto: una sezione fissa «Rischi aperti» e sotto «## Lavori» le sezioni nuove in alto, con obiettivo, stato, file toccati, decisioni e prossimo passo. Quando scopro un fatto stabile scrivo una riga «Per SISTEMA.md: …». In CLAUDE.md c'è scritto: se un lavoro si interrompe, prima aggiorna l'HANDOFF; prima di mappare un sistema o attribuire un account, leggi SISTEMA.md.

**Perché così.** Sono due tempi diversi: i fatti stabili si leggono per primi e devono stare in poche pagine; il lavoro aperto cambia ogni giorno. Mescolarli fa sparire i primi. Con l'HANDOFF aggiornato, una sessione nuova o un altro assistente riparte dal prossimo passo senza chiedermi il contesto.

**Quando ti serve.** Su clienti o progetti che durano settimane, con più persone e sistemi, e quando lavori in sessioni che si interrompono (limite d'uso, contesto pieno).

**Quando non ti serve.** Su lavori che si chiudono in una o due sessioni: il file sarebbe più lungo del lavoro. Per un cliente semplice basta la sua nota nel vault.

**Come prenderlo.** Copia `SISTEMA.md` e `HANDOFF.md` nella cartella del cliente o del progetto e aggiungi in CLAUDE.md le due righe scritte nel LEGGIMI.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-handoff-e-sistema/LEGGIMI.md).
