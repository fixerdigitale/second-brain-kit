---
name: salva-in-memoria
description: Salva una nota nel posto giusto. Usala quando l'utente dice «salva in memoria», «ricordati che», «segnati» o detta una nota su un cliente o un progetto. I fatti (clienti, progetti, decisioni, persone) vanno nel vault; le correzioni su come lavorare vanno nella memoria di Claude Code.
---

# Salva in memoria

Due memorie, ognuna con un compito:

| Cosa | Dove | Esempio |
|---|---|---|
| Fatto su un cliente, progetto, persona, decisione | Vault: `<cartella-vault>/Clienti/<Nome>.md` o `<cartella-vault>/Progetti/<Nome>.md` | «Il cliente X ha approvato il preventivo il 12/10» |
| Correzione su come lavori tu | Memoria di Claude Code: `feedback_<nome>.md` + riga in MEMORY.md | «Non mandarmi più i link come testo semplice» |

## Passi

1. Decidi se è un **fatto** o una **correzione**. Nel dubbio è un fatto: va nel vault.
2. **Fatto** →
   - trova la nota giusta (cerca per nome nel vault; se non c'è, creala con il frontmatter del vault);
   - aggiungi in coda alla sezione `## Dalle sessioni` (creala se manca) una voce:
     `- **gg/mm/aaaa · titolo breve** — Obiettivo: … / Fatto: … / Aperto: …`
   - niente copia nella memoria di Claude Code: una cosa sta in un posto solo.
3. **Correzione** →
   - se esiste già un `feedback_*.md` sullo stesso tema, aggiungi in fondo `**Aggiornamento del gg/mm:** …`;
   - se no, crea `feedback_<nome>.md` con le parti Why e How to apply e aggiungi il nome in MEMORY.md
     (gruppo del tema o «Da smistare»).
4. Rispondi in una riga: dove l'hai scritto (percorso) e cosa c'è scritto.

## Mai

- Password, token, chiavi, codici: né nel vault né in memoria. Al massimo il nome della chiave.
- Riassumere tagliando fatti: meglio una voce lunga e ordinata.
