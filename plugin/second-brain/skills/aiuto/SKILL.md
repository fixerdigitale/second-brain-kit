---
name: aiuto
description: >
  Risponde alle domande sul metodo Second Brain e su come usare Claude Code, leggendo le guide
  del pacchetto. Usala quando la persona scrive /second-brain:aiuto, quando chiede «come
  funziona…», «cos'è…», «come si fa…» su memoria, vault, skill, pipeline, correzioni,
  modelli, consumi, limiti d'uso, contesto, permessi, come tornare indietro, Google con più
  account, aggiornamenti del pacchetto, cosa si può aggiungere dal catalogo (backup, ricerca,
  agenti, automazioni, call trascritte, approvazioni e altro), e i comandi
  dell'onboarding («più piano», «più veloce», «salta»).
argument-hint: "[argomento: memoria, skill, modelli, consumi, google, tornare indietro, aggiornare…]"
---

# Aiuto del Second Brain

Rispondi alle domande sul metodo partendo **solo** dalle guide del pacchetto, che stanno in `${CLAUDE_PLUGIN_ROOT}/guide/`.

## Come rispondi

1. Se la persona ha scritto un argomento (`$ARGUMENTS`), apri la guida giusta dalla tabella. Se non l'ha scritto, apri `INIZIA-DA-QUI.md` e mostrale il menu.
2. Rispondi in parole semplici, con un esempio preso dal **suo** lavoro (leggi la sua nota in `memoria/` o il suo `CLAUDE.md` per trovarne uno). Massimo 15 righe, poi chiedi se vuole approfondire.
3. Chiudi con **una** cosa che può provare subito, in meno di 2 minuti.
4. Se la guida non risponde, dillo: «La guida non lo dice». Poi proponi di cercarlo nella documentazione ufficiale di Claude Code (https://code.claude.com/docs) e di' da dove viene quello che trovi. Non inventare comandi, impostazioni o numeri.
5. I limiti d'uso e i prezzi cambiano spesso: per i numeri esatti rimanda sempre alla pagina ufficiale o al comando `/usage`, anche se la guida ne cita qualcuno.

## Quale guida aprire

| Argomento | Guida |
|---|---|
| Da dove si parte, i primi 10 giorni, il menu | `INIZIA-DA-QUI.md` |
| La cartella di lavoro, dove stanno le cose, il backup | `01-cartella-di-lavoro.md` |
| Memoria, vault, note dei clienti, «salva in memoria» | `02-memoria.md` |
| Correzioni, regole d'oro, «non rifarlo» | `03-correzioni.md` |
| Skill: cosa sono, quando crearle, dove trovarne | `04-skill.md` |
| Sicurezza, tornare indietro, Esc Esc, `/rewind`, git, copie | `05-tornare-indietro.md` |
| Modelli, impegno, consumi, limite delle 5 ore e settimanale, contesto | `06-modelli-e-consumi.md` |
| Google con più account, gog, connettori | `07-google-piu-account.md` |
| Pipeline, lavori che si ripetono, automatizzare | `08-pipeline.md` |
| Aggiornare il pacchetto, versioni, novità | `09-aggiornare.md` |
| Impostazioni consigliate, permessi, barra di stato | `10-impostazioni.md` |
| Da dove parto, l'onboarding, la mappa, il piano, la rimisura | `INIZIA-DA-QUI.md` e la skill `onboarding` |
| Cosa potrei aggiungere: tutto quello che uso io, come opzione (memoria, ricerca, agenti, automazioni, canali, sicurezza, skill) | l'indice `${CLAUDE_PLUGIN_ROOT}/catalogo-indice.json`, poi la scheda intera nella repo del kit (vedi «Dove sta il catalogo» in `skills/piano-upgrade/SKILL.md`) |
| Cosa ho provato e lasciato, e perché | `catalogo/scartati.md` nella repo del kit |

## Più piano, più veloce

La persona può scrivere in qualsiasi momento `più piano` / `slower` o `più veloce` / `faster`.

- **più piano:** una cosa per messaggio, un esempio per ogni scelta, le parole tecniche spiegate tra
  parentesi.
- **più veloce:** dritto al punto, tabelle, domande raggruppate fino a 3.

Se esiste `second-brain/.onboarding/stato.json`, salva la scelta:
`python3 "${CLAUDE_PLUGIN_ROOT}/scripts/stato.py" imposta ritmo piano` (o `veloce`, `normale`) e
segui `skills/onboarding/tono.md`. Altrimenti vale per questa sessione. Le regole di sicurezza
restano uguali in tutti e due i ritmi.

## Lingua

Rispondi nella lingua in cui scrive la persona (italiano o inglese). Le guide sono in italiano:
se la persona scrive in inglese, traduci tu la parte che serve.

## Modo passo passo

Se in `memoria/Correzioni/REGOLE-ORO.md` c'è «Modo: passo passo» (o la vecchia «Modalità: principiante», o la riga manca), spiega anche le parole tecniche che usi, tra parentesi. Con «Modo: diretto» (o la vecchia «Modalità: esperto») vai dritto al punto.
