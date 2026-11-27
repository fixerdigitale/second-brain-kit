#!/usr/bin/env python3
"""Quanto tempo passi con Claude su ogni task, contato dagli hook.

La task attiva si sceglie in due modi:
  - nel messaggio a Claude: scrivi «#task <nome>» (per esempio «#task landing-corso»). Vale per
    quella sessione finché non ne scrivi un'altra; «#task fine» la chiude;
  - a mano, per una cartella: python3 registro_tempo.py task "<nome>"  (dalla cartella del lavoro).
Senza task, il tempo va sotto il nome della cartella.

Come hook (UserPromptSubmit, PostToolUse, Stop):
    python3 registro_tempo.py segna
  Aggiunge una riga a ~/.claude/registro-tempo.jsonl: ora, sessione, cartella, task. Niente testi.

Riepilogo:
    python3 registro_tempo.py riepilogo            (ultimi 7 giorni)
    python3 registro_tempo.py riepilogo 30         (ultimi 30 giorni)
  Per ogni giorno e task somma i tratti fra due segni a meno di 15 minuti: una pausa più lunga
  non conta. Due sessioni in parallelo sulla stessa task non raddoppiano il tempo.

Solo libreria standard. Mac, Windows, Linux. Come hook non stampa niente e non blocca mai.
"""
import collections
import datetime
import json
import os
import re
import sys
import time

BASE = os.path.join(os.path.expanduser("~"), ".claude")
REGISTRO = os.path.join(BASE, "registro-tempo.jsonl")
ATTIVE = os.path.join(BASE, "task-attive.json")  # {"sessione:<id>": task, "cartella:<percorso>": task}
PAUSA_MAX = 15 * 60  # secondi
TAG = re.compile(r"#task\s+([\w.\-/àèéìòù]+)", re.I)


def leggi_attive():
    try:
        with open(ATTIVE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def salva_attive(a):
    os.makedirs(BASE, exist_ok=True)
    tmp = ATTIVE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(a, f, ensure_ascii=False)
    os.replace(tmp, ATTIVE)


def segna():
    try:
        dati = json.load(sys.stdin)
    except ValueError:
        dati = {}
    sessione, cartella = dati.get("session_id"), dati.get("cwd") or os.getcwd()
    attive = leggi_attive()
    m = TAG.search(dati.get("prompt") or "")
    if m and sessione:
        if m.group(1).lower() == "fine":
            attive.pop(f"sessione:{sessione}", None)
        else:
            attive[f"sessione:{sessione}"] = m.group(1)
        salva_attive(attive)
    task = attive.get(f"sessione:{sessione}") or attive.get(f"cartella:{cartella}")
    riga = {"ts": int(time.time()), "sessione": sessione, "cartella": cartella, "task": task,
            "evento": dati.get("hook_event_name")}
    os.makedirs(BASE, exist_ok=True)
    with open(REGISTRO, "a", encoding="utf-8") as f:
        f.write(json.dumps(riga, ensure_ascii=False) + "\n")


def imposta_cartella(nome):
    attive = leggi_attive()
    chiave = f"cartella:{os.getcwd()}"
    if nome.lower() == "fine":
        attive.pop(chiave, None)
        print("Nessuna task per questa cartella.")
    else:
        attive[chiave] = nome
        print(f"Task «{nome}» per {os.getcwd()}")
    salva_attive(attive)


def riepilogo(giorni):
    limite = time.time() - giorni * 86400
    per_chiave = collections.defaultdict(list)
    try:
        with open(REGISTRO, encoding="utf-8") as f:
            for r in f:
                try:
                    d = json.loads(r)
                except ValueError:
                    continue
                if d.get("ts", 0) < limite:
                    continue
                giorno = datetime.date.fromtimestamp(d["ts"]).isoformat()
                chiave = d.get("task") or "(senza task) " + os.path.basename(str(d.get("cartella", "?")).rstrip("/\\"))
                per_chiave[(giorno, chiave)].append(d["ts"])
    except OSError:
        print("Nessun registro ancora:", REGISTRO)
        return
    for (giorno, chiave), tempi in sorted(per_chiave.items()):
        tempi.sort()
        s = sum(b - a for a, b in zip(tempi, tempi[1:]) if b - a <= PAUSA_MAX)
        if s >= 60:
            print(f"{giorno}  {s // 3600:>2}h {s % 3600 // 60:02d}m  {chiave}")


if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else ""
    if comando == "segna":
        try:
            segna()
        except Exception:
            pass
    elif comando == "task" and len(sys.argv) > 2:
        imposta_cartella(sys.argv[2])
    elif comando == "riepilogo":
        riepilogo(int(sys.argv[2]) if len(sys.argv) > 2 else 7)
    else:
        print(__doc__)
