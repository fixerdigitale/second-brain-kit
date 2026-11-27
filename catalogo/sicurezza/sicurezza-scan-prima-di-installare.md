---
slug: sicurezza-scan-prima-di-installare
titolo: Controllo di sicurezza prima di installare skill e MCP presi da fuori
area: sicurezza
dove_gira: PC
livello: medio
costo: 0 €. Serve Docker (gratis); circa 20 minuti la prima volta, poi un minuto a controllo.
pacchetto: "nessuno: solo idea"
stato: lo uso
---
# Controllo di sicurezza prima di installare skill e MCP presi da fuori

**Il problema.** Le skill e i server MCP che trovo su GitHub sono istruzioni e codice che Claude esegue con i miei permessi. Una skill può dire a Claude di mandare file da qualche parte, uno script può fare cose che il README non dice. Leggerle tutte a mano per me non è realistico.

**Come l'ho risolto.** Prima di installare qualunque skill, MCP, plugin o repo di agenti presi da fuori, anche quando ho già deciso di prenderla, la faccio passare da SkillSpector di NVIDIA (open source, Apache-2.0) in sola analisi statica: il codice non viene eseguito. Dà un punteggio da 0 a 100. Da 21 a 49 leggo le segnalazioni prima di installare; da 50 in su leggo ogni segnalazione e non installo se ce n'è una vera. Lo lancio in un container Docker senza segreti montati, in sola lettura e senza privilegi.

**Perché così.** Mi costa un minuto e intercetta cose che a occhio non vedo: comandi nascosti, istruzioni a Claude di ignorare le regole, dipendenze con vulnerabilità note. Un punteggio basso non vuol dire «sicuro»: vuol dire che lo strumento non ha trovato niente, e lo tratto così.

**Quando ti serve.** Quando installi una skill o un MCP da un autore che non conosci, o una repo con script.

**Quando non ti serve.** Per le skill che scrivi tu o per i plugin ufficiali di Anthropic non mi serve. Se installi una cosa ogni tanto, un'alternativa senza Docker è aprire i file e chiedere a Claude di leggerli cercando comandi di rete, accesso a chiavi e istruzioni strane: è meno completo, ma è già qualcosa.

**Come prenderlo.** Strumento di terzi, non ricopiato: [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector), con le istruzioni nel README. Io lo lancio in Docker senza segreti montati e con l'opzione `--no-llm` per l'analisi solo statica. Per ricontrollare gli aggiornamenti delle cose già installate: scheda [Aggiornamenti mai automatici](sicurezza-aggiornamenti-mensili.md).
