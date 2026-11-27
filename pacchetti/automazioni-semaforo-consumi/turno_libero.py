#!/usr/bin/env python3
"""Turno libero: quando sei fermo e l'abbonamento ha quota che andrebbe persa, fa un lavoro della coda.

Da lanciare ogni 15 minuti con un'attività pianificata. A ogni giro:
  1. se un altro giro sta ancora lavorando, esce;
  2. se hai scritto a Claude negli ultimi INATTIVITA_MIN minuti, esce (il PC è tuo);
  3. chiede al semaforo: c'è margine nella settimana? nessuna soglia superata?
  4. se sì, prende il primo lavoro non fatto di CODA.md, lo fa con `claude -p`, salva il risultato
     e lo aggiunge a DA-RIVEDERE.md con una casella sì/no. Un lavoro per giro, così il semaforo
     si richiede prima di ognuno.

CODA.md, nella cartella che scegli:
    ## Titolo corto
    Brief completo: obiettivo, file, cosa consegnare. Niente invii a nessuno.

    python3 turno_libero.py --cartella <cartella>          un giro
    python3 turno_libero.py --cartella <cartella> --prova  dice cosa farebbe, non lancia niente

Solo libreria standard. Mac, Windows, Linux. Gira solo a PC acceso e sveglio.
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))
import semaforo  # noqa: E402

INATTIVITA_MIN = 45
MAX_LAVORI_GIORNO = 6
MAX_MINUTI_PER_LAVORO = 45
PARTI_SENZA_LETTURA = 1     # lavori permessi al giorno quando il semaforo «non sa» (lettura vecchia)
PROGETTI = Path.home() / ".claude" / "projects"
STATO = Path.home() / ".claude" / "turno-libero.json"


def leggi_stato():
    try:
        s = json.loads(STATO.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        s = {}
    oggi = dt.date.today().isoformat()
    if s.get("giorno") != oggi:
        s.update(giorno=oggi, lavori=0, senza_lettura=0)
    s.setdefault("sessioni_mie", [])
    return s


def salva_stato(s):
    STATO.parent.mkdir(parents=True, exist_ok=True)
    STATO.write_text(json.dumps(s), encoding="utf-8")


def minuti_da_ultimo_messaggio(mie):
    ultimo = 0.0
    for f in glob.glob(str(PROGETTI / "*" / "*.jsonl")):
        if Path(f).stem in mie:
            continue  # le sessioni dei turni liberi non contano come «sei al PC»
        try:
            ultimo = max(ultimo, os.stat(f).st_mtime)
        except OSError:
            pass
    return (time.time() - ultimo) / 60 if ultimo else 10**6


def primo_lavoro(coda):
    for blocco in re.split(r"^## ", coda.read_text(encoding="utf-8"), flags=re.M)[1:]:
        titolo, _, brief = blocco.partition("\n")
        if "[fatto]" not in titolo and brief.strip():
            return titolo.strip(), brief.strip()
    return None


def segna_fatto(coda, titolo):
    t = coda.read_text(encoding="utf-8").replace(f"## {titolo}\n", f"## {titolo} [fatto]\n", 1)
    coda.write_text(t, encoding="utf-8")


def salva_lettura_da_evento(info):
    """Un evento rate_limit_event di `claude -p` diventa una lettura per il semaforo (se ha i numeri)."""
    tipo, uso = info.get("rateLimitType"), info.get("utilization")
    if tipo not in ("five_hour", "seven_day") or uso is None:
        return
    perc = uso * 100 if uso <= 1 else uso
    vecchia = semaforo.leggi() or {}
    vecchia.update(ts=int(time.time()), fonte="turno libero")
    vecchia[tipo] = {"used_percentage": float(perc), "resets_at": info.get("resetsAt")}
    Path(semaforo.FILE).parent.mkdir(parents=True, exist_ok=True)
    Path(semaforo.FILE).write_text(json.dumps(vecchia), encoding="utf-8")


def esegui(claude, brief, cartella, s):
    cmd = [claude, "-p", brief, "--output-format", "stream-json", "--verbose", "--permission-mode", "acceptEdits"]
    r = subprocess.run(cmd, cwd=cartella, capture_output=True, text=True, encoding="utf-8",
                       timeout=MAX_MINUTI_PER_LAVORO * 60)
    testo, esito = "", "errore"
    for riga in r.stdout.splitlines():
        try:
            ev = json.loads(riga)
        except ValueError:
            continue
        if ev.get("session_id") and ev["session_id"] not in s["sessioni_mie"]:
            s["sessioni_mie"] = (s["sessioni_mie"] + [ev["session_id"]])[-200:]
        if ev.get("type") == "rate_limit_event":
            salva_lettura_da_evento(ev.get("rate_limit_info") or {})
        if ev.get("type") == "result":
            testo = ev.get("result") or ""
            esito = "ok" if not ev.get("is_error") else "errore"
    return esito, testo or r.stderr[-2000:]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cartella", required=True, help="dove stanno CODA.md e i risultati")
    p.add_argument("--prova", action="store_true")
    p.add_argument("--claude", default=shutil.which("claude") or "claude")
    a = p.parse_args()
    cartella = Path(a.cartella).expanduser()
    coda = cartella / "CODA.md"
    lock = cartella / ".turno-libero.lock"
    if lock.exists() and time.time() - lock.stat().st_mtime < (MAX_MINUTI_PER_LAVORO + 5) * 60:
        print("Un altro giro sta lavorando.")
        return 0
    s = leggi_stato()
    fermo = minuti_da_ultimo_messaggio(set(s["sessioni_mie"]))
    if fermo < INATTIVITA_MIN:
        print(f"Sei attivo da {fermo:.0f} minuti fa: non parto.")
        return 0
    if s["lavori"] >= MAX_LAVORI_GIORNO:
        print(f"Già {s['lavori']} lavori oggi: basta così.")
        return 0
    lavoro = primo_lavoro(coda) if coda.exists() else None
    if not lavoro:
        print("Coda vuota o mancante.")
        return 0
    sys.argv = ["semaforo", "margine"]
    margine = semaforo.main()
    sys.argv = ["semaforo"]
    luce = semaforo.main()
    if 1 in (margine, luce):
        print("Semaforo rosso o niente margine: non parto.")
        return 0
    if 2 in (margine, luce):
        if s["senza_lettura"] >= PARTI_SENZA_LETTURA:
            print("Il semaforo non sa e ho già usato il lavoro «alla cieca» di oggi: non parto.")
            return 0
        s["senza_lettura"] += 1
    titolo, brief = lavoro
    if a.prova:
        print(f"Farei: {titolo}")
        return 0
    lock.write_text(str(os.getpid()))
    try:
        esito, testo = esegui(a.claude, brief, cartella, s)
    except subprocess.TimeoutExpired:
        esito, testo = "errore", f"fermato dopo {MAX_MINUTI_PER_LAVORO} minuti"
    finally:
        lock.unlink(missing_ok=True)
    oggi = cartella / "notte" / dt.date.today().isoformat()
    oggi.mkdir(parents=True, exist_ok=True)
    nome = re.sub(r"[^a-zA-Z0-9]+", "-", titolo.lower()).strip("-")[:40] or "lavoro"
    (oggi / f"{nome}.md").write_text(f"# {titolo}\n\nEsito: {esito}\n\n{testo}\n", encoding="utf-8")
    with open(oggi / "DA-RIVEDERE.md", "a", encoding="utf-8") as f:
        f.write(f"- [ ] sì / no · {titolo} · {esito} · [{nome}.md]({nome}.md)\n")
    if esito == "ok":
        segna_fatto(coda, titolo)
    s["lavori"] += 1
    salva_stato(s)
    print(f"{titolo}: {esito}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
