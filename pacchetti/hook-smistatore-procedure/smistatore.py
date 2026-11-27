#!/usr/bin/env python3
"""Hook UserPromptSubmit per Claude Code: riconosce dalle parole il tipo di lavoro che chiedi
e ricorda a Claude la procedura scritta per quel lavoro (una volta per sessione e per procedura).

Le procedure stanno in procedure.json, accanto a questo file:
  [
    {"nome": "Landing page",
     "parole": ["landing", "pagina di vendita", "sito"],
     "file": "<cartella-vault>/procedure/landing.md"}
  ]

Facoltativo: se accanto c'è promemoria.txt e il messaggio sembra un lavoro (fai, crea, sistema…),
una volta per sessione aggiunge anche quel testo (per esempio: «prima di cominciare segui la skill
smistamento»), così la regia si ricorda di decidere chi fa il lavoro.

Indovina dalle parole: è un promemoria, non un ordine. Claude lo dice e chiede se vale.
Solo libreria standard. Mac, Windows, Linux. Ogni errore = nessun effetto.
"""
import json
import os
import re
import sys
import tempfile
import unicodedata

PROCEDURE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "procedure.json")
PROMEMORIA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "promemoria.txt")
VISTI = os.path.join(tempfile.gettempdir(), "claude-smistatore")
VERBI_LAVORO = ["fai", "fammi", "crea", "scrivi", "prepara", "sistema", "aggiorna", "costruisci",
                "rifai", "correggi", "implementa", "aggiungi", "togli", "migra", "riordina"]


def normalizza(t):
    t = unicodedata.normalize("NFKD", t.lower())
    return "".join(c for c in t if not unicodedata.combining(c))


def contiene(testo, parola):
    return re.search(r"\b" + re.escape(normalizza(parola)) + r"\b", testo) is not None


def prima_volta(sessione, chiave):
    segno = os.path.join(VISTI, f"{sessione or 'x'}.{re.sub(r'[^a-z0-9]+', '-', normalizza(chiave))}")
    if os.path.exists(segno):
        return False
    os.makedirs(VISTI, exist_ok=True)
    open(segno, "w").close()
    return True


def main():
    dati = json.load(sys.stdin)
    testo = (dati.get("prompt") or "").strip()
    if not testo or testo.startswith(("/", "<")):  # comandi e messaggi automatici
        return
    norm = normalizza(testo)
    with open(PROCEDURE, encoding="utf-8") as f:
        procedure = json.load(f)
    righe = []
    for p in procedure:
        if any(contiene(norm, w) for w in p.get("parole", [])) and prima_volta(dati.get("session_id"), p["nome"]):
            righe.append(f"- {p['nome']}: {p['file']}")
    pezzi = []
    if righe:
        pezzi.append("PROCEDURA POSSIBILE (indovinata dalle parole, da verificare):\n" + "\n".join(righe) +
                     "\nSe una vale per questa richiesta, leggila e seguila, e dillo all'utente in una riga. "
                     "Se non c'entra, ignora questo avviso.")
    if (os.path.exists(PROMEMORIA) and any(contiene(norm, v) for v in VERBI_LAVORO)
            and prima_volta(dati.get("session_id"), "promemoria-regia")):
        with open(PROMEMORIA, encoding="utf-8") as f:
            pezzi.append(f.read().strip())
    if pezzi:
        avviso = "\n\n".join(p for p in pezzi if p)
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                                 "additionalContext": avviso}}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
