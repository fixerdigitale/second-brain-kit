#!/usr/bin/env python3
"""Salva l'ultima lettura dei limiti dell'abbonamento, da usare come riga di stato.

Claude Code passa alla riga di stato (statusLine) un JSON che, nelle versioni recenti e con un
abbonamento Pro/Max, contiene `rate_limits` (finestra di 5 ore e settimana, con percentuale e
reset). Questo script ne salva una copia in ~/.claude/limiti-ultimi.json e poi:
  - se dopo `--` gli dai un altro comando (per esempio la tua riga di stato), gli passa lo
    stesso JSON e stampa quello che stampa lui;
  - altrimenti stampa una riga corta: «5 ore 31% · settimana 12%».

Esempio in settings.json:
  "statusLine": {"type": "command",
                 "command": "python3 \"$HOME/.claude/semaforo/registra_limiti.py\""}

Solo libreria standard. Non blocca mai: in caso di errore stampa «Claude».
"""
import json
import os
import subprocess
import sys
import time

FILE = os.path.join(os.path.expanduser("~"), ".claude", "limiti-ultimi.json")


def salva(limiti, fonte):
    dati = {"ts": int(time.time()), "fonte": fonte}
    for chiave in ("five_hour", "seven_day"):
        v = limiti.get(chiave) or {}
        if v.get("used_percentage") is not None:
            dati[chiave] = {"used_percentage": float(v["used_percentage"]), "resets_at": v.get("resets_at")}
    if len(dati) <= 2:
        return False
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    tmp = FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(dati, f)
    os.replace(tmp, FILE)
    return True


def main():
    grezzo = sys.stdin.read()
    try:
        d = json.loads(grezzo or "{}")
    except ValueError:
        d = {}
    limiti = d.get("rate_limits") or {}
    salva(limiti, "riga di stato")
    if "--" in sys.argv:
        comando = sys.argv[sys.argv.index("--") + 1:]
        r = subprocess.run(comando, input=grezzo, capture_output=True, text=True, timeout=5)
        print(r.stdout.rstrip("\n"))
        return
    pezzi = []
    for chiave, nome in (("five_hour", "5 ore"), ("seven_day", "settimana")):
        p = (limiti.get(chiave) or {}).get("used_percentage")
        if p is not None:
            pezzi.append(f"{nome} {round(p)}%")
    print(" · ".join(pezzi) or "Claude")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Claude")
