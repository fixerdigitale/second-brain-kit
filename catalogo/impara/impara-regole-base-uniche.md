---
slug: impara-regole-base-uniche
titolo: "Regole base uniche per tutti gli agenti, ricopiate da sole"
area: impara
dove_gira: PC
livello: medio
costo: "0 €. 15 minuti, più il tempo per scrivere le tue regole comuni."
pacchetto: "pacchetti/impara-regole-base-uniche/"
stato: "versione per PC del mio"
---

# Regole base uniche per tutti gli agenti, ricopiate da sole

**Il problema.** Ogni agente aveva il suo file di istruzioni, e le regole che valevano per tutti (come si scrive, come si verifica, cosa non si manda fuori) erano copiate a mano in ognuno. Col tempo le copie divergevano, e un agente a volte modificava le sue.

**Come l'ho risolto.** Le regole comuni stanno in un file solo. Uno script le copia, fra due segni, dentro il file di ogni agente; fuori dai segni non tocca niente. Se qualcuno cambia il blocco in una copia, al giro dopo torna uguale alla fonte. Una regola si cambia in un posto solo, e vale per tutti. Da me la fonte è un file che gli agenti non possono modificare, si ricopia ogni ora, e le regole nuove ci entrano solo con il mio ok (scheda [regole proposte con l'ok](impara-regole-proposte-con-ok.md)).

**Perché così.** Una regola copiata a mano in dieci posti, per me, è dieci regole diverse dopo un mese. Una fonte unica rigenerata da sola mi toglie il lavoro e il dubbio su quale versione vale.

**Quando ti serve.** Se hai almeno due o tre file di istruzioni diversi: sotto-agenti di Claude Code, un AGENTS.md per Codex, le regole di un altro strumento.

**Quando non ti serve.** Se usi solo Claude Code con un CLAUDE.md: quello lo legge già ogni sessione, e uno script in più non aggiunge niente. Sul PC la protezione è solo «torna com'era al giro dopo»: per impedire davvero le modifiche servono un utente separato o un server.

**Come prenderlo.** Copia i tre file in una cartella (per esempio `~/.claude/regole-base/`), scrivi le tue regole in `REGOLE-BASE.md` e i file da aggiornare in `destinazioni.txt`, poi lancia lo script a mano, ogni ora o con un hook SessionStart. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/impara-regole-base-uniche/LEGGIMI.md).
