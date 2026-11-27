# MEMORY.md compatto con le Regole d'oro

**Cosa fa.** Un indice della memoria automatica di Claude Code in due parti:
1. **Regole d'oro** (massimo 20): il testo della regola è nell'indice, quindi Claude la legge sempre.
2. **Per tema**: solo i nomi dei file, raggruppati. Claude apre il file quando il tema è pertinente.

Perché: Claude Code carica solo l'inizio di MEMORY.md (circa 200 righe / 25 KB). Con un indice
«una riga per file» oltre i 200 file le righe in fondo spariscono senza avviso.

**Dove si copia.** Nella cartella della memoria del progetto:
- Mac/Linux: `~/.claude/projects/<nome-cartella-del-progetto>/memory/MEMORY.md`
- Windows: `C:\Users\<tu>\.claude\projects\<nome-cartella-del-progetto>\memory\MEMORY.md`

Il nome della cartella è il percorso del progetto con i separatori sostituiti da trattini. Se la memoria
automatica non c'è ancora, chiedi a Claude «ricordati che…» una volta: crea lui la cartella.
Se hai già un MEMORY.md, non sovrascriverlo: copiane la struttura a mano.

**Come si prova.** Sessione nuova, chiedi «quali sono le tue regole d'oro?». Dovrebbe elencarle senza aprire file.

**Come si toglie.** Rimetti il tuo MEMORY.md di prima (fanne una copia prima di cambiarlo).

**Regola del tetto.** Quando una regola entra, controlla di non superare 20. Il tetto serve: se tutte
sono d'oro, nessuna lo è. Per me è la parte più difficile: tendo a sforarlo, e ogni tanto sfoltisco spostando le regole meno usate in CLAUDE.md o nel loro tema.

## English

A compact `MEMORY.md` structure for Claude Code's automatic memory, which only loads the first ~200 lines. Two parts: "Golden Rules" (the rule text written in the index, capped at 20, always read) and "By topic" (only file names grouped by subject, opened when relevant), plus a "To sort" group for new corrections.

Install: copy the structure of `MEMORY.md` into your project's memory folder (`~/.claude/projects/<project-folder-name>/memory/`). If you already have a MEMORY.md, back it up and reorganize it by hand.
