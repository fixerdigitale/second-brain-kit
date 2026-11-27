#!/usr/bin/env python3
"""immagine.py - un'immagine col Codex di OpenAI, cioè con l'abbonamento ChatGPT, senza API a consumo.

Uso:
    python3 immagine.py "descrizione dell'immagine" -o copertina.png
    python3 immagine.py "cambia lo sfondo in blu notte" --partenza foto.png -o foto-blu.png

Serve il Codex CLI installato e collegato al tuo account ChatGPT (`codex login`).
Ogni immagine gira in una cartella temporanea vuota, in sola lettura, con shell, browser e plugin
spenti: il Codex può solo usare lo strumento immagini. Il file che genera finisce in
~/.codex/generated_images/<sessione>/; lo script lo copia dove dici tu e cancella l'originale.

Consuma la quota del tuo piano ChatGPT come una richiesta normale. Usalo per lavoro tuo:
l'abbonamento è personale, non generare immagini per conto di altri.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ISTRUZIONE = ("Genera UNA immagine con lo strumento di generazione immagini integrato, seguendo la richiesta qui sotto. "
              "Non fare altro e non chiedere conferme. Se ci sono immagini allegate, usale come riferimento o da modificare.\n\n"
              "Richiesta:\n")
# Funzioni del Codex da tenere spente. Se la tua versione dà errore su un nome sconosciuto, toglilo da qui.
SPENTI = ["shell_tool", "unified_exec", "apps", "plugins", "multi_agent", "computer_use", "browser_use"]
TIMEOUT_S = 600


def cartella_generate() -> Path:
    base = os.environ.get("CODEX_HOME") or str(Path.home() / ".codex")
    return Path(base) / "generated_images"


def main():
    p = argparse.ArgumentParser(description="Immagine col Codex (abbonamento ChatGPT)")
    p.add_argument("prompt")
    p.add_argument("-o", "--output", required=True)
    p.add_argument("--partenza", action="append", default=[], help="immagine di partenza (fino a 3)")
    a = p.parse_args()

    codex = shutil.which("codex")
    if not codex:
        sys.exit("Non trovo il comando codex nel PATH. Installa il Codex CLI e fai `codex login`.")
    if len(a.partenza) > 3:
        sys.exit("Al massimo 3 immagini di partenza.")
    uscita = Path(a.output).expanduser().resolve()

    with tempfile.TemporaryDirectory(prefix="immagine-") as tmp:
        args = [codex, "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "-C", tmp, "--json"]
        for f in SPENTI:
            args += ["--disable", f]
        for i, src in enumerate(a.partenza):
            dest = Path(tmp) / f"partenza-{i + 1}{Path(src).suffix or '.png'}"
            shutil.copyfile(Path(src).expanduser(), dest)
            args += ["-i", str(dest)]
        args += ["--", ISTRUZIONE + a.prompt]   # «--»: -i accetta più file e senza separatore prenderebbe anche il testo
        try:
            r = subprocess.run(args, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=TIMEOUT_S, cwd=tmp)
        except subprocess.TimeoutExpired:
            sys.exit(f"Il Codex non ha finito in {TIMEOUT_S} secondi.")

    sessione, messaggio = None, ""
    for riga in r.stdout.splitlines():
        try:
            d = json.loads(riga)
        except ValueError:
            continue
        if d.get("type") == "thread.started":
            sessione = d.get("thread_id")
        elif d.get("type") == "item.completed" and (d.get("item") or {}).get("type") == "agent_message":
            messaggio = d["item"].get("text") or ""
    dove = cartella_generate() / sessione if sessione else None
    file = None
    if dove and dove.is_dir():
        candidati = sorted(dove.iterdir(), key=lambda x: x.stat().st_mtime)
        file = candidati[-1] if candidati else None
    if not file:
        motivo = messaggio.strip()[:300] or ((r.stderr.strip().splitlines() or ["nessun messaggio"])[-1][:300])
        sys.exit(f"Nessuna immagine prodotta: {motivo}")
    uscita.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(file, uscita)
    shutil.rmtree(dove, ignore_errors=True)
    print(f"Immagine salvata in {uscita}")


if __name__ == "__main__":
    main()
