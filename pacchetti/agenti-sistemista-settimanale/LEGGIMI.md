# Sistemista settimanale (sola lettura)

**Cosa fa.** Una volta a settimana controlla che il vault sia davvero al sicuro: backup su GitHub e Drive, repo privata, una prova di ripristino, segreti finiti per sbaglio nei commit, programmi vecchi. Non corregge niente: ti dà OK, PROBLEMA o NON VERIFICABILE per ogni punto, con le prove.

**Dove si copia.** `.claude/agents/sistemista.md` → `~/.claude/agents/sistemista.md`. Sostituisci i segnaposto: `<cartella-vault>`, `<utente>/<repo-vault>`, `<url-repo>`, `<cartella-drive>`, `<cartella-temporanea>`.

**Come si lancia.**
- A mano, una volta a settimana: in Claude Code «lancia il sistemista».
- In automatico (gira solo a PC acceso): un'attività pianificata del sistema che esegue
  `claude -p "lancia il sotto-agente sistemista e scrivi il verdetto in <cartella-vault>/controlli/<data>.md"`.
  Su Windows con l'Utilità di pianificazione, su Mac con launchd o un promemoria. Nota: per scrivere il file del verdetto serve il permesso di scrittura in quella cartella; il sotto-agente resta in sola lettura e il file lo scrive la sessione.

**Facoltativi.** `gh` (GitHub CLI) per verificare che la repo sia privata; `gitleaks` per la ricerca dei segreti. Senza, il controllo funziona lo stesso e segna quei punti «non verificabile».

**Come si prova.** Lancialo una volta: il punto 4 deve dire quante note ha ripristinato rispetto all'originale.

**Come si toglie.** Cancella il file e l'eventuale attività pianificata.

## English

A read-only weekly check-up sub-agent: vault pushed to GitHub and in sync, repo private, Drive folder up to date, a restore test in a temporary folder, suspicious words in commit history (never showing values), files that shouldn't be in the repo, very old programs. Each item comes back OK, PROBLEM or NOT VERIFIABLE.

Install: copy `.claude/agents/sistemista.md` into `~/.claude/agents/` and replace the placeholders (vault, repo, Drive). Run it by hand once a week, or schedule `claude -p` with your OS scheduler. Optional: `gh` and `gitleaks`. Read-only is enforced by instructions, not technically, since it uses Bash.
