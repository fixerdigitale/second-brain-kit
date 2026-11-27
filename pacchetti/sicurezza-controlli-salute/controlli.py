#!/usr/bin/env python3
"""Controlli di salute che avvisano solo quando lo stato cambia (rotto -> ok, ok -> rotto).

Guarda il RISULTATO, non se qualcosa è partito: un sito che risponde 200 ma con un file rotto,
un backup che "gira" ma il cui esito è vecchio di due giorni, un comando che esce con errore.

Uso:
  python3 controlli.py                 un giro: controlla, salva lo stato, avvisa solo sui cambi
  python3 controlli.py --prova         controlla e stampa, senza avvisare e senza salvare lo stato
  python3 controlli.py --config F      usa un altro file di controlli (di serie: controlli.json accanto)

Su Windows: py controlli.py
Solo libreria standard di Python 3. Mac, Windows e Linux.

Tipi di controllo in controlli.json:
  {"nome": "...", "tipo": "url", "url": "https://...", "file_collegati": true}
      la pagina deve rispondere 200; con file_collegati controlla anche script, css e immagini
      dello stesso dominio (una pagina a 200 con un .js a 404 per chi la apre è rotta).
  {"nome": "...", "tipo": "file_recente", "percorso": "...", "ore_max": 30, "contiene": "ESITO: OK"}
      il file deve esistere, essere più giovane di ore_max e (se indicato) contenere quel testo.
  {"nome": "...", "tipo": "comando", "comando": ["git", "-C", "...", "status"], "timeout": 60}
      il comando deve uscire con codice 0. È una lista: niente shell, niente sorprese con le virgolette.
"""
import argparse
import datetime
import json
import os
import pathlib
import platform
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

QUI = pathlib.Path(__file__).resolve().parent
UA = {"User-Agent": "Mozilla/5.0 controlli-salute"}


def leggi_url(u, timeout=20):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # rete giù, certificato scaduto, nome che non risolve...
        return 0, type(e).__name__.encode()


def controllo_url(c):
    codice, corpo = leggi_url(c["url"])
    if codice != 200:
        return False, f"risponde {codice or 'niente'}"
    if not c.get("file_collegati"):
        return True, "200"
    dominio = urllib.parse.urlparse(c["url"]).netloc
    html = corpo.decode("utf-8", "ignore")
    rotti = []
    for a in sorted(set(re.findall(r'(?:src|href)="([^"]+\.(?:js|css|woff2?|svg|png|jpe?g|webp)[^"]*)"', html))):
        pieno = urllib.parse.urljoin(c["url"], a)
        if urllib.parse.urlparse(pieno).netloc != dominio:
            continue
        cc, _ = leggi_url(pieno)
        if cc != 200:
            rotti.append(f"{a[:60]} → {cc}")
    if rotti:
        return False, "pagina 200 ma file rotti: " + "; ".join(rotti[:3])
    return True, "200, file collegati ok"


def controllo_file_recente(c):
    p = pathlib.Path(os.path.expanduser(c["percorso"]))
    if not p.is_file():
        return False, "il file non c'è"
    ore = (datetime.datetime.now().timestamp() - p.stat().st_mtime) / 3600
    if ore > float(c.get("ore_max", 30)):
        return False, f"vecchio di {ore:.0f} ore (massimo {c.get('ore_max', 30)})"
    atteso = c.get("contiene")
    if atteso and atteso not in p.read_text(encoding="utf-8", errors="ignore"):
        return False, f"non contiene «{atteso}»"
    return True, f"aggiornato {ore:.1f} ore fa"


def controllo_comando(c):
    try:
        r = subprocess.run(c["comando"], capture_output=True, text=True, timeout=int(c.get("timeout", 60)))
    except FileNotFoundError:
        return False, "comando non trovato"
    except subprocess.TimeoutExpired:
        return False, "troppo lento (timeout)"
    if r.returncode != 0:
        return False, f"uscito con codice {r.returncode}"
    return True, "ok"


TIPI = {"url": controllo_url, "file_recente": controllo_file_recente, "comando": controllo_comando}


def avvisa(testo):
    """Notifica del sistema. Il testo passa come argomento o variabile, mai dentro un comando."""
    sistema = platform.system()
    try:
        if sistema == "Darwin":
            subprocess.run(["osascript", "-e", "on run argv", "-e",
                            'display notification (item 1 of argv) with title "Controlli di salute"',
                            "-e", "end run", testo], timeout=20)
        elif sistema == "Windows":
            script = ("Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; "
                      "$n = New-Object System.Windows.Forms.NotifyIcon; "
                      "$n.Icon = [System.Drawing.SystemIcons]::Warning; $n.Visible = $true; "
                      "$n.ShowBalloonTip(15000, 'Controlli di salute', $env:AVVISO_TESTO, 'Warning'); "
                      "Start-Sleep -Seconds 16; $n.Dispose()")
            subprocess.run(["powershell", "-NoProfile", "-Command", script],
                           env={**os.environ, "AVVISO_TESTO": testo[:250]}, timeout=40)
        elif shutil.which("notify-send"):
            subprocess.run(["notify-send", "Controlli di salute", testo], timeout=20)
    except Exception:
        pass  # se la notifica non parte, resta la riga nel registro
    print("AVVISO: " + testo)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(QUI / "controlli.json"))
    ap.add_argument("--prova", action="store_true")
    a = ap.parse_args()

    config = json.loads(pathlib.Path(a.config).read_text(encoding="utf-8"))
    file_stato = pathlib.Path(os.path.expanduser(config.get("file_stato", str(QUI / "stato.json"))))
    registro = file_stato.with_name("registro.jsonl")
    prima = json.loads(file_stato.read_text(encoding="utf-8")) if file_stato.exists() else {}

    ora = {}
    cambi = []
    for c in config["controlli"]:
        funz = TIPI.get(c.get("tipo"))
        ok, dettaglio = funz(c) if funz else (False, f"tipo sconosciuto: {c.get('tipo')}")
        ora[c["nome"]] = {"ok": ok, "dettaglio": dettaglio}
        print(f"{'OK   ' if ok else 'ROTTO'} {c['nome']}: {dettaglio}")
        era_ok = prima.get(c["nome"], {}).get("ok", True)  # alla prima volta, «ok» è lo stato di partenza
        if era_ok and not ok:
            cambi.append(f"ROTTO {c['nome']}: {dettaglio}")
        elif not era_ok and ok:
            cambi.append(f"di nuovo ok: {c['nome']}")

    if a.prova:
        print("\n(prova: nessun avviso, stato non salvato)")
        return 0 if all(v["ok"] for v in ora.values()) else 1

    file_stato.parent.mkdir(parents=True, exist_ok=True)
    file_stato.write_text(json.dumps(ora, ensure_ascii=False, indent=1), encoding="utf-8")
    quando = datetime.datetime.now().isoformat(timespec="seconds")
    with registro.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"quando": quando, "rotti": [k for k, v in ora.items() if not v["ok"]],
                            "cambi": cambi}, ensure_ascii=False) + "\n")
    if cambi:
        avvisa(" | ".join(cambi))
    return 0 if all(v["ok"] for v in ora.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
