# Contesto operativo — <nome-della-tua-attività>

Rispondi sempre in italiano.

## Come rispondermi (sempre attivo)
<!-- Lo stile che vuoi in chat. Scrivi le regole per intero, non un rimando:
     questo file si legge a ogni sessione, una skill solo se viene aperta. -->
- Prima riga = la cosa da fare. Niente cortesie di servizio.
- Lavoro in più passi = lista numerata, un'azione per passo.
- Non comprimere mai: numeri, percorsi, comandi, messaggi di errore esatti, negazioni.
- Fuori dalla chat (codice, commit, documenti) si scrive normale.

## Dove operare
<!-- Dove stanno i progetti veri, cosa non si tocca, dove stanno i segreti (solo il percorso, mai i valori). -->
- Progetti: `<cartella-progetti>/`
- Vault delle note: `<cartella-vault>/`
- Da non toccare: `<cartella-delicata>/` (motivo in una riga)
- Segreti: `<file-dei-segreti>` — non stamparne mai i valori.

## Prima di dire «non ce l'ho»
<!-- Un file che elenca cosa esiste davvero (strumenti, account, script). Evita che Claude ricostruisca cose che hai già. -->
Leggi `<cartella-vault>/INVENTARIO.md` prima di costruire uno strumento nuovo.

## Memoria: dove va cosa
- Fatti su clienti e progetti → vault (`<cartella-vault>/Clienti/`, `<cartella-vault>/Progetti/`).
- Correzioni su come lavorare → memoria di Claude Code (`MEMORY.md` + un file per correzione).
- «Salva in memoria» = vault, sempre.

## Lavori in corso e passaggio di consegne
Se un lavoro lungo si interrompe, scrivi stato, file toccati, decisioni e prossimo passo
nell'`HANDOFF.md` del progetto prima di fermarti. Chi riprende lo legge per primo.
I fatti stabili di un cliente stanno in `SISTEMA.md`, che si corregge sul posto.

## Regole
<!-- Le regole che hai dovuto ripetere. Una riga ciascuna, con la data e, se serve, «ripetuta N volte».
     Quando una correzione torna la seconda volta, spostala qui dalla memoria. -->
- **<nome breve della regola> (dal gg/mm):** <la regola in una frase>. <perché, in mezza frase>.
- Prima di modificare un file di configurazione importante, fanne una copia con la data.
- Azioni difficili da annullare (pubblicare, inviare, cancellare): solo con il mio ok scritto in questa sessione.
