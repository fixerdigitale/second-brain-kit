---
slug: skill-media
titolo: "Immagini, video e voce: cosa uso e quanto costa"
area: skill
dove_gira: PC
livello: medio
costo: "immagini 0 € in più con l'abbonamento ChatGPT; video e voce a consumo (circa 0,15-0,45 $ per 5 secondi di video a ottobre 2026)"
pacchetto: "pacchetti/skill-media/"
stato: "versione per PC del mio"
---
# Immagini, video e voce: cosa uso e quanto costa

**Il problema.** Per immagini, video e audio c'erano decine di servizi, ognuno con il suo credito e la sua chiave. Pagavo a immagine anche quando avevo un abbonamento ChatGPT che restava fermo.

**Come l'ho risolto.** Ho messo un ordine fisso. Le immagini (nuove o modificate da una foto) le faccio col Codex di OpenAI, cioè con l'abbonamento ChatGPT: nel mio sistema passa da un ponte sul server che si ferma da solo quando l'uso settimanale supera il 70%, senza passare di nascosto a un servizio a pagamento. I video da testo o da immagine li faccio con l'API video di OpenRouter; quelli scritti come codice (titoli animati, motion graphics) con HyperFrames, che è gratis. Musica, effetti, upscale, rimozione dello sfondo e lipsync passano da MuAPI. Per trascrivere uso Whisper, gratis; per la voce narrante ElevenLabs o Fish Audio, che controllano l'emozione. Per i video ho anche due skill mie (regia di un video fatto in codice, e un video illustrato a partire da un vocale) che nel kit non metto, perché sono legate al mio modo di lavorare.

**Perché così.** L'abbonamento già pagato copre la cosa che faccio più spesso, le immagini. Il resto lo pago solo quando serve. Per la voce ho imparato che una pronuncia perfetta non basta: in un video conta la recitazione, quindi scelgo motori dove si segna l'emozione nel testo.

**Quando ti serve.** Se produci spesso immagini per pagine, post o presentazioni e hai già un piano ChatGPT; se ogni tanto ti serve un video breve o una voce.

**Quando non ti serve.** Se ti servono poche immagini al mese, l'app di ChatGPT fa lo stesso senza script. Se i materiali sono di clienti con dati riservati, controlla prima le condizioni sui dati di ogni servizio: non tutti cancellano quello che carichi. E non generare per conto di altri con il tuo abbonamento personale.

**Come prenderlo.** Il pacchetto ha `immagine.py` (Codex da riga di comando, provato solo con un Codex finto) e la tabella dei servizi con le fonti pubbliche: Codex https://github.com/openai/codex, OpenRouter https://openrouter.ai, HyperFrames https://github.com/heygen-com/hyperframes, MuAPI https://muapi.ai/docs, skill ElevenLabs https://github.com/elevenlabs/skills, Whisper https://github.com/openai/whisper. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/skill-media/LEGGIMI.md).
