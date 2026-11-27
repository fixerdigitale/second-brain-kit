# Regole proposte di notte, fisse solo dopo il tuo ok

**Cosa fa.** Ogni notte guarda le correzioni salvate nella memoria di Claude Code e trova quelle
che sono tornate almeno due volte. Non le mette da sole fra le Regole d'oro: le scrive in
`PROPOSTE-REGOLE.md` come domanda, «la rendo fissa?». Tu metti `[x]` (sì), `[-]` (no) o lasci
`[ ]`. Il giro dopo applica solo i sì, con una copia datata di `MEMORY.md` prima di scrivere.

Da me lo stesso giro passa da una card con due bottoni sul telefono. Qui la card è una riga di
un file: meno comoda, ma funziona senza server.

**Richiede.** La memoria con i file `feedback_*.md` nel formato del pacchetto
`memoria-feedback-why-how` (ogni ritorno della correzione = una riga
`**Aggiornamento del gg/mm:**` in fondo) e un `MEMORY.md` con la sezione `## Regole d'oro`
(pacchetto `memoria-indice-e-regole-doro`). Python 3, nessuna libreria in più.

**Dove si copia.** `regole_doro.py` dove vuoi, per esempio `~/.claude/strumenti/`.
La cartella della memoria è `~/.claude/projects/<nome-cartella-del-progetto>/memory/`.

Due attività pianificate (Utilità di pianificazione su Windows, cron o launchd su Mac):

    # di notte: prepara le proposte
    python3 ~/.claude/strumenti/regole_doro.py proponi --memoria <cartella-memoria>
    # al mattino, o a mano dopo che hai risposto
    python3 ~/.claude/strumenti/regole_doro.py applica --memoria <cartella-memoria>

Se non vuoi pianificare niente, lancia tu i due comandi una volta a settimana: funziona uguale.

**Regole del giro.**
- Soglia: 2 ritorni (`SOGLIA` in cima allo script).
- Tetto: 20 Regole d'oro (`TETTO`). A tetto pieno il sì resta in attesa e lo script te lo dice:
  prima ne togli una tu.
- Un no si ricorda: la stessa correzione non torna più fra le proposte (sta in `STORICO-REGOLE.md`).
- Puoi correggere il testo della proposta prima di mettere `[x]`: entra la tua versione.

**Come si prova (su dati finti).**
1. Crea una cartella vuota, copiaci il `MEMORY.md` d'esempio e due file `feedback_prova.md` con
   due righe `**Aggiornamento del …**` ciascuno.
2. `python3 regole_doro.py proponi --memoria <cartella>` → deve creare `PROPOSTE-REGOLE.md` con due righe `[ ]`.
3. Metti `[x]` su una e `[-]` sull'altra, poi `applica --prova` (mostra senza scrivere) e `applica`.
4. Controlla: in `MEMORY.md` c'è una riga nuova numerata, accanto c'è `MEMORY.md.bak-<data>`,
   in `STORICO-REGOLE.md` ci sono un SÌ e un NO. Un secondo `proponi` non ripropone niente.

Io l'ho provato così, su file finti, il 27/11/2026.

**Come si toglie.** Cancella le due attività pianificate e lo script. `PROPOSTE-REGOLE.md` e
`STORICO-REGOLE.md` puoi tenerli o cancellarli: `MEMORY.md` resta com'è.

## English

A model-free script that, at night, finds corrections saved in memory that came back at least twice and proposes them as "make it a Golden Rule?" lines in a file. In the morning you mark [x] or [-]; another run applies only the yeses, with a dated copy first, keeps a history and remembers the noes. The 20 Golden Rules cap applies.

Install: copy `regole_doro.py`, then schedule `regole_doro.py proponi` at night and `regole_doro.py applica` in the morning, passing the path of your Claude Code memory folder.
