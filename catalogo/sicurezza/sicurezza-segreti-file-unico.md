---
slug: sicurezza-segreti-file-unico
titolo: Le chiavi in un file solo, caricate solo quando servono
area: sicurezza
dove_gira: PC
livello: medio
costo: 0 €. Circa 30 minuti per spostare le chiavi.
pacchetto: "nessuno: solo idea"
stato: versione per PC del mio
---
# Le chiavi in un file solo, caricate solo quando servono

**Il problema.** Le chiavi API finivano ovunque: negli script, nei file .env di ogni progetto, a volte nelle note. Quando una andava cambiata non sapevo più dove fosse, e ogni copia era un posto in più da cui poteva uscire.

**Come l'ho risolto.** Tengo tutte le chiavi in un file solo, fuori dalle cartelle su cui lavora Claude, e i programmi non lo leggono direttamente. Un piccolo lanciatore apre il file, prende solo le chiavi scritte in un elenco di nomi ammessi e lancia il comando con quelle variabili. Non esegue il file come uno script, quindi una riga strana messa lì dentro non parte. Nelle note scrivo solo come si chiama una chiave e dove sta, mai il valore. Sul PC la versione semplice è la stessa idea senza lanciatore: un file fuori dal vault, escluso da git e messo nel deny dei permessi.

**Perché così.** Un posto solo vuol dire un posto solo da proteggere e da aggiornare. L'elenco dei nomi ammessi evita che una variabile delicata (per esempio PATH) cambi cosa gira. E Claude può usare una chiave senza vederla.

**Quando ti serve.** Quando hai più di due o tre chiavi API usate da script diversi, o quando Claude lancia script che chiamano servizi a pagamento.

**Quando non ti serve.** Se usi una o due chiavi in un solo progetto, per me basta un file .env escluso da git e messo nel deny dei permessi. Il lanciatore con l'elenco dei nomi serve davvero su un server dove gli agenti e l'amministratore sono utenti diversi.

**Come prenderlo.** Non c'è un pacchetto: è un modo di sistemare le cose. Sposta le chiavi in un file fuori dal vault (per esempio `~/.chiavi/chiavi.env`), escludilo da git e mettilo nel deny dei permessi (scheda [Permessi](sicurezza-permessi-deny-ask.md)). Su Mac e Windows un'alternativa è il portachiavi del sistema o un gestore di password con riga di comando (1Password CLI, Bitwarden CLI).
