#!/usr/bin/env python3
"""Prova di ripristino: riapre davvero un backup in una cartella temporanea.

Non scrive niente nella cartella di lavoro e non tocca il backup. Copia (o clona)
il backup in una cartella temporanea, controlla cosa c'e', poi cancella la
cartella temporanea.

Uso:
  prova_ripristino.py --sorgente <backup> [--modo auto|claude|documenti]
                      [--originale <cartella>] [--attesi CLAUDE.md,memoria]
                      [--cartella-lavoro <cartella>] [--json] [--tieni]

  <backup> puo' essere:
    - un repository git (indirizzo remoto, oppure una cartella con .git: se ha un
      remoto, si prova il remoto, perche' la copia locale non e' un backup)
    - un file .zip (anche quello del Finder o di Esplora file, con una cartella in cima)
    - una cartella copiata (disco esterno, cartella sincronizzata)

  --modo claude     controlla profilo (CLAUDE.md), memoria e regole.
  --modo documenti  per chi non ha file di Claude: controlla che i documenti ci
                    siano e che i .docx/.xlsx/.pptx si aprano. Con --originale
                    confronta numero e dimensione dei file con la cartella vera.
  --modo auto       (di serie) claude se nella copia c'e' un CLAUDE.md o una
                    memoria, altrimenti documenti.
  --cartella-lavoro di serie la cartella corrente: una «copia» che sta li' dentro
                    (o che la contiene) non e' un backup.

Esiti separati:
  ripristinabile  la copia si riapre e contiene quello che serve
  fuori_dal_pc    true / false / "da confermare" (cartella sincronizzata: va
                  confermato dal sito o da un altro dispositivo)
  pulito          nessun segreto dentro la copia
  riuscito        ripristinabile E fuori_dal_pc == true: solo allora e' «verde»

Codici di uscita: 0 riuscito, 1 non riuscito o da confermare, 2 errore d'uso.
Solo libreria standard di Python 3 (git serve solo per i repository).
"""
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerca_segreti  # noqa: E402

NOMI_MEMORIA = {"memoria", "memory", "vault", "note", "notes"}
NOMI_REGOLE = re.compile(r"(regole[-_ ]?oro|golden[-_ ]?rules|feedback_.*\.md$|correzioni|corrections)", re.I)
SINCRONIZZATE = re.compile(r"(onedrive|dropbox|icloud|mobile documents|google ?drive|my drive|il mio drive|"
                           r"googledrive|pcloud|nextcloud|syncthing)", re.I)
SALTA = {".git", "node_modules", ".venv", "__pycache__", "__MACOSX"}


def esegui(cmd, cwd=None):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never")
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=600, env=env)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return 99, "", str(e)


def e_remoto(s):
    return bool(re.match(r"^(https?://|git@|ssh://)", s))


def e_git(sorgente):
    if e_remoto(sorgente) or sorgente.startswith("file://"):
        return True
    if os.path.isdir(sorgente):
        return os.path.exists(os.path.join(sorgente, ".git")) or os.path.exists(os.path.join(sorgente, "HEAD"))
    return False


def nome_github(sorgente):
    m = re.search(r"github\.com[:/]([^/]+)/([^/\s]+?)(?:\.git)?/?$", sorgente)
    return "%s/%s" % (m.group(1), m.group(2)) if m else None


def oscura_url(u):
    # toglie un eventuale utente:password@ o token=... dall'indirizzo prima di stamparlo
    u = re.sub(r"://[^/@\s]+@", "://[OSCURATO]@", u)
    return re.sub(r"([?&][^=&\s]*(?:token|key|secret|pass)[^=&\s]*=)[^&\s]+", r"\1[OSCURATO]", u, flags=re.I)


def dentro(a, b):
    """True se il percorso a sta dentro b (o coincide)."""
    a, b = os.path.normcase(os.path.realpath(a)), os.path.normcase(os.path.realpath(b))
    return a == b or a.startswith(b.rstrip(os.sep) + os.sep)


def dove_sta(percorso, cartella_lavoro):
    """(fuori_dal_pc, motivo) per una copia che sta su questo computer."""
    if dentro(percorso, cartella_lavoro) or dentro(cartella_lavoro, percorso):
        return False, "e' la cartella di lavoro stessa, o una sua parte: non e' un backup"
    if SINCRONIZZATE.search(os.path.realpath(percorso)):
        return "da confermare", ("cartella sincronizzata: la copia online va confermata dal sito o da un altro "
                                 "dispositivo (una cancellazione qui si sincronizza anche li')")
    try:
        stesso_disco = os.stat(percorso).st_dev == os.stat(os.path.expanduser("~")).st_dev
    except OSError:
        return "da confermare", "non riesco a capire su che disco sta"
    if stesso_disco:
        return False, "sta sullo stesso disco del computer: se il computer si rompe, si perdono tutte e due"
    return "da confermare", "sta su un'altra unita': vale come copia fuori dal PC solo se e' un disco che si stacca e sta altrove"


def radice_utile(dest):
    """Se la copia ha una sola cartella in cima (zip del Finder), usa quella come radice."""
    voci = [v for v in os.listdir(dest) if v not in ("__MACOSX", ".DS_Store")]
    if len(voci) == 1 and os.path.isdir(os.path.join(dest, voci[0])) and voci[0] != ".git":
        return os.path.join(dest, voci[0])
    return dest


def conta(radice):
    claude_md, note, memoria, regole, env, documenti, rotti = [], 0, [], [], [], 0, []
    ha_claude_dir = False
    for cartella, sotto, files in os.walk(radice):
        if ".claude" in sotto:
            ha_claude_dir = True
        sotto[:] = [d for d in sotto if d not in SALTA]
        rel = os.path.relpath(cartella, radice)
        base = os.path.basename(cartella).lower()
        if base in NOMI_MEMORIA:
            memoria.append(rel)
        for f in files:
            p = os.path.join(rel, f) if rel != "." else f
            documenti += 1
            if f == "CLAUDE.md":
                claude_md.append(p)
            if f.endswith(".md"):
                note += 1
            if f == "MEMORY.md":
                memoria.append(p)
            if (NOMI_REGOLE.search(f) or NOMI_REGOLE.search(rel)) and f.endswith(".md"):
                regole.append(p)
            if f == ".env" or (f.startswith(".env.") and not f.endswith((".example", ".sample"))) \
                    or f.endswith((".pem", ".key")) or f in ("id_rsa", "id_ed25519", "credentials.json"):
                env.append(p)
            if os.path.splitext(f)[1].lower() in cerca_segreti.OFFICE:
                try:
                    with zipfile.ZipFile(os.path.join(cartella, f)) as z:
                        if z.testzip() is not None:
                            rotti.append(p)
                except (zipfile.BadZipFile, OSError):
                    rotti.append(p)
    return {"claude_md": claude_md, "note": note, "memoria": sorted(set(memoria)), "regole": regole,
            "env": env, "documenti": documenti, "office_rotti": rotti, "ha_claude_dir": ha_claude_dir}


def misura_cartella(radice):
    n, byte, nuovo = 0, 0, 0.0
    for cartella, sotto, files in os.walk(radice):
        sotto[:] = [d for d in sotto if d not in SALTA]
        for f in files:
            if f in (".DS_Store", "Thumbs.db", "desktop.ini"):
                continue
            try:
                st = os.stat(os.path.join(cartella, f))
            except OSError:
                continue
            n += 1
            byte += st.st_size
            nuovo = max(nuovo, st.st_mtime)
    return n, byte, nuovo


def main(argv):
    sorgente, attesi, come_json, tieni, modo, originale = None, [], False, False, "auto", None
    cartella_lavoro = os.getcwd()
    i = 0
    while i < len(argv):
        a = argv[i]
        v = argv[i + 1] if i + 1 < len(argv) else None
        if a == "--sorgente" and v:
            sorgente = v; i += 2; continue
        if a == "--attesi" and v:
            attesi = [x.strip() for x in v.split(",") if x.strip()]; i += 2; continue
        if a == "--modo" and v:
            modo = v; i += 2; continue
        if a == "--originale" and v:
            originale = os.path.expanduser(v); i += 2; continue
        if a == "--cartella-lavoro" and v:
            cartella_lavoro = os.path.expanduser(v); i += 2; continue
        if a == "--json":
            come_json = True
        elif a == "--tieni":
            tieni = True
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        i += 1
    if not sorgente or modo not in ("auto", "claude", "documenti"):
        print(__doc__, file=sys.stderr)
        return 2
    sorgente = os.path.expanduser(sorgente)

    esito = {"sorgente": oscura_url(sorgente), "data": dt.date.today().isoformat(),
             "problemi": [], "da_sistemare": [], "note": []}
    fuori, motivo_fuori = "da confermare", ""
    tmp = tempfile.mkdtemp(prefix="prova-ripristino-")
    dest = os.path.join(tmp, "ripristino")
    radice = dest
    try:
        if sorgente.lower().endswith(".zip") and os.path.isfile(sorgente):
            esito["tipo"] = "zip"
            fuori, motivo_fuori = dove_sta(sorgente, cartella_lavoro)
            with zipfile.ZipFile(sorgente) as z:
                for nome in z.namelist():
                    finale = os.path.realpath(os.path.join(dest, nome))
                    if not finale.startswith(os.path.realpath(dest) + os.sep) and finale != os.path.realpath(dest):
                        esito["problemi"].append("lo zip contiene un percorso fuori cartella: non lo estraggo")
                        raise RuntimeError("zip non sicuro")
                if z.testzip() is not None:
                    esito["problemi"].append("lo zip e' rovinato: almeno un file non si legge")
                z.extractall(dest)
                date = [dt.datetime(*zi.date_time) for zi in z.infolist() if not zi.is_dir()]
            if date:
                esito["giorni_dall_ultima_modifica"] = (dt.datetime.now() - max(date)).days
            radice = radice_utile(dest)
        elif e_git(sorgente):
            esito["tipo"] = "git"
            da_clonare = sorgente
            if not e_remoto(sorgente):
                locale = sorgente[7:] if sorgente.startswith("file://") else sorgente
                rc, url, _ = esegui(["git", "-C", locale, "remote", "get-url", "origin"])
                if rc == 0 and url and e_remoto(url):
                    da_clonare = url
                    esito["note"].append("il repository locale ha una copia online: provo quella (%s)" % oscura_url(url))
                    rc2, stato, _ = esegui(["git", "-C", locale, "status", "-sb"])
                    if rc2 == 0 and re.search(r"\[(?:ahead|avanti) \d+", stato.splitlines()[0] if stato else ""):
                        esito["problemi"].append("ci sono salvataggi locali non ancora mandati alla copia online")
                elif rc == 0 and url:
                    fuori, motivo_fuori = False, "il remoto del repository e' una cartella sullo stesso PC: non e' un backup fuori dal PC"
                else:
                    fuori, motivo_fuori = False, "repository git sullo stesso PC, senza una copia online: non e' un backup"
            if e_remoto(da_clonare):
                fuori, motivo_fuori = True, "copia online"
            rc, _, err = esegui(["git", "clone", "--quiet", da_clonare, dest])
            if rc != 0:
                esito["problemi"].append("il clone non riesce: " + oscura_url(err.splitlines()[-1] if err else "errore sconosciuto"))
                raise RuntimeError("clone")
            if not [x for x in os.listdir(dest) if x != ".git"]:
                _, rami, _ = esegui(["git", "branch", "-r"], cwd=dest)
                altri = [r.strip() for r in rami.splitlines() if "->" not in r and r.strip()]
                esito["problemi"].append("il clone e' vuoto: il ramo principale della copia online non ha file"
                                         + (" (rami presenti: %d; forse i file stanno su un altro ramo)" % len(altri) if altri else ""))
            rc, data, _ = esegui(["git", "log", "-1", "--format=%cI"], cwd=dest)
            if rc == 0 and data:
                esito["ultimo_salvataggio"] = data
                try:
                    esito["giorni_dall_ultimo_salvataggio"] = (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(data)).days
                except ValueError:
                    pass
            rc, n, _ = esegui(["git", "rev-list", "--count", "HEAD"], cwd=dest)
            if rc == 0 and n.isdigit():
                esito["salvataggi"] = int(n)
            gh = nome_github(da_clonare)
            if gh and shutil.which("gh"):
                rc, vis, _ = esegui(["gh", "repo", "view", gh, "--json", "visibility", "-q", ".visibility"])
                esito["visibilita"] = vis.lower() if rc == 0 and vis else "da confermare"
            else:
                esito["visibilita"] = "da confermare"
            if esito.get("visibilita") == "public":
                esito["da_sistemare"].append("il repository del backup e' PUBBLICO")
        elif os.path.isdir(sorgente):
            esito["tipo"] = "cartella"
            fuori, motivo_fuori = dove_sta(sorgente, cartella_lavoro)
            shutil.copytree(sorgente, dest, symlinks=True,
                            ignore=shutil.ignore_patterns("node_modules", ".venv", "__pycache__"))
            _, _, nuovo = misura_cartella(sorgente)
            if nuovo:
                esito["giorni_dall_ultima_modifica"] = int((dt.datetime.now().timestamp() - nuovo) // 86400)
        else:
            esito["problemi"].append("sorgente non trovata o di tipo sconosciuto")
            raise RuntimeError("sorgente")

        c = conta(radice)
        if modo == "auto":
            modo = "claude" if (c["claude_md"] or c["memoria"] or "CLAUDE.md" in attesi) else "documenti"
        esito["modo"] = modo
        esito["file"] = c["documenti"]
        esito["note_md"] = c["note"]
        if modo == "claude":
            esito["profilo_claude_md"] = len(c["claude_md"])
            esito["memoria"] = c["memoria"][:10]
            esito["regole"] = len(c["regole"])
            if not c["claude_md"]:
                esito["problemi"].append("nel backup non c'e' nessun CLAUDE.md (il profilo)")
            if not c["memoria"] and c["note"] < 5:
                esito["problemi"].append("nel backup non si vede la memoria (nessuna cartella memoria/vault, meno di 5 note)")
            if not c["regole"]:
                esito["note"].append("nessun file di regole o correzioni riconosciuto: da confermare a vista")
            if not c["ha_claude_dir"]:
                esito["note"].append("la cartella ~/.claude (impostazioni, skill personali, memoria automatica) non e' "
                                     "in questa copia: se ti serve, va salvata a parte")
        else:
            if c["documenti"] == 0:
                esito["problemi"].append("la copia e' vuota")
            if c["office_rotti"]:
                esito["problemi"].append("%d documenti Office non si aprono: %s" % (
                    len(c["office_rotti"]), ", ".join(c["office_rotti"][:5])))
        if originale:
            if not os.path.isdir(originale):
                esito["problemi"].append("cartella originale non trovata: " + originale)
            else:
                n_o, b_o, _ = misura_cartella(originale)
                n_c, b_c, _ = misura_cartella(radice)
                esito["confronto"] = {"file_originale": n_o, "file_copia": n_c, "mb_originale": round(b_o / 1048576, 1),
                                      "mb_copia": round(b_c / 1048576, 1)}
                if n_c < n_o:
                    esito["problemi"].append("nella copia mancano %d file rispetto all'originale" % (n_o - n_c))
                elif b_o and b_c < 0.9 * b_o:
                    esito["problemi"].append("la copia pesa meno del 90%% dell'originale (%s MB contro %s MB)" % (
                        esito["confronto"]["mb_copia"], esito["confronto"]["mb_originale"]))
        eta = esito.get("giorni_dall_ultimo_salvataggio", esito.get("giorni_dall_ultima_modifica"))
        if isinstance(eta, int) and eta > 30:
            esito["da_sistemare"].append("la copia e' ferma da %d giorni: quello che hai fatto dopo non c'e'" % eta)
        esito["file_di_segreti"] = c["env"][:20]
        if c["env"]:
            esito["da_sistemare"].append("nel backup ci sono %d file di segreti (.env, chiavi): andrebbero esclusi" % len(c["env"]))
        segreti = 0
        for p in cerca_segreti.file_da_guardare(radice):
            for _n, _nomi in cerca_segreti.righe_con_segreti(p):
                segreti += 1
        esito["segreti_in_chiaro"] = segreti
        if segreti:
            esito["da_sistemare"].append("nel backup ci sono %d righe con possibili segreti in chiaro "
                                         "(lancia cerca-segreti per file e riga)" % segreti)
        for a in attesi:
            if not (os.path.exists(os.path.join(radice, a)) or os.path.exists(os.path.join(dest, a))
                    or any(os.path.exists(os.path.join(radice, d, a)) for d in os.listdir(radice)
                           if os.path.isdir(os.path.join(radice, d)))):
                esito["problemi"].append("manca nel backup: " + a)
    except RuntimeError:
        pass
    except Exception as e:  # errore imprevisto: lo diciamo senza nascondere
        esito["problemi"].append("errore: %s" % e)
    finally:
        if tieni:
            esito["cartella_temporanea"] = dest
        else:
            shutil.rmtree(tmp, ignore_errors=True)

    esito["ripristinabile"] = not esito["problemi"]
    esito["fuori_dal_pc"] = fuori
    if motivo_fuori:
        esito["dove_sta"] = motivo_fuori
    esito["pulito"] = not esito["da_sistemare"]
    esito["riuscito"] = esito["ripristinabile"] and fuori is True
    if come_json:
        print(json.dumps(esito, ensure_ascii=False, indent=2))
    else:
        print("Prova di ripristino del %s" % esito["data"])
        print("Sorgente: %s (%s, modo %s)" % (esito["sorgente"], esito.get("tipo", "?"), esito.get("modo", modo)))
        for k, etichetta in [("file", "file nella copia"), ("profilo_claude_md", "CLAUDE.md trovati"),
                             ("note_md", "note .md"), ("regole", "file di regole/correzioni"),
                             ("segreti_in_chiaro", "righe con possibili segreti"),
                             ("giorni_dall_ultimo_salvataggio", "giorni dall'ultimo salvataggio"),
                             ("giorni_dall_ultima_modifica", "giorni dall'ultima modifica nella copia"),
                             ("visibilita", "visibilita' del repository")]:
            if k in esito:
                print("- %s: %s" % (etichetta, esito[k]))
        if esito.get("memoria"):
            print("- memoria: " + ", ".join(esito["memoria"]))
        if esito.get("confronto"):
            cf = esito["confronto"]
            print("- confronto con l'originale: %d file / %s MB contro %d file / %s MB" % (
                cf["file_copia"], cf["mb_copia"], cf["file_originale"], cf["mb_originale"]))
        print("- fuori dal PC: %s%s" % ({True: "si'", False: "no"}.get(fuori, fuori),
                                         (" (" + motivo_fuori + ")") if motivo_fuori else ""))
        for n in esito["note"]:
            print("  nota: " + n)
        if esito["riuscito"]:
            print("ESITO: ripristino riuscito, copia fuori dal PC")
        elif esito["ripristinabile"]:
            print("ESITO: si riapre, ma %s" % ("non e' un backup fuori dal PC" if fuori is False else "che sia fuori dal PC e' da confermare"))
        else:
            print("ESITO: problemi")
            for pr in esito["problemi"]:
                print("  - " + pr)
        if esito["da_sistemare"]:
            print("Da sistemare (non impedisce il ripristino):")
            for pr in esito["da_sistemare"]:
                print("  - " + pr)
        if tieni:
            print("Cartella temporanea tenuta: " + dest)
    return 0 if esito["riuscito"] else 1


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
