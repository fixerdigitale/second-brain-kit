# Pagine legali di un sito italiano

**Cosa fa.** Prima guarda cosa fa davvero il sito (scansione del codice e prova del banner cookie nel browser: cosa parte prima della scelta, dopo «Rifiuta», dopo «Accetta»), poi scrive privacy, cookie policy, condizioni di servizio, informativa sull'uso dell'AI e testi del banner. Quello che non ha una fonte resta come segnaposto `{{...}}` e finisce in `da-verificare.md`. **Non è consulenza legale**: sono bozze da far rivedere a un professionista.

**Licenza.** È un adattamento italiano di https://github.com/gricyk/claude-skill-eu-web-compliance (Apache 2.0). `LICENSE` e `NOTICE` vanno tenuti insieme alla skill.

**Dove si copia.** La cartella `pagine-legali/` in `~/.claude/skills/pagine-legali/`.
Servono:
- Python 3 per `scripts/scan.py` (solo libreria standard);
- Node.js e Playwright con Chromium per `scripts/consenso.mjs`: `npm i -g playwright` e `npx playwright install chromium`. Senza, la skill fa solo la scansione e la parte nel browser la salti.

La cartella di lavoro di ogni sito è `<tuo-progetto>/pagine-legali-<dominio>-<data>`, fuori dalle cartelle pubblicate del sito.

**Come si prova.** Chiedi «controlla le pagine legali di <un tuo sito>». Deve uscire la scheda dei fatti con la fonte accanto a ogni dato, l'esito della prova del banner e l'elenco `da-verificare.md`. Niente ragione sociale o P.IVA inventate.

**Come si toglie.** Cancella `~/.claude/skills/pagine-legali/`. Playwright si toglie con `npm rm -g playwright`.

**Da sapere.** Le norme in `riferimenti.md` sono state verificate a ottobre 2026: la sezione «Da ricontrollare a ogni consegna» dice quali cambiano spesso.

**Da affiancare, se ti serve citare le norme dal testo vigente.** Il plugin `legal-it` di mcp-legal-it
(https://github.com/capazme/mcp-legal-it, Apache 2.0) dà a Claude strumenti per leggere il testo
vigente da Normattiva, EUR-Lex e Brocardi, più calcoli e ricerche di giurisprudenza. Si installa come
plugin di Claude Code dal suo marketplace (istruzioni nella repo, serve Python 3.10 o più recente).
Io lo tengo installato ma spento di serie e lo accendo quando devo controllare un articolo: ogni
sessione aperta avvia un suo server, e per il lavoro normale non mi serve.

## English

`pagine-legali`, an Italian adaptation of a public Apache 2.0 skill: it scans a site's code and tests the cookie banner in a browser (what fires before the choice, after Reject, after Accept), then drafts privacy policy, cookie policy, terms, an AI-use notice and banner texts. Missing facts stay as placeholders. Drafts for a professional to review, not legal advice.

Install: copy `pagine-legali/` into `~/.claude/skills/`, keeping LICENSE and NOTICE. You need Python 3 and, for the banner test, Node.js with Playwright and Chromium. Original: https://github.com/gricyk/claude-skill-eu-web-compliance.
