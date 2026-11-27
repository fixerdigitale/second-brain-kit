# Installazione

🇬🇧 [English](INSTALL.md)

Ci sono tre strade. Scegli quella che ti somiglia: puoi sempre cambiare dopo.

| Strada | Per chi | Cosa ottieni |
|---|---|---|
| [A. Plugin dal marketplace](#a-plugin-dal-marketplace-da-github) | Hai Claude Code e vuoi gli aggiornamenti | Onboarding con `/second-brain:onboarding`, aggiornabile |
| [B. Zip](#b-zip) | Non usi git, o vuoi tutto in una cartella tua | Stessa cosa, da una cartella sul tuo computer |
| [C. Solo catalogo](#c-solo-catalogo-senza-plugin) | Vuoi solo leggere e copiare qualche pezzo | Schede e pacchetti, niente onboarding |

Prima di tutto serve **Claude Code installato, con il login fatto**. Per l'onboarding non serve altro; alcuni pacchetti usano script Python 3, e il loro LEGGIMI lo dice. Se non ce l'hai ancora, guarda [Prima di iniziare](#prima-di-iniziare).

---

## A. Plugin dal marketplace (da GitHub)

Dentro Claude Code scrivi:

```text
/plugin marketplace add fixerdigitale/second-brain-kit
/plugin install second-brain@second-brain-kit
```

Poi riavvia Claude Code (chiudi e riapri la sessione) e scrivi:

```text
/second-brain:onboarding
```

oppure, a parole, «avvia l'onboarding».

**Aggiornare.** `/plugin marketplace update second-brain-kit`, poi riapri la sessione.
**Togliere.** `/plugin uninstall second-brain@second-brain-kit` e, se vuoi, `/plugin marketplace remove second-brain-kit`. I file che l'onboarding ha creato nelle tue cartelle restano: li togli tu, se vuoi.

## B. Zip

1. Sulla pagina della repo: **Code → Download ZIP**.
2. Estrai lo zip in una cartella che non cancellerai, per esempio dentro Documenti: sul disco quella cartella si chiama quasi sempre `Documents`, anche con il sistema in italiano. Meglio non usare Scrivania o Download.
3. Apri Claude Code e aggiungi la cartella come marketplace locale, scrivendo il percorso dove l'hai estratta:
   ```text
   /plugin marketplace add ~/Documents/second-brain-kit
   /plugin install second-brain@second-brain-kit
   ```
   Su Windows il percorso è del tipo `C:\Users\<tuo-nome>\Documents\second-brain-kit`, oppure `C:\Users\<tuo-nome>\OneDrive\Documenti\second-brain-kit` se Windows tiene Documenti dentro OneDrive (in Esplora file, clic destro sulla cartella → «Copia come percorso»).
4. Riavvia la sessione e scrivi «avvia l'onboarding» oppure `/second-brain:onboarding`.

Per aggiornare scarica lo zip nuovo in una cartella nuova, poi ripeti il punto 3 con il nuovo percorso. Non cancellare la vecchia finché quella nuova non funziona.

## C. Solo catalogo, senza plugin

Non serve installare niente.

1. Leggi l'[indice del catalogo](../catalogo/README.md) e scegli una scheda.
2. Ogni scheda con un pacchetto rimanda al suo `LEGGIMI.md` in `pacchetti/<nome>/`: lì c'è cosa fa, dove si copia e come si toglie.
3. Copia solo quello che ti serve. Se vuoi, chiedi a Claude Code: «leggi `pacchetti/<nome>/LEGGIMI.md` e aiutami a installarlo qui, chiedendomi prima di ogni modifica».

Prima di copiare un hook o uno script, leggilo: gira sul tuo computer con i tuoi permessi.

---

## Prima di iniziare

### Mac

1. Apri il Terminale e installa Claude Code con il comando che trovi nella [documentazione ufficiale](https://docs.claude.com/en/docs/claude-code/setup).
2. Scrivi `claude` e fai il login.
3. Se vuoi clonare la repo invece di scaricare lo zip serve git: il Mac te lo propone la prima volta che scrivi `git`.

### Windows

1. Installa [Git per Windows](https://git-scm.com/downloads/win): Claude Code lo usa anche se tu non usi git.
2. Installa Claude Code seguendo la [documentazione ufficiale](https://docs.claude.com/en/docs/claude-code/setup) (PowerShell oppure WSL).
3. Apri un nuovo terminale, scrivi `claude` e fai il login.
4. Gli script dei pacchetti sono in Python: per usarli serve Python 3 (da python.org). Quando un pacchetto vuole qualcosa di diverso su Windows, il suo LEGGIMI lo dice.

### Linux (anche un server)

1. Usa un utente normale, non root.
2. Installa Claude Code dalla [documentazione ufficiale](https://docs.claude.com/en/docs/claude-code/setup), scrivi `claude` e fai il login.
3. Su un server: accesso SSH con chiave e nessuna porta nuova aperta per il kit. L'onboarding non ne ha bisogno.

## Dove usarlo

### Terminale

```bash
cd second-brain-kit
claude
```

### VS Code

1. Installa l'estensione **Claude Code** dal marketplace di VS Code.
2. **File → Apri cartella** e scegli la cartella dove lavori (o quella del kit).
3. Apri il pannello di Claude Code e scrivi i comandi della strada A o B.

Se nella tua versione dell'estensione il comando `/plugin` non c'è, apri il terminale integrato di VS Code, scrivi `claude`, installa il plugin da lì e poi torna al pannello.

### App desktop

1. Apri l'app Claude e passa alla sezione **Code**.
2. Scegli come cartella di lavoro quella dove lavori (o quella del kit).
3. Scrivi i comandi della strada A o B.

Se `/plugin` non risponde, installa il plugin una volta dal terminale come nella strada A: il plugin installato vale per il tuo utente, quindi lo ritrovi anche nell'app.

---

## Se qualcosa non va

- **«marketplace not found» o errore di rete.** Controlla di aver scritto `fixerdigitale/second-brain-kit` e che il computer raggiunga GitHub. In alternativa usa la strada B.
- **Il comando `/second-brain:onboarding` non compare.** Riapri la sessione dopo l'installazione e scrivi `/plugin` per vedere se `second-brain` è attivo.
- **Un errore che non capisci.** Copialo tutto in Claude Code e chiedi di spiegartelo prima di fare qualsiasi cosa.

Non incollare mai password, chiavi o token nella chat.
