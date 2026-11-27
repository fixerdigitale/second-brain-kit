---
name: smistamento
description: >
  Primo passo su ogni richiesta: capisce se è una domanda (rispondi e basta) o un lavoro,
  per quale cliente, se ha già una pipeline, quanto è grande e con quale modello farlo.
  Si accende solo a mano, con /second-brain:smistamento: da sola non parte, perché cambierebbe
  ogni conversazione dal giorno dell'installazione e potrebbe scontrarsi con uno smistamento che la
  persona ha già. Le sue regole, se la persona le vuole sempre, vanno nel CLAUDE.md (missione
  cassetti-memoria).
disable-model-invocation: true
---

# Smistamento

Prima di fare, capisci cosa ti stanno chiedendo. Quattro domande, in quest'ordine.

## 1. Domanda o lavoro?

- **Domanda** («com'era…», «dov'è…», «cosa ne pensi…»): rispondi, con la fonte. Non costruire niente.
- **Lavoro** («fammi…», «prepara…», «sistema…»): vai avanti con le domande sotto.
- **Non è chiaro**: chiedi in una riga. «Vuoi che te lo spieghi o che lo faccia?»

## 2. Per quale cliente?

- Se il cliente è chiaro, apri la sua nota in `memoria/Clienti/` e leggi «Strumenti e account» prima di toccare qualunque cosa.
- Se non è chiaro, chiedi: «È per X o per Y?». Mai indovinare da un lavoro simile fatto per un altro cliente.
- Lavoro personale o interno: scrivilo, così non finisce nella nota di un cliente.

## 3. C'è già una pipeline?

Cerca in `pipeline/PIPELINE.md` il tipo di lavoro per quel cliente.

- **C'è**: dillo in una riga («Seguo ROSSI-1 · Report del lunedì») e seguila, passo per passo, con l'ok della persona (skill `definisci-pipeline`, «Come si usa: fase 1»).
- **Non c'è, ma c'è una registrazione** dello stesso lavoro: è la seconda volta. Seguila e alla fine proponi di farne una pipeline.
- **Non c'è niente**: fai il lavoro e alla fine registra i passi (due righe in fondo a `PIPELINE.md`).

## 4. Quanto è grande?

Dillo in una riga prima di iniziare, la persona può correggerti.

| Taglia | Come si riconosce | Cosa fai |
|---|---|---|
| Piccola | un passo, meno di 15 minuti | fallo, poi le tre righe: cosa, dove, come si torna indietro |
| Media | più passi, meno di un'ora | piano in 3-6 passi, ok della persona, poi passo per passo |
| Grande | più ore, più file, più giorni | piano con passi, tempi e decisioni della persona; spezzalo; `HANDOFF.md` se ti fermi |

Per i lavori medi e grandi, scegli chi fa cosa:

- cercare, contare, leggere tanti file, copiare dati già decisi → sotto-agente `esecutore`;
- ritocchi già decisi, script brevi → sotto-agente `costruttore`;
- decisioni, analisi, testi per il cliente, revisione → tu.

Se pensi che il lavoro consumi molto (tanti file, tante pagine, molte ore), dillo prima: la persona ha un limite d'uso ogni 5 ore e uno settimanale.

## Esempio

Persona: «Fammi il report della settimana.»
Bene: «Per quale cliente: Rossi o Bianchi? Per Rossi c'è la pipeline ROSSI-1, per Bianchi no.»
Male: partire con il foglio dell'ultimo cliente usato.
