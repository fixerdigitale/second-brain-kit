---
slug: impara-skill-migliorate-dalle-sessioni
titolo: "Skill che migliorano leggendo le sessioni, adottate da me"
area: impara
dove_gira: PC acceso
livello: avanzato
costo: "0 € in più con l'abbonamento Claude, ma consuma quota di notte (io ho un tetto di 150.000 token per notte). Installazione: 30-60 minuti."
pacchetto: "pacchetti/impara-skill-migliorate-dalle-sessioni/"
stato: "lo uso"
---

# Skill che migliorano leggendo le sessioni, adottate da me

**Il problema.** Le mie skill le scrivevo una volta e poi restavano com'erano, anche quando nelle sessioni vedevo Claude inciampare sempre sugli stessi passaggi. Riscriverle a mano, guardando decine di sessioni, non lo facevo mai.

**Come l'ho risolto.** Uso SkillOpt-Sleep, parte del progetto open source SkillOpt di Microsoft. Di notte legge le sessioni recenti, trova i lavori che ripeto, li rigioca con e senza una modifica alla skill e propone la modifica solo se migliora su compiti tenuti da parte. Io l'ho configurato con l'abbonamento Claude, mai con chiavi a consumo, e con l'adozione automatica spenta: ogni proposta mi arriva da approvare, con le regole che non deve contraddire. Su 7 notti da quando le approvo: 1 adottata, 1 scartata da me, 2 senza proposta perché il controllo non è passato, le altre ritirate o in attesa.

**Perché così.** Le sessioni contengono già la prova di cosa funziona e cosa no; uno strumento può leggerle meglio di me. Ma una skill cambia il comportamento di tutte le sessioni dopo, quindi l'ultima parola resta mia.

**Quando ti serve.** Se hai skill che usi ogni giorno su lavori ripetuti, e il PC può restare acceso di notte.

**Quando non ti serve.** Se hai poche skill o lavori sempre diversi: non ci sono compiti ricorrenti da rigiocare, e il giro consuma quota per niente. Non usarlo su progetti con dati che hai promesso di non far uscire: pezzi delle sessioni vanno al fornitore del modello, e la documentazione dice che l'oscuramento dei segreti non è una garanzia. Io l'ho sul server: sul PC non l'ho provato.

**Come prenderlo.** Dalla fonte: https://github.com/microsoft/SkillOpt (`pip install skillopt`). Nel pacchetto c'è la mia configurazione d'esempio, con l'adozione automatica spenta, e i passi per provarlo prima senza scrivere niente. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/impara-skill-migliorate-dalle-sessioni/LEGGIMI.md).
