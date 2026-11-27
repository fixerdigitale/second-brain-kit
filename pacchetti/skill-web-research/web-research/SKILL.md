---
name: web-research
description: Ricerca sul web e raccolta di referenze. Cerca fonti, estrae il contenuto delle pagine in markdown e produce una sintesi con citazioni. Usala per ricerche di mercato, informazioni aggiornate, analisi di competitor, confronti di prezzi e prodotti, raccolta di esempi e referenze visive o di copy, verifica di fatti, e per aprire un link singolo che ti passa l'utente (anche un video).
---

# Web Research

## Cercare fonti

Usa il tool di ricerca che hai (`WebSearch` in Claude Code). Scegli 2-4 risultati davvero
rilevanti e apri solo quelli: niente scrape a tappeto.

**Prezzi e prodotti:** parti dai comparatori (Trovaprezzi, idealo, Keepa per Amazon). Una
pagina sola ti dà i prezzi di molti negozi, e i comparatori bloccano meno dei singoli shop.

## Aprire un link (in ordine: fermati al primo che funziona)

1. **Lettura diretta** (`WebFetch`). Gratis. Va bene per pagine semplici.
2. **Lightpanda** (facoltativo, https://github.com/lightpanda-io/browser): browser leggero che
   esegue il JavaScript e restituisce il testo. Serve per le pagine che si riempiono dopo il
   caricamento. Non fa screenshot veri.
3. **Browser vero** (per esempio Chrome DevTools MCP): per guardare davvero una pagina o quando
   serve cliccare. Molti e-commerce e siti dietro Cloudflare bloccano comunque i browser
   automatici.
4. **Servizio di scraping a pagamento** (facoltativo, es. Crawlbase, da ~0,002 a ~0,01 $ a
   richiesta): proxy e rendering veri. Mai come primo tentativo.

Se falliscono tutti (login, captcha, contenuto riservato): fermati e dillo all'utente. Proponi
di incollarti il testo. Non inventare il contenuto.

## Guardare un video (reel, TikTok, YouTube)

Per contenuti pubblici, con `yt-dlp` e `ffmpeg` installati:

```bash
yt-dlp -o "video.%(ext)s" "URL_DEL_VIDEO"
ffmpeg -i video.mp4 -vf "select='eq(n\,0)+eq(n\,300)+eq(n\,600)'" -vsync vfr frame_%d.jpg -y
```

Poi leggi i frame con il tool Read (le immagini si vedono davvero). Un frame ogni ~10 s è un
buon inizio; per un reel breve 3-4 frame bastano. `yt-dlp` prende anche titolo, didascalia,
autore e numeri dai metadati.

Limiti reali: LinkedIn e i contenuti privati richiedono un login; senza, si vede solo quello che
vede un visitatore anonimo.

## Come lavorare

1. **Cerca prima, leggi dopo.** Apri solo le 2-4 pagine che servono.
2. **Verifica su più fonti.** Un dato su una fonte sola va riportato come «secondo X».
3. **Cita sempre l'URL** accanto a ogni affermazione.
4. **Segnala le date.** Se la pagina non ha data, dillo.
5. **Distingui fatto da opinione.** Un blog che dice «il tool migliore è X» è un'opinione interessata.
6. **Di' quali pagine non sei riuscito ad aprire** e a quale gradino ti sei fermato.

## Formato dell'output

```
## Risposta breve
[2-3 righe che rispondono davvero alla domanda]

## Cosa ho trovato
- **[Affermazione]** — fonte: <url> (data se nota)

## Incertezze
[Cosa non sono riuscito a verificare, pagine bloccate, contraddizioni fra fonti]
```
