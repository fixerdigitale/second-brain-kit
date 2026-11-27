#!/usr/bin/env python3
"""Pulizia delle sessioni ferme: chiude i processi di Claude Code che non lavorano da 30 minuti.

Ogni chat o terminale con Claude Code aperto tiene acceso un processo, con i suoi server MCP:
qualche centinaio di MB di memoria ciascuno. Se una sessione non lavora e non aspetta niente
da INATTIVA_MIN minuti, questo script chiude il suo processo. La conversazione non si perde:
è salvata nel file .jsonl in ~/.claude/projects/ e si riprende con `claude --resume`
(o riaprendo la chat nell'app).

Una sessione NON si chiude se:
  - il suo file di conversazione è cambiato negli ultimi INATTIVA_MIN minuti;
  - ha un comando in corso (un processo figlio nato dopo l'avvio);
  - l'ultimo strumento chiamato non ha ancora una risposta (sta lavorando o aspetta un permesso);
  - è nella lista «tieni»;
  - è una sessione senza interfaccia (claude -p): finisce da sola.

    python3 ferma_sessioni.py             mostra cosa farebbe (non chiude niente)
    python3 ferma_sessioni.py ferma       chiude davvero (da mettere in un'attività pianificata)
    python3 ferma_sessioni.py tieni <id-sessione|cartella>    mai chiudere questa
    python3 ferma_sessioni.py libera <id-sessione|cartella>   toglie dalla lista «tieni»

Linux e Mac con la libreria standard; su Windows serve `pip install psutil`.
"""
import glob
import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

INATTIVA_MIN = 30
NATO_DOPO_S = 180
PROGETTI = Path.home() / ".claude" / "projects"
TIENI = Path.home() / ".claude" / "ferma-sessioni-tieni.txt"
REGISTRO = Path.home() / ".claude" / "ferma-sessioni.jsonl"

try:
    import psutil  # facoltativo: serve su Windows
except ImportError:
    psutil = None


def processi():
    """(pid, ppid, secondi di vita, argomenti) di tutti i processi."""
    if psutil:
        adesso = time.time()
        for p in psutil.process_iter(["pid", "ppid", "create_time", "cmdline"]):
            i = p.info
            yield i["pid"], i["ppid"], adesso - (i["create_time"] or adesso), i["cmdline"] or []
        return
    formato = "pid=,ppid=,etimes=,args=" if sys.platform.startswith("linux") else "pid=,ppid=,etime=,args="
    out = subprocess.run(["ps", "-axo", formato], capture_output=True, text=True).stdout
    for riga in out.splitlines():
        parti = riga.split(None, 3)
        if len(parti) < 4:
            continue
        yield int(parti[0]), int(parti[1]), durata(parti[2]), parti[3].split()


def durata(t):
    if t.isdigit():
        return int(t)
    giorni, _, resto = t.rpartition("-")
    pezzi = [int(x) for x in resto.split(":")]
    while len(pezzi) < 3:
        pezzi.insert(0, 0)
    return (int(giorni) if giorni else 0) * 86400 + pezzi[0] * 3600 + pezzi[1] * 60 + pezzi[2]


def cartella_di(pid):
    if psutil:
        try:
            return psutil.Process(pid).cwd()
        except Exception:
            return None
    if sys.platform.startswith("linux"):
        try:
            return os.readlink(f"/proc/{pid}/cwd")
        except OSError:
            return None
    out = subprocess.run(["lsof", "-a", "-p", str(pid), "-d", "cwd", "-Fn"], capture_output=True, text=True).stdout
    return next((r[1:] for r in out.splitlines() if r.startswith("n")), None)


def e_claude(args):
    if not args:
        return False
    nome = os.path.basename(args[0]).lower()
    if nome in ("claude", "claude.exe"):
        return True
    return nome.startswith("node") and any("claude-code" in a for a in args[1:3])


def id_sessione(args):
    for i, a in enumerate(args):
        for chiave in ("--session-id", "--resume", "-r"):
            if a.startswith(chiave + "="):
                return a.split("=", 1)[1]
            if a == chiave and i + 1 < len(args) and not args[i + 1].startswith("-"):
                return args[i + 1]
    return None


def file_sessione(args, cwd):
    sid = id_sessione(args)
    if sid:
        trovati = glob.glob(str(PROGETTI / "*" / f"{sid}.jsonl"))
        if trovati:
            return Path(trovati[0])
    if cwd:
        # Claude Code chiama la cartella del progetto come il percorso, con i segni non alfanumerici cambiati in «-»
        nome = re.sub(r"[^A-Za-z0-9]", "-", cwd)
        candidati = sorted((PROGETTI / nome).glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
        if candidati:
            return candidati[-1]
    return None


def strumento_aperto(jsonl):
    with open(jsonl, "rb") as f:
        f.seek(0, 2)
        f.seek(max(0, f.tell() - 3_000_000))
        righe = f.read().decode("utf-8", "replace").splitlines()
    usi, risposte = {}, set()
    for r in righe:
        try:
            d = json.loads(r)
        except ValueError:
            continue
        c = (d.get("message") or {}).get("content")
        for x in c if isinstance(c, list) else []:
            if isinstance(x, dict) and x.get("type") == "tool_use":
                usi[x.get("id")] = x.get("name")
            elif isinstance(x, dict) and x.get("type") == "tool_result":
                risposte.add(x.get("tool_use_id"))
    aperti = [n for k, n in usi.items() if k not in risposte]
    return aperti[-1] if aperti else None


def lista_tieni():
    try:
        return {r.strip() for r in TIENI.read_text(encoding="utf-8").splitlines() if r.strip()}
    except OSError:
        return set()


def valuta():
    tutti = list(processi())
    figli = {}
    for pid, ppid, vita, args in tutti:
        figli.setdefault(ppid, []).append((pid, vita))
    tieni = lista_tieni()
    for pid, ppid, vita, args in tutti:
        if not e_claude(args) or pid == os.getpid():
            continue
        if "-p" in args or "--print" in args:
            continue
        cwd = cartella_di(pid)
        jsonl = file_sessione(args, cwd)
        etichetta = jsonl.stem if jsonl else "?"
        motivo = None
        if etichetta in tieni or (cwd and cwd in tieni):
            motivo = "nella lista «tieni»"
        elif not jsonl:
            motivo = "non trovo la sua conversazione: la lascio stare"
        else:
            ferma_da = (time.time() - jsonl.stat().st_mtime) / 60
            if ferma_da < INATTIVA_MIN:
                motivo = f"attiva {ferma_da:.0f} minuti fa"
            elif any(vita - v > NATO_DOPO_S for _, v in figli.get(pid, [])):
                motivo = "ha un comando in corso"
            else:
                aperto = strumento_aperto(jsonl)
                if aperto:
                    motivo = f"aspetta la risposta di {aperto}"
        yield pid, etichetta, cwd, motivo


def main():
    comando = sys.argv[1] if len(sys.argv) > 1 else "prova"
    if comando in ("tieni", "libera"):
        if len(sys.argv) < 3:
            sys.exit("Serve l'id della sessione o la cartella.")
        voci = lista_tieni()
        voci = voci | {sys.argv[2]} if comando == "tieni" else voci - {sys.argv[2]}
        TIENI.parent.mkdir(parents=True, exist_ok=True)
        TIENI.write_text("\n".join(sorted(voci)) + "\n", encoding="utf-8")
        print("Fatto.")
        return
    for pid, sessione, cwd, motivo in valuta():
        if motivo:
            print(f"tengo  {pid:>7}  {sessione[:8]}  {cwd}  ({motivo})")
            continue
        if comando != "ferma":
            print(f"CHIUDEREI {pid:>7}  {sessione[:8]}  {cwd}")
            continue
        try:
            os.kill(pid, signal.SIGTERM)
            esito = "chiusa"
        except OSError as e:
            esito = f"errore: {e}"
        print(f"{esito:<6} {pid:>7}  {sessione[:8]}  {cwd}")
        with open(REGISTRO, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": int(time.time()), "pid": pid, "sessione": sessione, "cartella": cwd, "esito": esito}) + "\n")


if __name__ == "__main__":
    main()
