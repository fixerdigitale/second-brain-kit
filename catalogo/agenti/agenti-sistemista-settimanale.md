---
slug: agenti-sistemista-settimanale
titolo: "Sistemista settimanale in sola lettura"
area: agenti
dove_gira: PC acceso
livello: medio
costo: "0 € in più. Circa 5 minuti di corsa a settimana. Facoltativi e gratuiti: gh e gitleaks."
pacchetto: "pacchetti/agenti-sistemista-settimanale/"
stato: "versione per PC del mio"
---

# Sistemista settimanale in sola lettura

**Il problema.** Credevo di avere i backup. Ma un backup che non ho mai provato a ripristinare è solo una speranza, e una chiave finita per sbaglio in un commit non la vedo finché non fa danno.

**Come l'ho risolto.** Sul server il Sistemista tiene in piedi tutto e controlla il lavoro degli altri con prove allegate. Per il PC ho scritto un sotto-agente che una volta a settimana controlla, senza toccare niente: vault salvato su GitHub e allineato, repo privata, cartella Drive aggiornata, prova di ripristino in una cartella temporanea, parole sospette (password, token, chiavi) nella storia dei commit senza mai mostrarne il valore, file che non dovrebbero stare nel repo, programmi molto vecchi. Ogni punto torna OK, PROBLEMA o NON VERIFICABILE.

**Perché così.** Chi controlla non aggiusta: se aggiusta, nessuno controlla più lui. E tenere «non verificabile» separato da «ok» mi impedisce di scambiare un controllo saltato per un controllo superato.

**Quando ti serve.** Se il vault è su GitHub o Drive e ci tieni dentro cose che non vuoi perdere, o se ci hai mai incollato una chiave.

**Quando non ti serve.** Se il vault è piccolo e lo copi a mano ogni settimana su un disco che controlli tu. Nota onesta: la sola lettura è garantita dalle istruzioni, non da un blocco tecnico, perché il sotto-agente usa Bash; se vuoi un blocco vero, togli Bash dagli strumenti e perdi i controlli git.

**Come prenderlo.** Copia `sistemista.md` in `~/.claude/agents/` e sostituisci i segnaposto (vault, repo, Drive). Lancialo a mano una volta a settimana o con un'attività pianificata che esegue `claude -p`. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/agenti-sistemista-settimanale/LEGGIMI.md).
