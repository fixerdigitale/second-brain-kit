# Riferimenti normativi e tecnici

> **Avviso.** Questo elenco serve a scrivere bozze, non è consulenza legale. Prima di pubblicare
> pagine costruite su questi riferimenti è consigliata la revisione di un professionista.

Ogni voce dice cosa ci serve, la fonte primaria letta, la data della verifica e lo stato.

- **Verificato**: testo letto il giorno indicato su una fonte primaria (EUR-Lex, Normattiva,
  Gazzetta Ufficiale, Garante). Si può citare.
- **Da verificare**: il testo c'è, ma resta un dubbio su come si applica a noi, oppure manca una
  fonte primaria. Non va scritto come certo: va nell'elenco per il professionista.

Tutte le verifiche sono del **2 ottobre 2026**. Prima di citare una norma assente da questo file,
leggila su una fonte primaria e aggiungila qui con fonte e data.

## Da ricontrollare a ogni consegna

Sono i punti che cambiano più spesso. Bastano dieci minuti.

1. **AI Act.** Elenco delle modifiche nella scheda EUR-Lex (voce «Modified by»):
   https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=CELEX:32024R1689
   Al 2 ottobre 2026 l'unica modifica è il Reg. (UE) 2026/1744 (voce 8).
2. **Riforma di GDPR e regole sui cookie («Omnibus digitale», proposta COM(2025) 837).** Al 2 ottobre
   2026 è solo una proposta: la scheda EUR-Lex del GDPR la elenca come «Amendment proposed by»,
   non come modifica, e il Parlamento europeo la segna «Tabled» (aggiornamento del 1° agosto 2026).
   Il voto del Consiglio sul mandato, previsto per il 26 giugno 2026, è stato annullato.
   Fonte: https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-digital-package
   Finché non è pubblicata in Gazzetta UE, per i cookie valgono l'art. 122 del Codice privacy e le
   linee guida del Garante.
3. **P.IVA in home page.** Dal 1° gennaio 2027 si cita l'art. 68 del testo unico IVA al posto
   dell'art. 35 del DPR 633/1972 (voce 7). Controlla che la data non sia stata spostata.
4. **Trasferimenti negli Stati Uniti.** Stato della decisione 2023/1795 (voce 10).
5. **Garante privacy.** Nuove linee guida o provvedimenti su cookie, pixel, AI:
   https://www.garanteprivacy.it
6. **Fonti tecniche** (voce 12): nuova versione di vanilla-cookieconsent, regole di consenso di
   Microsoft Clarity, Google e Meta.

## Tabella riassuntiva

| # | Riferimento | Stato |
|---|---|---|
| 1 | GDPR, Reg. (UE) 2016/679 | Verificato |
| 2 | Codice privacy, D.lgs. 196/2003 come modificato dal D.lgs. 101/2018 | Verificato |
| 3 | Linee guida cookie del Garante, 10 giugno 2021 | Verificato |
| 4 | Codice del consumo, D.lgs. 206/2005 | Verificato |
| 5 | Codice civile, artt. 1229, 1341, 1342, 1454, 2220, 2250, 2946 | Verificato |
| 6 | Ritardi di pagamento tra imprese, D.lgs. 231/2002 | Verificato |
| 7 | Dati dell'azienda sul sito: art. 35 DPR 633/1972, testo unico IVA, art. 7 D.lgs. 70/2003 | Verificato; applicazione dell'art. 7 a una landing vetrina da verificare |
| 8 | AI Act, Reg. (UE) 2024/1689 e Omnibus sull'IA, Reg. (UE) 2026/1744 | Verificato; ruolo per i chatbot dei clienti da verificare |
| 9 | Legge italiana sull'IA, L. 132/2025 | Testo verificato; applicazione dell'art. 13 a uno studio digitale da verificare |
| 10 | Trasferimenti verso gli USA, decisione (UE) 2023/1795 | Verificato; da ricontrollare |
| 11 | Contitolarità con i plug-in social, CGUE C-40/17 | Verificato; estensione ai pixel da verificare |
| 12 | Fonti tecniche: vanilla-cookieconsent, Microsoft Clarity, Google Analytics, Meta | Verificato sulla documentazione dei fornitori |

---

## 1. GDPR, Regolamento (UE) 2016/679

- **Fonte:** EUR-Lex, testo italiano:
  https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32016R0679
  Scheda con le modifiche: https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=CELEX:32016R0679
- **Verificato il:** 2 ottobre 2026.
- **Stato:** in vigore. Solo rettifiche. Due proposte di modifica non approvate: COM(2025) 501 e
  COM(2025) 837.

Articoli che usiamo:

- **Art. 4, n. 11.** Il consenso è una manifestazione di volontà «libera, specifica, informata e
  inequivocabile», data con dichiarazione o «azione positiva inequivocabile».
- **Art. 6, par. 1.** Le basi giuridiche: a) consenso; b) contratto o misure precontrattuali chieste
  dall'interessato; c) obbligo di legge; d) interessi vitali; e) interesse pubblico; f) legittimo
  interesse, se non prevalgono i diritti dell'interessato.
- **Art. 7.** Par. 2: se il consenso sta in un testo che parla anche d'altro, la richiesta va
  presentata «in modo chiaramente distinguibile». Par. 3: si revoca in ogni momento, «con la stessa
  facilità con cui è accordato». Par. 4: non si condiziona un contratto a un consenso che al
  contratto non serve.
- **Art. 12.** Par. 1: informazioni «in forma concisa, trasparente, intelligibile e facilmente
  accessibile, con un linguaggio semplice e chiaro». Par. 3: risposta alle richieste sui diritti
  senza ritardo e al più tardi entro un mese, prorogabile di due mesi se serve, avvisando.
- **Art. 13.** Cosa dire quando i dati si raccolgono dall'interessato, nel momento in cui si
  ottengono.
  - Par. 1: a) identità e contatti del titolare; b) contatti del DPO, se c'è; c) finalità e base
    giuridica; d) il legittimo interesse, se è la base; e) destinatari o categorie di destinatari;
    f) trasferimenti verso Paesi terzi, con la decisione di adeguatezza o le garanzie e il modo per
    averne copia.
  - Par. 2: a) tempo di conservazione o criteri; b) diritti di accesso, rettifica, cancellazione,
    limitazione, opposizione, portabilità; c) revoca del consenso; d) reclamo all'autorità di
    controllo; e) se dare i dati è obbligatorio e cosa succede se non si danno; f) decisioni
    automatizzate e profilazione dell'art. 22.
  - Par. 3: se i dati servono a una finalità nuova, si informa prima.
- **Art. 21, par. 2-4.** Opposizione al marketing diretto in ogni momento. Il diritto va presentato
  «chiaramente e separatamente da qualsiasi altra informazione», al più tardi alla prima
  comunicazione.
- **Art. 22, par. 1.** Diritto di non essere sottoposti a decisioni basate unicamente su un
  trattamento automatizzato che producono effetti giuridici o incidono in modo analogo
  significativamente.
- **Art. 26.** Contitolari: accordo interno; il contenuto essenziale va messo a disposizione
  dell'interessato.
- **Art. 28, par. 1-3.** Responsabili del trattamento: garanzie sufficienti, contratto scritto,
  sub-responsabili solo con autorizzazione.
- **Art. 45, par. 1.** Trasferimenti verso Paesi con decisione di adeguatezza della Commissione.
- **Art. 77, par. 1.** Reclamo all'autorità di controllo dello Stato in cui l'interessato vive,
  lavora o dove è avvenuta la violazione.

## 2. Codice privacy, D.lgs. 196/2003 come modificato dal D.lgs. 101/2018

- **Fonti:** Normattiva:
  https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196 ;
  testo coordinato del Garante, versione 12.0 di aprile 2026 (doc. web 9042678):
  https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9042678
- **D.lgs. 101/2018:** GU n. 205 del 4 settembre 2018, in vigore dal 19 settembre 2018 (Normattiva).
- **Verificato il:** 2 ottobre 2026. Gli articoli sotto risultano invariati dal 19 settembre 2018.

Articoli che usiamo:

- **Art. 122, comma 1.** Archiviare informazioni nel dispositivo dell'utente, o leggerle, è
  consentito solo con il consenso, dato dopo un'informativa semplificata. Fanno eccezione
  l'archiviazione e l'accesso tecnici: quelli necessari a trasmettere la comunicazione o «nella
  misura strettamente necessaria» a erogare un servizio richiesto dall'utente. È la regola dei
  cookie. Il comma 2-bis vieta di usare la rete per accedere al dispositivo, archiviare informazioni
  o «monitorare le operazioni dell'utente» fuori da questi casi.
- **Art. 130, commi 1-2.** Comunicazioni commerciali con sistemi automatizzati, email, SMS e simili:
  serve il consenso.
- **Art. 130, comma 4.** Eccezione per i clienti: l'email data durante una vendita si può usare per
  offrire prodotti o servizi analoghi, senza consenso, se l'interessato è informato e non si
  oppone. Ad ogni invio va ricordata la possibilità di opporsi, in modo facile e gratuito.
- **Art. 130, comma 5.** Vietato celare l'identità del mittente o non dare un recapito per
  esercitare i diritti.
- **Art. 2-quinquies.** Il minore che ha compiuto 14 anni può dare il consenso per i servizi della
  società dell'informazione offerti direttamente a lui. Sotto i 14 anni serve chi ha la
  responsabilità genitoriale.
- **Autorità di controllo:** Garante per la protezione dei dati personali, Piazza Venezia 11, 00187
  Roma, https://www.garanteprivacy.it (dati letti sul sito il 2 ottobre 2026).

## 3. Linee guida cookie del Garante, 10 giugno 2021

- **Atto:** «Linee guida cookie e altri strumenti di tracciamento», provvedimento n. 231 del
  10 giugno 2021, doc. web 9677876, pubblicato nella GU n. 163 del 9 luglio 2021. Il Garante ha dato
  6 mesi dalla pubblicazione per adeguarsi.
- **Fonte:** https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9677876
- **Verificato il:** 2 ottobre 2026.

I punti che usiamo, con il paragrafo:

- **Par. 3.** Le regole valgono anche per gli altri strumenti di tracciamento, compreso il
  fingerprinting (strumenti «passivi»).
- **Par. 5.** Per i cookie non tecnici la sola base è il consenso. Il legittimo interesse del
  titolare non si può invocare.
- **Par. 6.1, scorrimento.** Il semplice scroll della pagina non è consenso. Può essere solo una
  parte di un processo più articolato, che produca una scelta registrabile.
- **Par. 6.1, cookie wall.** Il meccanismo «prendere o lasciare» è illecito, salvo il caso, da
  verificare volta per volta, in cui il sito offra un contenuto o servizio equivalente senza
  consenso.
- **Par. 6.2, nuova richiesta.** La scelta va registrata. Il banner non si ripropone, salvo tre casi:
  cambiano in modo significativo le condizioni del trattamento (per esempio le terze parti); il sito
  non può sapere la scelta (cookie cancellati); sono passati almeno 6 mesi.
- **Par. 7.1, primo accesso.** Al primo accesso nessun cookie o strumento diverso da quelli tecnici.
- **Par. 7.1, X e pulsanti.** Una X in alto a destra nel banner chiude e lascia solo i tecnici. La
  X deve avere «evidenza grafica pari» agli altri comandi. Comandi e caratteri «di uguali
  dimensioni, enfasi e colori». Proseguire senza consenso deve essere facile quanto consentire.
- **Par. 7.1, contenuto minimo del banner.** (i) avviso che la X lascia solo i cookie tecnici;
  (ii) informativa minima sui cookie usati e su quelli che si usano solo col consenso;
  (iii) link all'informativa estesa, raggiungibile con un clic anche da un link nel piè di pagina di
  ogni pagina; (iv) comando per accettare tutto; (v) link a un'area per scegliere in modo analitico
  funzioni, terze parti (elenco aggiornato) e cookie, anche per categorie.
- **Par. 7.1, scelte granulari.** Tutte preimpostate sul rifiuto.
- **Par. 7.1, cambiare idea.** Link nel piè di pagina con dicitura del tipo «rivedi le tue scelte
  sui cookie».
- **Par. 7.1, solo cookie tecnici.** Basta l'informazione nella home page o nell'informativa
  generale: niente banner.
- **Informativa a due livelli.** Il banner è l'informativa breve (primo livello). L'informativa
  estesa sta in un secondo livello (par. 7.1, punto iii). Il par. 8.1 ammette informative su più
  livelli e più canali.
- **Par. 7.2, analitici.** Si equiparano ai tecnici solo se riducono il potere identificativo (per
  esempio mascherando almeno la quarta parte dell'indirizzo IPv4), servono a statistiche aggregate
  su un solo sito, e il fornitore non li incrocia con altri dati né li cede a terzi.
- **Par. 8.2, criteri di classificazione.** Nell'informativa vanno dichiarati i criteri con cui il
  titolare classifica i cookie (tecnici, analitici, di profilazione).

## 4. Codice del consumo, D.lgs. 206/2005 (solo per i clienti consumatori)

- **Fonte:** Normattiva: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206
  GU n. 235 dell'8 ottobre 2005, S.O. n. 162.
- **Verificato il:** 2 ottobre 2026.
- **B2B o B2C.** Il codice protegge il **consumatore**: «la persona fisica che agisce per scopi
  estranei all'attività imprenditoriale, commerciale, artigianale o professionale eventualmente
  svolta» (art. 3, comma 1, lett. a). Il **professionista** è chi agisce nell'esercizio della propria
  attività (lett. c). Se il cliente compra per la sua azienda o professione, queste regole non si
  applicano: valgono codice civile (voce 5) e D.lgs. 231/2002 (voce 6).

Articoli che usiamo per la parte B2C dei termini:

- **Art. 33, commi 1-2.** Clausole vessatorie, presunte tali fino a prova contraria. Fra queste:
  lett. a), escludere o limitare la responsabilità del professionista per morte o danno alla
  persona; lett. b), escludere o limitare le azioni del consumatore se il professionista non adempie
  o adempie male; lett. t), deroghe alla competenza del giudice; lett. u), foro diverso dalla
  residenza o dal domicilio del consumatore.
- **Art. 36.** Le clausole vessatorie sono nulle; il contratto resta valido per il resto.
- **Art. 49, comma 1.** Informazioni da dare prima del contratto a distanza: caratteristiche,
  identità, indirizzo e contatti, prezzo totale con imposte, recesso con il modulo tipo
  dell'allegato I, parte B, e così via.
- **Art. 51, comma 8.** Se il consumatore vuole che il servizio inizi durante il periodo di recesso,
  deve chiederlo in modo esplicito e riconoscere che perderà il recesso a contratto eseguito.
- **Art. 52.** Recesso entro 14 giorni dai contratti a distanza o fuori dei locali commerciali, senza
  motivo; per i servizi i 14 giorni partono dalla conclusione del contratto.
- **Art. 54, comma 1.** Per recedere il consumatore usa il modulo tipo (allegato I, parte B) oppure
  una qualsiasi altra dichiarazione esplicita.
- **Art. 54-bis.** Per i contratti a distanza conclusi tramite un'interfaccia online serve una
  «funzione di recesso» con la scritta «recedere dal contratto qui» e la conferma «conferma recesso».
  Si applica dal 19 giugno 2026 ai contratti conclusi dopo quella data (D.lgs. 209/2025).
- **Art. 57, comma 3.** Se il consumatore recede dopo aver chiesto l'inizio del servizio, paga una
  quota proporzionale a quanto ricevuto.
- **Art. 59, comma 1, lett. a).** Niente recesso dopo la completa prestazione del servizio, se
  l'esecuzione è iniziata con il consenso espresso del consumatore e l'accettazione della perdita
  del recesso.
- **Art. 66-bis.** Per le controversie su questi contratti il giudice competente è quello del luogo
  di residenza o domicilio del consumatore, se in Italia. La regola non si deroga.

## 5. Codice civile

- **Fonte:** Normattiva, R.D. 16 marzo 1942, n. 262:
  https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2
- **Verificato il:** 2 ottobre 2026.

- **Art. 1229.** È nullo il patto che esclude o limita in anticipo la responsabilità per dolo o colpa
  grave, o per violazioni di norme di ordine pubblico.
- **Art. 1341.** Le condizioni generali scritte da una parte valgono se l'altra le conosceva o
  poteva conoscerle. Alcune clausole hanno effetto solo se «specificamente approvate per iscritto»:
  limitazioni di responsabilità, facoltà di recedere o di sospendere l'esecuzione, decadenze,
  limiti alle eccezioni, restrizioni nei rapporti con terzi, tacita proroga o rinnovazione, clausole
  compromissorie, deroghe alla competenza del giudice.
- **Art. 1342.** Nei contratti su moduli o formulari, le clausole aggiunte prevalgono su quelle del
  modulo. Si applica anche il secondo comma dell'art. 1341 (approvazione specifica per iscritto).
- **Art. 1454.** Diffida ad adempiere: il termine non può essere inferiore a quindici giorni, salvo
  diverso accordo o termine più breve congruo per natura del contratto o usi.
- **Art. 2220.** Scritture contabili, fatture e corrispondenza si conservano per dieci anni dalla data
  dell'ultima registrazione.
- **Art. 2250.** Negli atti e nella corrispondenza:
  - le società iscritte al registro delle imprese indicano sede, ufficio del registro e numero di
    iscrizione (comma 1);
  - S.p.A., S.a.p.a. e S.r.l. indicano il capitale effettivamente versato e risultante dall'ultimo
    bilancio (comma 2);
  - le società sciolte indicano che sono in liquidazione (comma 3);
  - S.p.A. e S.r.l. indicano se hanno un socio unico (comma 4).
  L'ultimo comma chiede alle società dei capi V, VI e VII del titolo V (S.p.A., S.a.p.a., S.r.l.)
  che hanno un sito di dare lì tutte queste informazioni.
- **Art. 2946.** La prescrizione ordinaria è di dieci anni.

## 6. Ritardi di pagamento tra imprese, D.lgs. 231/2002

- **Fonte:** Normattiva: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2002-10-09;231
- **Verificato il:** 2 ottobre 2026.

- **Art. 2.** «Transazioni commerciali» sono i contratti fra imprese (o fra imprese e pubbliche
  amministrazioni) per la consegna di merci o la prestazione di servizi contro un prezzo. Per
  «imprenditore» si intende anche chi esercita una libera professione (lett. c). Gli interessi legali
  di mora sono pari al tasso di riferimento della BCE più otto punti percentuali.
- **Art. 4.** Gli interessi di mora decorrono dal giorno dopo la scadenza, senza bisogno di
  costituzione in mora. Senza accordi diversi il termine è di trenta giorni, di regola dal
  ricevimento della fattura. Tra imprese si possono pattuire termini più lunghi; oltre sessanta
  giorni vanno pattuiti espressamente e provati per iscritto.
- **Art. 5.** Il saggio è quello degli interessi legali di mora; tra imprese si può concordare un
  tasso diverso, nei limiti dell'art. 7.
- **Art. 6.** Spetta un importo forfettario di 40 euro per i costi di recupero, salvo maggior danno.

## 7. Dati dell'azienda sul sito

- **P.IVA nella home page, fino al 31 dicembre 2026.** Art. 35, comma 1, DPR 26 ottobre 1972, n. 633:
  il numero di partita IVA «deve essere indicato nelle dichiarazioni, nella home-page dell'eventuale
  sito web e in ogni altro documento ove richiesto». Testo in vigore dal 22 febbraio 2024 al
  31 dicembre 2026.
  Fonte: https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1972-10-26;633~art35!vig=2026-10-02
- **Dal 1° gennaio 2027.** L'art. 35 è abrogato dal D.lgs. 19 gennaio 2026, n. 10, che approva il
  testo unico IVA (GU n. 24 del 30 gennaio 2026, S.O. n. 4/L). L'art. 68, comma 1, del testo unico
  ripete lo stesso obbligo. L'art. 171 dice che il testo unico si applica dal 1° gennaio 2027.
  Fonti: Normattiva, allegato art. 68
  (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art68)
  e art. 171 (stesso indirizzo con `~art171`); Gazzetta Ufficiale:
  https://www.gazzettaufficiale.it/eli/id/2026/01/30/26G00022/sg
- **Art. 7 D.lgs. 9 aprile 2003, n. 70.** Il prestatore rende accessibili «in modo diretto e
  permanente»: a) nome, denominazione o ragione sociale; b) domicilio o sede legale; c) contatti
  rapidi, compresa l'email; d) numero REA o del registro delle imprese; e) autorità di vigilanza, se
  l'attività è autorizzata; f) per le professioni regolamentate: ordine, numero di iscrizione,
  titolo, norme professionali; g) partita IVA; h) prezzi chiari, con imposte e costi aggiuntivi;
  i) attività consentite al consumatore ed estremi del contratto, se l'attività è autorizzata o
  data in licenza. Le informazioni vanno tenute aggiornate (comma 2). Testo in vigore dal
  14 maggio 2003.
  Fonte: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-04-09;70~art7
- **Da verificare.** L'art. 7 si applica al «prestatore» di servizi della società
  dell'informazione, cioè di «attività economiche svolte in linea» (art. 2, lett. a e b). Se basti
  una landing che presenta servizi resi fuori dal web, non l'ho trovato in una fonte primaria. Nel
  dubbio i dati si mettono comunque nel piè di pagina: non costano nulla.
- **Verificato il:** 2 ottobre 2026.

## 8. AI Act, Regolamento (UE) 2024/1689

- **Fonti:** EUR-Lex, testo italiano:
  https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32024R1689 ;
  Reg. (UE) 2026/1744 dell'8 luglio 2026, «Omnibus digitale sull'IA», GU L del 24 luglio 2026:
  https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32026R1744
  Secondo EUR-Lex le modifiche valgono dal 27 luglio 2026.
- **Verificato il:** 2 ottobre 2026.

Cosa ci serve:

- **Definizioni (art. 3).** «Sistema di IA» (n. 1); «fornitore» è chi sviluppa o fa sviluppare un
  sistema e lo mette in servizio con il proprio nome o marchio (n. 3); «deployer» è chi usa un
  sistema di IA sotto la propria autorità, fuori dall'uso personale (n. 4); «deep fake» è un
  contenuto generato o manipolato che somiglia a persone, oggetti, luoghi o eventi esistenti e
  sembrerebbe falsamente autentico (n. 60).
- **Art. 4, come sostituito dal Reg. 2026/1744.** Fornitori e deployer adottano misure per sostenere
  l'alfabetizzazione sull'IA del personale. La norma precisa che non impone di garantire un livello
  specifico.
- **Art. 50, par. 1.** I fornitori fanno sì che le persone sappiano di interagire con un sistema di
  IA, salvo che sia evidente.
- **Art. 50, par. 2.** I fornitori di sistemi che generano contenuti sintetici li marcano in un
  formato leggibile da una macchina.
- **Art. 50, par. 3.** Chi usa sistemi di riconoscimento delle emozioni o di categorizzazione
  biometrica informa le persone esposte.
- **Art. 50, par. 4.** Chi usa un sistema che genera o manipola un deep fake rende noto che il
  contenuto è artificiale (per opere manifestamente artistiche, satiriche o di finzione basta
  rivelarlo in modo adeguato). Il testo pubblicato per informare il pubblico su questioni di
  interesse pubblico va dichiarato come generato, salvo revisione umana o controllo editoriale con
  una persona che ne ha la responsabilità.
- **Art. 50, par. 5.** Le informazioni si danno in modo chiaro e distinguibile, al più tardi alla
  prima interazione o esposizione.
- **Date.** Art. 113: il regolamento si applica dal 2 agosto 2026. L'art. 50 è nel capo IV e non ha
  date speciali: si applica già. I capi I e II (comprese le pratiche vietate e l'art. 4) dal
  2 febbraio 2025; i nuovi divieti aggiunti dal Reg. 2026/1744 dal 2 dicembre 2026. Sistemi ad alto
  rischio: dal 2 dicembre 2027 (allegato III) e dal 2 agosto 2028 (allegato I). Nuovo art. 111,
  par. 4: i fornitori di sistemi generativi immessi sul mercato prima del 2 agosto 2026 si adeguano
  all'art. 50, par. 2, entro il 2 dicembre 2026.
- **Da verificare.** Se lo studio costruisce un chatbot e lo mette sul sito di un cliente, chi è
  «fornitore» e chi «deployer» dipende da chi lo mette in servizio con il proprio nome. L'obbligo
  di avvisare esiste comunque; cambia solo chi ne risponde.

## 9. Legge italiana sull'intelligenza artificiale, L. 23 settembre 2025, n. 132

- **Atto:** «Disposizioni e deleghe al Governo in materia di intelligenza artificiale», GU n. 223 del
  25 settembre 2025, in vigore dal 10 ottobre 2025. Normattiva segnala un aggiornamento dell'atto
  pubblicato il 26 giugno 2026; gli articoli sotto risultano invariati dal 10 ottobre 2025.
- **Fonte:** https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-09-23;132
- **Verificato il:** 2 ottobre 2026.

- **Art. 13, comma 1.** «L'utilizzo di sistemi di intelligenza artificiale nelle professioni
  intellettuali è finalizzato al solo esercizio delle attività strumentali e di supporto
  all'attività professionale e con prevalenza del lavoro intellettuale oggetto della prestazione
  d'opera.»
- **Art. 13, comma 2.** «Per assicurare il rapporto fiduciario tra professionista e cliente, le
  informazioni relative ai sistemi di intelligenza artificiale utilizzati dal professionista sono
  comunicate al soggetto destinatario della prestazione intellettuale con linguaggio chiaro,
  semplice ed esaustivo.»
- **Art. 4, commi 3-4.** Le informazioni sui trattamenti di dati legati all'IA si danno in modo
  chiaro e semplice. I minori di 14 anni accedono alle tecnologie di IA solo con il consenso di chi
  ha la responsabilità genitoriale.
- **Art. 25.** Modifica l'art. 1 della legge sul diritto d'autore (L. 633/1941): sono protette le
  «opere dell'ingegno umano», anche create con l'ausilio dell'IA, «purché costituenti risultato del
  lavoro intellettuale dell'autore».
- **Da verificare.** L'art. 13 parla di «professioni intellettuali» e di «professionista». Se si
  applichi a uno studio digitale organizzato come impresa, non l'ho trovato in una fonte primaria.
  Nell'art. 13 non ho trovato sanzioni specifiche. Scelta prudente: dare comunque l'informativa
  (modello `modelli/informativa-ai.md`) e chiedere conferma al professionista.

## 10. Trasferimenti verso gli Stati Uniti

- **Atto:** Decisione di esecuzione (UE) 2023/1795 della Commissione del 10 luglio 2023, sul quadro
  UE-USA per la protezione dei dati personali (Data Privacy Framework), GU L 231 del 20 settembre
  2023.
- **Fonte:** https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=CELEX:32023D1795
- **Verificato il:** 2 ottobre 2026.
- **Stato:** in vigore. EUR-Lex la segna confermata dal Tribunale UE (causa T-553/23) e riporta un
  rinvio pregiudiziale che la riguarda (causa C-804/25). Ricontrolla a ogni consegna.
- **Art. 1.** L'adeguatezza vale per i dati trasferiti alle organizzazioni statunitensi «che figurano
  nell'elenco degli aderenti al quadro per la protezione dei dati personali», tenuto dal Dipartimento
  del Commercio degli Stati Uniti.
- **Uso pratico.** Controlla che il fornitore sia nell'elenco ufficiale:
  https://www.dataprivacyframework.gov/list (pagina «Data Privacy Framework List», controllata il
  2 ottobre 2026). Se non c'è, servono altre garanzie, per esempio clausole contrattuali tipo
  (GDPR art. 46).

## 11. Contitolarità con i plug-in social, CGUE C-40/17 Fashion ID

- **Atto:** sentenza della Corte di giustizia (Seconda Sezione) del 29 luglio 2019, causa C-40/17.
- **Fonte:** https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:62017CJ0040
- **Verificato il:** 2 ottobre 2026.
- **Cosa dice.** Il gestore di un sito che inserisce un plug-in social, che fa trasmettere dati del
  visitatore al fornitore del plug-in, può essere responsabile del trattamento insieme al
  fornitore. La responsabilità è limitata alla raccolta e alla trasmissione dei dati.
- **Da verificare.** La sentenza riguarda un pulsante «Mi piace» e la vecchia direttiva 95/46.
  Applicarla ai pixel pubblicitari è un'interpretazione diffusa, ma va confermata dal professionista
  insieme ai termini del fornitore del pixel.

## 12. Fonti tecniche (non sono norme)

Controllate il 2 ottobre 2026 sulla documentazione dei fornitori.

- **vanilla-cookieconsent 3.1.0** (ultima versione su npm e GitHub, 4 febbraio 2025).
  - Script bloccati con `type="text/plain"` e `data-category="..."`; `data-service` crea un
    interruttore per servizio: https://cookieconsent.orestbida.com/advanced/manage-scripts.html
  - Link per riaprire le preferenze: `data-cc="show-preferencesModal"`:
    https://cookieconsent.orestbida.com/essential/getting-started.html
  - `closeIconLabel` crea una X che agisce come «accetta solo i necessari», visibile solo con il
    layout `box`; `equalWeightButtons` vale `true` di base; `cookie.expiresAfterDays` vale 182 di
    base; `mode` vale `opt-in` di base; `revision` richiede di nuovo il consenso;
    `{{revisionMessage}}` nella descrizione mostra il messaggio di revisione:
    https://cookieconsent.orestbida.com/reference/configuration-reference.html e
    https://cookieconsent.orestbida.com/advanced/revision-management.html
  - Dal codice della versione 3.1.0: `serviceCounterLabel` accetta «singolare|plurale»; con
    `hideFromBots` attivo (predefinito) il banner non compare se `navigator.webdriver` è vero, cioè
    nei browser automatici: `scripts/consenso.mjs` lo disattiva.
- **Microsoft Clarity.** Dal 31 ottobre 2025 Clarity applica i requisiti sul segnale di consenso per
  le visite da SEE, Regno Unito e Svizzera. Il segnale si passa con
  `clarity('consentv2', {ad_Storage, analytics_Storage})`. Senza consenso Clarity lavora in modalità
  senza cookie, con un identificativo per ogni pagina vista. Cookie: `_clck`, `_clsk` (prima parte),
  `CLID`, `ANONCHK`, `MR`, `MUID`, `SM` (terze parti).
  Fonti: https://learn.microsoft.com/en-us/clarity/setup-and-installation/cookie-consent ,
  https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-consent-api-v2 ,
  https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-cookies
  **Da verificare:** usare la modalità senza cookie senza chiedere il consenso. Il Garante include
  anche gli strumenti passivi (voce 3, par. 3): nel dubbio si blocca Clarity fino al consenso.
- **Google Analytics 4.** Cookie `_ga` e `_ga_<container-id>`, durata 2 anni:
  https://developers.google.com/analytics/devguides/collection/ga4/cookie-usage
- **Meta Pixel.** Cookie `_fbp` e `_fbc`:
  https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/fbp-and-fbc/

## Cosa non è in questo file

Se ti serve una norma che qui non c'è (commercio elettronico con pagamento sul sito, accessibilità,
servizi digitali con contenuti degli utenti, minori come pubblico principale), fermati: verifica su
una fonte primaria e aggiungi la voce qui, con fonte e data, prima di usarla.
