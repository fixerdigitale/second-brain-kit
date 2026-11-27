#!/usr/bin/env python3
"""Conteggi e temi delle sessioni passate di Claude Code, senza il testo intero.

Si usa SOLO con il consenso separato della persona (fase 0 dell'onboarding).
Legge i file .jsonl in ~/.claude/projects/ (o in <CLAUDE_CONFIG_DIR>/projects/ se
quella variabile d'ambiente e' impostata, o nella cartella indicata), prende
solo i messaggi scritti dalla persona e stampa:
  - sessioni, giorni attivi, richieste, richieste al giorno;
  - le parole piu' frequenti (i temi), senza frasi;
  - quante richieste sembrano correzioni («te l'ho gia' detto», «again»...).
Con --correzioni N stampa anche le ultime N correzioni (senza doppioni), tagliate
a 160 caratteri e oscurate (le parole con la maiuscola a meta' frase diventano
[NOME]): servono al primo risultato «3 regole d'oro».

Oscuramento: da una parola come password, pass, pwd, token, chiave, key, secret,
bearer, wifi, pin in poi si toglie TUTTO il resto della riga; si tolgono anche
email, numeri di telefono, IBAN, token riconoscibili e le parole con cifre.
I temi non contengono parole con la maiuscola a meta' frase (di solito nomi di
persone o di clienti) ne' pezzi delle righe oscurate.

Senza --progetto legge le sessioni di TUTTI i progetti: l'onboarding passa sempre
--progetto con la cartella della sessione di lavoro.

Uso:
  temi_sessioni.py [--cartella ~/.claude/projects] [--progetto <nome-cartella>]
                   [--giorni 14] [--correzioni N] [--json]

Sola lettura. Solo libreria standard di Python 3.
"""
import collections
import datetime as dt
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerca_segreti  # noqa: E402

CORREZIONE = re.compile(
    r"(te l'?ho gi[aà] detto|ti ho gi[aà] detto|te l'?avevo detto|ti avevo detto|ancora una volta|di nuovo|non cos[iì]|"
    r"ricordati|non farlo pi[uù]|sbagliato|hai sbagliato|ti ho chiesto|smettila|"
    r"i told you|again\b|not like that|that'?s wrong|stop doing|remember to|i already said|"
    r"don'?t do that|you forgot)", re.I)
STOP = set("""
a ad al alla alle anche ancora che chi ci come con da dal dalla de dei del della delle di
e ed era fa fai fare gli ha hai ho il in io la le lo ma mi ne nel nella no non o per piu più
poi quella quello questa questo se si sia sono su sul sulla ti tra tu tutto un una uno va vedi
mio mia tuo tua suo sua cosa cose fammi puoi dimmi metti allora perché perche quando dove
the and for you your with that this are was have has not but can will what how all from
into then them they there here please just make like want need would could should about
http https www com file files oscurato l'ho l'hai detto
""".split())
OSCURATO = "[OSCURATO]"
PAROLA = re.compile(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'\-]{3,}")
# da una parola sensibile in poi, tutto il resto della riga
SEGRETO_IN_TESTO = re.compile(
    r"(passw\w*|(?<![A-Za-z])pass(?![A-Za-z])|(?<![A-Za-z])pwd(?![A-Za-z])|(?<![A-Za-z])psw(?![A-Za-z])|"
    r"(?<![A-Za-z])pin(?![A-Za-z])|token\w*|chiav\w*|api[_\- ]?key|(?<![A-Za-z])key(?![A-Za-z])|"
    r"secret\w*|segret\w*|bearer|credenzial\w*|credential\w*|parola d'ordine|codic\w*|"
    r"(?<![A-Za-z])log-?in(?![A-Za-z])|(?<![A-Za-z])accesso(?![A-Za-z])|chiocciola|"
    r"(?<![A-Za-z])wi-?fi(?![A-Za-z])|iban)[^\n]*", re.I)
EMAIL = re.compile(r"[\w.+\-]+@[\w\-]+(?:\.[\w\-]+)+")
IBAN = re.compile(r"\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]){11,30}\b")
TELEFONO = re.compile(r"(?<![\w])\+?\d[\d \-/.]{5,}\d(?![\w])")
CON_CIFRE = re.compile(r"\S*(?:[A-Za-zÀ-ÿ]\S*\d|\d\S*[A-Za-zÀ-ÿ])\S*")


def testi_utente(record):
    if record.get("type") != "user" or record.get("isMeta"):
        return []
    msg = record.get("message") or {}
    if msg.get("role") not in (None, "user"):
        return []
    c = msg.get("content")
    pezzi = []
    if isinstance(c, str):
        pezzi = [c]
    elif isinstance(c, list):
        for b in c:
            if isinstance(b, dict) and b.get("type") == "text":
                pezzi.append(b.get("text", ""))
    fuori = []
    for t in pezzi:
        t = t.strip()
        if not t or t.startswith(("<command-", "<local-command", "<system-reminder", "Caveat:", "[Request interrupted")):
            continue
        fuori.append(t)
    return fuori


def oscura(t):
    t = SEGRETO_IN_TESTO.sub(lambda m: m.group(1) + " " + OSCURATO, t)
    for _, espr in cerca_segreti.FORME:
        t = espr.sub(OSCURATO, t)
    t = EMAIL.sub(OSCURATO, t)
    t = IBAN.sub(OSCURATO, t)
    t = TELEFONO.sub(OSCURATO, t)
    t = CON_CIFRE.sub(lambda m: m.group(0) if m.group(0) == OSCURATO else OSCURATO, t)
    return t


def senza_nomi(t):
    """Per le correzioni mostrate: le parole con la maiuscola a meta' frase (di solito
    nomi di persone o di clienti) diventano [NOME]."""
    def sost(m):
        if t[max(0, m.start() - 1):m.start()] == "[":  # [OSCURATO] resta com'e'
            return m.group(0)
        prima = t[:m.start()].rstrip()
        if m.group(0)[0].isupper() and prima and prima[-1] not in ".!?:\n\"«(":
            return "[NOME]"
        return m.group(0)
    return PAROLA.sub(sost, t)


def parole_dei_temi(t):
    """Parole per i temi: niente parole con la maiuscola a meta' frase (nomi propri)."""
    fuori = []
    for m in PAROLA.finditer(t):
        p = m.group(0)
        if p[0].isupper():
            prima = t[:m.start()].rstrip()
            if prima and prima[-1] not in ".!?:\n\"«(":
                continue
        p = p.lower()
        if p not in STOP:
            fuori.append(p)
    return fuori


def main(argv):
    base = (os.environ.get("CLAUDE_CONFIG_DIR") or "").strip()
    base = os.path.abspath(os.path.expanduser(base)) if base else os.path.join(os.path.expanduser("~"), ".claude")
    cartella = os.path.join(base, "projects")
    progetto, giorni, n_corr, come_json = None, 14, 0, False
    i = 0
    while i < len(argv):
        a = argv[i]
        v = argv[i + 1] if i + 1 < len(argv) else None
        if a == "--cartella" and v:
            cartella = os.path.expanduser(v); i += 2; continue
        if a == "--progetto" and v:
            progetto = v; i += 2; continue
        if a in ("--giorni", "--correzioni") and v:
            try:
                n = int(v)
            except ValueError:
                print(a + " vuole un numero", file=sys.stderr); return 2
            if a == "--giorni":
                giorni = n
            else:
                n_corr = n
            i += 2; continue
        if a == "--json":
            come_json = True
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            # Un argomento non capito (una cartella scritta senza --cartella, un'opzione
            # sbagliata) non deve far leggere in silenzio le sessioni di TUTTI i progetti.
            print("argomento non capito: " + a + " (vedi --help; la cartella va con --cartella)",
                  file=sys.stderr)
            return 2
        i += 1

    schema = os.path.join(cartella, progetto or "*", "*.jsonl")
    limite = dt.datetime.now().timestamp() - giorni * 86400
    sessioni, giorni_attivi, richieste = 0, set(), 0
    parole = collections.Counter()
    correzioni = []
    for f in sorted(glob.glob(schema)):
        try:
            if os.path.getmtime(f) < limite:
                continue
        except OSError:
            continue
        contate = 0
        with open(f, encoding="utf-8", errors="replace") as fh:
            for riga in fh:
                try:
                    r = json.loads(riga)
                except ValueError:
                    continue
                if r.get("isSidechain"):
                    continue
                ts = r.get("timestamp") or ""
                try:
                    quando = dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    if quando.timestamp() < limite:
                        continue
                except ValueError:
                    quando = None
                for t in testi_utente(r):
                    t = oscura(t)  # prima di tutto: nessun segreto entra nei temi
                    contate += 1
                    if quando:
                        giorni_attivi.add(quando.astimezone().date().isoformat())
                    for p in parole_dei_temi(t):
                        parole[p] += 1
                    if CORREZIONE.search(t):
                        correzioni.append((ts, t))
        if contate:
            sessioni += 1
            richieste += contate

    correzioni.sort()
    # niente doppioni: la stessa frase ripetuta conta una volta sola fra le ultime
    unici, visti = [], set()
    for ts, t in reversed(correzioni):
        chiave = " ".join(t.lower().split())[:160]
        if chiave not in visti:
            visti.add(chiave)
            unici.append((ts, t))
    unici.reverse()
    uscita = {
        "giorni_guardati": giorni,
        "sessioni": sessioni,
        "giorni_attivi": len(giorni_attivi),
        "richieste": richieste,
        "richieste_al_giorno": round(richieste / len(giorni_attivi), 1) if giorni_attivi else 0,
        "temi_parole": [p for p, _ in parole.most_common(20)],
        "richieste_che_sembrano_correzioni": len(correzioni),
    }
    if n_corr:
        uscita["ultime_correzioni"] = [
            {"data": ts[:10], "testo": " ".join(senza_nomi(t).split())[:160]} for ts, t in unici[-n_corr:]
        ]
    if come_json:
        print(json.dumps(uscita, ensure_ascii=False, indent=2))
    else:
        print("Ultimi %d giorni: %d sessioni, %d giorni attivi, %d richieste (%s al giorno)" % (
            giorni, sessioni, uscita["giorni_attivi"], richieste, uscita["richieste_al_giorno"]))
        print("Parole piu' frequenti: " + ", ".join(uscita["temi_parole"]))
        print("Richieste che sembrano correzioni: %d" % len(correzioni))
        for c in uscita.get("ultime_correzioni", []):
            print("- %s: %s" % (c["data"], c["testo"]))
    return 0


if __name__ == "__main__":
    for _f in (sys.stdout, sys.stderr):
        try:
            _f.reconfigure(encoding="utf-8", errors="backslashreplace")
        except (AttributeError, ValueError):
            pass
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as e:
        print("errore: %s" % e, file=sys.stderr)
        sys.exit(2)
