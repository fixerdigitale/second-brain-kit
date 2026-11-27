---
slug: sicurezza-controlli-salute
titolo: Controlli di salute che avvisano solo quando lo stato cambia
area: sicurezza
dove_gira: PC acceso
livello: medio
costo: 0 €. 20 minuti per scrivere i controlli.
pacchetto: pacchetti/sicurezza-controlli-salute/
stato: versione per PC del mio
---
# Controlli di salute che avvisano solo quando lo stato cambia

**Il problema.** Quando le cose girano da sole, il rischio che mi preoccupa di più è che si rompano in silenzio: un'automazione che scrive «tutto ok» senza fare niente, un sito che risponde ma resta bianco perché un file è sparito, un backup fermo da giorni. E all'opposto, un controllo che mi avvisa a ogni giro finisce che non lo leggo più.

**Come l'ho risolto.** Sul server ho dei controlli automatici che guardano il risultato, non se una cosa è partita: le pagine pubbliche lette come le legge un browser (pagina più script, css e font), la memoria del server, i lavori notturni che devono aver prodotto qualcosa, i backup che devono essere recenti. Ognuno salva il suo stato e mi scrive solo quando cambia: una volta quando si rompe, una volta quando torna a posto. Se resta rotto, niente promemoria a ogni giro. Prima di dire a qualcuno «funziona» faccio anche un controllo a mano, in sola lettura. Per il PC ho scritto una versione piccola: un file con l'elenco dei controlli (indirizzi, file che devono essere recenti, comandi che devono riuscire) e una notifica del sistema solo sui cambi.

**Perché così.** Un avviso che arriva solo quando qualcosa cambia lo leggo. E guardare l'esito invece della partenza è l'unico modo che conosco per accorgermi di un'automazione che mente con sicurezza.

**Quando ti serve.** Quando hai almeno una cosa che gira da sola e ti costa se si ferma: un backup, un sito, uno script notturno, un'automazione per un cliente.

**Quando non ti serve.** Se non hai niente che gira da solo, non c'è niente da controllare. La versione per PC controlla solo quando il PC è acceso: per un sito che deve stare su anche di notte serve un servizio di monitoraggio esterno o un server. E se un servizio ha già i suoi avvisi affidabili, non lo duplico.

**Come prenderlo.** Scrivi i tuoi controlli in `controlli.json`, provali con `--prova`, poi programma `controlli.py` ogni ora. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-controlli-salute/LEGGIMI.md).
