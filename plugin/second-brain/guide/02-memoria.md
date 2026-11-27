# 02 · La memoria

## Perché serve

In una chat normale ogni conversazione riparte da zero: rispieghi chi sei, che clienti hai, come vuoi i report. Le informazioni utili restano sparse nelle chat vecchie.

Con il second brain la memoria sono **file di testo tuoi** nella cartella `memoria/`. Dici una cosa una volta, Claude la scrive lì e la ritrova domani. Li puoi aprire, correggere, copiare. E se un giorno cambi strumento (un altro Claude, un'altra AI), la memoria viene con te.

## Le parole

- **Vault**: una cartella piena di file di testo collegati fra loro. Il tuo vault è `memoria/`.
- **Markdown (`.md`)**: testo semplice con titoli (`#`) ed elenchi (`-`). Si apre con qualsiasi editor.
- **Obsidian**: un programma gratuito per leggere e scrivere quelle note in modo comodo (obsidian.md). Facoltativo: a Claude basta la cartella.
- **CLAUDE.md**: il foglio di istruzioni che Claude legge all'inizio di ogni sessione.

## Come è organizzata

Una nota per cliente in `memoria/Clienti/`, una per progetto in `memoria/Progetti/`, e così via. Il dettaglio delle cartelle è in `memoria/COME-FUNZIONA.md`.

La nota più importante è quella del cliente, e la sezione più importante della nota è **«Strumenti e account»**: quale account Google, quali piattaforme, quali strumenti creativi si usano **per quel cliente**. Claude la legge prima di toccare qualunque cosa, e se manca un dato chiede invece di indovinare. È la difesa contro l'errore più costoso: usare il metodo o l'account di un cliente per un altro.

## Come si usa, in pratica

- **«Salva in memoria che…»**: Claude scrive il fatto nella nota giusta, con la data e la fonte, e ti dice dove l'ha messo.
- **Alla fine di un lavoro importante** Claude ti propone una voce per la nota del cliente: dici sì o no.
- **«Cosa sai del cliente X?»**: Claude legge la nota e ti risponde da lì, non da quello che si immagina.
- **Ogni mese**: «rileggi la memoria e dimmi cosa è vecchio, doppio o in contraddizione».

## Se hai importato le chat da claude.ai

Se hai già fatto l'importazione, in `memoria/` ci sono file come `chi-sono.md`, `clienti.md`, `persone.md`, `lavori-ricorrenti.md`. Vanno benissimo così. Quando hai tempo, chiedi a Claude di spostare **un cliente alla volta** da `clienti.md` a una nota sua in `memoria/Clienti/`, copiando il modello: «sposta il cliente X in una nota sua, non cancellare niente da clienti.md finché non controllo». `lavori-ricorrenti.md` è il punto di partenza delle pipeline (guida 08).

## Cosa non mettere mai in memoria

Password, chiavi, codici di accesso, dati bancari, dati personali di lead e contatti. Se una cosa serve, si scrive solo *dove* sta («nel gestore password»).

Ricorda anche che quello che Claude legge passa dai server di Anthropic: per i documenti che un cliente ti ha dato in riservatezza, chiediti prima se puoi farli leggere a un servizio esterno.

## Prova adesso (2 minuti)

Scrivi: «crea la nota del mio cliente principale in memoria. Fammi tre domande alla volta, a partire dagli strumenti e dagli account».
