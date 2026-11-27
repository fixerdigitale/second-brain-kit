---
slug: skill-web-research
titolo: "Ricerche sul web con le fonti accanto"
area: skill
dove_gira: PC
livello: base
costo: "0 € con ricerca e lettura diretta; scraping a pagamento facoltativo, circa 0,002-0,01 $ a pagina"
pacchetto: "pacchetti/skill-web-research/"
stato: "versione per PC del mio"
---
# Ricerche sul web con le fonti accanto

**Il problema.** Le ricerche dell'AI mescolavano fatti e opinioni, senza date e senza link. Le pagine che non si aprivano sparivano in silenzio.

**Come l'ho risolto.** Una skill che cerca prima e legge dopo: 2-4 fonti vere, una scala di modi per aprire una pagina (lettura diretta, poi un browser leggero che esegue il JavaScript, poi un browser vero, a pagamento solo per ultimo). Per i prezzi parte dai comparatori. Per i video scarica e legge i fotogrammi. Esce sempre con una risposta breve, ogni affermazione con il suo link e una sezione «Incertezze» con le pagine che non si sono aperte. Dalla mia versione ho tolto i comandi che dipendono dal mio server.

**Perché così.** Una ricerca mi serve per decidere: senza link non la posso verificare. Un dato trovato su una fonte sola va scritto come «secondo X». Se una pagina è bloccata preferisco saperlo, invece di leggere un riassunto inventato.

**Quando ti serve.** Confronti di prezzi e strumenti, concorrenti, verifiche di fatti, aprire un link o un video che ti hanno girato.

**Quando non ti serve.** Per domande che non dipendono da informazioni recenti basta chiedere. Per studi lunghi su un mercato serve una ricerca più profonda, con più giri.

**Come prenderlo.** Copia `web-research/` in `~/.claude/skills/`. Facoltativi: yt-dlp e ffmpeg per i video, Lightpanda (https://github.com/lightpanda-io/browser) o un MCP di browser. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/skill-web-research/LEGGIMI.md).
