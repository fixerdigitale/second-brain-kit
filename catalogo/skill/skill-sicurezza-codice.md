---
slug: skill-sicurezza-codice
titolo: "Controlli di sicurezza su codice e siti"
area: skill
dove_gira: PC
livello: avanzato
costo: "0 €; una revisione completa di un progetto medio consuma parecchio contesto"
pacchetto: "nessuno: skill di terzi dalla fonte"
stato: "lo uso"
---
# Controlli di sicurezza su codice e siti

**Il problema.** Quando faccio costruire all'AI strumenti con accessi, chiavi o dati di altri, mi serve un secondo sguardo che cerchi i buchi, non solo i bug.

**Come l'ho risolto.** Ho due skill di terzi. security-audit (di Cloudflare) guida una revisione del codice per classi di attacco: autenticazione, isolamento dei dati, catena di fornitura, AI e prompt, con validatori per il report. security-scanner è un kit di comandi per scansioni di porte e vulnerabilità con nmap e nuclei, solo su bersagli autorizzati.

**Perché così.** security-audit la uso sul codice delicato: ragiona per classi di attacco invece di fare una lista generica. security-scanner la tengo come promemoria di comandi: nmap e nuclei non li ho installati, quindi di fatto non la uso.

**Quando ti serve.** Prima di mettere online uno strumento con login, chiavi o dati di terzi; quando qualcuno ti chiede di controllare il suo sito (con autorizzazione scritta).

**Quando non ti serve.** Per siti vetrina senza moduli né accessi. La scansione di porte non va mai su sistemi che non sono tuoi o per cui non hai un'autorizzazione.

**Come prenderlo.** Skill di terzi, dalla fonte: security-audit da https://github.com/cloudflare/security-audit-skill; security-scanner dal registro ClawHub (https://clawhub.ai/dmx64/security-scanner), che è aperto: leggila prima. nmap e nuclei si installano a parte.
