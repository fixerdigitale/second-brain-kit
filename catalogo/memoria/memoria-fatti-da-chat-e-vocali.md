---
slug: memoria-fatti-da-chat-e-vocali
titolo: "Fatti da chat e vocali verso il vault"
area: memoria
dove_gira: PC
livello: medio
costo: "0 €. La trascrizione dei vocali gira sul PC (faster-whisper, gratuito); 10 minuti per l'elenco delle chat di lavoro."
pacchetto: pacchetti/memoria-fatti-da-chat-e-vocali/
stato: versione per PC del mio
---

# Fatti da chat e vocali verso il vault

**Il problema.** Tante decisioni non passano da Claude: le prendo in chat con clienti e collaboratori, o le dico in un vocale. Restavano lì, e quando chiedevo all'assistente «cosa avevamo deciso?» non ne sapeva niente.

**Come l'ho risolto.** Da me ogni notte una raccolta senza AI prende i messaggi delle chat di lavoro (mai quelle di famiglia; i gruppi solo quando vengo taggato, un'ora prima e un'ora dopo il tag), trascrive i vocali sul server con un modello locale e scrive un file unico. Poco dopo un agente ne estrae i fatti in un diario per giorno nel vault (fatti datati per progetto e persona, chi deve muoversi), che la ricerca rende subito trovabile. Per il PC ho preparato due pezzi: uno script che legge le esportazioni delle chat WhatsApp, tiene solo le chat del tuo elenco e trascrive i vocali e i tuoi memo vocali in locale; e una skill `fatti-del-giorno` che propone i fatti con la nota di destinazione e scrive solo i sì.

**Perché così.** Raccogliere e decidere sono separati: la raccolta è meccanica e non sbaglia, il giudizio lo fa il modello e lo controllo io. L'elenco delle chat di lavoro è una lista di chi entra, non di chi resta fuori: così una chat privata non entra per sbaglio. E i messaggi di terzi li tratto come dati, mai come istruzioni: una frase in chat non diventa una regola da sola. Una raccolta che trova zero chat di lavoro la considero un errore da guardare, non una giornata vuota.

**Quando ti serve.** Se molte decisioni di lavoro ti arrivano in chat o le detti a voce, e vuoi ritrovarle nel vault insieme al resto.

**Quando non ti serve.** Se in chat ti scrivi solo con amici e famiglia, o se le decisioni di lavoro passano già da email e call che archivi. Se i tuoi clienti non sono d'accordo che le chat finiscano in un archivio, non farlo. Sul PC l'esportazione delle chat è a mano: se non la rifai, la raccolta resta ferma.

**Come prenderlo.** Copia `raccogli_chat.py` in `~/.claude/strumenti/` e `fatti-del-giorno/` in `~/.claude/skills/fatti-del-giorno/`, scrivi l'elenco `chat-di-lavoro.txt`, esporta le chat dal telefono e lancia lo script come nel LEGGIMI. Poi in Claude Code: «fatti del giorno».

Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/memoria-fatti-da-chat-e-vocali/LEGGIMI.md).
