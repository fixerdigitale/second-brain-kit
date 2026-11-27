#!/usr/bin/env python3
"""Ponte telefono: un lavoro lungo chiede l'ok sul telefono e riparte da solo quando rispondi.

    python3 ponte_telefono.py configura                  crea ~/.claude/ponte/config.json con un argomento casuale
    python3 ponte_telefono.py chiedi <id> "<domanda>" [--cartella DIR]
                                                         manda la domanda al telefono (con i bottoni Sì / No)
    python3 ponte_telefono.py giro [--prova]             legge le risposte e fa ripartire Claude Code (--prova: registra le risposte, non lancia)
    python3 ponte_telefono.py rispondi <id> "<testo>"    risposta data dal PC (o per le prove)
    python3 ponte_telefono.py stato                      elenco delle domande

Canali:
  - "ntfy": notifiche push con l'app gratuita ntfy (https://ntfy.sh, o un server ntfy tuo).
    La domanda arriva con due bottoni; per una risposta libera pubblichi sull'argomento delle
    risposte un messaggio «<codice> <testo>».
  - "file": niente rete, per le prove. Le domande vanno in ~/.claude/ponte/uscita/, le risposte
    si leggono da ~/.claude/ponte/risposte-finte.txt (una riga «<codice> <testo>»).

Ogni domanda ha un codice casuale: una risposta senza il codice giusto si ignora.
Una ripartenza alla volta; la domanda è segnata «in ripartenza» prima del lancio, così non
riparte due volte per la stessa risposta. Se trova semaforo.py (accanto o in ~/.claude/semaforo/) e dice stop, aspetta.
Solo libreria standard. Mac, Windows, Linux.
"""
import argparse
import json
import os
import secrets
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

CARTELLA = Path.home() / ".claude" / "ponte"
CONFIG = CARTELLA / "config.json"
DOMANDE = CARTELLA / "domande.json"
LOCK = CARTELLA / "ripartenza.lock"
QUI = Path(__file__).resolve().parent
PROMPT = """Riprendi il lavoro «{id}», che si era fermato per chiedermi un ok.
La domanda era: {domanda}
La mia risposta, dal telefono: {risposta}

Prima leggi HANDOFF.md in questa cartella (lì c'è lo stato e il prossimo passo).
Se la risposta è un no o una correzione, non andare avanti sul piano vecchio: aggiorna HANDOFF.md e fermati.
Se ti serve un altro ok, aggiorna HANDOFF.md e usa di nuovo: python3 "{script}" chiedi <id-nuovo> "<domanda>" --cartella "{cartella}".
Niente invii a terzi senza un ok esplicito sul testo esatto."""


def carica(p, vuoto):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return vuoto


def salva(p, dati):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(dati, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, p)


def config():
    c = carica(CONFIG, None)
    if not c:
        sys.exit("Manca la configurazione: lancia prima «ponte_telefono.py configura».")
    return c


def richiesta(c, url, dati=None, intestazioni=None):
    h = dict(intestazioni or {})
    if c.get("token"):
        h["Authorization"] = "Bearer " + c["token"]
    req = urllib.request.Request(url, data=dati, headers=h, method="POST" if dati is not None else "GET")
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "replace")


def manda(c, codice, testo):
    if c["canale"] == "file":
        (CARTELLA / "uscita").mkdir(parents=True, exist_ok=True)
        (CARTELLA / "uscita" / f"{codice}.txt").write_text(testo, encoding="utf-8")
        return
    base = c["server"].rstrip("/")
    risposte = f"{base}/{c['argomento']}-risposte"
    azioni = (f"http, Sì, {risposte}, method=POST, body={codice} sì, clear=true; "
              f"http, No, {risposte}, method=POST, body={codice} no, clear=true")
    richiesta(c, f"{base}/{c['argomento']}", testo.encode("utf-8"),
              {"Title": f"Serve il tuo ok ({codice})", "Actions": azioni, "Priority": "high"})


def risposte_arrivate(c, dal):
    """Restituisce una lista di (testo, momento)."""
    if c["canale"] == "file":
        f = CARTELLA / "risposte-finte.txt"
        if not f.exists():
            return []
        righe = [r.strip() for r in f.read_text(encoding="utf-8").splitlines() if r.strip()]
        f.unlink()
        return [(r, time.time()) for r in righe]
    base = c["server"].rstrip("/")
    testo = richiesta(c, f"{base}/{c['argomento']}-risposte/json?poll=1&since={int(dal)}")
    out = []
    for riga in testo.splitlines():
        try:
            m = json.loads(riga)
        except ValueError:
            continue
        if m.get("event") == "message" and m.get("message"):
            out.append((m["message"].strip(), m.get("time", time.time())))
    return out


def configura(a):
    if CONFIG.exists():
        print(f"Esiste già {CONFIG}: lo lascio com'è.")
        return
    c = {"canale": a.canale, "server": "https://ntfy.sh",
         "argomento": "ponte-" + secrets.token_urlsafe(18).replace("_", "").replace("-", "")[:24],
         "ultimo_giro": time.time()}
    salva(CONFIG, c)
    print(f"Creato {CONFIG}.")
    if a.canale == "ntfy":
        print("Nell'app ntfy del telefono iscriviti all'argomento scritto nel file (chiave «argomento»).")
        print("Non scriverlo in chat e non condividerlo: chi lo conosce legge le domande.")


def chiedi(a):
    c = config()
    dom = carica(DOMANDE, {})
    if a.id in dom:
        sys.exit(f"L'id «{a.id}» esiste già: usane uno nuovo.")
    codice = secrets.token_hex(2)
    testo = a.domanda.strip()[:3500]
    dom[a.id] = {"codice": codice, "domanda": testo, "cartella": str(Path(a.cartella).resolve()),
                 "stato": "in_attesa", "chiesta": time.time()}
    manda(c, codice, f"{testo}\n\nRispondi con i bottoni, oppure «{codice} <testo>».")
    salva(DOMANDE, dom)
    print(f"Domanda «{a.id}» mandata (codice {codice}). Ora puoi fermarti: riparto quando risponde.")


def rispondi_locale(a):
    dom = carica(DOMANDE, {})
    d = dom.get(a.id)
    if not d or d["stato"] != "in_attesa":
        sys.exit("Nessuna domanda in attesa con questo id.")
    d.update(stato="risposta", risposta=a.testo, risposta_il=time.time())
    salva(DOMANDE, dom)
    print("Risposta registrata: riparte al prossimo giro.")


def semaforo_rosso():
    candidati = [QUI / "semaforo.py", Path.home() / ".claude" / "semaforo" / "semaforo.py"]
    s = next((c for c in candidati if c.exists()), None)
    if not s:
        return False
    return subprocess.run([sys.executable, str(s)], capture_output=True).returncode == 1


def giro(a):
    c = config()
    dom = carica(DOMANDE, {})
    per_codice = {d["codice"]: k for k, d in dom.items() if d["stato"] == "in_attesa"}
    for testo, quando in risposte_arrivate(c, c.get("ultimo_giro", time.time()) - 60):
        codice, _, resto = testo.partition(" ")
        k = per_codice.get(codice.strip().lower())
        if k:
            dom[k].update(stato="risposta", risposta=resto.strip() or "(vuota)", risposta_il=quando)
    c["ultimo_giro"] = time.time()
    salva(CONFIG, c)
    salva(DOMANDE, dom)
    pronte = [k for k, d in dom.items() if d["stato"] == "risposta"]
    if not pronte:
        print("Nessuna risposta nuova.")
        return
    if LOCK.exists() and time.time() - LOCK.stat().st_mtime < 3 * 3600:
        print("Una ripartenza è già in corso: le altre al prossimo giro.")
        return
    if semaforo_rosso():
        print("Semaforo dei consumi rosso: riparto al prossimo giro.")
        return
    k = pronte[0]
    d = dom[k]
    prompt = PROMPT.format(id=k, domanda=d["domanda"], risposta=d["risposta"],
                           script=Path(__file__).resolve(), cartella=d["cartella"])
    if a.prova:
        print(f"Farei ripartire «{k}» in {d['cartella']} con questo prompt:\n\n{prompt}")
        return
    d["stato"] = "in_ripartenza"
    salva(DOMANDE, dom)
    LOCK.write_text(k)
    try:
        claude = a.claude or shutil.which("claude") or "claude"
        r = subprocess.run([claude, "-p", prompt, "--permission-mode", "acceptEdits"], cwd=d["cartella"],
                           capture_output=True, text=True, encoding="utf-8", timeout=3 * 3600)
        d["stato"] = "ripartita" if r.returncode == 0 else "errore"
        d["esito"] = (r.stdout or r.stderr)[-1500:]
    except (OSError, subprocess.TimeoutExpired) as e:
        d["stato"], d["esito"] = "errore", str(e)
    finally:
        LOCK.unlink(missing_ok=True)
        salva(DOMANDE, dom)
    print(f"«{k}»: {d['stato']}")


def stato(_a):
    for k, d in carica(DOMANDE, {}).items():
        print(f"{d['stato']:<14} {k:<24} {time.strftime('%d/%m %H:%M', time.localtime(d['chiesta']))}  {d['domanda'][:60]}")


def main():
    p = argparse.ArgumentParser(description="Ok dal telefono e ripartenza automatica.")
    sub = p.add_subparsers(dest="comando", required=True)
    s = sub.add_parser("configura"); s.add_argument("--canale", choices=["ntfy", "file"], default="ntfy"); s.set_defaults(f=configura)
    s = sub.add_parser("chiedi"); s.add_argument("id"); s.add_argument("domanda"); s.add_argument("--cartella", default="."); s.set_defaults(f=chiedi)
    s = sub.add_parser("rispondi"); s.add_argument("id"); s.add_argument("testo"); s.set_defaults(f=rispondi_locale)
    s = sub.add_parser("giro"); s.add_argument("--prova", action="store_true"); s.add_argument("--claude"); s.set_defaults(f=giro)
    s = sub.add_parser("stato"); s.set_defaults(f=stato)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
