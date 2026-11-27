#!/usr/bin/env python3
"""Semaforo dei consumi: dice se un lavoro lungo può partire o deve fermarsi.

Legge l'ultima lettura dei limiti dell'abbonamento (~/.claude/limiti-ultimi.json, scritta da
registra_limiti.py o da turno_libero.py) e risponde con il codice di uscita:
    0 = verde, si può continuare
    1 = stop: una soglia è superata
    2 = non lo so: lettura assente o troppo vecchia

    python3 semaforo.py                 soglie che salgono man mano che il reset si avvicina
    python3 semaforo.py --tetto 80      soglia fissa all'80% per 5 ore e settimana
    python3 semaforo.py margine         0 solo se nella settimana avanza quota che andrebbe persa

Le soglie sono scelte mie, da adattare: in cima al file. Solo libreria standard.
"""
import datetime as dt
import json
import os
import sys
import time

FILE = os.path.join(os.path.expanduser("~"), ".claude", "limiti-ultimi.json")
LETTURA_MAX_MIN = 30
# (ore al reset almeno, stop in %): lontano dal reset si lascia spazio a te, vicino si può spendere.
SOGLIE_5ORE = [(3, 65), (2, 70), (1, 75), (0.5, 80), (0, 90)]
# (giorni al reset almeno, stop in %)
SOGLIE_SETTIMANA = [(4, 50), (3, 60), (2, 70), (1, 80), (0, 90)]
# margine: quota della settimana che si può usare senza togliere niente a te
TETTO_SETTIMANA = 95        # mai oltre questo
RISERVA_PER_ORA = 0.45      # punti % lasciati a te per ogni ora che manca al reset
MARGINE_MIN = 5             # sotto questo non vale la pena partire


def a_secondi(v):
    """resets_at può arrivare come secondi, millisecondi o testo ISO."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return v / 1000 if v > 1e12 else float(v)
    try:
        return dt.datetime.fromisoformat(str(v).replace("Z", "+00:00")).timestamp()
    except ValueError:
        return None


def soglia(tabella, mancano):
    for almeno, tetto in tabella:
        if mancano >= almeno:
            return tetto
    return tabella[-1][1]


def leggi():
    try:
        with open(FILE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def main():
    args = sys.argv[1:]
    tetto = None
    if "--tetto" in args:
        tetto = float(args[args.index("--tetto") + 1])
    d = leggi()
    if not d:
        print(f"Nessuna lettura in {FILE}: apri una sessione con la riga di stato attiva.")
        return 2
    eta = (time.time() - d.get("ts", 0)) / 60
    adesso = time.time()
    sett = d.get("seven_day")
    if not sett:
        print("Nella lettura manca la settimana.")
        return 2
    cs = sett["used_percentage"]
    rs = a_secondi(sett.get("resets_at")) or adesso + 7 * 86400
    if "margine" in args:
        ore = max(0.0, (rs - adesso) / 3600)
        margine = TETTO_SETTIMANA - cs - RISERVA_PER_ORA * ore
        print(f"settimana {cs:.0f}%, reset fra {ore:.0f} ore, margine libero {margine:.1f} punti")
        if eta > LETTURA_MAX_MIN:
            print(f"lettura vecchia di {eta:.0f} min")
            return 2
        return 0 if margine >= MARGINE_MIN else 1
    ts = tetto if tetto is not None else soglia(SOGLIE_SETTIMANA, max(0.0, (rs - adesso) / 86400))
    print(f"settimana: {cs:.0f}% (stop a {ts:.0f}%)")
    cinque = d.get("five_hour")
    if cinque:
        c5 = cinque["used_percentage"]
        r5 = a_secondi(cinque.get("resets_at")) or adesso + 5 * 3600
        t5 = tetto if tetto is not None else soglia(SOGLIE_5ORE, max(0.0, (r5 - adesso) / 3600))
        print(f"5 ore: {c5:.0f}% (stop a {t5:.0f}%)")
    if eta > LETTURA_MAX_MIN:
        print(f"Lettura vecchia di {eta:.0f} min: non so dire.")
        return 2
    if cs >= ts:
        print("STOP: settimana")
        return 1
    if cinque and c5 >= t5:
        print("STOP: finestra di 5 ore")
        return 1
    print("VERDE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
