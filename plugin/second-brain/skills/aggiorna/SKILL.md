---
name: aggiorna
description: >
  Updates Second Brain in your work folder, showing every change and protecting your personal files.
  Opened with /second-brain:aggiorna. — Aggiorna Second Brain nella cartella di lavoro mostrando
  ogni modifica e proteggendo i file personali. Si apre con /second-brain:aggiorna.
disable-model-invocation: true
---

# Aggiorna Second Brain

Questa procedura parte solo quando la persona scrive `/second-brain:aggiorna`.

## 1. Mostra sempre il piano

Esegui sempre `piano`, anche quando le versioni coincidono, con `bash` davanti allo script:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/second-brain.sh" piano --cartella "<cartella aperta>"
```

Scrivi «già aggiornato» e fermati soltanto se non ci sono voci `NUOVO`, `AGGIORNABILE`, `CONFLITTO`, `BLOCCO-AGGIORNABILE` o `BLOCCO-CONFLITTO`. `TUO` e `BLOCCO-MODIFICATO` non impediscono «già aggiornato».

Su Windows converti prima i percorsi dalla forma `C:\...` alla forma `/c/...` e passa allo script soltanto percorsi con `/`.

Su Windows serve **Git Bash**, non un `bash` qualunque. Se il tuo strumento per i comandi è Bash, controlla la prima volta con `bash --version`: deve contenere `msys`; se contiene `linux` è WSL e non va usato. Se il tuo strumento è PowerShell, non scrivere `bash` da solo (su molti computer porta a WSL, `C:\Windows\System32\bash.exe`): usa il percorso completo, per esempio `& "C:\Program Files\Git\bin\bash.exe" "<script>" piano --cartella "<cartella>"`, oppure `%LOCALAPPDATA%\Programs\Git\bin\bash.exe`. Se Git Bash non c'è, proponi di installarlo con `winget install --id Git.Git -e`, solo dopo il sì, e di riaprire l'app di Claude.

Se lo script esce con codice 2, mostra alla persona il messaggio con parole semplici. Non riprovare con opzioni diverse: proponi il passo indicato dal messaggio.

## 2. Riassumi le novità

Leggi prima `${CLAUDE_PLUGIN_ROOT}/CHANGELOG.md`. Soltanto se manca, leggi `${CLAUDE_PLUGIN_ROOT}/../CHANGELOG.md`. Considera soltanto le versioni successive a quella installata e riassumi ogni novità in due righe: cosa cambia e cosa deve decidere o fare la persona.

## 3. Spiega il piano

Usa l'output già ottenuto al passo 1. Non scrivere ancora nulla.

## 4. Raccogli le decisioni

- Per ogni `NUOVO`, mostra il percorso e chiedi sì/no.
- Per ogni `AGGIORNABILE`, mostra il percorso, spiega che la persona non lo ha cambiato e chiedi sì/no.
- Non modificare `UGUALE`, `TUO` o `BLOCCO-MODIFICATO`.
- Per ogni `CONFLITTO`, mostra `diff` fra file della persona e file seme, spiegalo in parole semplici e chiedi quali parti tenere.
- Per `BLOCCO-CONFLITTO`, estrai il blocco fra i due marcatori, confrontalo con `modelli/CLAUDE-blocco.md`, spiega le differenze e chiedi quali parti tenere.

Se su un `CONFLITTO` o `BLOCCO-CONFLITTO` la persona dice «tengo il mio», chiedi il suo sì per registrare quella decisione con `registra --voce` o `registra --blocco`: così la stessa proposta non torna al prossimo aggiornamento.

Una fusione si fa con i tuoi strumenti soltanto dopo la risposta. Prima crea nello stesso posto una copia `.bak-AAAAMMGG-second-brain`, oppure il primo suffisso libero `-2`, `-3` e così via. Non cambiare mai le righe di `CLAUDE.md` fuori dal blocco. Se l'ultima riga di `CLAUDE.md` non ha un a capo, l'aggiornamento del blocco ne aggiunge uno. Se `CLAUDE.md` usa fine riga Windows (CRLF), il blocco nuovo entra con fine riga LF; la parte della persona resta com'è.

Dopo ogni fusione registra con lo script l'impronta del seme accettato, senza cambiare di nuovo il file:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/second-brain.sh" registra --cartella "<cartella>" --voce "<percorso>"
bash "${CLAUDE_PLUGIN_ROOT}/scripts/second-brain.sh" registra --cartella "<cartella>" --blocco
```

## 5. Applica le voci scelte

Se tutte le risposte sono no, non lanciare `applica`.

Esegui un solo comando con un `--voce` per ogni `AGGIORNABILE` accettato, un `--escludi` per ogni `NUOVO` rifiutato e `--claude aggiorna` solo se accettato:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/scripts/second-brain.sh" applica --cartella "<cartella>" [--voce "<percorso>"] [--escludi "<percorso>"] [--claude aggiorna]
```

Se la persona accetta soltanto il blocco di CLAUDE.md, usa `applica --solo-claude --claude aggiorna`. Non scrivere mai `.second-brain/stato.txt` a mano. Le voci escluse non vanno create neppure temporaneamente.

Dopo, riapri ogni file cambiato. Controlla che le parti personali e le voci rifiutate siano identiche a prima.

## 6. Chiudi in tre righe

Scrivi soltanto:

1. cosa è stato aggiornato;
2. dove si trovano i file e le copie;
3. come tornare indietro.
