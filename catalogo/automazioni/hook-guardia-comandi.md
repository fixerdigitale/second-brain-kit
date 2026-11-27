---
slug: hook-guardia-comandi
titolo: "Guardia che ferma i comandi sbagliati e spiega quelli giusti"
area: automazioni
dove_gira: PC
livello: medio
costo: "0 €. 20 minuti per scrivere e provare le prime regole."
pacchetto: "pacchetti/hook-guardia-comandi/"
stato: "versione per PC del mio"
---

# Guardia che ferma i comandi sbagliati e spiega quelli giusti

**Il problema.** Avevo una regola chiara: due agenti specialisti si lanciano solo su ChatGPT, con un comando preciso. Era scritta nelle istruzioni, nelle skill e in memoria, e Claude ogni tanto la sbagliava lo stesso.

**Come l'ho risolto.** Ho messo un hook PreToolUse che legge ogni comando prima che parta: se è il lancio sbagliato lo blocca e nel motivo scrive il comando giusto, già pronto. Claude legge e si corregge da solo. Da me registra anche ogni lancio: su 774 ne ha fermati 7. Per il PC ho scritto una versione generale: le regole stanno in un file JSON (strumento, espressione da cercare, eccezione, «ferma» o «chiedi conferma», messaggio con il modo giusto). Ci sono tre esempi: push forzati, cancellazioni ricorsive, scritture nei file .env.

**Perché così.** Una regola che dipende dalla memoria di Claude prima o poi si sbaglia, una regola in un hook no. Quello che la fa funzionare, per me, è il messaggio: se dice anche come si fa bene, Claude non riprova uguale, si corregge.

**Quando ti serve.** Quando hai una regola ripetuta più volte che Claude continua a sbagliare: comandi pericolosi, un modo preciso di fare il deploy, file da non toccare.

**Quando non ti serve.** Se le tue regole Claude le rispetta già. Per bloccare e basta, senza spiegare, bastano i permessi di settings.json (scheda [permessi](../sicurezza/sicurezza-permessi-deny-ask.md)). Le espressioni regolari vanno provate: una scritta male ferma comandi innocui.

**Come prenderlo.** Copia `guardia_comandi.py` e `regole_comandi.json` in `~/.claude/hooks/`, il blocco di `settings-esempio.json` in `~/.claude/settings.json`, poi riscrivi le regole con le tue. Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/hook-guardia-comandi/LEGGIMI.md).
