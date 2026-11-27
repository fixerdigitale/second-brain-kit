> **Prima di usare questo modello (nota per chi compila, non si pubblica)**
> - Questi testi non sono consulenza legale. Prima di metterli online è consigliata la revisione di
>   un professionista.
> - I testi sono per vanilla-cookieconsent 3.1.0. La configurazione della sezione 5 è stata provata
>   con quella versione il 2 ottobre 2026, su schermo da computer e da telefono.
> - Il banner serve solo se ci sono cookie o strumenti non tecnici. Con soli cookie tecnici basta
>   l'informativa (linee guida del Garante, par. 7.1).
> - Le categorie del banner devono essere quelle vere, uscite dal passo 3 della skill. Togli la
>   categoria che non usi, e togli dai testi le frasi che la nominano.
> - `{{revisionMessage}}` è un segnaposto della libreria: resta così com'è. Gli altri `{{...}}` si
>   sostituiscono.
> - Riferimenti: linee guida del Garante del 10 giugno 2021 e documentazione della libreria
>   (`riferimenti.md`, voci 3 e 12).

# Testi del banner cookie

## 1. Cosa deve fare il banner e come si ottiene

| Regola (linee guida del Garante) | Come si ottiene con vanilla-cookieconsent |
|---|---|
| Nessun cookie non tecnico prima della scelta (par. 7.1) | `mode: "opt-in"` e tutti gli script non tecnici con `type="text/plain"` e `data-category` (sezione 6) |
| X in alto a destra che chiude e lascia solo i tecnici (par. 7.1) | `closeIconLabel` nel primo livello e layout `box`: con gli altri layout la X non compare |
| X e «Rifiuta» con lo stesso peso di «Accetta» (par. 7.1) | `equalWeightButtons: true` e `acceptNecessaryBtn` accanto ad `acceptAllBtn` |
| Niente cookie wall (par. 6.1) | `disablePageInteraction: false` (è il valore predefinito): la pagina resta usabile |
| Lo scorrimento non vale come consenso (par. 6.1) | La libreria registra il consenso solo con un clic sui pulsanti |
| Scelte per categoria, tutte spente all'inizio (par. 7.1) | Categorie senza `enabled: true`, tranne `necessary` |
| Scelta ricordata, nuova richiesta dopo almeno 6 mesi (par. 6.2) | `cookie.expiresAfterDays: 182` |
| Nuova richiesta se cambiano le terze parti (par. 6.2) | Aumenta `revision` di 1 e scrivi `revisionMessage` |
| Link nel piè di pagina per cambiare idea (par. 7.1) | Pulsante con `data-cc="show-preferencesModal"` (sezione 4) |
| Informativa breve nel banner, estesa con un clic (par. 7.1, punto iii) | Link a privacy e cookie policy nel `footer` del primo livello |

## 2. Primo livello: il banner

| Campo | Testo |
|---|---|
| `title` | Questo sito usa i cookie |
| `description` | Usiamo cookie tecnici, necessari per far funzionare il sito. Solo con il tuo consenso usiamo anche cookie analitici, per misurare le visite, e cookie di marketing, per misurare le campagne e mostrarti pubblicità in linea con i tuoi interessi. Se chiudi con la X o premi «Rifiuta», continui a navigare solo con i cookie tecnici. Puoi cambiare idea quando vuoi dal link «Preferenze cookie» in fondo a ogni pagina. {{revisionMessage}} |
| `revisionMessage` | Abbiamo cambiato i servizi che usano i cookie: rivedi la tua scelta. |
| `closeIconLabel` | Chiudi senza accettare |
| `acceptAllBtn` | Accetta tutti |
| `acceptNecessaryBtn` | Rifiuta |
| `showPreferencesBtn` | Scegli quali cookie |
| `footer` | Link a «Privacy policy» e «Cookie policy» |

Varianti della frase centrale di `description`:

- **Solo analitici:** «Solo con il tuo consenso usiamo anche cookie analitici, per capire come viene
  usato il sito.»
- **Solo marketing:** «Solo con il tuo consenso usiamo anche cookie di marketing, per misurare le
  campagne e mostrarti pubblicità in linea con i tuoi interessi.»
- **Con contenuti esterni** (video, calendari, mappe), da aggiungere: «Anche {{tipo_contenuti_esterni}}
  di altri siti si caricano solo con il tuo consenso.»

## 3. Secondo livello: le preferenze

| Campo | Testo |
|---|---|
| `title` | Preferenze cookie |
| `acceptAllBtn` | Accetta tutti |
| `acceptNecessaryBtn` | Rifiuta tutti |
| `savePreferencesBtn` | Salva le mie scelte |
| `closeIconLabel` | Chiudi |
| `serviceCounterLabel` | servizio\|servizi |

Sezioni, nell'ordine:

1. **Come usiamo i cookie.** «Qui scegli quali cookie attivare. Le categorie facoltative partono
   spente: si accendono solo se lo decidi tu. Puoi cambiare idea in ogni momento.»
2. **Cookie tecnici (sempre attivi)** — categoria `necessary`. «Servono a far funzionare il sito e a
   ricordare la tua scelta sui cookie. Non serve il consenso.»
3. **Cookie analitici** — categoria `analytics`. «Ci dicono come viene usato il sito: quante visite,
   da quali pagine, per quanto tempo. Li attiviamo solo con il tuo consenso.»
   [SOLO SE UNO STRUMENTO REGISTRA CLIC E MOVIMENTI] Aggiungi: «{{nome_servizio}} registra anche
   clic, scorrimento e movimenti sulla pagina, per mappe di calore e registrazioni delle visite.»
4. **Cookie di marketing** — categoria `marketing`. «Servono a misurare le campagne pubblicitarie e a
   mostrarti annunci in linea con i tuoi interessi, anche su altri siti. Li attiviamo solo con il tuo
   consenso.»
5. **Altre informazioni.** «Per domande sui cookie e sui tuoi dati leggi la privacy policy o scrivi a
   {{email_privacy}}.»

Ogni categoria ha una tabella con i cookie veri (nome, fornitore, a cosa serve, durata): gli stessi
della cookie policy.

## 4. Link nel piè di pagina di ogni pagina

```html
<a href="{{url_privacy}}">Privacy policy</a> ·
<a href="{{url_cookie_policy}}">Cookie policy</a> ·
<button type="button" data-cc="show-preferencesModal">Preferenze cookie</button>
```

## 5. Configurazione completa

Ospita sul sito i due file della libreria (`cookieconsent.umd.js` e `cookieconsent.css`, versione
3.1.0) invece di caricarli da un CDN: anche un CDN riceve l'indirizzo IP del visitatore.

Nella pagina:

```html
<link rel="stylesheet" href="/{{cartella}}/cookieconsent.css">
<!-- ... in fondo al body: -->
<script type="module" src="/{{cartella}}/cookieconsent-config.js"></script>
```

File `cookieconsent-config.js`:

```js
import "./cookieconsent.umd.js";

CookieConsent.run({
  mode: "opt-in",
  revision: 1, // +1 quando cambiano le terze parti: il banner si ripresenta a tutti
  cookie: { name: "cc_cookie", expiresAfterDays: 182 }, // circa 6 mesi
  guiOptions: {
    consentModal: { layout: "box", position: "bottom right", equalWeightButtons: true, flipButtons: false },
    preferencesModal: { layout: "box", equalWeightButtons: true, flipButtons: false }
  },
  categories: {
    necessary: { enabled: true, readOnly: true },
    // Al ritiro del consenso cancella i cookie e ricarica la pagina, cosi' gli script si fermano.
    analytics: { autoClear: { cookies: [{ name: "{{nome_cookie_analitico}}" }], reloadPage: true } },
    marketing: { autoClear: { cookies: [{ name: "{{nome_cookie_marketing}}" }], reloadPage: true } }
  },
  language: {
    default: "it",
    translations: {
      it: {
        consentModal: {
          title: "Questo sito usa i cookie",
          description: "Usiamo cookie tecnici, necessari per far funzionare il sito. Solo con il tuo consenso usiamo anche cookie analitici, per misurare le visite, e cookie di marketing, per misurare le campagne e mostrarti pubblicità in linea con i tuoi interessi. Se chiudi con la X o premi «Rifiuta», continui a navigare solo con i cookie tecnici. Puoi cambiare idea quando vuoi dal link «Preferenze cookie» in fondo a ogni pagina. {{revisionMessage}}",
          revisionMessage: "Abbiamo cambiato i servizi che usano i cookie: rivedi la tua scelta.",
          closeIconLabel: "Chiudi senza accettare",
          acceptAllBtn: "Accetta tutti",
          acceptNecessaryBtn: "Rifiuta",
          showPreferencesBtn: "Scegli quali cookie",
          footer: '<a href="{{url_privacy}}">Privacy policy</a> <a href="{{url_cookie_policy}}">Cookie policy</a>'
        },
        preferencesModal: {
          title: "Preferenze cookie",
          acceptAllBtn: "Accetta tutti",
          acceptNecessaryBtn: "Rifiuta tutti",
          savePreferencesBtn: "Salva le mie scelte",
          closeIconLabel: "Chiudi",
          serviceCounterLabel: "servizio|servizi",
          sections: [
            { title: "Come usiamo i cookie",
              description: "Qui scegli quali cookie attivare. Le categorie facoltative partono spente: si accendono solo se lo decidi tu. Puoi cambiare idea in ogni momento." },
            { title: "Cookie tecnici (sempre attivi)", linkedCategory: "necessary",
              description: "Servono a far funzionare il sito e a ricordare la tua scelta sui cookie. Non serve il consenso.",
              cookieTable: {
                headers: { nome: "Nome", fornitore: "Fornitore", scopo: "A cosa serve", durata: "Durata" },
                body: [{ nome: "cc_cookie", fornitore: "Questo sito", scopo: "Ricorda la tua scelta sui cookie", durata: "6 mesi" }]
              } },
            { title: "Cookie analitici", linkedCategory: "analytics",
              description: "Ci dicono come viene usato il sito: quante visite, da quali pagine, per quanto tempo. Li attiviamo solo con il tuo consenso.",
              cookieTable: {
                headers: { nome: "Nome", fornitore: "Fornitore", scopo: "A cosa serve", durata: "Durata" },
                body: [{ nome: "{{nome_cookie}}", fornitore: "{{fornitore}}", scopo: "{{scopo}}", durata: "{{durata}}" }]
              } },
            { title: "Cookie di marketing", linkedCategory: "marketing",
              description: "Servono a misurare le campagne pubblicitarie e a mostrarti annunci in linea con i tuoi interessi, anche su altri siti. Li attiviamo solo con il tuo consenso.",
              cookieTable: {
                headers: { nome: "Nome", fornitore: "Fornitore", scopo: "A cosa serve", durata: "Durata" },
                body: [{ nome: "{{nome_cookie}}", fornitore: "{{fornitore}}", scopo: "{{scopo}}", durata: "{{durata}}" }]
              } },
            { title: "Altre informazioni",
              description: 'Per domande sui cookie e sui tuoi dati leggi la <a href="{{url_privacy}}">privacy policy</a> o scrivi a {{email_privacy}}.' }
          ]
        }
      }
    }
  }
});
```

`autoClear` accetta anche espressioni regolari al posto del nome, per esempio per i cookie che
cambiano suffisso: `{ name: /^{{prefisso}}/ }`.

## 6. Come si bloccano gli script e i contenuti esterni

Ogni script non tecnico cambia così. Prima:

```html
<script>
  /* codice dello strumento */
</script>
```

Dopo (la categoria è quella del passo 3; `data-service` crea un interruttore con il suo nome):

```html
<script type="text/plain" data-category="{{analytics_o_marketing}}" data-service="{{nome_servizio}}">
  /* codice dello strumento */
</script>
```

Per uno script esterno usa `data-src` al posto di `src`:

```html
<script type="text/plain" data-category="{{categoria}}" data-src="{{url_script}}"></script>
```

Regole:

- Togli le versioni `<noscript>` dei pixel: partono senza consenso quando JavaScript è spento.
- Se la piattaforma inserisce uno strumento da un campo delle impostazioni (codice di tracciamento
  del funnel, integrazione nativa con un ID), il banner non lo blocca: toglilo da lì e mettilo a mano
  nella pagina, bloccato come sopra.
- Se uno strumento chiede un segnale di consenso (alcuni lo richiedono per i visitatori europei),
  mandalo dentro lo script bloccato, dopo il caricamento, come indica la sua documentazione.

Video, calendari e mappe incorporati: l'iframe parte senza `src`, e uno script bloccato lo
attiva solo dopo il consenso.

```html
<iframe data-src="{{url_contenuto_esterno}}" title="{{titolo}}" width="560" height="315"></iframe>
<p class="nota-consenso">Il contenuto si carica se accetti i cookie di marketing.
  <button type="button" data-cc="show-preferencesModal">Preferenze cookie</button></p>
<script type="text/plain" data-category="marketing">
  document.querySelectorAll("iframe[data-src]").forEach(function (f) { f.src = f.dataset.src; });
  document.querySelectorAll(".nota-consenso").forEach(function (n) { n.remove(); });
</script>
```

Dopo ogni modifica rifai i controlli D1-D7 di `checklist.md`.
