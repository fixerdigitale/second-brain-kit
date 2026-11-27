#!/usr/bin/env python3
"""Raccoglie in un file markdown le tue richieste a Claude Code delle ultime N ore, da tutti i progetti.

Legge solo i TUOI messaggi (non le risposte, non gli strumenti) dai file delle sessioni in
~/.claude/projects/*/*.jsonl e scrive un digest per progetto e per sessione. Nessuna AI, nessuna rete.
Serve a una sessione nuova per sapere cosa hai chiesto nelle altre.

Uso:
  python3 raccogli_sessioni.py                          # ultime 12 ore, stampa a schermo
  python3 raccogli_sessioni.py --ore 24 --out <cartella-vault>/Fonti/raccolta/ultima.md

Mac, Windows, Linux. Python 3.8+, nessuna libreria esterna.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

MAX_CARATTERI = 600   # per messaggio: i messaggi lunghi (incolla di log) si tagliano
# oscura cose che sembrano segreti prima di scriverle
SEGRETI = re.compile(r"(sk-[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|"
                     r"(?i:(password|passwd|token|secret|api[_-]?key)\s*[:=]\s*)\S+)")


def testo_utente(riga: dict) -> str:
    if riga.get("type") != "user" or riga.get("isMeta") or riga.get("isSidechain"):
        return ""
    contenuto = (riga.get("message") or {}).get("content")
    if isinstance(contenuto, str):
        testo = contenuto
    elif isinstance(contenuto, list):
        testo = " ".join(p.get("text", "") for p in contenuto
                         if isinstance(p, dict) and p.get("type") == "text")
    else:
        return ""
    testo = testo.strip()
    # salta i messaggi generati dal sistema (comandi, promemoria, risultati di strumenti)
    if not testo or testo.startswith(("<command-", "<local-command", "<system-reminder", "<task-notification", "Caveat:")):
        return ""
    testo = SEGRETI.sub("[OSCURATO]", " ".join(testo.split()))
    return testo[:MAX_CARATTERI] + (" […]" if len(testo) > MAX_CARATTERI else "")


def quando(riga: dict):
    t = riga.get("timestamp")
    try:
        return datetime.fromisoformat(t.replace("Z", "+00:00")) if t else None
    except ValueError:
        return None


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ore", type=float, default=12)
    p.add_argument("--out", help="file markdown da scrivere (se manca, stampa a schermo)")
    a = p.parse_args()

    radice = Path.home() / ".claude" / "projects"
    da = datetime.now(timezone.utc) - timedelta(hours=a.ore)
    per_progetto = {}
    for f in radice.glob("*/*.jsonl"):
        if datetime.fromtimestamp(f.stat().st_mtime, timezone.utc) < da:
            continue
        messaggi = []
        with f.open(encoding="utf-8", errors="ignore") as fh:
            for linea in fh:
                try:
                    riga = json.loads(linea)
                except json.JSONDecodeError:
                    continue
                t = quando(riga)
                if t and t >= da:
                    testo = testo_utente(riga)
                    if testo:
                        messaggi.append((t, testo))
        if messaggi:
            per_progetto.setdefault(f.parent.name, []).append((f.stem[:8], messaggi))

    out = [f"# Raccolta richieste a Claude Code — ultime {a.ore:g} ore",
           f"_Generata il {datetime.now():%d/%m/%Y %H:%M}. Solo i miei messaggi, senza risposte._", ""]
    if not per_progetto:
        out.append("Nessuna sessione nel periodo.")
    for progetto, sessioni in sorted(per_progetto.items()):
        out.append(f"## {progetto}")
        for sid, messaggi in sorted(sessioni, key=lambda s: s[1][0][0]):
            out.append(f"### sessione {sid} · {messaggi[0][0].astimezone():%d/%m %H:%M}")
            out += [f"- {t.astimezone():%H:%M} {testo}" for t, testo in messaggi]
            out.append("")
    testo = "\n".join(out) + "\n"
    if a.out:
        dest = Path(a.out).expanduser()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(testo, encoding="utf-8")
        print(f"Scritto {dest} ({sum(len(s) for s in per_progetto.values())} sessioni)")
    else:
        sys.stdout.write(testo)
    return 0


if __name__ == "__main__":
    sys.exit(main())
