# Riordino di HANDOFF e SISTEMA

**Cosa fa.** Due pezzi:
1. `prompt-riordino.md`: il testo da dare a Claude per portare i fatti stabili da HANDOFF.md a SISTEMA.md.
   Lo incolli in chat (o lo salvi come comando, vedi sotto) quando un progetto ha accumulato lavoro.
2. `archivia_handoff.py`: sposta in `HANDOFF-ARCHIVIO-AAAA-MM.md` le sezioni più vecchie quando HANDOFF.md
   supera 80 KB, finché torna a 60 KB. Tiene sempre almeno 3 sezioni, fa una copia datata, controlla che
   nessuna riga si perda. Senza `--applica` non scrive niente.

**Dove si copia.**
- `prompt-riordino.md` come comando: `~/.claude/commands/riordino.md` → in chat scrivi `/riordino`.
- `archivia_handoff.py` dove vuoi, fuori dalle cartelle dei progetti (es. `<tuo-progetto>/strumenti/`).

**Come si prova.**
`python3 archivia_handoff.py <cartella-progetto>` (Windows: `py archivia_handoff.py <cartella-progetto>`).
Su un HANDOFF sotto 80 KB risponde «Niente da fare». Per vederlo lavorare, provalo su una copia di un file lungo.

**Come si toglie.** Cancella i file. Gli archivi creati restano: sono testo normale.

**Differenza con il mio.** Da me lo fa un servizio sul server ogni notte alle 4:40, con Sonnet, senza chiedermi niente,
e scrive «(riordino gg/mm)» su ogni riga. Su un PC basta lanciarlo a mano quando serve (o con l'Utilità di pianificazione
di Windows / launchd sul Mac, ma solo a PC acceso).

## English

Two halves to keep HANDOFF files from swelling. `prompt-riordino.md` is a `/riordino` command that moves stable facts from new HANDOFF sections into SISTEMA.md (at most 12 lines, shown to you before applying). `archivia_handoff.py` moves the oldest sections of a HANDOFF over 80 KB into a monthly archive until it's back to 60 KB, checking no line is lost.

Install: save `prompt-riordino.md` as `~/.claude/commands/riordino.md` and use `/riordino` in the project folder. Run `python3 archivia_handoff.py <project-folder>` (dry run), then again with `--applica`.
