# Media: immagini con l'abbonamento ChatGPT, video e voce

**Cosa c'è.** Uno script mio, `immagine.py`, e l'elenco dei servizi e delle skill pubbliche che uso
per il resto. Le skill dei servizi sono di terzi: si prendono dalla fonte, non da qui.

## Immagini: `immagine.py` (Codex, abbonamento ChatGPT)

Fa un'immagine nuova, o ne modifica una partendo da una foto, con il Codex CLI di OpenAI collegato
al tuo account ChatGPT. Niente API a consumo: usa la quota del piano che paghi già.

**Cosa serve.** Python 3 e il Codex CLI (https://github.com/openai/codex) con `codex login` fatto con
l'account ChatGPT. Verifica sul tuo piano che la generazione di immagini dal Codex sia inclusa.

**Come si usa.**

    python3 immagine.py "copertina per un articolo sul lavoro da remoto, toni caldi, niente testo" -o copertina.png
    python3 immagine.py "togli la tazza dal tavolo" --partenza foto.png -o foto-pulita.png

Ogni richiesta gira in una cartella temporanea vuota, in sola lettura, con shell, browser e plugin
spenti: il Codex può solo generare l'immagine. Se la tua versione del Codex dà errore su una funzione
sconosciuta, togli quel nome dalla lista `SPENTI` in cima allo script. Ci mette circa 20-30 secondi.
Il modello di immagine lo sceglie OpenAI: se ti serve un modello preciso, usa un servizio a consumo.

**Come si prova.** `python3 immagine.py "un cerchio rosso su sfondo bianco" -o prova.png`, poi apri il file.

**Limite onesto.** L'ho provato con un Codex finto, non su un PC Windows o Mac con un account vero.
Nel mio sistema la stessa chiamata gira su un server dietro una coda, con uno stop quando l'uso
settimanale di ChatGPT passa il 70%: qui la soglia la guardi tu.

## Il resto: servizi e skill pubbliche

| Cosa | Servizio o skill | Fonte | Costo |
|---|---|---|---|
| Video da testo o da immagine | API video di OpenRouter (Veo, Kling e altri) | https://openrouter.ai | a consumo, a ottobre 2026 circa 0,15-0,45 $ per 5 secondi |
| Video scritti come codice (motion graphics, titoli animati) | HyperFrames di HeyGen (Apache 2.0) | https://github.com/heygen-com/hyperframes | gratis, serve ffmpeg |
| Musica, effetti, upscale, sfondo, lipsync | MuAPI (server MCP e skill) | https://muapi.ai/docs e https://github.com/SamurAIGPT/Generative-Media-Skills | credito prepagato |
| Trascrizione, effetti sonori, voce isolata | skill ufficiali ElevenLabs (MIT) | https://github.com/elevenlabs/skills | a consumo, con chiave ElevenLabs |
| Voce narrante con emozione | ElevenLabs v3 o Fish Audio | https://elevenlabs.io e https://fish.audio | a consumo |
| Trascrizione gratis sul tuo computer | Whisper | https://github.com/openai/whisper | gratis, meglio con una GPU |

Ogni chiave va in una variabile d'ambiente o nel gestore di segreti, mai nel testo della skill.
Prima di installare una skill di terzi, passala dal metodo di `pacchetti/skill-cerca-strumento/`.

**Come si toglie.** Cancella `immagine.py`. Le skill dei servizi si tolgono dalla loro cartella in `~/.claude/skills/`.

## English

`immagine.py` generates or edits images from the command line with OpenAI's Codex CLI, using a ChatGPT subscription instead of pay-per-image services; this guide also has the table of services I use for video, music, voice and transcription, with their public sources.

Install: install and log into Codex CLI (https://github.com/openai/codex), copy `immagine.py` wherever you like and run it as described above. It was tested only with a fake Codex. Check each service's data terms before uploading client material.
