#!/usr/bin/env python3
"""Due hook di Claude Code per non perdere il filo quando una sessione viene compressa.

  python3 handoff_compressione.py prima   -> evento PreCompact
      Salva in ~/.claude/handoff-backup/ le ultime richieste che hai scritto in questa
      sessione (solo i tuoi messaggi, testo semplice, con le cose che sembrano chiavi
      oscurate) con data, cartella e motivo della
      compressione. Serve come rete: dopo la compressione Claude ricorda solo un riassunto.

  python3 handoff_compressione.py dopo    -> evento SessionStart con matcher "compact"
      Appena la sessione riparte compressa, dice a Claude: rileggi HANDOFF.md, confrontalo con
      le richieste salvate, aggiornalo se manca qualcosa, poi continua.

Solo libreria standard. Mac, Windows, Linux. Non blocca mai: un errore = nessun effetto.
"""
import datetime
import json
import os
import re
import sys

CARTELLA_BACKUP = os.path.join(os.path.expanduser("~"), ".claude", "handoff-backup")
QUANTE_RICHIESTE = 15
CODA_BYTE = 5_000_000
# Oscura quello che sembra una chiave prima di scriverlo nel backup.
SEGRETI = re.compile(r"(sk-[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|"
                     r"(?i:(password|passwd|token|secret|api[_-]?key)\s*[:=]\s*)\S+)")


def testo_utente(m):
    """Il testo scritto da te in un messaggio 'user' (niente risultati di strumenti)."""
    c = m.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        pezzi = [b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text"]
        return "\n".join(p for p in pezzi if p)
    return ""


def ultime_richieste(percorso):
    try:
        with open(percorso, "rb") as f:
            f.seek(0, os.SEEK_END)
            f.seek(max(0, f.tell() - CODA_BYTE))
            righe = f.read().decode("utf-8", "ignore").splitlines()
    except OSError:
        return []
    richieste = []
    for riga in righe:
        try:
            d = json.loads(riga)
        except ValueError:
            continue
        if d.get("type") != "user" or d.get("isSidechain") or d.get("isMeta"):
            continue
        t = testo_utente(d.get("message") or {}).strip()
        if t and not t.startswith("<"):  # salta comandi e avvisi automatici
            richieste.append(SEGRETI.sub("[OSCURATO]", t)[:1500])
    return richieste[-QUANTE_RICHIESTE:]


def file_backup(sessione):
    return os.path.join(CARTELLA_BACKUP, f"{sessione or 'sessione'}.md")


def prima(dati):
    richieste = ultime_richieste(dati.get("transcript_path", ""))
    ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    righe = [f"## Compressione del {ora}",
             f"- Cartella: {dati.get('cwd', '?')}",
             f"- Motivo: {dati.get('trigger', '?')} (manual = /compact, auto = contesto pieno)",
             "", "### Le tue ultime richieste in questa sessione", ""]
    righe += [f"{i}. {r}" for i, r in enumerate(richieste, 1)] or ["(nessuna trovata)"]
    os.makedirs(CARTELLA_BACKUP, exist_ok=True)
    with open(file_backup(dati.get("session_id")), "a", encoding="utf-8") as f:
        f.write("\n".join(righe) + "\n\n")


def dopo(dati):
    backup = file_backup(dati.get("session_id"))
    handoff = os.path.join(dati.get("cwd") or os.getcwd(), "HANDOFF.md")
    parti = ["SESSIONE APPENA COMPRESSA: ricordi solo un riassunto."]
    if os.path.exists(handoff):
        parti.append(f"Rileggi {handoff} prima di continuare.")
    else:
        parti.append(f"Nella cartella non c'è HANDOFF.md: crealo ({handoff}) con stato, decisioni, file toccati e prossimo passo.")
    if os.path.exists(backup):
        parti.append(f"Le ultime richieste dell'utente sono salvate in {backup}: confrontale con l'HANDOFF "
                     "e aggiungi quello che manca.")
    parti.append("Poi di' all'utente in una riga a che punto eravate.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                             "additionalContext": " ".join(parti)}}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        dati = json.load(sys.stdin)
        quando = sys.argv[1] if len(sys.argv) > 1 else ""
        if quando == "prima":
            prima(dati)
        elif quando == "dopo":
            dopo(dati)
    except Exception:
        pass  # un hook non deve mai fermare il lavoro
