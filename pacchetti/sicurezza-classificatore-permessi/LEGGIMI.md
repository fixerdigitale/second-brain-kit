# Classificatore dei permessi: come mi comporto quando blocca

Nella modalità automatica di Claude Code un controllo valuta ogni azione e può negare quelle a rischio (rilasci in produzione, timer permanenti, modifiche alla propria configurazione, scritture su server remoti), anche quando tu hai già detto sì in chat. Questa regola dice a Claude cosa fare in quel caso.

## Dove si copia

Incolla `regola-claude-md.md` nel tuo `~/.claude/CLAUDE.md` (vale per tutti i progetti).

## Come si prova

Non serve forzarlo. La prossima volta che un'azione viene negata, controlla che Claude si fermi e ti spieghi invece di cercare un'altra via.

## Come si toglie

Togli il paragrafo dal `CLAUDE.md`.

## English

A rule for CLAUDE.md: when an action is denied by Claude Code's permission check, Claude stops and explains; with your written ok naming the exact action it retries the identical command once; if denied again it proposes a permission rule or gives you the command to run. No workarounds.

Install: paste `regola-claude-md.md` into `~/.claude/CLAUDE.md`.
