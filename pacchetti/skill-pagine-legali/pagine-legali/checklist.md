# Lista di controllo

> **Avviso.** Questa lista aiuta a trovare errori, non certifica che un sito sia in regola e non è
> consulenza legale. Prima di pubblicare le pagine è consigliata la revisione di un professionista.

Per ogni punto scrivi **OK**, **KO** o **NON SI APPLICA**, con la prova: comando e risultato, URL,
schermata. Salva l'esito in `$W/checklist-esito.md`. Un KO non si chiude a parole: si corregge e si
rifà il controllo.

Prima di iniziare:

```bash
S=~/.claude/skills/pagine-legali
W=<tuo-progetto>/pagine-legali-<dominio>-<AAAA-MM-GG>
U=https://<dominio>/              # home page
P=https://<dominio>/<altra-pagina> # una pagina interna, meglio se con un modulo
D=<dominio>
mkdir -p $W
```

Controlli nel browser: `node $S/scripts/consenso.mjs` (Playwright, Chromium). Controlli sul codice:
`python3 $S/scripts/scan.py`. Il browser dice cosa succede davvero; la scansione dice dove cercare.

## A. Dati dell'azienda sul sito

**A1. P.IVA nella home page.**
```bash
node $S/scripts/consenso.mjs $U --salva-html $W/html --attesa 3000 > /dev/null
python3 $S/scripts/scan.py $W/html --domain $D | grep -A3 "P.IVA"
```
OK se la home page non compare tra le «Pagine senza P.IVA visibile» e il numero trovato è quello
giusto. Rif.: art. 35 DPR 633/1972 fino al 31/12/2026, art. 68 testo unico IVA dal 1/1/2027
(`riferimenti.md`, voce 7).

**A2. Dati dell'art. 7 del D.lgs. 70/2003**, raggiungibili in modo diretto e permanente (di solito
nel piè di pagina): ragione sociale, sede, email, numero REA o registro imprese, P.IVA; per le
professioni regolamentate anche ordine, numero e titolo. Controllo a vista sull'HTML salvato:
```bash
grep -o -i -E "\brea\b[^<]{0,40}|registro (delle )?imprese[^<]{0,40}|capitale[^<]{0,40}" $W/html/*.html | head
```
Rif.: `riferimenti.md`, voce 7 (applicazione a una landing vetrina da verificare).

**A3. Solo S.p.A., S.a.p.a., S.r.l.:** sede, ufficio del registro e numero di iscrizione, capitale
versato, socio unico se c'è (art. 2250 c.c.). Stesso comando di A2.

**A4. Stessi dati ovunque.** Ragione sociale, email e P.IVA uguali in tutte le pagine scritte:
```bash
grep -h -o -E "P\.IVA [0-9]{11}|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}" $W/*.md | sort | uniq -c
```

## B. Link e raggiungibilità

**B1. Link a privacy e cookie policy in ogni pagina.**
```bash
for u in $U $P; do node $S/scripts/consenso.mjs $u --salva-html $W/html --attesa 3000 > /dev/null; done
python3 $S/scripts/scan.py $W/html --domain $D | sed -n '/Controlli italiani/,/^$/p'
```
OK se «Pagine senza link alla privacy policy» e «... alla cookie policy» sono 0. Controlla anche la
pagina di ringraziamento e le pagine dei moduli. Rif.: linee guida del Garante, par. 7.1, punto iii.

**B2. Link «Preferenze cookie» che riapre le scelte**, in ogni pagina.
```bash
node $S/scripts/consenso.mjs $U --rifiuta --pagina $P > $W/consenso-rifiuto.txt
grep 'Link "Preferenze cookie"' $W/consenso-rifiuto.txt
```
OK se dice «apre ...». Rif.: linee guida del Garante, par. 7.1.

**B3. Ogni modulo ha il link all'informativa vicino al pulsante di invio.** Scansione: «Moduli
senza link all'informativa privacy» = 0. I moduli dentro un iframe (CRM, prenotazioni) non si
vedono: apri l'indirizzo dell'iframe con `consenso.mjs` e controlla a vista. Rif.: GDPR art. 13, par. 1
(l'informativa si dà quando i dati si raccolgono).

## C. Moduli e consensi

**C1. Nessuna casella già spuntata.** Scansione: «caselle o radio già selezionati: 0». Per i moduli
in iframe, controllo a vista. Rif.: GDPR art. 4, n. 11 (serve un'azione positiva).

**C2. Il consenso al marketing è separato e facoltativo.** Scansione: «Moduli con una casella che
unisce privacy e marketing» = 0. La casella del marketing non deve essere obbligatoria:
```bash
grep -o -i -E '<input[^>]*type="?checkbox"?[^>]*>' $W/html/*.html | grep -i required
```
OK se la casella del marketing non compare (o se `required` riguarda un'altra casella). Rif.: GDPR
art. 7, par. 2 e 4; Codice privacy art. 130, commi 1-2.

**C3. Niente «consenso al trattamento» obbligatorio quando la base non è il consenso.** Per
rispondere a una richiesta la base è la richiesta stessa (GDPR art. 6, par. 1, lett. b): basta il
link all'informativa, al massimo una casella «Ho letto l'informativa». Se il modulo chiede un
consenso obbligatorio per inviare, segnalalo in `da-verificare.md`.

**C4. Email di marketing.** In un'email di prova: mittente riconoscibile, link per disiscriversi,
avviso che ci si può opporre. Rif.: Codice privacy art. 130, commi 4-5; GDPR art. 21, par. 4.

## D. Cookie e tracciamento nel browser

**D1. Prima di qualsiasi scelta niente tracciamento**, anche scorrendo la pagina e su una seconda
pagina.
```bash
node $S/scripts/consenso.mjs $U --pagina $P > $W/consenso-prima.txt
sed -n '/^1)/,/^$/p;/Esito/,$p' $W/consenso-prima.txt
```
OK se nella fase 1 non ci sono cookie o richieste di «tracciamento» e nessuna riga «ATTENZIONE -
Prima della scelta». Gli host «terza parte» vanno comunque spiegati (D8-D10). Rif.: Codice privacy
art. 122; linee guida del Garante, par. 6.1 e 7.1.

**D2. Nel codice gli script non tecnici sono bloccati** con `type="text/plain"` e `data-category`.
Scansione, sezione «Strumenti riconosciuti»: nessuno strumento di tracciamento «attivo al
caricamento» e nessun host «dentro <noscript>».

**D3. Dopo «Rifiuta» e dopo la X non parte nulla**, anche ricaricando e cambiando pagina, e il
banner non torna.
```bash
node $S/scripts/consenso.mjs $U --rifiuta --pagina $P > $W/consenso-rifiuto.txt
node $S/scripts/consenso.mjs $U --rifiuta '#cc-main .cm__btn--close' --pagina $P > $W/consenso-x.txt
grep "ATTENZIONE" $W/consenso-rifiuto.txt $W/consenso-x.txt
```
OK se non esce nulla. Con un banner diverso da vanilla-cookieconsent passa il selettore, per esempio
`--rifiuta 'testo:Rifiuta tutti'`. Rif.: linee guida del Garante, par. 6.2 e 7.1.

**D4. Dopo «Accetta» i cookie sono quelli della cookie policy.**
```bash
node $S/scripts/consenso.mjs $U --accetta --pagina $P > $W/consenso-accetta.txt
sed -n '/^3)/,/^$/p' $W/consenso-accetta.txt
```
OK se ogni cookie e ogni host della fase 3 è nella tabella della cookie policy, e viceversa.

**D5. Il banner si vede bene ed è equo**, su computer e su telefono.
```bash
node $S/scripts/consenso.mjs $U --foto $W/banner-desktop.png --attesa 3000 | head -3
node $S/scripts/consenso.mjs $U --mobile --foto $W/banner-mobile.png --attesa 3000 | head -3
```
Guarda le due immagini. OK se: c'è la X in alto a destra; «Rifiuta» (o la X) ha la stessa evidenza
di «Accetta» (lo script stampa le misure dei pulsanti); la pagina sotto resta usabile (niente cookie
wall); il testo dice che la X lascia solo i cookie tecnici; ci sono i link alle informative; su
telefono il banner non copre i pulsanti. Rif.: linee guida del Garante, par. 6.1 e 7.1.

**D6. Le scelte per categoria partono spente.** Nella riga «Link "Preferenze cookie"» di D3 tutti
gli interruttori, tranne quelli tecnici, devono essere «spento».

**D7. La scelta dura almeno 6 mesi e si richiede se cambiano le terze parti.** In D3 il cookie della
scelta (`cc_cookie`) dura 182 giorni. Nel file di configurazione `revision` è stato aumentato
dall'ultima modifica delle terze parti. Rif.: linee guida del Garante, par. 6.2.

**D8. Font.** Nessuna richiesta a host di font esterni in D1, oppure font ospitati sul sito. Se
restano esterni, il fornitore va tra i destinatari dell'informativa privacy.

**D9. Contenuti incorporati** (video, calendari, mappe, moduli di terzi): in D1 non partono, oppure
c'è un'anteprima che li carica al clic. Un modulo di terzi che si carica subito va in
`da-verificare.md`, con la domanda per il professionista.

**D10. Banner ospitato sul sito.** In D1 nessun host «CDN pubblico».

## E. Contenuto delle pagine

**E1. L'informativa privacy ha tutti i punti dell'art. 13 GDPR.** Spunta: identità e contatti del
titolare; DPO se c'è; finalità e base giuridica per ogni attività; legittimo interesse spiegato,
dove è la base; destinatari; trasferimenti fuori dal SEE con le garanzie e il modo per averne
copia; tempi di conservazione; diritti; revoca del consenso; reclamo al Garante; obbligo o no di
dare i dati e conseguenze; decisioni automatizzate. Il diritto di opporsi al marketing è scritto a
parte, in evidenza (art. 21, par. 4).

**E2. La cookie policy** dichiara i criteri di classificazione (linee guida del Garante, par. 8.2),
ha la tabella dei cookie veri (D4), spiega come cambiare idea e dove sta il link «Preferenze
cookie».

**E3. Le condizioni di servizio**
- dicono se valgono per aziende, consumatori o entrambi;
- elencano per l'approvazione scritta le clausole dell'art. 1341 c.c. che contengono;
- non escludono la responsabilità per dolo o colpa grave (art. 1229 c.c.);
- fissano pagamenti oltre 60 giorni solo se pattuiti espressamente e per iscritto (D.lgs. 231/2002,
  art. 4);
- con consumatori: recesso di 14 giorni, modulo tipo, funzione di recesso online se il contratto
  si chiude sul sito, foro del consumatore (Codice del consumo, artt. 52, 54, 54-bis, 66-bis).

**E4. L'informativa sull'AI** c'è se lo studio usa l'AI nel lavoro per i clienti o se il sito ha una
chat con AI. Se c'è la chat, il primo messaggio dice che si parla con un'AI (AI Act, art. 50, par. 1
e 5).

**E5. Date e coerenza.** «Ultimo aggiornamento» presente in ogni pagina; stessi dati in tutte (A4).

**E6. Niente segnaposto né etichette rimaste.**
```bash
grep -n "{{" $W/*.md | grep -v "revisionMessage"
grep -n -E "\[SOLO SE|\[SCEGLI|\[TIENI SOLO|\[ALTRIMENTI|NOTA PER CHI COMPILA|Prima di usare questo modello" $W/*.md
```
OK se ogni riga rimasta corrisponde a un punto di `da-verificare.md`, e nei testi da pubblicare non
resta nessuna nota.

## F. Consegna

**F1.** `da-verificare.md` esiste e contiene almeno: la revisione complessiva di un professionista,
i fatti mancanti, i punti «da verificare» di `riferimenti.md` che riguardano questo sito.

**F2.** Il lavoro è passato da un secondo revisore (un'altra sessione o una persona).

**F3.** Niente è stato pubblicato e niente è stato mandato al cliente senza l'ok di chi ha chiesto il lavoro.
