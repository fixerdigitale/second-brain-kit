---
slug: memoria-indice-e-regole-doro
titolo: "Memoria a file, indice compatto e Regole d'oro"
area: memoria
dove_gira: PC
livello: base
costo: "0 €. Un'ora per riordinare un indice che hai già."
pacchetto: pacchetti/memoria-indice-e-regole-doro/
stato: lo uso
---

# Memoria a file, indice compatto e Regole d'oro

**Il problema.** La memoria automatica di Claude Code carica solo l'inizio di MEMORY.md (circa 200 righe o 25 KB). Con un indice «una riga per file», quando i file hanno superato i 200 le correzioni in fondo sparivano senza nessun avviso: risultavano salvate, ma Claude non le leggeva più.

**Come l'ho risolto.** Ogni correzione sta in un file suo (oggi ne ho più di 440). MEMORY.md è compatto e ha due parti. «Regole d'oro»: il testo della regola è scritto nell'indice, con un tetto di 20, così Claude le legge sempre. «Per tema»: solo i nomi dei file raggruppati per argomento, che Claude apre quando il tema è pertinente. Le correzioni nuove entrano in un gruppo «Da smistare». Una correzione sale fra le Regole d'oro solo se è tornata almeno due volte, e solo con il mio ok.

**Perché così.** Il testo nell'indice si legge sempre, un file si apre solo se il nome sembra giusto: le regole più ripetute meritano il posto garantito. Il tetto serve perché se tutte sono d'oro nessuna lo è. Per me è la parte più difficile da tenere: tendo a sforarlo, e ogni tanto sfoltisco spostando le meno usate in CLAUDE.md o nel loro tema.

**Quando ti serve.** Quando la memoria automatica supera qualche decina di file, o quando noti che Claude dimentica una correzione che ti risulta salvata.

**Quando non ti serve.** Con meno di 50 file di memoria un indice semplice va benissimo. Se le regole davvero importanti sono poche, puoi metterle direttamente in CLAUDE.md e saltare le Regole d'oro.

**Come prenderlo.** Copia la struttura di `MEMORY.md` del pacchetto nella cartella della memoria del progetto (`~/.claude/projects/<nome-cartella-del-progetto>/memory/`). Se hai già un MEMORY.md, fanne una copia e riordinalo a mano.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-indice-e-regole-doro/LEGGIMI.md).
