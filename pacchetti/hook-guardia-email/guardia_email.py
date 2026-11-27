#!/usr/bin/env python3
"""Hook PreToolUse per Claude Code: i tuoi indirizzi email non escono verso siti terzi.

Perché: Claude vede l'email del tuo account nelle istruzioni di partenza e a volte la mette da
solo in un User-Agent, in un header o in un URL quando chiama un sito. Questa guardia:
- WebFetch / WebSearch: indirizzo nell'URL o nella ricerca -> bloccato;
- Bash: indirizzo + comando di rete (curl, wget, http://…) verso un host che non è nella lista
  dei tuoi -> chiede conferma a te;
riconosce l'indirizzo anche codificato nell'URL (%40) o in base64.

Gli indirizzi stanno in indirizzi_email.txt (uno per riga), accanto a questo file: nel codice
non ce n'è nessuno. Gli host dove l'email può andare (Google, il tuo dominio…) in HOST_AMMESSI.
Solo libreria standard. Mac, Windows, Linux. Se qualcosa va storto lascia passare.
"""
import base64
import json
import os
import re
import sys
from urllib.parse import unquote_plus

CARTELLA = os.path.dirname(os.path.abspath(__file__))
INDIRIZZI = os.path.join(CARTELLA, "indirizzi_email.txt")
# Aggiungi qui i tuoi domini e i servizi dove usi quell'email.
HOST_AMMESSI = ("localhost", "127.0.0.1", "google.com", "googleapis.com", "github.com")
RETE = re.compile(r"\b(?:curl|wget|httpie|Invoke-WebRequest|iwr)\b|https?://|requests\.|urllib|fetch\(", re.I)
HOST = re.compile(r"https?://([^/\s\"':?#]+)", re.I)


def indirizzi():
    try:
        with open(INDIRIZZI, encoding="utf-8") as f:
            return [r.strip().lower() for r in f if "@" in r and not r.startswith("#")]
    except OSError:
        return []


def varianti(email):
    b64 = base64.b64encode(email.encode()).decode().rstrip("=")
    return [email, b64[:-2] if len(b64) > 8 else b64]


def contiene_email(testo, lista):
    t = testo.lower()
    piano = unquote_plus(testo).lower()
    for e in lista:
        if e in t or e in piano:
            return True
        if varianti(e)[1] in testo:
            return True
    return False


def host_esterni(testo):
    return [h.lower() for h in HOST.findall(testo)
            if not any(h.lower() == a or h.lower().endswith("." + a) for a in HOST_AMMESSI)]


def decidi(decisione, motivo):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "permissionDecision": decisione,
                                             "permissionDecisionReason": motivo}}, ensure_ascii=False))


def main():
    dati = json.load(sys.stdin)
    lista = indirizzi()
    if not lista:
        return
    strumento = dati.get("tool_name") or ""
    entrata = dati.get("tool_input") or {}
    if strumento in ("WebFetch", "WebSearch"):
        testo = " ".join(str(entrata.get(k, "")) for k in ("url", "query", "prompt"))
        if contiene_email(testo, lista) and (strumento == "WebSearch" or host_esterni(testo)):
            decidi("deny", "GUARDIA EMAIL: l'indirizzo email dell'utente non va mandato a un sito terzo. "
                           "Rifai la richiesta senza l'indirizzo.")
        return
    if strumento == "Bash":
        cmd = entrata.get("command") or ""
        if RETE.search(cmd) and contiene_email(cmd, lista) and (host_esterni(cmd) or "$" in cmd):
            decidi("ask", "GUARDIA EMAIL: questo comando manda l'indirizzo email dell'utente in rete. "
                          "Confermi? Di solito basta togliere l'indirizzo (es. User-Agent generico).")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
