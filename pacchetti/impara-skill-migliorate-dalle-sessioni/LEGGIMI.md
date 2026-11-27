# Skill che migliorano leggendo le sessioni (le adotti tu)

**Cosa fa.** Di notte uno strumento legge le tue sessioni recenti di Claude Code, trova i lavori
che ripeti, li rigioca con e senza una modifica alla skill e propone la modifica solo se passa un
controllo su compiti tenuti da parte. La proposta resta in attesa: la skill cambia solo quando la
adotti tu.

Lo strumento non è mio: è **SkillOpt-Sleep**, parte del progetto pubblico SkillOpt di Microsoft
(licenza MIT): https://github.com/microsoft/SkillOpt (documentazione: `docs/sleep/README.md`).
Io lo uso con l'abbonamento Claude, mai con chiavi a consumo, e con l'adozione automatica spenta.
Questo pacchetto contiene solo la mia configurazione d'esempio e il modo in cui lo tengo sotto controllo.

**Cosa ho visto finora.** Da quando le proposte mi arrivano da approvare, su 7 notti: 1 adottata,
1 scartata da me, 2 senza proposta perché il controllo non è passato, le altre ritirate o in
attesa. Quindi non aspettarti una skill nuova ogni mattina: spesso la risposta giusta è «niente».

**Richiede.** Python 3.10 o più, Claude Code già collegato al tuo abbonamento, il PC acceso di
notte. Il giro consuma quota dell'abbonamento: per questo ha un tetto di token per notte.

**Dove si copia.**
1. Installa: `pip install skillopt` (versione su PyPI). Alcune opzioni più nuove, come
   `preferences`, secondo la documentazione richiedono l'installazione dal sorgente.
2. Copia `config-esempio.json` in `~/.skillopt-sleep/config.json` e adattalo:
   - `auto_adopt: false` è il punto che conta: niente si adotta da solo;
   - `max_tokens_per_night` e `max_tasks_per_night` tengono basso il consumo;
   - `preferences`: le regole che le proposte non devono violare (le tue regole fisse).
3. Prima prova senza scrivere niente: `skillopt-sleep dry-run` nella cartella del progetto.
4. Se ti convince, `skillopt-sleep schedule` mette il giro di notte.

**Come decidi.** Al mattino `skillopt-sleep status` mostra l'ultima proposta. Leggila tutta.
Se va bene: `skillopt-sleep adopt --legacy` (o `--skill NOME` per una sola skill). Se no, non
fare niente: resta lì e la notte dopo ne arriva un'altra.

**Attenzione ai dati.** Con un modello vero il giro manda pezzi delle tue sessioni al fornitore
del modello (qui Anthropic, lo stesso che usi già). La documentazione dice che l'oscuramento dei
segreti è una difesa in più, non una garanzia. Non usarlo su progetti con dati che hai promesso
di non far uscire, e lascia `redact_secrets: true`.

**Come si prova.** Non l'ho provato su un PC: da me gira su un server, con la configurazione da
cui è preso l'esempio. Il primo passo sicuro è il `dry-run`, che non mette in attesa niente.

**Come si toglie.** Togli il giro notturno che `schedule` ha creato (su Mac e Linux è una riga
di cron: `crontab -e`; su Windows un'attività pianificata), poi `pip uninstall skillopt` e
cancella `~/.skillopt-sleep/`.

## English

My example configuration for SkillOpt-Sleep (part of Microsoft's open source SkillOpt): at night it reads recent sessions, replays recurring tasks with and without a skill change, and proposes the change only if it improves on held-out tasks. In my configuration automatic adoption is off: every proposal waits for your approval.

Install: `pip install skillopt` from https://github.com/microsoft/SkillOpt, start from `config-esempio.json` and follow the steps above to try it first without writing anything. It uses subscription quota at night, and pieces of your sessions go to the model provider: don't use it on projects with data you promised not to share.
