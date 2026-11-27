---
name: pagine-legali
description: "Scrive le pagine legali di un sito o di una landing italiana: informativa privacy, cookie policy, condizioni generali di servizio, informativa sull'uso dell'AI e testi del banner cookie (vanilla-cookieconsent). Prima verifica il sito (scansione del codice e prova nel browser), raccoglie i fatti dal committente, poi scrive con segnaposto per quello che manca. Usala quando chiedono «fai la privacy» o «la cookie policy», «serve il banner cookie», «termini e condizioni», «informativa AI»; quando una landing va online o aggiunge strumenti (Meta Pixel, Clarity, Google Analytics, moduli GoHighLevel, video, calendari); per controllare se le pagine legali esistenti sono ancora vere. Produce bozze da far rivedere a un professionista: non è consulenza legale."
---

# Pagine legali

> **Avviso.** I testi prodotti con questa skill non sono consulenza legale. Sono bozze costruite su
> fatti verificati. Prima di pubblicarli è consigliata la revisione di un professionista (avvocato o
> consulente privacy). Dillo sempre anche a chi riceve la consegna.

La skill serve a scrivere, per i tuoi siti e per quelli dei clienti, cinque cose: informativa privacy,
cookie policy, condizioni di servizio, informativa sull'uso dell'AI, testi del banner cookie. Il
metodo è semplice: prima si guarda cosa fa davvero il sito, poi si scrive. Mai il contrario.

## Regole fisse

1. **Prima i fatti, poi i testi.** Nessuna pagina senza scansione del sito (passo 2) e scheda dei
   fatti compilata (passo 1).
2. **Niente dati inventati.** Ragione sociale, indirizzi, P.IVA, fornitori, tempi di conservazione:
   se non hanno una fonte, resta il segnaposto `{{...}}` e il punto va in `da-verificare.md`.
3. **Niente citazioni inventate.** Citi solo le norme di `riferimenti.md`. Se ne serve un'altra,
   leggila su una fonte primaria (EUR-Lex, Normattiva, Gazzetta Ufficiale, Garante), aggiungila a
   `riferimenti.md` con fonte e data, poi usala. Se non la trovi, scrivi «da verificare».
4. **Le date cambiano.** Prima di ogni consegna rifai i controlli di `riferimenti.md`, sezione «Da
   ricontrollare a ogni consegna» (AI Act, riforma dei cookie, P.IVA dal 2027, trasferimenti USA).
5. **Non tocchi il sito e non pubblichi.** Consegni bozze e un piano. Le modifiche al codice le fa
   chi gestisce il sito, dopo il tuo ok. Si pubblica dopo la revisione del professionista.
6. **Non togli le parole del cliente senza chiedere.** Se aggiorni pagine esistenti, correggi quello
   che è falso o manca. Il resto si tocca solo se il cliente è d'accordo.
7. **Le bozze stanno fuori dal sito.** Mai nelle cartelle pubblicate: una bozza con segnaposto non
   deve finire online.

## Dove lavori

```bash
S=~/.claude/skills/pagine-legali                          # questa skill
W=<tuo-progetto>/pagine-legali-<dominio>-<AAAA-MM-GG>     # cartella di lavoro
D=<dominio>
mkdir -p $W
```

Nella cartella di lavoro finiscono: `fatti.md`, `scansione.txt`, i file `consenso*.txt`, la
cartella `html/`, le schermate del banner, le pagine (`privacy.md`, `cookie-policy.md`,
`termini-servizio.md`, `informativa-ai.md`, `banner.md`), `checklist-esito.md` e `da-verificare.md`.

## Il flusso

### 1. Raccogli i fatti dal sito e dal committente

1. Copia la scheda: `cp $S/modelli/scheda-fatti.md $W/fatti.md`.
2. Dal sito: leggi piè di pagina, pagine legali esistenti, moduli, pagina contatti. Accanto a ogni
   dato scrivi la fonte (URL e data).
3. Dal committente: usa le domande della sezione 8 della scheda. Mandale tutte insieme, numerate,
   passando da chi segue il cliente.
4. Senza ragione sociale, sede, P.IVA ed email per la privacy si prepara solo una bozza con i
   segnaposto, dichiarata come tale.
5. Decidi se è **B2B, B2C o tutti e due**. Se vendi soprattutto ad aziende vale il B2B; se anche un solo
   servizio si vende a consumatori (persone fisiche che comprano fuori dalla loro attività: art. 3
   del Codice del consumo), servono le parti B2C delle condizioni di servizio.

### 2. Verifica gli strumenti presenti

Due strumenti, da usare insieme. Il browser dice cosa succede davvero; la scansione dice dove cercare
nel codice.

```bash
# Prova nel browser: prima della scelta, dopo «Rifiuta», dopo «Accetta».
# Salva l'HTML di tutte le pagine visitate e la schermata del banner.
node $S/scripts/consenso.mjs https://$D/ --rifiuta --accetta --pagina https://$D/<pagina-con-modulo> \
  --salva-html $W/html --foto $W/banner-desktop.png > $W/consenso.txt
node $S/scripts/consenso.mjs https://$D/ --mobile --foto $W/banner-mobile.png > $W/consenso-mobile.txt

# Scansione dell'HTML salvato (o della cartella del progetto, se hai il codice)
python3 $S/scripts/scan.py $W/html --domain $D > $W/scansione.txt
```

- Se hai il codice del sito, scansiona anche quello. Per i siti generati (Next.js, Hugo) scansiona la
  cartella generata e leggi i sorgenti a mano.
- I moduli e i calendari dentro un iframe non si vedono dalla pagina: apri l'indirizzo dell'iframe
  con `consenso.mjs` e guardalo a parte.
- La scansione è una lista di indizi: conferma ogni punto leggendo il codice o nel browser.
- Se guardi il sito con un browser automatico e il banner non compare, può dipendere da questo:
  vanilla-cookieconsent nasconde il banner quando `navigator.webdriver` è vero, come nei browser
  automatici. `consenso.mjs` lo disattiva.

Cosa cercare e cosa significa:

| Strumento | Come lo riconosci | Categoria | Cosa scrivere o fare |
|---|---|---|---|
| Meta Pixel | `connect.facebook.net`, `fbq(`, cookie `_fbp` `_fbc` | marketing | Bloccalo fino al consenso; togli il pixel in `<noscript>`. In privacy: chi è il fornitore e dove tratta i dati (dai suoi termini); contitolarità per raccolta e trasmissione dei dati (CGUE C-40/17, applicata ai pixel per analogia: da far confermare). |
| Microsoft Clarity | `clarity.ms`, cookie `_clck` `_clsk` | analitici, con consenso | Dal 31/10/2025 Microsoft chiede un segnale di consenso per le visite da SEE, Regno Unito e Svizzera. Blocca lo script fino al consenso, poi manda `clarity('consentv2', ...)`. Registra clic e movimenti: dillo nei testi. |
| Google Analytics 4 | `gtag(`, `googletagmanager.com/gtag/js`, cookie `_ga` `_ga_<ID>` | analitici, con consenso | Il Garante equipara ai tecnici solo gli analitici minimizzati (par. 7.2 delle linee guida). Per GA4 configurato in modo standard chiedi il consenso; ogni eccezione la decide il professionista. |
| Google Tag Manager | `gtm.js`, `GTM-` | dipende dai tag | Carica altri strumenti: guarda in `consenso.txt` cosa parte prima del consenso. |
| Font da CDN | `fonts.googleapis.com`, `fonts.gstatic.com` | nessun cookie, ma l'IP va al fornitore | Meglio ospitare i font sul sito. Se restano, il fornitore va tra i destinatari. |
| Video (YouTube, Vimeo, Bunny) | `youtube.com/embed`, `youtube-nocookie.com`, `player.vimeo.com`, `mediadelivery.net` | marketing (contenuti esterni) | Caricali solo dopo il consenso o con un'anteprima cliccabile (`modelli/testi-banner.md`, sezione 6). |
| Moduli GoHighLevel | iframe o script da `leadconnectorhq.com`, `msgsndr.com` | dipende: guarda i cookie nel browser | Il modulo raccoglie dati: in privacy finalità, base giuridica, fornitore come responsabile, dove stanno i dati. L'iframe parte subito: chiedi al professionista se basta l'informativa o se va caricato dopo un clic. |
| WhatsApp | link `wa.me`, `api.whatsapp.com`; widget di terzi | il link non carica nulla; i widget sì | In privacy è un canale di contatto: i messaggi passano dal fornitore dell'app. I widget si bloccano come gli altri script. |
| Calendari (Google Calendar, Calendly) | iframe `calendar.google.com`, `calendly.com` | contenuti esterni | Meglio un link che apre il calendario. Se è incorporato: bloccato o anteprima. In privacy: dati della prenotazione. |
| n8n | moduli che inviano a `/webhook/...` | nessun cookie | È un passaggio dei dati: in privacy dove gira (server, Paese) e chi lo gestisce. |
| NocoDB | moduli `/nc/form/`, chiamate alle sue API | nessun cookie | È un archivio: dove sta, chi accede, per quanto tempo restano i dati. |
| reCAPTCHA | `recaptcha` | terze parti | Manda dati al fornitore: va nelle informative. Valuta un'alternativa. |
| Chat con AI | widget di chat, chiamate a modelli AI | dipende | Avviso «stai parlando con un'AI» al primo messaggio (AI Act, art. 50). Vedi `modelli/informativa-ai.md`. |

### 3. Classifica cookie e trattamenti

**Cookie.** Tre categorie, le stesse del banner:

- **tecnici**: servono a far funzionare il sito o un servizio chiesto dall'utente; niente consenso,
  ma vanno nell'informativa (art. 122 Codice privacy);
- **analitici**: con consenso, salvo le condizioni del par. 7.2 delle linee guida del Garante;
- **marketing**: con consenso; qui finiscono anche i contenuti esterni che usano cookie propri.

Come si fa:

1. Parti dalla fase 3 di `consenso.txt` («dopo l'accettazione»): nome, dominio, durata, prima o terza
   parte.
2. Lo scopo lo prendi dalla documentazione del fornitore. Se non lo trovi, il cookie va in
   `da-verificare.md`: non si indovina.
3. Il legittimo interesse non giustifica i cookie (linee guida del Garante, par. 5).
4. Scrivi in `fatti.md` anche il criterio con cui classifichi: la cookie policy lo deve dire (par. 8.2).

**Trattamenti.** Compila la tabella della sezione 4 di `fatti.md`: attività, dati, finalità, base
giuridica, conservazione, destinatari, trasferimenti. Le basi tipiche di una landing B2B:

| Attività | Base giuridica di solito |
|---|---|
| Rispondere a una richiesta o preparare un preventivo | Misure precontrattuali chieste dall'interessato (GDPR art. 6, par. 1, lett. b) |
| Clienti: contratto e fatture | Contratto (lett. b) e obblighi di legge (lett. c); fatture e scritture per dieci anni (art. 2220 c.c.) |
| Newsletter e offerte | Consenso (lett. a). Ai clienti, per servizi analoghi, l'eccezione dell'art. 130, comma 4, Codice privacy |
| Statistiche e pubblicità con cookie | Consenso (lett. a e art. 122 Codice privacy) |
| Sicurezza del sito e log | Legittimo interesse (lett. f), da descrivere |

- **Trasferimenti negli USA:** controlla che il fornitore sia nell'elenco del Data Privacy Framework
  (https://www.dataprivacyframework.gov/list). Se non c'è, servono altre garanzie.
- **Ruoli:** quando lo studio gestisce per un cliente i dati dei suoi contatti (CRM, moduli,
  automazioni, archivi), lo studio è responsabile del trattamento (GDPR art. 28): serve un accordo
  scritto. Segnalalo se manca.
- Decisioni automatizzate con effetti giuridici (art. 22): di norma non ci sono. Se ci sono, fermati
  e chiedi al professionista.

### 4. Scrivi le pagine

Copia i modelli nella cartella di lavoro e riempili con i dati di `fatti.md`.

| Modello | Quando serve |
|---|---|
| `modelli/privacy.md` | Quasi sempre: basta un modulo, una chat o un cookie non tecnico |
| `modelli/cookie-policy.md` | Se ci sono cookie, archivio locale o contenuti di terzi. Con soli cookie tecnici basta una sezione breve |
| `modelli/termini-servizio.md` | Se il sito vende servizi o il cliente vuole condizioni standard per i preventivi |
| `modelli/informativa-ai.md` | Se lo studio usa l'AI nel lavoro per i clienti, o il sito ha una chat con AI o pubblica contenuti generati |
| `modelli/testi-banner.md` | Se c'è almeno un cookie o uno strumento non tecnico |

Come si riempiono:

- Ogni `{{segnaposto}}` si sostituisce solo con un dato di `fatti.md`. Se manca, resta visibile e
  va in `da-verificare.md`.
- Le parti `[SOLO SE ...]` restano solo se il caso c'è. Le note per chi compila si tolgono.
- Scrivi come chiede l'art. 12 del GDPR: forma concisa, chiara, linguaggio semplice. Frasi corte,
  niente gergo, niente calchi dall'inglese. Nelle informative si dà del tu; nelle condizioni si
  parla di «Studio» e «Cliente».
- Stessi dati in tutte le pagine: ragione sociale, email, indirizzo, data di aggiornamento.
- Prepara anche il testo del piè di pagina: ragione sociale, sede, P.IVA, REA, link a privacy e
  cookie policy, link «Preferenze cookie». Per le S.r.l. aggiungi capitale versato e socio unico, se
  c'è (art. 2250 c.c.).

### 5. Controlla con la checklist

1. Segui `checklist.md` dall'inizio alla fine. Ogni punto: OK, KO o NON SI APPLICA, con la prova.
2. Salva l'esito in `$W/checklist-esito.md`.
3. Quando il Designer ha messo il banner e i link (prima in prova, poi online), rifai le sezioni B e D.
4. Un KO si corregge e si ricontrolla. Non si chiude a parole.

### 6. Consegna con l'elenco dei punti da far verificare

1. Scrivi `$W/da-verificare.md`, un elenco numerato. Per ogni punto: cosa, perché (fatto mancante o
   dubbio), chi risponde (committente o professionista), riferimento. Ci sono sempre:
   - la revisione complessiva dei testi da parte di un professionista;
   - i fatti mancanti (segnaposto rimasti);
   - i punti «da verificare» di `riferimenti.md` che toccano questo sito.
2. Prepara per chi gestisce il sito le modifiche: script da bloccare, banner, link nel piè di pagina.
3. Prima di dire che è pronto, fai rileggere tutto a un secondo revisore (un'altra sessione o una persona): sono testi per un
   cliente.
4. Il messaggio di consegna dice: cosa è pronto, cosa manca, cosa deve vedere il professionista, la
   prossima azione. I problemi del sito si scrivono al presente e senza colpe: «manca la P.IVA in
   home page», non «non avete messo la P.IVA».
5. Non pubblichi nulla e non mandi nulla al cliente senza l'ok di chi ti ha chiesto il lavoro.

## File della skill

| File | A cosa serve |
|---|---|
| `riferimenti.md` | Norme e fonti tecniche verificate, con data. Cosa ricontrollare a ogni consegna |
| `checklist.md` | Controlli con i comandi da lanciare |
| `modelli/scheda-fatti.md` | La scheda dei fatti e le domande per il committente |
| `modelli/privacy.md` | Informativa privacy (GDPR art. 13) |
| `modelli/cookie-policy.md` | Cookie policy con la tabella dei cookie |
| `modelli/termini-servizio.md` | Condizioni di servizio B2B, con la parte per i consumatori |
| `modelli/informativa-ai.md` | Come lo studio usa l'AI |
| `modelli/testi-banner.md` | Testi e configurazione di vanilla-cookieconsent 3 |
| `scripts/consenso.mjs` | Prova nel browser: cookie e richieste prima della scelta, dopo «Rifiuta», dopo «Accetta» |
| `scripts/scan.py` | Scansione del codice o dell'HTML salvato, solo libreria standard di Python |
| `NOTICE`, `LICENSE` | Crediti e licenza Apache 2.0 della parte presa da gricyk |

## Crediti

Il metodo (verifica prima di scrivere, niente dati inventati, citazioni solo verificate, lista di
controllo) e lo scanner `scripts/scan.py` vengono da
[claude-skill-eu-web-compliance](https://github.com/gricyk/claude-skill-eu-web-compliance) di Igor
Gricyk, licenza Apache 2.0. Cosa è stato preso e cosa è stato cambiato è scritto nel file `NOTICE`.
