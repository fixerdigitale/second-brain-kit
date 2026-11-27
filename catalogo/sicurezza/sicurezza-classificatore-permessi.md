---
slug: sicurezza-classificatore-permessi
titolo: Quando Claude viene bloccato, si ferma e chiede
area: sicurezza
dove_gira: PC
livello: base
costo: 0 €. 2 minuti.
pacchetto: pacchetti/sicurezza-classificatore-permessi/
stato: lo uso
---
# Quando Claude viene bloccato, si ferma e chiede

**Il problema.** Nella modalità automatica Claude Code ha un controllo che a volte nega un'azione a rischio, per esempio un rilascio in produzione, un timer permanente o una scrittura sul server di un cliente, anche quando in chat ho già detto sì. La tentazione, per Claude, è trovare un'altra strada per fare la stessa cosa.

**Come l'ho risolto.** Ho una regola fissa. Se un'azione viene negata, Claude si ferma e mi dice cosa voleva fare e perché. Se do l'ok scritto nominando l'azione precisa, non un «sì» generico, riprova una volta lo stesso comando identico. Se viene negato di nuovo, mi propone una regola di permesso o mi dà il comando da lanciare io. Niente giri: altro strumento, comando spezzato, file rinominato. In più tiene le azioni che cambiano qualcosa in un comando separato dalle letture, così se viene negato si capisce perché.

**Perché così.** Il blocco è un secondo paio d'occhi, e aggirarlo vuol dire spegnerlo. Ho visto che un ok che nomina l'azione esatta di solito passa, mentre un ok generico a una lista di consigli no.

**Quando ti serve.** Se usi la modalità automatica o lasci lavorare Claude a lungo da solo su cose che toccano produzione o clienti.

**Quando non ti serve.** Se lavori sempre con le richieste di permesso manuali, approvi tu ogni passo e la regola serve poco.

**Come prenderlo.** Incolla `regola-claude-md.md` in `~/.claude/CLAUDE.md`. Istruzioni: [LEGGIMI](../../pacchetti/sicurezza-classificatore-permessi/LEGGIMI.md).
