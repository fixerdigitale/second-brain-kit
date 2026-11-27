---
slug: memoria-revisore-notturno
titolo: "Revisore notturno delle sessioni"
area: memoria
dove_gira: PC
livello: medio
costo: "0 € in più con l'abbonamento Claude (una corsa su Sonnet). 3-5 minuti al giorno per approvare."
pacchetto: pacchetti/memoria-revisore-notturno/
stato: versione per PC del mio
---

# Revisore notturno delle sessioni

**Il problema.** Le decisioni prese durante il giorno, in sessioni diverse, non finivano in memoria se non lo chiedevo esplicitamente. Il vault invecchiava, con note superate e doppioni. E le correzioni ripetute non salivano mai di importanza.

**Come l'ho risolto.** Da me un revisore gira ogni notte alle 4:00 su un server. Legge tutte le sessioni delle ultime ore (Claude Code, Codex, agenti, call, chat di lavoro); una sola chiamata a Sonnet decide voce per voce cosa salvare, dove, e cosa scartare con il motivo; poi scrive nel vault (Obiettivo, Richiesta, Fatto, Aperto) e nella memoria. Se una correzione è tornata almeno due volte, propone di farla diventare Regola d'oro con una card che approvo io. Il principio: le informazioni non si tagliano, si ordinano. Per il PC ho fatto una versione che si chiama «archivista di fine giornata»: scrivi «fine giornata», un sotto-agente legge le tue richieste di oggi e le note cambiate, e propone fino a 15 voci (fatto da salvare, correzione, nota superata, doppione, candidata Regola d'oro), ognuna con la fonte. Non scrive niente: una skill te le mostra una alla volta e applica solo i sì.

**Perché così.** Chiedere «salva» a ogni decisione non funziona: me ne dimentico. Un giro unico vede tutto insieme e trova i doppioni. Il conteggio delle ripetizioni rende oggettivo cosa diventa Regola d'oro. Sul server lo lascio scrivere da solo perché leggo i resoconti; sul PC ho preferito che chieda l'ok, perché di notte il PC di solito è spento e un errore salvato in memoria resta per settimane.

**Quando ti serve.** Se lavori molte ore al giorno con Claude, prendi decisioni in sessioni diverse e usi il vault ogni giorno.

**Quando non ti serve.** Se usi Claude per compiti brevi e scollegati, o se ti basta dire «salva in memoria» quando serve. Se scrivi nel vault poche volte a settimana, 15 proposte al giorno diventano rumore: sotto le 5-10 note cambiate a settimana basta rileggerle tu.

**Come prenderlo.** Copia `.claude/agents/archivista.md` in `~/.claude/agents/` e `.claude/skills/fine-giornata/` in `~/.claude/skills/fine-giornata/`, sostituisci i segnaposto, poi scrivi «fine giornata» in Claude Code. Va meglio insieme al pacchetto `pacchetti/memoria-raccolta-sessioni/`.

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-revisore-notturno/LEGGIMI.md).
