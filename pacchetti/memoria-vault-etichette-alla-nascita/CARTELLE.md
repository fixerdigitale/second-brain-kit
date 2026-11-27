# Schema delle cartelle del vault

<cartella-vault>/
├── Clienti/       una nota per cliente (fatti stabili + «## Dalle sessioni»)
├── Progetti/      una nota per progetto interno o di un cliente
├── Decisioni/     una nota per decisione importante (data, cosa, perché, alternative scartate)
├── Risorse/       guide, procedure, riferimenti riusabili
├── Fatti/AAAA-MM/ diario dei fatti di giornata (facoltativo, se usi una raccolta automatica)
├── Fonti/         materiale grezzo: trascrizioni di call, esportazioni, copie di HANDOFF
└── _Stato.md      cosa è aperto adesso, letto all'inizio di ogni sessione

Etichette nel frontmatter di ogni nota (vedi `nota-modello.md`):
- `entita`: a quale cliente o progetto si riferisce (serve per cercare e per filtrare);
- `livello`: operativo / economico / personale (serve per decidere cosa mostrare a chi);
- `visibile_a`: chi può leggerla. Se un giorno dai accesso a un collaboratore, filtri su questo campo.
