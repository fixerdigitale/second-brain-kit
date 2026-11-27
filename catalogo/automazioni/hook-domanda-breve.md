---
slug: hook-domanda-breve
titolo: "Domanda breve: risposta, non lavoro"
area: automazioni
dove_gira: PC
livello: base
costo: "0 €. 5 minuti."
pacchetto: "pacchetti/hook-domanda-breve/"
stato: "lo uso"
---

# Domanda breve: risposta, non lavoro

**Il problema.** Facevo una domanda veloce («ma la mail parte da sola?») e Claude partiva con letture, sotto-agenti e a volte modifiche. Volevo una risposta, mi trovavo un lavoro avviato.

**Come l'ho risolto.** Ho messo un hook UserPromptSubmit che decide solo dal testo: se il messaggio è breve, è una domanda e non ha verbi di lavoro (fai, crea, sistema…), aggiunge a Claude «rispondi in poche righe, al massimo 3 letture; se serve lavoro proponilo e aspetta l'ok». Da me è scattato circa 450 volte.

**Perché così.** Distinguere una domanda da un ordine è facile per una persona e meno per un modello zelante. Una regola fissa sul testo non costa niente, e i verbi di lavoro la spengono quando non deve scattare.

**Quando ti serve.** Se usi Claude anche per domande al volo nella stessa sessione dove lavori.

**Quando non ti serve.** Se Claude con te risponde già corto alle domande. Se scrivi molto a voce o con frasi lunghe, il filtro sulla lunghezza lo fa scattare poco.

**Come prenderlo.** Copia `domanda_breve.py` in `~/.claude/hooks/` e il blocco di `settings-esempio.json` in `~/.claude/settings.json`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-domanda-breve/LEGGIMI.md).
