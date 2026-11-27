# 07 · Google con più account

## Il problema

Se lavori con più account Google (il tuo, quello di un'agenzia che ti ha dato un indirizzo sul suo dominio, quello di un cliente), il connettore Google di Claude di solito ne collega **uno solo**. Per gli altri serve un'altra strada.

## La strada: gog

**gog** è un programma gratuito e open source che fa parlare Claude Code con Gmail, Drive, Fogli, Documenti, Presentazioni, Calendar, Contatti e altri servizi Google. Si installa una volta e ci colleghi **tutti gli account che vuoi**. In ogni comando si dice con quale account lavorare.

- Pagina del progetto: github.com/openclaw/gogcli
- Funziona su Windows, Mac e Linux.
- Le credenziali restano sul tuo computer, nel portachiavi del sistema (Gestione credenziali su Windows, Portachiavi su Mac).

Il pacchetto ha una skill, `google-account`, che insegna a Claude a usarlo bene: sempre l'account scritto nella nota del cliente, sola lettura quando basta leggere, email solo in bozza.

## L'installazione, in 5 passi

Fallo con Claude, un passo alla volta: «aiutami a installare gog seguendo la guida 07, un passo alla volta, e aspetta il mio ok a ogni passo». Ci vogliono circa 30 minuti la prima volta.

1. **Installa il programma.**
   - Windows: dalla pagina delle versioni (github.com/openclaw/gogcli/releases) si scarica lo ZIP `windows_amd64`, si estrae `gog.exe` in una cartella e la si aggiunge al percorso dei programmi. Claude lo fa per te, dopo averti detto dove lo mette.
   - Mac: con Homebrew, `brew install openclaw/tap/gogcli`.
   - Controllo: `gog --version` risponde con un numero di versione.
2. **Crea il tuo «progetto» Google** (una volta sola, con il tuo account personale): su console.cloud.google.com si crea un progetto, si attivano le API che servono (Gmail, Drive, Fogli, Documenti, Calendar: solo quelle che userai), si imposta la schermata di consenso come «Esterno» e si crea un **client OAuth di tipo Desktop**. Si scarica un file `client_secret_….json`. È la parte più lunga: Claude ti guida schermata per schermata.
3. **Dai il file a gog**: `gog auth credentials <percorso del file client_secret>`. Il file è una credenziale: non incollarne mai il contenuto in chat e non metterlo nella cartella di lavoro.
4. **Collega gli account, uno alla volta**: `gog auth add tuo@email.it --services gmail,drive,sheets,docs,calendar`. Si apre il browser, accedi con quell'account e dai il permesso. Poi lo stesso per l'account dell'agenzia o del cliente.
5. **Dai un nome corto a ogni account** e scrivilo nelle note dei clienti:
   ```bash
   gog auth alias set agenzia tuo@agenzia.it
   gog auth list
   ```
   Nella nota del cliente, sezione «Strumenti e account»: «Account Google: alias `agenzia` (tuo@agenzia.it)».

## Rendere l'accesso stabile

Se il progetto Google resta in modalità **«Testing»**, Google fa scadere l'accesso **ogni 7 giorni** e gli account vanno ricollegati. Per evitarlo: nella console Google, sezione **Audience** (Pubblico), premi **Publish app** e conferma. L'app passa «In production» senza revisione di Google: per un uso personale va bene. Poi ricollega gli account una volta con `gog auth add … --force-consent`.

## Se l'account dell'agenzia non si collega

Gli account aziendali (Google Workspace) possono avere regole dell'amministratore che bloccano le app esterne. Se Google ti dice che l'accesso è bloccato, non cercare altre strade: chiedi all'amministratore dell'agenzia di autorizzare l'app, o di condividere i file che ti servono con un account che hai già collegato.

## Sicurezza

- Per leggere, Claude usa `--readonly`: gog blocca qualunque modifica.
- Per le email usa `--gmail-no-send`: prepara bozze, le mandi tu.
- Prima di scrivere in un foglio di un cliente: copia o tabella «prima / dopo», e il tuo sì.
- Mai usare l'account di un cliente per il lavoro di un altro.

## Prova adesso (2 minuti)

Se gog è già installato: «elenca gli account Google collegati e dimmi quale usa ogni cliente secondo le note». Se non lo è: «leggi la guida 07 e dimmi cosa mi serve per installare gog, senza installare niente».
