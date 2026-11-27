#!/usr/bin/env python3
"""board.py - una board di task in un file, con stima, tempo vero e chi ci lavora adesso.

Uso:
    python3 board.py nuova "Bozza preventivo" --stima 45 --progetto clienti/x --fonte "call del 12/11"
    python3 board.py inizia T-3 --chi claude      # passa In corso, segna chi ci lavora adesso
    python3 board.py pausa T-3                    # somma i minuti al tempo vero, toglie «adesso»
    python3 board.py fatta T-3                    # come pausa, poi Fatto
    python3 board.py tempo T-3 20                 # aggiunge 20 minuti a mano (call, lavoro fuori)
    python3 board.py elenco                       # mostra la board

I dati stanno in task.json; ogni comando riscrive TASK.md, la vista da leggere (anche dal telefono,
se la cartella si sincronizza). Cartella di serie: quella da cui lanci il comando, oppure --cartella.
La stima non si tocca mai da sola: il tempo vero si conta a parte, così a fine mese vedi la differenza.
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

STATI = ["Da fare", "In corso", "Fatto"]
MAX_MINUTI_TRATTO = 240   # un «inizia» dimenticato aperto non diventa una giornata intera
GIORNI_FERMA = 3          # In corso senza movimento da più giorni = ferma


def ora():
    return dt.datetime.now().replace(microsecond=0)


def carica(cartella: Path) -> dict:
    f = cartella / "task.json"
    if not f.exists():
        return {"prossimo": 1, "task": []}
    return json.loads(f.read_text(encoding="utf-8"))


def salva(cartella: Path, dati: dict) -> None:
    tmp = cartella / "task.json.tmp"
    tmp.write_text(json.dumps(dati, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(cartella / "task.json")
    (cartella / "TASK.md").write_text(vista(dati), encoding="utf-8")


def trova(dati: dict, ident: str) -> dict:
    for t in dati["task"]:
        if t["id"].lower() == ident.lower():
            return t
    sys.exit(f"Task {ident} non trovata.")


def chiudi_tratto(t: dict) -> int:
    if not t.get("inizio"):
        return 0
    minuti = int((ora() - dt.datetime.fromisoformat(t["inizio"])).total_seconds() // 60)
    minuti = max(0, min(minuti, MAX_MINUTI_TRATTO))
    t["tempo_vero"] += minuti
    t["inizio"] = None
    t["adesso"] = ""
    return minuti


def vista(dati: dict) -> str:
    righe = ["# Board", "", f"_Aggiornata {ora():%d/%m/%Y %H:%M}. Non modificare a mano: usa board.py._", ""]
    for stato in STATI:
        task = [t for t in dati["task"] if t["stato"] == stato]
        righe += [f"## {stato} ({len(task)})", ""]
        if not task:
            righe += ["(nessuna)", ""]
            continue
        righe += ["| ID | Titolo | Progetto | Stima | Tempo vero | Adesso | Fonte |", "|---|---|---|---|---|---|---|"]
        for t in task:
            adesso = f"● {t['adesso']}" if t.get("adesso") else ""
            mosso = dt.datetime.fromisoformat(t["mossa"])
            if stato == "In corso" and not adesso and (ora() - mosso).days >= GIORNI_FERMA:
                adesso = f"ferma da {(ora() - mosso).days} giorni"
            righe.append(f"| {t['id']} | {t['titolo']} | {t['progetto']} | {t['stima']} min | {t['tempo_vero']} min | {adesso} | {t['fonte']} |")
        righe.append("")
    return "\n".join(righe)


def main():
    p = argparse.ArgumentParser(description="Board di task in un file")
    p.add_argument("--cartella", default=".", help="dove stanno task.json e TASK.md")
    sub = p.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("nuova")
    n.add_argument("titolo")
    n.add_argument("--stima", type=int, required=True, help="minuti")
    n.add_argument("--progetto", default="")
    n.add_argument("--fonte", default="", help="da dove nasce: call, messaggio, link")
    for nome in ("inizia", "pausa", "fatta"):
        s = sub.add_parser(nome)
        s.add_argument("id")
        if nome == "inizia":
            s.add_argument("--chi", default="io", help="io, claude, il nome di chi ci lavora")
    t = sub.add_parser("tempo")
    t.add_argument("id")
    t.add_argument("minuti", type=int)
    sub.add_parser("elenco")
    a = p.parse_args()

    cartella = Path(a.cartella).expanduser()
    cartella.mkdir(parents=True, exist_ok=True)
    dati = carica(cartella)

    if a.cmd == "nuova":
        ident = f"T-{dati['prossimo']}"
        dati["prossimo"] += 1
        dati["task"].append({"id": ident, "titolo": a.titolo.replace("|", "/"), "progetto": a.progetto,
                             "stima": a.stima, "tempo_vero": 0, "stato": "Da fare", "adesso": "",
                             "inizio": None, "fonte": a.fonte.replace("|", "/"), "mossa": ora().isoformat()})
        print(f"Creata {ident}.")
    elif a.cmd == "inizia":
        task = trova(dati, a.id)
        for altra in dati["task"]:          # una persona lavora su una task alla volta
            if altra is not task and altra.get("adesso") == a.chi:
                print(f"{altra['id']}: in pausa, +{chiudi_tratto(altra)} min.")
        chiudi_tratto(task)
        task.update(stato="In corso", adesso=a.chi, inizio=ora().isoformat(), mossa=ora().isoformat())
        print(f"{task['id']} in corso ({a.chi}).")
    elif a.cmd in ("pausa", "fatta"):
        task = trova(dati, a.id)
        minuti = chiudi_tratto(task)
        task["mossa"] = ora().isoformat()
        if a.cmd == "fatta":
            task["stato"] = "Fatto"
        print(f"{task['id']}: +{minuti} min, tempo vero {task['tempo_vero']} su {task['stima']} stimati.")
    elif a.cmd == "tempo":
        task = trova(dati, a.id)
        task["tempo_vero"] += a.minuti
        task["mossa"] = ora().isoformat()
        print(f"{task['id']}: tempo vero {task['tempo_vero']} min.")
    salva(cartella, dati)
    if a.cmd == "elenco":
        print(vista(dati))


if __name__ == "__main__":
    main()
