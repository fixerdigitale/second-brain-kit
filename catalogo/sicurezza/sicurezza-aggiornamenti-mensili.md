---
slug: sicurezza-aggiornamenti-mensili
titolo: "Aggiornamenti mai automatici: un controllo al mese, poi decido io"
area: sicurezza
dove_gira: PC acceso
livello: base
costo: 0 €. 10 minuti per configurarlo, poi pochi minuti al mese per leggere la nota.
pacchetto: pacchetti/sicurezza-aggiornamenti-mensili/
stato: versione per PC del mio
---
# Aggiornamenti mai automatici: un controllo al mese, poi decido io

**Il problema.** Le skill e gli strumenti presi da GitHub cambiano a monte. Un aggiornamento automatico può portare dentro un hook nuovo, uno script di installazione diverso o un'impostazione che non ho mai letto, e il controllo di sicurezza che avevo fatto all'installazione non vale più.

**Come l'ho risolto.** Per gli strumenti di terzi niente aggiornamenti automatici. Una volta al mese un controllo guarda cosa è cambiato a monte e mi scrive una nota: quanti commit nuovi, quali file sensibili sono stati toccati (hook, script, impostazioni, file che lanciano comandi). Non aggiorna niente. Poi decido io: se cambiano parti delicate rifaccio il controllo di sicurezza, faccio una copia, e aggiorno una cosa alla volta. Per il PC ho scritto la stessa idea: controlla le skill installate con git e i pacchetti npm globali.

**Perché così.** Così ogni aggiornamento passa dagli stessi occhi dell'installazione. Una volta al mese è abbastanza per non restare troppo indietro, e abbastanza raro da leggere la nota con attenzione.

**Quando ti serve.** Se hai installato skill, MCP o strumenti da repository di terzi, soprattutto se contengono script o hook.

**Quando non ti serve.** Per Claude Code stesso e per i plugin ufficiali mi tengo gli aggiornamenti normali. Per le correzioni di sicurezza urgenti di un programma che usi tutti i giorni aspettare un mese può essere troppo: lì aggiorno subito, dopo aver letto cosa cambia. Se non hai niente preso da fuori, non serve.

**Come prenderlo.** Cambia la cartella delle note in `controlla_aggiornamenti.py` e programmalo il primo del mese. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-aggiornamenti-mensili/LEGGIMI.md). Il controllo di sicurezza da rifare è nella scheda [Controllo prima di installare](sicurezza-scan-prima-di-installare.md).
