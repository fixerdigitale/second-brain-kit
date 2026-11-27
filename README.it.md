🇬🇧 [English](README.md)

# Second Brain Kit

**Il mio second brain con Claude Code: cosa uso, cosa ho scartato, e un onboarding che studia il tuo sistema prima di proporti qualcosa.**

[![Licenza: MIT](https://img.shields.io/badge/licenza-MIT-informational)](LICENSE)
[![Versione](https://img.shields.io/badge/versione-2.0.0-informational)](CHANGELOG.md)
[![Plugin per Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-informational)](docs/INSTALLA.md)
[![Lingua](https://img.shields.io/badge/lingua-italiano%20%7C%20English-informational)](README.md)

[English](README.md) · [Installazione](docs/INSTALLA.md) · [Catalogo](catalogo/README.md) · [Cosa ho scartato](catalogo/scartati.md)

![Il giro del second brain: cattura, ordina, ritrova, usa, impara, intorno a una memoria fatta di note](docs/giro.svg)

## Perché lo condivido

Lavoro ogni giorno con Claude Code e con un piccolo gruppo di agenti. Mi sono costruito un sistema per non rispiegare tutto a ogni sessione, e un po' di persone mi hanno chiesto come funziona.
Questo è il mio modo, con i suoi limiti: non è un metodo e non è l'unico giusto. Prendi quello che ti serve e lascia il resto.

## Inizia in 2 minuti

1. Scarica la repo come zip (bottone **Code → Download ZIP**) oppure clonala:
   ```bash
   git clone https://github.com/fixerdigitale/second-brain-kit.git
   ```
2. Apri la cartella in Claude Code: dal terminale con `cd second-brain-kit && claude`, oppure da VS Code o dall'app desktop.
3. Scrivi **«avvia l'onboarding»**, oppure `/second-brain:onboarding` se hai installato il plugin.

Le altre strade (plugin dal marketplace, solo catalogo, Mac, Windows, Linux) sono in [docs/INSTALLA.md](docs/INSTALLA.md).

## Cosa c'è dentro

| Parte | Cosa fa | Dove |
|---|---|---|
| **Onboarding** | Prima guarda cosa hai già (solo nomi e conteggi, con il tuo permesso), ti dà un primo risultato concreto in circa 15 minuti, poi una mappa del tuo sistema e un piano di al massimo 3 passi. Dopo 14 giorni rifà le stesse misure. | [plugin/second-brain/](plugin/second-brain/) |
| **Catalogo** | 88 schede su quello che uso, divise in 8 aree: memoria, ricerca, impara, automazioni, agenti, canali, skill, sicurezza. Ogni scheda dice il problema, come l'ho risolto, perché così e quando **non** ti serve. | [catalogo/](catalogo/README.md) |
| **Scarti** | 45 strumenti e idee che ho provato o valutato e poi lasciato, con il motivo e quando a te potrebbero servire lo stesso. | [catalogo/scartati.md](catalogo/scartati.md) |
| **Pacchetti** | I file pronti da copiare per 64 schede: skill, hook, script, modelli di note. Ognuno ha un LEGGIMI con cosa fa, dove si copia e come si toglie. | [pacchetti/](pacchetti/) |

## Per chi è

- **Se parti da zero.** L'onboarding non usa gergo, ti fa una domanda alla volta e lancia lui i comandi. Il primo risultato è un lavoro vero che rifai spesso, fatto meglio.
- **Se hai già qualche file e un CLAUDE.md.** Ti mostra dove il sistema perde pezzi (memoria, correzioni, backup) e ti propone i passi più piccoli per chiuderli.
- **Se hai già un vault, skill tue, hook e agenti.** Lo studia area per area e ti parla da pari. Probabilmente in qualche punto il tuo sistema è migliore del mio: il catalogo ti serve più come confronto che come lista da installare.

Il livello non te lo chiede: lo legge dai file, area per area. Puoi essere avanzato sulla memoria e a zero sul backup, ed è normale.

## La mia giornata con l'AI

Come usano questi pezzi insieme, dal brief del mattino al lavoro della notte: [La mia giornata con l'AI](catalogo/canali/canali-giornata-con-ai.md).
Molte cose io le faccio girare su un server. Tutto può girare anche su un PC: la differenza è che il PC non è sempre acceso, il server sì. Ogni scheda dice dove gira.

## Cosa ho scartato

Di solito si racconta solo quello che funziona. Io ho tenuto anche l'elenco di quello che ho provato e lasciato: sistemi di memoria per agenti, motori di ricerca, piattaforme di automazione, canali. Non sono bocciature: sono scelte fatte per il mio modo di lavorare. [Leggi cosa ho scartato](catalogo/scartati.md).

## Sicurezza

L'onboarding lavora in sola lettura finché non dici sì. In particolare non fa mai da solo queste cose:

- leggere fuori dalle cartelle che hai autorizzato, o aprire browser, email e chat;
- stampare, copiare o mettere in memoria i valori di password, chiavi e token;
- scrivere, spostare, rinominare o cancellare senza un sì per ogni voce (prima fa una copia datata, e invece di cancellare sposta in `_da-cancellare/`);
- fare push, creare repository o condividere qualcosa;
- installare skill, MCP o plugin presi da fuori senza un controllo e un sì;
- attivare hook, permessi larghi o la modalità automatica senza spiegarti l'effetto;
- mandare qualcosa all'esterno: niente telemetria, la mappa e il piano restano sul tuo computer.

Non incollare mai password o chiavi nella chat, nemmeno qui.

## Limiti onesti

- È il sistema di una persona sola, con il suo lavoro (un piccolo studio digitale) e i suoi abbonamenti (Claude Max e ChatGPT). Alcune scelte hanno senso solo lì.
- Le schede marcate «server» descrivono come lo faccio io: sul PC vanno adattate, e alcune non hanno un pacchetto.
- Le versioni per PC sono adattamenti dei miei originali: le ho usate molto meno a lungo.
- Claude Code cambia spesso. Qualche comando o impostazione potrebbe essere già diverso quando leggi.
- I testi sono nati in italiano; la versione inglese è una traduzione.
- Non è consulenza: su backup, permessi e dati di altre persone decidi tu, con i tuoi criteri.

## Contribuire

Mi interessa soprattutto sapere cosa non ha funzionato per te: apri una issue con il tuo sistema operativo, la versione di Claude Code e cosa è successo.
Se hai un modo migliore per fare qualcosa che sta nel catalogo, una pull request con una scheda nuova o una correzione è benvenuta. Tieni lo stesso schema delle altre schede, con la sezione «Quando non ti serve», e niente nomi di persone, clienti o dati veri.

## Licenza

[MIT](LICENSE) © 2026 Daniel Martines / Fixer Digitale. Usalo, cambialo, rigiralo: se ti è stato utile mi fa piacere saperlo.
