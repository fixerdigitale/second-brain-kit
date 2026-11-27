#!/usr/bin/env python3
"""Hook Stop / Notification per Claude Code: un suono (e su Mac una notifica) quando Claude ha
finito il turno o aspetta una tua risposta. Così puoi fare altro mentre lavora.

  python3 fine_lavoro.py fine      -> evento Stop: Claude ha finito
  python3 fine_lavoro.py attesa    -> evento Notification: Claude aspetta te (permesso, domanda)

Solo libreria standard. Mac (afplay + notifica), Windows (winsound), Linux (paplay o campanello).
Non si sente nelle sessioni dei sotto-agenti: l'evento Stop vale per la conversazione principale.
"""
import json
import os
import subprocess
import sys

MAC_SUONI = {"fine": "/System/Library/Sounds/Glass.aiff", "attesa": "/System/Library/Sounds/Ping.aiff"}
TESTI = {"fine": "Claude ha finito", "attesa": "Claude aspetta una tua risposta"}


def suona(tipo):
    if sys.platform == "darwin":
        subprocess.Popen(["afplay", MAC_SUONI[tipo]])
        subprocess.Popen(["osascript", "-e", f'display notification "{TESTI[tipo]}" with title "Claude Code"'])
    elif os.name == "nt":
        import winsound
        winsound.MessageBeep(winsound.MB_OK if tipo == "fine" else winsound.MB_ICONASTERISK)
    else:
        suono = "/usr/share/sounds/freedesktop/stereo/complete.oga"
        if os.path.exists(suono):
            subprocess.Popen(["paplay", suono])
        else:
            sys.stderr.write("\a")


if __name__ == "__main__":
    try:
        try:
            json.load(sys.stdin)
        except ValueError:
            pass
        tipo = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in TESTI else "fine"
        suona(tipo)
    except Exception:
        pass
