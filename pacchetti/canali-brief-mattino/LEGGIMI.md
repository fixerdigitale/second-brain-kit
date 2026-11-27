# Brief del mattino (skill)

**Cosa fa.** Legge il tuo vault (task, HANDOFF, note delle call, calendario se hai il connettore)
e scrive un messaggio corto in quattro parti: la cosa di oggi, chi aspetta, cosa è in ritardo e
conta, cosa serve da te. Lo salva in `<cartella-vault>/brief/AAAA-MM-GG.md`.

**Dove si copia.** La cartella `brief-mattino/` in `~/.claude/skills/brief-mattino/`
(Windows: `%USERPROFILE%\.claude\skills\brief-mattino\`). Apri `SKILL.md` e sostituisci
`<cartella-vault>` e i nomi dei file con quelli tuoi (es. se i task stanno in `Progetti/*/task.md`).

**Come si prova.** In Claude Code, dentro VS Code, aperto sulla cartella del vault: scrivi
`/brief-mattino`. Controlla che citi la fonte di ogni fatto e che non inventi date.

**Se lo vuoi in automatico la mattina (solo a PC acceso).**
- Windows, Utilità di pianificazione: azione `claude`, argomenti `-p "/brief-mattino"`,
  cartella di avvio = la cartella del vault, ogni giorno feriale alle 08:00.
- Mac: `crontab -e` e una riga `0 8 * * 1-5 cd <cartella-vault> && claude -p "/brief-mattino"`.
Se il PC è spento alle 08:00 il brief salta: lo lanci a mano quando accendi.

**Come si toglie.** Cancella la cartella `~/.claude/skills/brief-mattino/` (e l'attività
pianificata, se l'hai creata).

## English

A `brief-mattino` skill that writes a morning brief from your vault: the most important thing today, who's waiting and for how long (with draft replies), the delays that really hurt, the decisions that need you. At most five pending items, each with done / drop / postpone.

Install: copy `brief-mattino/` into `~/.claude/skills/brief-mattino/` and adapt the vault paths. Run it with `/brief-mattino`, or schedule it at 8 am with Task Scheduler (Windows) or cron (Mac); it only runs while the PC is on. The skill text is in Italian.
