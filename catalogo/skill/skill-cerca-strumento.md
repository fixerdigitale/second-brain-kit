---
slug: skill-cerca-strumento
titolo: "Valutare uno strumento prima di installarlo"
area: skill
dove_gira: PC
livello: medio
costo: "0 €; 5-15 minuti di sessione per valutazione"
pacchetto: "pacchetti/skill-cerca-strumento/"
stato: "lo uso"
---
# Valutare uno strumento prima di installarlo

**Il problema.** Mi giravano link a skill, MCP e repo «utilissimi». Installarli al volo vuol dire far girare codice di sconosciuti accanto alle mie chiavi e ai dati dei clienti. E a volte rifacevo la stessa valutazione due volte.

**Come l'ho risolto.** Una skill che prima guarda cosa ho già, poi cerca nei registri giusti (registro ufficiale MCP, PulseMCP, Glama, Smithery, GitHub). Confronta al massimo tre candidati: se è vivo, chi lo mantiene, cosa tocca, licenza, codice letto e non solo il README. Chiude con un verdetto in tre righe: INSTALLO, PROVO ISOLATO o LASCIO PERDERE. Ogni verdetto, anche i no, va in `valutati.md`.

**Perché così.** Nel 2026 ci sono state campagne di skill malevole nei registri aperti, con nomi quasi uguali a quelli veri. Uno scanner statico (io uso SkillSpector di NVIDIA) aiuta, ma dà molti falsi positivi: senza leggere il codice a mano non decido. Separare il cercare dall'installare mi evita le installazioni d'impulso.

**Quando ti serve.** Se installi spesso skill, plugin o MCP presi da fuori.

**Quando non ti serve.** Se usi solo le skill ufficiali di Anthropic o quelle di un fornitore che conosci, è troppo.

**Come prenderlo.** Copia `cerca-strumento/` (con `valutati.md`) in `~/.claude/skills/`. Scanner facoltativo, serve Docker: https://github.com/NVIDIA/SkillSpector. Istruzioni passo passo: [LEGGIMI del pacchetto](../../pacchetti/skill-cerca-strumento/LEGGIMI.md).
