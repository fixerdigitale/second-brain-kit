#!/usr/bin/env python3
"""Hook SessionStart per Claude Code: a ogni sessione nuova mette nel contesto lo stato VERO di
oggi (data, ora e le prime righe dei file che scegli tu), prima che Claude si fidi della memoria.

Perché: la memoria è una fotografia del passato. Se un file di stato dice com'è adesso,
deve arrivare da solo, non quando qualcuno si ricorda di leggerlo.

I file da leggere stanno in stato_file.txt, accanto a questo script: un percorso per riga.
Solo libreria standard. Mac, Windows, Linux. Ogni errore = una riga che dice cosa manca.
"""
import datetime
import json
import os
import sys

CARTELLA = os.path.dirname(os.path.abspath(__file__))
ELENCO = os.path.join(CARTELLA, "stato_file.txt")
RIGHE_PER_FILE = 40
GIORNI = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]


def file_da_leggere():
    try:
        with open(ELENCO, encoding="utf-8") as f:
            return [os.path.expanduser(r.strip()) for r in f if r.strip() and not r.startswith("#")]
    except OSError:
        return []


def main():
    try:
        json.load(sys.stdin)  # l'input non serve, ma va letto
    except ValueError:
        pass
    ora = datetime.datetime.now()
    parti = [f"OGGI: {GIORNI[ora.weekday()]} {ora:%d/%m/%Y}, ore {ora:%H:%M}.",
             "Lo stato qui sotto è letto adesso dai file e vale più della memoria: se una memoria lo "
             "contraddice, correggi la memoria."]
    for percorso in file_da_leggere():
        try:
            with open(percorso, encoding="utf-8") as f:
                testo = "".join(f.readlines()[:RIGHE_PER_FILE]).strip()
            agg = datetime.datetime.fromtimestamp(os.path.getmtime(percorso))
            parti.append(f"\n--- {percorso} (aggiornato {agg:%d/%m %H:%M}) ---\n{testo}")
        except OSError as e:
            parti.append(f"\n--- {percorso}: non leggibile ({type(e).__name__}). Non inventare il contenuto. ---")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                             "additionalContext": "\n".join(parti)}}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
