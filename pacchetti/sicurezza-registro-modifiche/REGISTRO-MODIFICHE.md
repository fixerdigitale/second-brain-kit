# Registro delle modifiche — <nome-server-o-sistema>

Chi cambia qualcosa qui scrive una voce. Voci recenti in alto. Mai password, token o chiavi:
scrivi dove stanno, non cosa sono.

Prima di toccare un servizio, leggi le ultime 5 voci: magari qualcuno ci sta lavorando.

---

## AAAA-MM-GG HH:MM UTC — <titolo breve>

- **Chi**: <nome della persona> (con Claude Code / a mano / altro agente)
- **Cosa**: <file, servizio o impostazione cambiata, con il percorso>
- **Perché**: <richiesta o problema, con il link alla task se c'è>
- **Come tornare indietro**: <comando o passi; nome della copia datata se c'è>
- **Verificato**: <cosa hai controllato dopo, e l'esito>

---

## 2026-01-15 09:30 UTC — Esempio: alzato il limite di upload del sito

- **Chi**: Daniel, con Claude Code
- **Cosa**: `<percorso-config-web>` riga `client_max_body_size` da 10M a 50M
- **Perché**: il cliente non riusciva a caricare i video del corso
- **Come tornare indietro**: ripristinare `<file>.bak-20260115-upload` e ricaricare il servizio web
- **Verificato**: caricato un file da 40 MB, risposta 200
