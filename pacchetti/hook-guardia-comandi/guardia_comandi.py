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

Per Bash il comando si divide in pezzi su ; && || | & e a capo, e ogni regola si valuta pezzo per
pezzo: «tranne_se» vale solo per il pezzo in cui compare. Così «git push --force-with-lease; git push -f»
si ferma lo stesso. La divisione è semplice (non capisce le virgolette): nel dubbio ferma di più.

È un promemoria, non una barriera: le regex coprono le forme che prevedi, non tutte quelle possibili
(alias, script, variabili). Per bloccare davvero usa permissions.deny in settings.json.

Solo libreria standard. Mac, Windows, Linux. Se le regole mancano o sono scritte male lascia
passare tutto: la guardia non deve mai fermare il lavoro per un suo errore.
"""
import json
import os
import re
import sys

REGOLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "regole_comandi.json")
SEPARATORI = re.compile(r"\|\||&&|[;|&\n]")


def pezzi_da_controllare(strumento, entrata):
    """Per Bash: i singoli comandi della riga. Per gli altri strumenti: l'input intero, in JSON."""
    if strumento == "Bash":
        comando = entrata.get("command") or ""
        pezzi = [x.strip() for x in SEPARATORI.split(comando) if x.strip()]
        return pezzi or [comando]
    return [json.dumps(entrata, ensure_ascii=False)]


def regola_scatta(r, pezzi):
    for pezzo in pezzi:
        if not re.search(r["se_contiene"], pezzo, re.I):
            continue
        if r.get("tranne_se") and re.search(r["tranne_se"], pezzo, re.I):
            continue
        return True
    return False


def main():
    dati = json.load(sys.stdin)
    strumento = dati.get("tool_name") or ""
    entrata = dati.get("tool_input") or {}
    with open(REGOLE, encoding="utf-8") as f:
        regole = json.load(f)
    pezzi = pezzi_da_controllare(strumento, entrata)
    for r in regole:
        if not re.fullmatch(r.get("strumento", ".*"), strumento):
            continue
        if not regola_scatta(r, pezzi):
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
