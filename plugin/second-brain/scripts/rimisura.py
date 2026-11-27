#!/usr/bin/env python3
"""Hook SessionStart del plugin second-brain: propone la rimisura, una volta sola.

Non fa niente finche' nella cartella di lavoro non esiste
second-brain/.onboarding/stato.json con un piano e una data di rimisura.
Il giorno della rimisura (o dopo), alla prima sessione, aggiunge al contesto una
riga per Claude e segna nello stato che l'ha proposta: non la ripete.

Non legge altro, non manda niente fuori, esce sempre con codice 0.
"""
import datetime as dt
import json
import os
import sys


def main():
    cartella = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    try:
        dati_hook = json.load(sys.stdin)
        cartella = dati_hook.get("cwd") or cartella
    except Exception:
        pass
    p = os.path.join(cartella, "second-brain", ".onboarding", "stato.json")
    if not os.path.isfile(p):
        return
    try:
        with open(p, encoding="utf-8") as fh:
            stato = json.load(fh)
    except (OSError, ValueError):
        return
    dal = (stato.get("piano") or {}).get("rimisura_dal") or ""
    if not dal:
        return
    try:
        giorno = dt.date.fromisoformat(dal[:10])
    except ValueError:
        return
    if dt.date.today() < giorno or stato.get("rimisura_proposta_il") == dal:
        return
    # Nel contesto della sessione entrano solo date ricostruite, mai il testo del file:
    # stato.json puo' stare in una cartella sincronizzata o condivisa e qualcuno potrebbe
    # scriverci frasi rivolte all'AI.
    dal_pulita = giorno.isoformat()
    try:
        data_piano = dt.date.fromisoformat(str((stato.get("piano") or {}).get("data") or "")[:10]).isoformat()
    except ValueError:
        data_piano = "?"
    stato["rimisura_proposta_il"] = dal
    try:
        tmp = p + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(stato, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        os.replace(tmp, p)
    except OSError:
        return  # se non posso segnarla, non la propongo: meglio zero che ogni volta
    if (stato.get("lingua") or "it") == "en":
        riga = ("second-brain: the re-measure day has come (plan of %s, re-measure from %s). In ONE line, in the person's language, "
                "offer the re-measure (10 minutes, same measures as last time): it starts with /second-brain:onboarding. "
                "Do not start it without a yes." % (data_piano, dal_pulita))
    else:
        riga = ("second-brain: è arrivato il giorno della rimisura (piano del %s, rimisura dal %s). In UNA riga, nella lingua della persona, "
                "proponi la rimisura (10 minuti, stesse misure dell'altra volta): si fa con /second-brain:onboarding. "
                "Non partire senza un sì." % (data_piano, dal_pulita))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": riga}},
                     ensure_ascii=False))


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    except (AttributeError, ValueError):
        pass
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
