# Ricerca sul web con fonti

**Cosa fa.** Dà a Claude un metodo fisso per le ricerche: 2-4 fonti vere invece di cinquanta, una scala di modi per aprire una pagina (dal gratis al pagamento), i video letti a fotogrammi, e un formato di uscita con risposta breve, ogni affermazione con il suo link e una sezione «Incertezze».

**Dove si copia.** `web-research/` in `~/.claude/skills/web-research/`.
Facoltativi: `yt-dlp` e `ffmpeg` per i video (su Windows `winget install yt-dlp.yt-dlp Gyan.FFmpeg`, su Mac `brew install yt-dlp ffmpeg`); Lightpanda o un MCP di browser per le pagine difficili. Senza, la skill usa solo ricerca e lettura diretta.

**Come si prova.** Chiedi «quanto costa oggi un iPhone 15 Pro ricondizionato in Italia?». Deve uscire la risposta in 2-3 righe, ogni prezzo con il link, e le pagine che non si sono aperte elencate in «Incertezze».

**Come si toglie.** Cancella `~/.claude/skills/web-research/`.

## English

A `web-research` skill: search first, read after, 2-4 real sources, a ladder of ways to open a page (direct read, light browser, real browser, paid scraping only last), frames read from videos. It always returns a short answer with a link for every claim and an "Uncertainties" section listing pages that didn't open.

Install: copy `web-research/` into `~/.claude/skills/`. Optional: yt-dlp and ffmpeg for videos, Lightpanda (https://github.com/lightpanda-io/browser) or a browser MCP.
