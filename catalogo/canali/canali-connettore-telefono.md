---
slug: canali-connettore-telefono
titolo: "Il mio sistema dentro claude.ai, dal telefono"
area: canali
dove_gira: server
livello: avanzato
costo: "0 € in più per il modello; server sempre acceso (circa 15 €/mese, condiviso); giorni di lavoro sulla sicurezza"
pacchetto: "nessuno: solo idea"
stato: "lo uso"
---
# Il mio sistema dentro claude.ai, dal telefono

**Il problema.** Da claude.ai sul telefono Claude non sapeva niente di me: né le note, né le sessioni di lavoro della mattina, né cosa stava girando sul server.

**Come l'ho risolto.** Ho un connettore MCP personale (un indirizzo che aggiungo in claude.ai come connettore) protetto da un login. Da lì Claude sul telefono legge le mie sessioni di Claude Code e la memoria, guarda file e log del server in sola lettura con i segreti oscurati, cerca nella memoria del mio assistente principale e, con uno strumento apposta, fa partire un lavoro di Claude Code sul server. Quelle sessioni restano separate da quelle di VS Code, ma sono salvate e le ritrovo.

**Perché così.** Il telefono diventa un terminale vero del mio sistema, non una chat che riparte da zero. Lo uso per controllare a che punto è un lavoro o far partire una cosa piccola senza aprire il PC.

**Quando ti serve.** Se il tuo vault e il tuo lavoro stanno su una macchina sempre accesa e vuoi raggiungerli da claude.ai.

**Quando non ti serve.** Se il vault è sul PC e su Drive: i connettori ufficiali bastano e non devi mantenere niente. Un connettore fatto in casa è un ingresso al tuo sistema da internet: se non sei pronto a curarne la sicurezza (login, limiti ai tentativi, sola lettura), non farlo.

**Come prenderlo.** Nessun pacchetto: è solo l'idea, serve un server. Sul PC ti avvicini così: 1) in claude.ai attiva i connettori ufficiali (Google Drive, Gmail, Calendar): se il vault è sincronizzato su Drive, Claude lo legge anche dal telefono a PC spento; 2) su Claude Desktop aggiungi un server MCP per i file locali puntato sulla cartella del vault (solo a PC acceso); 3) se la tua versione di Claude Code ha il controllo remoto, segui dal telefono una sessione aperta sul PC.
