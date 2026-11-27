---
name: piano-upgrade
description: >
  Fase 5 dell'onboarding del second brain: dal catalogo «tutto quello che uso io, come opzione»
  sceglie al massimo 3 passi per la persona, in ordine fisso (non perdere, non rispiegare, non
  rifare, delegare), e scrive second-brain/PIANO-UPGRADE.md e .html con la tabella oggi / fra 14
  giorni. Usala dentro l'onboarding dopo la MAPPA, alla rimisura, o quando la persona chiede «cosa
  potrei aggiungere?», «cosa mi consigli dal catalogo?», «what should I add next?».
---

# Piano di upgrade

Scopo: dal catalogo, solo i passi che servono a questa persona adesso. Al massimo 3. Contro il
«biliardo» di possibilità, l'ordine è fisso.

## Dove sta il catalogo

1. **Indice** (sempre presente): `${CLAUDE_PLUGIN_ROOT}/catalogo-indice.json`. Per ogni scheda:
   `slug`, `titolo`, `area_onboarding`, `gruppo_piano`, `dove_gira`, `livello`, `tono_minimo`,
   `costo`, `stato_da_me`, `pacchetto`, `scheda` (percorso nella repo), `scheda_en` e `titolo_en`
   (versione inglese), `problema`, `quando_non_serve`, `segni_che_ce_l_hai`. Con lingua `en` usa
   `titolo_en` e apri `scheda_en` (cartella `catalog/`); se manca, la scheda italiana.
2. **Schede intere e pacchetti** stanno nella repo del kit, nelle cartelle `catalogo/` e
   `pacchetti/`. Per trovare la repo prova in quest'ordine, con Glob:
   - `${CLAUDE_PLUGIN_ROOT}/../../catalogo/` (plugin usato da una copia della repo);
   - `~/.claude/plugins/marketplaces/*/catalogo/memoria/memoria-claude-md-a-sezioni.md` (plugin
     installato dal marketplace: la repo è la cartella sopra `catalogo/`);
   - in `~/.claude/plugins/known_marketplaces.json` il campo `installLocation` del marketplace del
     kit (con l'installazione da cartella o da zip la repo sta lì, fuori da `marketplaces/`): cerca
     `catalogo/` dentro quel percorso. Leggi solo quel campo;
   - chiedi alla persona dove ha scaricato la repo del kit.
   Se non la trovi, lavora dall'indice e dillo: «la scheda intera non ce l'ho sul PC».
3. Le cose provate e lasciate, con il motivo, sono in `catalogo/scartati.md`: aprile se la persona
   chiede «e X? l'hai provato?».

## 1. Filtra le schede

Leggi da `stato.json`: `tono`, `ritmo`, `aree`, `saltati`, `missioni`, `primo_risultato`,
`pezzo_ripetibile`. Leggi da `MAPPA.md` le prove e «Dove si inceppa».

Per ogni scheda decidi una sola etichetta:

| Etichetta | Quando |
|---|---|
| **ce l'hai** | `studia` ha trovato i `segni_che_ce_l_hai`, completi |
| **ce l'hai, migliorabile** | segni trovati in parte, o la cosa c'è ma è ferma da più di 90 giorni |
| **adatta** | non ce l'ha, il tono basta (`tono_minimo` ≤ tono), l'area non è «non serve adesso», e la sua situazione non è quella di `quando_non_serve` |
| **non adesso** | tutto il resto: tono troppo alto, `dove_gira: server` senza un computer sempre acceso, `PC acceso` se la persona spegne il PC (`pc_acceso_di_notte: false` nello stato; se non lo sai, chiedilo prima di scegliere), area che non le serve, già saltata da lei |

`dove_gira: server` si propone solo se la persona ha o vuole un computer sempre acceso; in quel
caso dillo chiaro: «ha senso solo con un computer sempre acceso; qui c'è solo l'idea, non un
pacchetto». Con `T0` proponi solo `livello: base`.

Chi non ha nessuna copia fuori dal PC ha sempre almeno un passo che la crea: `sicurezza-copia-settimanale`
(base, funziona anche a PC spento) oppure `sicurezza-backup-notturno` se il PC resta acceso (su Mac basta
che vada in stop invece di spegnersi: launchd fa al risveglio il giro saltato; a Mac spento no). `sicurezza-prova-ripristino` ha senso solo
quando una copia c'è già: senza copia è «non adesso».

## 2. Scegli al massimo 3 passi, in ordine fisso

Vai per gruppi, in quest'ordine, e fermati a 3. **Al massimo 2 passi dallo stesso gruppo**: il terzo
viene dal gruppo dopo, così il piano non è fatto solo di sicurezza. Unica eccezione, l'emergenza:
una chiave già finita online **e** nessuna copia fuori dal PC; allora possono essere 3 passi «non
perdere», e lo dici.

1. **Non perdere** (`1-non-perdere`: backup, segreti, permessi). Entra **sempre per primo** se
   l'area Sicurezza e ripristino è a 0-1, se c'è una chiave in chiaro, se il backup non si
   ripristina o se il repository del backup è pubblico.
2. **Non rispiegare** (`2-non-rispiegare`: contesto, memoria, correzioni, ricerca). Prima l'area con
   il voto più basso.
3. **Non rifare** (`3-non-rifare`: skill e procedure). Prima quella che rende ripetibile il primo
   risultato, se la fase 3 ha messo solo il pezzo minimo.
4. **Delegare** (`4-delegare`: agenti, canali, automazioni). Solo se i primi tre gruppi sono a posto
   (aree a 2 o più) o «non servono adesso».

Dentro un gruppo, a parità: prima la scheda legata a una frase della persona o a un numero di «Dove
si inceppa», poi `livello: base`, poi quella con il pacchetto (si installa davvero) prima di quella
«solo idea». Non riproporre niente che la persona ha saltato in passato (`saltati`), salvo alla
rimisura e una volta sola.

Con `T3`, prima di scegliere, una domanda: «Cosa hai già provato e lasciato perdere, e perché?»
(EN: «What have you already tried and dropped, and why?»). Quello che dice non si ripropone.

Per chi ha già un vault (`T3` con vault): per ogni passo scrivi il confronto «tu hai X, la scheda
aggiunge Y, costa Z», e adatta la scheda alla sua struttura (i suoi cassetti, il formato delle sue
note). Niente migrazioni.

## 3. Per ogni passo, questi campi

- **La riga del perché**, prima degli altri campi: «**Non hai** <X>. **Significa che** <conseguenza,
  con un numero>. **Potresti** <azione> **perché** <beneficio misurabile>.» (EN: «**You don't have**
  … **It means** … **You could** … **because** …»). È la stessa forma della MAPPA.
- **Link alla scheda:** `[<slug>](<repo>/catalogo/<famiglia>/<slug>.md)` con il percorso vero della
  repo trovata (in inglese `catalog/`). In T0 nel testo va il titolo della scheda; lo slug solo nel
  link fra parentesi.
- **Tempo:** minuti per metterlo, dal campo `costo` della scheda o dal LEGGIMI del pacchetto. Se è
  una tua stima, scrivi «stima».
- **Costo abbonamento:** `basso` se sono file, script o regole che non chiamano un modello da soli;
  `medio` se c'è un giro programmato o un agente che consuma (revisore notturno, coda della notte,
  agenti). Il costo in euro, se la scheda lo dice, accanto.
- **Numero che sposta:** una delle misure della mappa, da oggi all'atteso, per esempio «giorni
  dall'ultimo backup verificato: da mai a 0».
- **Come si annulla:** il «come si toglie» del pacchetto (file da cancellare, riga da togliere) e il
  link a `${CLAUDE_PLUGIN_ROOT}/guide/05-tornare-indietro.md`.
- **Perché ora:** una riga, con la prova («2 chiavi in chiaro in `appunti/api.md:3`»).

## 4. Scrivi il PIANO

1. Usa `modelli/PIANO-UPGRADE.md` (o `modelli/en/PIANO-UPGRADE.md`). Data di oggi; «Rimisura dal»
   = oggi + 14 giorni.
2. «I tuoi output di oggi»: i file in `second-brain/output/`, il pezzo della fase 3, i minuti del
   primo risultato.
3. «Tabella oggi / fra 14 giorni»: le misure della mappa; nella colonna «fra 14 giorni» il valore
   atteso se i 3 passi si fanno, scritto come atteso.
4. «Il resto del catalogo»: le schede `adatta` non scelte, una riga ciascuna (titolo e slug), poi le
   `ce l'hai` e `ce l'hai, migliorabile`. Le `non adesso` non si elencano, si dice quante sono.
5. Fai rileggere il testo al sotto-agente `revisore`. Correggi. Poi scrivi
   `second-brain/PIANO-UPGRADE.md` e `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/pagina.py"
   second-brain/PIANO-UPGRADE.md --lingua <it|en>`.
6. Stato: `piano.data`, `piano.file`, `piano.rimisura_dal`, `piano.passi` (lista di
   `{"scheda": "<slug>", "missione": "<id della missione di installa, se diverso>", "titolo":
   "<breve>", "minuti": N}`). Il campo `missione` serve alla riga di ripresa: per esempio
   `sicurezza-permessi-deny-ask` si fa con la missione `regole-deny`.

## 5. In chat

Mostra i 3 passi in breve, nel tono giusto (T0: a parole, una riga ciascuno, senza slug; T2-T3:
tabella). Poi
una domanda: «Partiamo dal primo? Ci vogliono circa N minuti.» / «Shall we start with the first?
About N minutes.» Se la persona dice di no, va bene: il piano resta lì.

## Errori da evitare

- Più di 3 passi, più di 2 dallo stesso gruppo (fuori dall'emergenza), o passi fuori dall'indice.
- Saltare l'ordine (per esempio un agente prima del backup quando il backup manca).
- Proporre una scheda che la persona ha già, solo con un altro nome: va fra «ce l'hai».
- Scrivere «devi»: è un'opzione, la decide lei.
