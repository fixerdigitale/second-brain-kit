#!/usr/bin/env python3
"""lavora.py - lancia un lavoro di Claude Code in background e avvisa quando finisce.

Uso:
    python3 lavora.py "brief completo del lavoro" --titolo "titolo corto"
    python3 lavora.py --stato

Il brief deve bastare a una sessione che parte da zero: obiettivo, file, link,
cosa consegnare. Il risultato finisce in <cartella-risultati>/AAAA-MM-GG-HHMM-<titolo>.md
e a fine lavoro arriva una notifica sul desktop (Windows, Mac, Linux).

Funziona solo a PC acceso: se spegni il PC, il lavoro si interrompe.
"""
import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Dove finiscono i risultati. Cambialo, o passa --cartella.
CARTELLA_PREDEFINITA = Path.home() / "lavori-claude"
MAX_INSIEME = 3  # oltre, il lavoro nuovo non parte: troppi insieme consumano il piano


def nome_file(titolo: str) -> str:
    pulito = re.sub(r"[^a-zA-Z0-9]+", "-", titolo.lower()).strip("-")[:40] or "lavoro"
    return dt.datetime.now().strftime("%Y-%m-%d-%H%M-") + pulito


def notifica(titolo: str, testo: str) -> None:
    testo = testo.replace('"', "'").replace("\\", "/")[:200]
    titolo = titolo.replace('"', "'").replace("\\", "/")[:60]
    try:
        if sys.platform == "darwin":
            subprocess.run(["osascript", "-e", f'display notification "{testo}" with title "{titolo}"'], check=False)
        elif os.name == "nt":
            # Stringhe fra apici singoli: PowerShell non esegue $(...) che arrivi dal testo del risultato.
            t_ps, s_ps = titolo.replace("'", "''"), testo.replace("'", "''")
            ps = (
                "Add-Type -AssemblyName System.Windows.Forms;"
                "$n=New-Object System.Windows.Forms.NotifyIcon;"
                "$n.Icon=[System.Drawing.SystemIcons]::Information;$n.Visible=$true;"
                f"$n.ShowBalloonTip(10000,'{t_ps}','{s_ps}',0);Start-Sleep 11;$n.Dispose()"
            )
            subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=False)
        elif shutil.which("notify-send"):
            subprocess.run(["notify-send", titolo, testo], check=False)
    except OSError:
        pass  # la notifica e' un di piu': il risultato resta comunque nel file


def in_corso(cartella: Path) -> list:
    return sorted(cartella.glob("*.in-corso.json"))


def esegui(args) -> int:
    """Gira in background: lancia claude -p, scrive il risultato, avvisa."""
    cartella = Path(args.cartella)
    base = cartella / args.nome
    segno = base.with_suffix(".in-corso.json")
    claude = shutil.which("claude") or "claude"
    comando = [claude, "-p", args.brief, "--output-format", "text", "--permission-mode", args.permessi]
    inizio = dt.datetime.now()
    try:
        r = subprocess.run(comando, cwd=args.cwd, capture_output=True, text=True, encoding="utf-8",
                           timeout=args.max_minuti * 60)
        ok = r.returncode == 0
        uscita = r.stdout.strip() or r.stderr.strip()
    except subprocess.TimeoutExpired:
        ok, uscita = False, f"Fermato dopo {args.max_minuti} minuti."
    except OSError as e:
        ok, uscita = False, f"Non riesco a lanciare claude: {e}"
    durata = int((dt.datetime.now() - inizio).total_seconds() // 60)
    stato = "fatto" if ok else "non riuscito"
    base.with_suffix(".md").write_text(
        f"# {args.titolo}\n\n- Stato: {stato}\n- Inizio: {inizio:%d/%m %H:%M}, durata {durata} min\n"
        f"- Cartella: {args.cwd}\n\n## Brief\n\n{args.brief}\n\n## Risultato\n\n{uscita}\n",
        encoding="utf-8",
    )
    segno.unlink(missing_ok=True)
    prima_riga = (uscita.splitlines() or [""])[0]
    notifica(("Fatto: " if ok else "Non riuscito: ") + args.titolo, prima_riga or "apri il file del risultato")
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser(description="Lavoro di Claude Code in background, con avviso a fine lavoro.")
    p.add_argument("brief", nargs="?", help="il brief completo")
    p.add_argument("--titolo", default="lavoro")
    p.add_argument("--cartella", default=str(CARTELLA_PREDEFINITA), help="dove scrivere i risultati")
    p.add_argument("--cwd", default=os.getcwd(), help="cartella su cui lavora Claude (di solito il progetto o il vault)")
    p.add_argument("--permessi", default="acceptEdits",
                   help="modo permessi di Claude Code: default, acceptEdits, plan (vedi LEGGIMI)")
    p.add_argument("--max-minuti", type=int, default=60)
    p.add_argument("--stato", action="store_true", help="elenca i lavori in corso")
    p.add_argument("--interno", action="store_true", help=argparse.SUPPRESS)
    p.add_argument("--nome", help=argparse.SUPPRESS)
    args = p.parse_args()

    cartella = Path(args.cartella)
    cartella.mkdir(parents=True, exist_ok=True)

    if args.stato:
        lavori = in_corso(cartella)
        if not lavori:
            print("Nessun lavoro in corso.")
        for f in lavori:
            d = json.loads(f.read_text(encoding="utf-8"))
            print(f"- {d['titolo']} (partito {d['inizio']})")
        return 0
    if args.interno:
        return esegui(args)
    if not args.brief:
        p.error("serve il brief")
    if len(in_corso(cartella)) >= MAX_INSIEME:
        print(f"Ci sono gia' {MAX_INSIEME} lavori in corso: aspetta che uno finisca (--stato).")
        return 2

    nome = nome_file(args.titolo)
    (cartella / f"{nome}.in-corso.json").write_text(
        json.dumps({"titolo": args.titolo, "inizio": f"{dt.datetime.now():%d/%m %H:%M}"}), encoding="utf-8")
    figlio = [sys.executable, os.path.abspath(__file__), args.brief, "--interno", "--nome", nome,
              "--titolo", args.titolo, "--cartella", str(cartella), "--cwd", args.cwd,
              "--permessi", args.permessi, "--max-minuti", str(args.max_minuti)]
    opzioni = {"stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    if os.name == "nt":
        opzioni["creationflags"] = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    else:
        opzioni["start_new_session"] = True
    subprocess.Popen(figlio, **opzioni)
    print(f"Avviato: {args.titolo}. Il risultato arrivera' in {cartella / (nome + '.md')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
