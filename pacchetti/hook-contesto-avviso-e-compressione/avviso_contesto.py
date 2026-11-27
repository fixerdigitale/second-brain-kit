#!/usr/bin/env python3
"""Hook UserPromptSubmit per Claude Code: avvisa quando il contesto della sessione cresce troppo.

Legge la coda del transcript, prende l'ultima risposta dell'assistente e somma i token di
contesto (input + cache letta + cache scritta). Sopra SOGLIA_AVVISO aggiunge, una sola volta
per sessione, un avviso al contesto del modello; sopra SOGLIA_ALTA lo aggiunge a ogni turno.
Il modello lo legge e te lo riferisce in una riga.

Solo libreria standard. Funziona su Mac, Windows e Linux. Non blocca mai niente:
qualsiasi errore = nessun avviso.
"""
import json
import os
import sys
import tempfile

# Soglie in token. Cambiale qui. Con una finestra da 200k, 120k/170k sono un buon inizio.
SOGLIA_AVVISO = int(os.environ.get("AVVISO_CONTESTO_SOGLIA", "120000"))
SOGLIA_ALTA = int(os.environ.get("AVVISO_CONTESTO_ALTA", "170000"))
CODA_BYTE = 3_000_000  # legge solo la fine del transcript: veloce anche su sessioni enormi
VISTI = os.path.join(tempfile.gettempdir(), "claude-avviso-contesto")


def prima_volta(sessione, chiave):
    """True la prima volta che vediamo (sessione, chiave); poi False."""
    if not sessione:
        return True
    segno = os.path.join(VISTI, f"{sessione}.{chiave}")
    if os.path.exists(segno):
        return False
    try:
        os.makedirs(VISTI, exist_ok=True)
        open(segno, "w").close()
    except OSError:
        pass
    return True


def ultima_risposta(percorso):
    try:
        with open(percorso, "rb") as f:
            f.seek(0, os.SEEK_END)
            f.seek(max(0, f.tell() - CODA_BYTE))
            righe = f.read().decode("utf-8", "ignore").splitlines()
    except OSError:
        return None
    for riga in reversed(righe):
        try:
            d = json.loads(riga)
        except ValueError:
            continue
        m = d.get("message") or {}
        # salta le risposte dei sotto-agenti: contano solo quelle della conversazione principale
        if d.get("type") == "assistant" and m.get("usage") and not d.get("isSidechain"):
            return m
    return None


def main():
    try:
        dati = json.load(sys.stdin)
    except ValueError:
        return
    m = ultima_risposta(dati.get("transcript_path", ""))
    if not m:
        return
    u = m["usage"]
    contesto = (u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                + u.get("cache_creation_input_tokens", 0))
    k = contesto // 1000
    sessione = dati.get("session_id")

    avviso = None
    if contesto >= SOGLIA_ALTA:
        avviso = (f"AVVISO CONTESTO: la sessione è a {k}k token, vicina alla compressione automatica. "
                  "Prima di continuare aggiorna HANDOFF.md del progetto (stato, decisioni, prossimo passo) "
                  "e dillo all'utente in una riga.")
    elif contesto >= SOGLIA_AVVISO and prima_volta(sessione, "avviso"):
        avviso = (f"AVVISO CONTESTO: la sessione è a {k}k token. Ogni messaggio rilegge tutto: "
                  "affida letture lunghe e ricerche a un sotto-agente, e dillo all'utente in una riga.")
    if avviso:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": avviso}}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # un hook non deve mai fermare il lavoro
