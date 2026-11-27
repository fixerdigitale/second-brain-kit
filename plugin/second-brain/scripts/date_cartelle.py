#!/usr/bin/env python3
"""Inventario di soli nomi, conteggi e date, in sola lettura.

Per ogni cartella indicata e per le sue sottocartelle (fino a --profondita):
numero di file, numero di note .md, data del file piu' recente e del piu' vecchio.
Con --file stampa la data di modifica dei file indicati (CLAUDE.md, settings.json...).
Non apre nessun file e non stampa nomi di file dentro le cartelle: solo i nomi
delle cartelle. Serve all'onboarding per distinguere una cartella viva da una
piena ma ferma da mesi.

Dentro una cartella .claude salta i file del programma e dei plugin (plugins,
cache, projects, ...): il kit appena installato non deve sembrare il lavoro della
persona. Salta anche second-brain/ (lo stato del kit stesso).
Una cartella che il sistema non lascia aprire (su Mac: «Non consentire» al popup
di accesso a Scrivania, Documenti o Download) risulta «accesso negato», non vuota.

Uso:
  date_cartelle.py <cartella> [altre...] [--profondita 2] [--file <percorso>]... [--json]
  date_cartelle.py --cartelle-utente [--json]
      elenca dove stanno davvero Documenti, Scrivania e Download su questo computer
      (nomi inglesi sul disco, cartelle spostate dentro OneDrive su Windows,
      iCloud su Mac) e dice quali esistono.

Solo libreria standard di Python 3. Mac, Windows, Linux.
"""
import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cerca_segreti import percorso_sicuro  # noqa: E402  (nessun segreto nei nomi stampati)

SALTA = {".git", "node_modules", ".venv", "venv", "__pycache__", ".cache", ".Trash", "$RECYCLE.BIN",
         "Library", "AppData", ".npm", ".cargo", "second-brain"}
SALTA_IN_CLAUDE = {"plugins", "projects", "tmp", "file-history", "cache", "backups", "shell-snapshots",
                   "todos", "statsig", "debug", "ide", "paste-cache", "session-env", "telemetry"}


def salta(cartella_madre, nome):
    return nome in SALTA or (os.path.basename(cartella_madre) == ".claude" and nome in SALTA_IN_CLAUDE)


def cartelle_utente():
    """Percorsi veri di Documenti, Scrivania e Download, con le varianti comuni."""
    home = os.path.expanduser("~")
    candidati = []
    for nomi in (("Documents", "Documenti"), ("Desktop", "Scrivania"), ("Downloads", "Download")):
        for n in nomi:
            candidati.append(os.path.join(home, n))
    onedrive = [os.environ.get(k) for k in ("OneDrive", "OneDriveCommercial", "OneDriveConsumer")]
    try:
        onedrive += [os.path.join(home, x) for x in os.listdir(home) if x.lower().startswith("onedrive")]
    except OSError:
        pass
    for od in [x for x in onedrive if x]:
        for n in ("Documents", "Documenti", "Desktop", "Scrivania"):
            candidati.append(os.path.join(od, n))
    candidati.append(os.path.join(home, "Library", "Mobile Documents", "com~apple~CloudDocs"))
    for n in ("Dropbox", "Google Drive", "My Drive"):
        candidati.append(os.path.join(home, n))
    if sys.platform.startswith("win"):
        try:
            import winreg
            chiave = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                    r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
            for valore in ("Personal", "Desktop", "{374DE290-123F-4565-9164-39C4925E467B}"):
                try:
                    v, _ = winreg.QueryValueEx(chiave, valore)
                    candidati.insert(0, os.path.expandvars(v))
                except OSError:
                    pass
        except (ImportError, OSError):
            pass
    visti, fuori = set(), []
    for c in candidati:
        k = os.path.normcase(os.path.realpath(c))
        if k in visti:
            continue
        visti.add(k)
        if os.path.isdir(c):
            fuori.append({"cartella": c, "esiste": True,
                          "sincronizzata": bool(re.search(r"(onedrive|dropbox|icloud|clouddocs|google drive|my drive)", c, re.I))})
    return fuori


def data(ts):
    return dt.date.fromtimestamp(ts).isoformat() if ts else None


def misura(cartella):
    n, md, nuovo, vecchio = 0, 0, 0.0, None
    negate = []

    def errore(e):
        if isinstance(e, PermissionError):
            negate.append(getattr(e, "filename", "") or "")
    if not os.access(cartella, os.R_OK | os.X_OK):
        negate.append(cartella)
    for radice, sotto, files in os.walk(cartella, onerror=errore):
        sotto[:] = [d for d in sotto if not salta(radice, d)]
        for f in files:
            try:
                mt = os.stat(os.path.join(radice, f)).st_mtime
            except OSError:
                continue
            n += 1
            if f.lower().endswith(".md"):
                md += 1
            nuovo = max(nuovo, mt)
            vecchio = mt if vecchio is None else min(vecchio, mt)
    if not negate:
        try:
            os.listdir(cartella)
        except PermissionError:
            negate.append(cartella)
    return {"accesso_negato": bool(negate), "sottocartelle_negate": len(negate), "file": n, "note_md": md, "piu_recente": data(nuovo), "piu_vecchio": data(vecchio),
            "giorni_da_ultima_modifica": int((dt.datetime.now().timestamp() - nuovo) // 86400) if nuovo else None}


def main(argv):
    cartelle, file_singoli, prof, come_json, utente = [], [], 2, False, False
    i = 0
    while i < len(argv):
        a = argv[i]
        v = argv[i + 1] if i + 1 < len(argv) else None
        if a == "--profondita" and v:
            try:
                prof = int(v)
            except ValueError:
                print("--profondita vuole un numero", file=sys.stderr); return 2
            i += 2; continue
        if a == "--file" and v:
            file_singoli.append(v); i += 2; continue
        if a == "--json":
            come_json = True
        elif a == "--cartelle-utente":
            utente = True
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            cartelle.append(a)
        i += 1
    if utente:
        elenco = cartelle_utente()
        if come_json:
            print(json.dumps(elenco, ensure_ascii=False, indent=1))
        else:
            for r in elenco:
                print("%s%s" % (r["cartella"], " (sincronizzata)" if r["sincronizzata"] else ""))
            if not elenco:
                print("nessuna delle cartelle solite trovata: chiedi alla persona dove tiene i documenti")
        return 0
    if not cartelle and not file_singoli:
        print(__doc__, file=sys.stderr)
        return 2
    righe = []
    for c in cartelle:
        c = os.path.expanduser(c)
        if not os.path.isdir(c):
            righe.append({"cartella": c, "esiste": False})
            continue
        base = os.path.realpath(c)
        livelli = [(base, 0)]
        while livelli:
            d, liv = livelli.pop(0)
            r = {"cartella": d, "esiste": True}
            r.update(misura(d))
            righe.append(r)
            if liv < prof - 1:
                try:
                    figli = sorted(x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x)) and not salta(d, x))
                except OSError:
                    figli = []
                livelli[0:0] = [(os.path.join(d, x), liv + 1) for x in figli]
    for f in file_singoli:
        p = os.path.expanduser(f)
        if os.path.isfile(p):
            st = os.stat(p)
            righe.append({"file": p, "esiste": True, "modificato": data(st.st_mtime), "byte": st.st_size})
        else:
            righe.append({"file": p, "esiste": False})
    for r in righe:
        for k in ("cartella", "file"):
            if isinstance(r.get(k), str):
                r[k] = percorso_sicuro(r[k])
    if come_json:
        print(json.dumps(righe, ensure_ascii=False, indent=1))
        return 0
    for r in righe:
        if "cartella" in r:
            if not r["esiste"]:
                print("%s: non esiste" % r["cartella"])
            elif r["accesso_negato"] and not r["file"]:
                print("%s: accesso negato dal sistema (su Mac: Impostazioni > Privacy e sicurezza > File e cartelle), non e' vuota" % r["cartella"])
            else:
                if r["accesso_negato"]:
                    print("%s: attenzione, %d sottocartelle con accesso negato: i numeri sotto sono parziali" % (
                        r["cartella"], r["sottocartelle_negate"]))
                print("%s: %d file, %d .md, piu' recente %s (%s giorni fa), piu' vecchio %s" % (
                    r["cartella"], r["file"], r["note_md"], r["piu_recente"], r["giorni_da_ultima_modifica"], r["piu_vecchio"]))
        else:
            print("%s: %s" % (r["file"], ("modificato %s, %d byte" % (r["modificato"], r["byte"])) if r["esiste"] else "non esiste"))
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
