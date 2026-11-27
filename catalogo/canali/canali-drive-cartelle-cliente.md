---
slug: canali-drive-cartelle-cliente
titolo: "Drive condiviso con le stesse cartelle per ogni cliente"
area: canali
dove_gira: PC
livello: base
costo: "0 € se hai già Google Workspace; dieci minuti"
pacchetto: "pacchetti/canali-drive-cartelle-cliente/"
stato: "versione per PC del mio"
---
# Drive condiviso con le stesse cartelle per ogni cliente

**Il problema.** I documenti creati dall'AI nascevano nel mio Drive personale, ognuno in un posto diverso. Chi lavora con me non li vedeva, e ogni volta dovevo condividerli a mano.

**Come l'ho risolto.** Ogni file nasce nel Drive condiviso dello studio, che vedono chi lavora con me e l'account del mio assistente principale. Ogni cliente ha sempre le stesse cinque cartelle: 01 Documenti iniziali, 02 Materiali, 03 Per le richieste, 04 Consegne, 05 Lavoro interno. Un comando dà a Claude la cartella giusta per cliente e tipo, così il file nasce già al suo posto. Bozze e verifiche vanno in «Lavoro interno», in «Consegne» solo quello che va al cliente. Mai nel condiviso: credenziali, contratti, fatture e banca, dati di candidati, cose personali. Nel pacchetto: uno script che crea la struttura in una cartella sincronizzata con Drive per desktop, e la regola per il CLAUDE.md.

**Perché così.** Una struttura uguale per tutti vuol dire che né io né l'AI dobbiamo decidere ogni volta dove mettere un file. La lista di quello che non entra mai protegge le cose che non devono girare.

**Quando ti serve.** Se lavori con un socio, un assistente o un collaboratore che deve vedere i file dei clienti.

**Quando non ti serve.** Se lavori da solo e non condividi niente: la struttura nel vault basta. Se il tuo Google Workspace non ha i Drive condivisi, puoi usare una cartella condivisa normale, ma i file restano di chi li crea.

**Come prenderlo.** Copia `cartella_cliente.py`, metti in `RADICE` il percorso locale della cartella Clienti del Drive condiviso e incolla `regola-per-CLAUDE.md` nel CLAUDE.md. Lo script crea solo cartelle: non cancella e non sposta mai niente. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/canali-drive-cartelle-cliente/LEGGIMI.md).
