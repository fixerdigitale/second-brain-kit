# Semaforo dei consumi e turno libero

**Cosa fa.** Tre file piccoli.
- `registra_limiti.py` fa da riga di stato di Claude Code e salva l'ultima lettura dei limiti
  dell'abbonamento (finestra di 5 ore e settimana) in `~/.claude/limiti-ultimi.json`.
- `semaforo.py` legge quella lettura e risponde con un codice: 0 verde, 1 stop, 2 «non lo so».
  Le soglie salgono man mano che il reset si avvicina: lontano dal reset lascia spazio a te,
  vicino si può spendere quello che resta. Con `margine` dice se nella settimana avanza quota
  che andrebbe persa.
- `turno_libero.py`, lanciato ogni 15 minuti: se non scrivi a Claude da 45 minuti e il semaforo
  dice che c'è margine, fa **un** lavoro della tua `CODA.md` e lo mette in `DA-RIVEDERE.md` con
  una casella sì/no. Un lavoro per giro, così il semaforo si richiede prima di ognuno.

Qualsiasi altro script lungo può chiedere al semaforo prima di partire:
`python3 semaforo.py || exit 0`.

Da me lo stesso semaforo legge i limiti da un servizio sul server ogni 5 minuti e ferma tutto:
code della notte, ripartenze dal telefono, lavori degli agenti. Sul PC la lettura arriva solo
dalla riga di stato (quando hai una sessione aperta) o dai lavori del turno libero.

**Richiede.** Abbonamento Claude Pro o Max, Claude Code in una versione che passa `rate_limits`
alla riga di stato (io l'ho verificato sulla 2.1.330), Python 3. Il PC acceso e sveglio quando
deve lavorare.

**Dove si copia.**
1. I tre file in `~/.claude/semaforo/`.
2. La chiave `statusLine` di `settings-esempio.json` in `~/.claude/settings.json`. Se hai già
   una riga di stato tua, mettila dopo `--`:
   `python3 "$HOME/.claude/semaforo/registra_limiti.py" -- python3 "$HOME/.claude/statusline.py"`.
3. Crea `CODA.md` in una cartella di lavoro (un `## titolo` e il brief sotto per ogni lavoro).
4. Pianifica `python3 ~/.claude/semaforo/turno_libero.py --cartella <cartella>` ogni 15 minuti
   (Utilità di pianificazione su Windows, launchd o cron su Mac).

Le soglie sono in cima a `semaforo.py` (`SOGLIE_5ORE`, `SOGLIE_SETTIMANA`, `RISERVA_PER_ORA`)
e i limiti del turno in cima a `turno_libero.py` (45 minuti di pausa, 6 lavori al giorno). Sono
i numeri che uso io: cambiali in base a quanto usi l'abbonamento tu.

**Limiti onesti.**
- Se la lettura è vecchia (più di 30 minuti) il semaforo risponde «non lo so». Il turno libero
  allora fa al massimo un lavoro al giorno «alla cieca» (`PARTI_SENZA_LETTURA`). Dopo quel
  lavoro prova ad aggiornare la lettura dagli eventi che `claude -p` scrive in uscita, ma non ho
  verificato che quegli eventi portino sempre la percentuale: se non la portano, il turno si
  ferma lì fino a quando riapri una sessione.
- In `claude -p` i comandi che chiedono permesso vengono negati: il brief deve chiedere lavori di
  lettura, riordino e bozze, mai invii.

**Come si prova (su dati finti).**
1. Lettura finta:
   `echo '{"rate_limits":{"seven_day":{"used_percentage":30,"resets_at":<secondi fra 2 giorni>}}}' | python3 registra_limiti.py`
2. `python3 semaforo.py; echo $?` → `VERDE` e 0. Rifai la lettura con 92: → `STOP` e 1.
3. Con un `claude` finto (uno script che stampa una riga `{"type":"result","result":"ok"}`)
   lancia `turno_libero.py --cartella <prova> --claude <finto> --prova`, poi senza `--prova`:
   in `CODA.md` il primo lavoro diventa `[fatto]`, in `notte/<data>/DA-RIVEDERE.md` c'è la casella.

Io l'ho provato così, con una home e un `claude` finti, il 27/11/2026. Non l'ho provato su Windows.

**Come si toglie.** Togli l'attività pianificata e la chiave `statusLine`. Cancella
`~/.claude/semaforo/`, `~/.claude/limiti-ultimi.json` e `~/.claude/turno-libero.json`.

## English

A usage traffic light for Claude subscriptions: it reads how much of the 5-hour window and of the week you've used and answers green, stop or "I don't know", with thresholds that rise as the weekly reset gets closer. Long jobs ask it before starting. A "free shift" runs one queued job when you've been idle for 45 minutes and weekly quota would otherwise be lost.

Install: copy `registra_limiti.py`, `semaforo.py` and `turno_libero.py` into `~/.claude/semaforo/`, set `registra_limiti.py` as your status line (see `settings-esempio.json`) and schedule `turno_libero.py` every 15 minutes. Works only while the PC is on and awake.
