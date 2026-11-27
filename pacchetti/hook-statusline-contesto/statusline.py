#!/usr/bin/env python3
"""Riga di stato per Claude Code: modello, contesto usato, limiti dell'abbonamento, cartella.

Esempio:  Opus 4 · contesto 84k/200k 42% · 5 ore 31% · settimana 12% · second-brain

Claude Code passa su stdin un JSON con modello, cartella, transcript e (nelle versioni recenti)
`context_window` e `rate_limits`. Se `context_window` manca, il contesto si calcola dal transcript.
Solo libreria standard. Mac, Windows, Linux.
"""
import json
import os
import sys

FINESTRA_DI_RISERVA = 200_000  # se Claude Code non dice la dimensione della finestra
CODA_BYTE = 3_000_000


def contesto_dal_transcript(percorso):
    try:
        with open(percorso, "rb") as f:
            f.seek(0, os.SEEK_END)
            f.seek(max(0, f.tell() - CODA_BYTE))
            righe = f.read().decode("utf-8", "ignore").splitlines()
    except (OSError, TypeError):
        return None
    for riga in reversed(righe):
        try:
            d = json.loads(riga)
        except ValueError:
            continue
        u = (d.get("message") or {}).get("usage")
        if d.get("type") == "assistant" and u and not d.get("isSidechain"):
            return (u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                    + u.get("cache_creation_input_tokens", 0))
    return None


def k(n):
    return f"{round(n / 1000)}k"


def main():
    try:
        d = json.load(sys.stdin)
    except ValueError:
        d = {}
    pezzi = [(d.get("model") or {}).get("display_name") or "?"]

    cw = d.get("context_window") or {}
    finestra = cw.get("context_window_size") or FINESTRA_DI_RISERVA
    usati = cw.get("total_input_tokens")
    if not usati:
        usati = contesto_dal_transcript(d.get("transcript_path"))
    if usati:
        perc = cw.get("used_percentage")
        if perc is None:
            perc = 100 * usati / finestra
        pezzi.append(f"contesto {k(usati)}/{k(finestra)} {round(perc)}%")

    limiti = d.get("rate_limits") or {}
    for chiave, nome in (("five_hour", "5 ore"), ("seven_day", "settimana")):
        p = (limiti.get(chiave) or {}).get("used_percentage")
        if p is not None:
            pezzi.append(f"{nome} {round(p)}%")

    cartella = (d.get("workspace") or {}).get("current_dir") or d.get("cwd") or ""
    if cartella:
        pezzi.append(os.path.basename(cartella.rstrip("/\\")))
    print(" · ".join(pezzi))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Claude")
