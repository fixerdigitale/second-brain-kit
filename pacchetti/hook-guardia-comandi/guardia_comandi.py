#!/usr/bin/env python3
"""Hook PreToolUse per Claude Code: ferma (o fa confermare) i comandi che hai deciso di non volere,
e spiega a Claude come si fa nel modo giusto.

Le regole stanno in regole_comandi.json, accanto a questo file:
  [
    {"strumento": "Bash",                       <- nome dello strumento (regex), es. "Bash", "WebFetch", "mcp__.*"
     "se_contiene": "git\\s+push\\s+.*--force",  <- regex cercata nel comando / nell'input dello strumento
     "tranne_se": "--force-with-lease",         <- facoltativo: se c'è anche questo, passa
     "azione": "deny",                          <- "deny" ferma, "ask" chiede conferma a te
     "messaggio": "Niente push forzati: usa --force-with-lease."}
  ]

Solo libreria standard. Mac, Windows, Linux. Se le regole mancano o sono scritte male lascia
passare tutto: la guardia non deve mai fermare il lavoro per un suo errore.
"""
import json
import os
import re
import sys

REGOLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "regole_comandi.json")


def testo_da_controllare(strumento, entrata):
    if strumento == "Bash":
        return entrata.get("command") or ""
    return json.dumps(entrata, ensure_ascii=False)


def main():
    dati = json.load(sys.stdin)
    strumento = dati.get("tool_name") or ""
    entrata = dati.get("tool_input") or {}
    with open(REGOLE, encoding="utf-8") as f:
        regole = json.load(f)
    testo = testo_da_controllare(strumento, entrata)
    for r in regole:
        if not re.fullmatch(r.get("strumento", ".*"), strumento):
            continue
        if not re.search(r["se_contiene"], testo, re.I):
            continue
        if r.get("tranne_se") and re.search(r["tranne_se"], testo, re.I):
            continue
        azione = r.get("azione", "deny")
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask" if azione == "ask" else "deny",
            "permissionDecisionReason": "GUARDIA COMANDI: " + r.get("messaggio", "comando non ammesso"),
        }}, ensure_ascii=False))
        return


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
