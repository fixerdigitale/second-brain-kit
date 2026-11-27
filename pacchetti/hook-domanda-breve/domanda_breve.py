#!/usr/bin/env python3
"""Hook UserPromptSubmit per Claude Code: se il tuo messaggio è una domanda breve e non un ordine,
ricorda a Claude di rispondere e basta, senza partire con lavori lunghi.

Decide solo dal testo: breve, finisce con "?" o comincia con una parola da domanda, e non
contiene verbi di lavoro (fai, crea, sistema, scrivi...). Non legge file, non blocca niente.
Solo libreria standard. Mac, Windows, Linux.
"""
import json
import re
import sys

MAX_CAR_CON_PUNTO = 220
MAX_CAR_SENZA_PUNTO = 120

INTERROGATIVE = (
    r"(come|com'è|cosa|che cosa|che|perché|perche|quanto|quanti|quanta|quante|dove|quando|chi|quale|quali|"
    r"è|c'è|posso|possiamo|riesci|conviene|serve|si può|ha senso|abbiamo|hai|esiste|funziona|vale)"
)
APERTURA = re.compile(r"^(?:(?:e|ma|allora|ok|poi|senti|scusa)[\s,.]+)*" + INTERROGATIVE + r"\b", re.I)
# Verbi di lavoro: se ci sono, non è una domanda pura e l'hook sta zitto. Aggiungi i tuoi.
LAVORO = re.compile(
    r"\b(fai|fammi|crea|creami|costruisci|scrivi|scrivimi|sistema|sistemami|aggiorna|installa|lancia|vai|"
    r"procedi|parti|implementa|cancella|elimina|modifica|metti|aggiungi|togli|cambia|prova|controlla|verifica|"
    r"cerca|guarda|apri|manda|pubblica|rifai|correggi|salva|leggi|carica|dimmi|dammi|mostrami|voglio|vorrei|"
    r"esegui|continua|prosegui)\b", re.I)
AUTONOMIA = re.compile(r"senza fermarti|fino alla fine|in autonomia", re.I)

MESSAGGIO = (
    "DOMANDA BREVE: l'utente sta chiedendo, non ordinando. Rispondi in poche righe. Niente sotto-agenti, "
    "niente modifiche a file, niente lavori lunghi: al massimo 3 letture rapide per verificare un fatto. "
    "Se per rispondere serve lavoro, dillo in una riga e proponi i passi: parte solo se l'utente conferma."
)


def e_domanda_breve(testo):
    t = (testo or "").strip()
    if not t or t.startswith(("/", "<", "[")) or AUTONOMIA.search(t) or LAVORO.search(t):
        return False
    if len(re.findall(r"[.!?]\s", t + " ")) > 3:
        return False
    if t.endswith("?") and len(t) <= MAX_CAR_CON_PUNTO:
        return True
    return len(t) <= MAX_CAR_SENZA_PUNTO and bool(APERTURA.match(t))


if __name__ == "__main__":
    try:
        if e_domanda_breve(json.load(sys.stdin).get("prompt", "")):
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                                     "additionalContext": MESSAGGIO}}, ensure_ascii=False))
    except Exception:
        pass
