---
description: Fermati a un punto di controllo e chiedi l'ok sul telefono; il lavoro riparte da solo quando rispondo
---
Siamo a un punto in cui ti serve un mio ok per andare avanti. Fai così, in quest'ordine:

1. Aggiorna HANDOFF.md nella cartella del progetto: cosa hai fatto, cosa resta, la domanda precisa e
   cosa farai con un sì e con un no. Chi riparte legge solo quel file.
2. Scegli un id corto e nuovo (minuscole e trattini, per esempio `landing-passo-3`).
3. Lancia: `python3 "$HOME/.claude/ponte/ponte_telefono.py" chiedi <id> "<domanda in max 3 righe: cosa approvo e cosa succede con sì e con no>" --cartella "<cartella del progetto>"`
4. Nella domanda niente password, chiavi o dati personali: passa da un servizio di notifiche.
5. Dimmi in una riga che hai chiesto e fermati. Non aspettare la risposta in questa sessione.

$ARGUMENTS
