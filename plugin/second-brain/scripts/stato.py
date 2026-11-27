#!/usr/bin/env python3
"""Legge e aggiorna second-brain/.onboarding/stato.json, lo stato dell'onboarding.

Lo stato contiene solo fasi, consensi, tono, voti per area, misure, missioni e
date: nomi di file e numeri, mai contenuti. Per questo un valore piu' lungo di
300 caratteri viene rifiutato.

Uso (la cartella di lavoro e' quella corrente, oppure --cartella <dir>; l'onboarding
passa sempre --cartella con la cartella di lavoro confermata dalla persona):
  stato.py crea [--lingua it|en]       crea lo stato se manca (non sovrascrive mai).
                                       Rifiuta la cartella personale intera, la radice,
                                       Scrivania, Download e Documenti interi.
  stato.py leggi                       stampa la riga di ripresa
  stato.py mostra                      stampa tutto il JSON
  stato.py imposta <chiave.sotto> <valore>   valore JSON (numero, true, [..]) o testo
  stato.py aggiungi <chiave.sotto> <valore>  aggiunge a una lista
  stato.py ora <chiave.sotto>          scrive l'ora di adesso (ISO, ora locale)
  stato.py minuti <chiave-inizio> <chiave-fine>   minuti fra due ore salvate
  stato.py fase <n>                    passa alla fase n e la segna come iniziata
  stato.py missione <id> <fatta|saltata|in-corso>
      <id> puo' essere lo slug della scheda o il nome della missione: la riga
      «Adesso» li riconosce tutti e due (campo «missione» dentro piano.passi).

Codici di uscita: 0 fatto, 1 stato mancante, 2 errore d'uso.

Solo libreria standard di Python 3.
"""
import datetime as dt
import json
import os
import shutil
import sys
import tempfile

LINGUE = ("it", "en")
# cartelle che non si usano mai intere come cartella di lavoro
VIETATE = ("Desktop", "Scrivania", "Downloads", "Download", "Documents", "Documenti")


class ErroreUso(Exception):
    pass


def cartella_vietata(cartella):
    """Un messaggio se la cartella non va bene come cartella di lavoro, altrimenti None."""
    c = os.path.normcase(os.path.realpath(cartella))
    home = os.path.normcase(os.path.realpath(os.path.expanduser("~")))
    if c == os.path.normcase(os.path.realpath(os.path.join(c, os.pardir))) or c.lower().rstrip("\\/") in ("/home", "/users", "c:\\users"):
        return "la radice del disco non va bene come cartella di lavoro"
    if c == home or home.startswith(c.rstrip(os.sep) + os.sep):
        return "la cartella personale intera non va bene come cartella di lavoro: scegline una dedicata"
    basi = [home] + [os.path.normcase(os.path.realpath(os.path.join(home, x))) for x in _onedrive(home)]
    for b in basi:
        for n in VIETATE:
            if c == os.path.normcase(os.path.realpath(os.path.join(b, n))):
                return ("%s intera non va bene come cartella di lavoro: usa una sua sottocartella dedicata "
                        "(per esempio %s)" % (n, os.path.join(cartella, "Lavoro")))
    # cartelle dei programmi e delle chiavi: mai, nemmeno una loro sottocartella
    for n in (".claude", ".ssh", ".gnupg", ".aws", ".config", "AppData"):
        x = os.path.normcase(os.path.realpath(os.path.join(home, n)))
        if c == x or c.startswith(x.rstrip(os.sep) + os.sep):
            return "%s e' una cartella di programmi o di chiavi, non una cartella di lavoro" % n
    # intere, non le loro sottocartelle (iCloud Drive/Lavoro va bene)
    for n in ("Library", os.path.join("Library", "Mobile Documents"),
              os.path.join("Library", "Mobile Documents", "com~apple~CloudDocs")):
        if c == os.path.normcase(os.path.realpath(os.path.join(home, n))):
            return "%s intera non va bene come cartella di lavoro: usa una sottocartella dedicata" % n
    return None


def _onedrive(home):
    try:
        return [x for x in os.listdir(home) if x.lower().startswith("onedrive")]
    except OSError:
        return []

QUI = os.path.dirname(os.path.abspath(__file__))
MODELLO = os.path.join(QUI, "..", "modelli", "stato.json")
NOMI_FASI = {
    "it": ["patto", "sguardo veloce", "primo risultato", "rendilo ripetibile", "studio completo e mappa",
           "piano", "passi scelti", "rimisura"],
    "en": ["agreement", "quick look", "first result", "make it repeatable", "full study and map",
           "plan", "chosen steps", "re-measure"],
}


def percorso(cartella):
    return os.path.join(cartella, "second-brain", ".onboarding", "stato.json")


def carica(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def salva(p, dati):
    dati["aggiornato_il"] = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    d = os.path.dirname(p)
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".stato-", suffix=".json")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(dati, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, p)


def valore(testo):
    try:
        v = json.loads(testo)
    except ValueError:
        v = testo
    if len(json.dumps(v, ensure_ascii=False)) > 300:
        raise SystemExit("Rifiuto: valore troppo lungo. Nello stato vanno solo nomi e numeri, non contenuti.")
    # una chiave o una password non entra mai nello stato (lo stato puo' stare in una
    # cartella sincronizzata e lo leggono le sessioni dopo)
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import cerca_segreti
        sospetto = bool(cerca_segreti.nomi_in_riga(json.dumps(v, ensure_ascii=False))
                        or cerca_segreti.nomi_in_riga(str(v)))
    except ImportError:
        sospetto = False
    if sospetto:
        raise ErroreUso("valore rifiutato: sembra contenere una chiave o una password. "
                        "Nello stato vanno solo nomi e numeri: scrivi il numero, non il segreto.")
    return v


def vai(dati, chiave, crea=True):
    # anche il nome della chiave passa dal controllo: «imposta sk-... 1» non deve salvare la chiave
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import cerca_segreti
        if cerca_segreti.segreto_nel_percorso(chiave) or cerca_segreti.nomi_in_riga(chiave):
            raise ErroreUso("chiave rifiutata: sembra contenere una chiave o una password.")
    except ImportError:
        pass
    if len(chiave) > 120:
        raise ErroreUso("chiave troppo lunga: nello stato vanno solo nomi brevi.")
    parti = chiave.split(".")
    nodo = dati
    for k in parti[:-1]:
        if k not in nodo or not isinstance(nodo[k], dict):
            if not crea:
                raise KeyError(chiave)
            nodo[k] = {}
        nodo = nodo[k]
    return nodo, parti[-1]


def leggi_chiave(dati, chiave):
    nodo = dati
    for k in chiave.split("."):
        nodo = nodo[k]
    return nodo


def riga_ripresa(dati):
    lingua = str(dati.get("lingua") or "it").lower()
    nomi = NOMI_FASI.get(lingua, NOMI_FASI["it"])
    try:
        fase = int(dati.get("fase") or 0)
    except (TypeError, ValueError):
        fase = 0
    pr = dati.get("primo_risultato") or {}
    prossima = nomi[fase] if 0 <= fase < len(nomi) else "?"
    if lingua == "en":
        s = "Step %d of %d (%s)." % (fase + 1, len(nomi), prossima)
        if pr.get("descrizione"):
            s += " Last time: %s" % pr["descrizione"]
            if pr.get("stima_prima_min") and pr.get("minuti_con_claude"):
                s += ", from %s to %s min" % (pr["stima_prima_min"], pr["minuti_con_claude"])
            s += "."
    else:
        s = "Passo %d di %d (%s)." % (fase + 1, len(nomi), prossima)
        if pr.get("descrizione"):
            s += " L'ultima volta: %s" % pr["descrizione"]
            if pr.get("stima_prima_min") and pr.get("minuti_con_claude"):
                s += ", da %s a %s min" % (pr["stima_prima_min"], pr["minuti_con_claude"])
            s += "."
    passi = (dati.get("piano") or {}).get("passi") or []
    fatte = {m.get("id") for m in dati.get("missioni", []) if m.get("stato") in ("fatta", "saltata")}
    for passo in passi:
        if not ({passo.get("scheda"), passo.get("missione")} - {None}) & fatte:
            s += (" Now: %s, %s min." if lingua == "en" else " Adesso: %s, %s min.") % (
                passo.get("titolo", passo.get("scheda")), passo.get("minuti", "?"))
            break
    return s


def main(argv):
    try:
        return _main(argv)
    except ErroreUso as e:
        print(str(e), file=sys.stderr)
        return 2
    except (KeyError, TypeError) as e:
        print("chiave mancante o vuota nello stato: %s" % e, file=sys.stderr)
        return 2
    except ValueError as e:
        print("valore non valido: %s" % e, file=sys.stderr)
        return 2


def _main(argv):
    cartella = os.getcwd()
    if "--cartella" in argv:
        i = argv.index("--cartella")
        if i + 1 >= len(argv):
            raise ErroreUso("--cartella vuole un percorso")
        cartella = os.path.expanduser(argv[i + 1])
        del argv[i:i + 2]
    if not argv:
        print(__doc__)
        return 2
    p = percorso(cartella)
    cmd, resto = argv[0], argv[1:]

    if cmd == "crea":
        # prima la cartella, poi l'esistenza: uno stato vecchio nella cartella personale
        # (versioni precedenti del kit) non deve far ripartire da li' in silenzio
        no = cartella_vietata(cartella) if os.path.isdir(cartella) else None
        if no:
            raise ErroreUso("Rifiuto: " + no + "." + (
                " C'e' uno stato vecchio in %s: si puo' spostare nella cartella di lavoro scelta." % p
                if os.path.exists(p) else ""))
        if os.path.exists(p):
            print("esiste gia': " + p)
            return 0
        lingua = "it"
        if "--lingua" in resto:
            j = resto.index("--lingua")
            if j + 1 >= len(resto) or resto[j + 1].lower() not in LINGUE:
                raise ErroreUso("--lingua vuole it oppure en")
            lingua = resto[j + 1].lower()
        if not os.path.isdir(cartella):
            raise ErroreUso("la cartella non esiste: " + cartella)
        no = cartella_vietata(cartella)
        if no:
            raise ErroreUso("Rifiuto: " + no + ".")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        os.makedirs(os.path.join(cartella, "second-brain", "output"), exist_ok=True)
        shutil.copyfile(MODELLO, p)
        dati = carica(p)
        adesso = dt.datetime.now().astimezone().isoformat(timespec="seconds")
        dati["iniziato_il"] = adesso
        dati["lingua"] = lingua
        dati["cartella_di_lavoro"] = os.path.realpath(cartella)
        salva(p, dati)
        print("creato: " + p)
        return 0

    if not os.path.exists(p):
        print("nessuno stato in " + p, file=sys.stderr)
        return 1
    dati = carica(p)

    if cmd == "leggi":
        print(riga_ripresa(dati))
    elif cmd == "mostra":
        print(json.dumps(dati, ensure_ascii=False, indent=2))
    elif cmd == "imposta" and len(resto) == 2:
        if not resto[0].strip(". "):
            raise ErroreUso("chiave vuota")
        nodo, k = vai(dati, resto[0])
        v = valore(resto[1])
        if resto[0] == "lingua":
            v = str(v).lower()
            if v not in LINGUE:
                raise ErroreUso("lingua: it oppure en")
        nodo[k] = v
        salva(p, dati)
    elif cmd == "aggiungi" and len(resto) == 2:
        nodo, k = vai(dati, resto[0])
        lista = nodo.get(k)
        if not isinstance(lista, list):
            lista = []
        v = valore(resto[1])
        if v not in lista:
            lista.append(v)
        nodo[k] = lista
        salva(p, dati)
    elif cmd == "ora" and len(resto) == 1:
        nodo, k = vai(dati, resto[0])
        nodo[k] = dt.datetime.now().astimezone().isoformat(timespec="seconds")
        salva(p, dati)
        print(nodo[k])
    elif cmd == "minuti" and len(resto) == 2:
        ore = []
        for chiave in resto:
            testo = leggi_chiave(dati, chiave)
            if not testo:
                raise ErroreUso("nessuna ora salvata in %s (prima: stato.py ora %s)" % (chiave, chiave))
            t = dt.datetime.fromisoformat(str(testo))
            if t.tzinfo is None:
                t = t.astimezone()
            ore.append(t)
        print(max(0, round((ore[1] - ore[0]).total_seconds() / 60)))
    elif cmd == "fase" and len(resto) == 1:
        n = int(resto[0])
        if not 0 <= n < len(NOMI_FASI["it"]):
            raise ErroreUso("fase: da 0 a %d" % (len(NOMI_FASI["it"]) - 1))
        prima = int(dati.get("fase") or 0)
        fatte = dati.setdefault("fasi_fatte", [])
        for f in range(prima, n):
            if f not in fatte:
                fatte.append(f)
        dati["fase"] = n
        salva(p, dati)
        print(riga_ripresa(dati))
    elif cmd == "missione" and len(resto) == 2:
        mid, st = resto
        if st not in ("fatta", "saltata", "in-corso"):
            print("stato missione: fatta | saltata | in-corso", file=sys.stderr)
            return 2
        missioni = dati.setdefault("missioni", [])
        for m in missioni:
            if m.get("id") == mid:
                m["stato"], m["data"] = st, dt.date.today().isoformat()
                break
        else:
            missioni.append({"id": mid, "stato": st, "data": dt.date.today().isoformat()})
        salva(p, dati)
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    for _f in (sys.stdout, sys.stderr):
        try:
            _f.reconfigure(encoding="utf-8", errors="backslashreplace")
        except (AttributeError, ValueError):
            pass
    sys.exit(main(sys.argv[1:]))
