#!/usr/bin/env python3
"""Cerca segreti (chiavi, token, password) in cartelle o file, in sola lettura.

Stampa SOLO righe nella forma  file:riga:NOME[,NOME...]
una riga per ogni riga sospetta (una chiave = una riga, anche se la riconoscono
due forme). NOME e' il nome della variabile (es. OPENAI_API_KEY), la parola che
l'annuncia (es. password) oppure il tipo riconosciuto (es. chiave-privata).
Il valore non viene mai stampato, nemmeno in parte.

Riga 0 = il NOME del file fa pensare a credenziali (password.txt, accessi.docx...):
il file va guardato dalla persona, anche se dentro non si e' riconosciuto niente.
Se un segreto riconoscibile sta nel nome di un file o di una cartella, il percorso
si stampa con quel pezzo sostituito da [OSCURATO] e la riga 0 dice segreto-nel-nome.
Nei .csv/.tsv una colonna con un nome sensibile (password, token...) rende
sospette tutte le righe che hanno un valore in quella colonna.

Legge anche il testo dei documenti Office (.docx, .xlsx, .pptx, .odt, .ods):
lì «riga» vuol dire paragrafo o riga del foglio. I PDF non si leggono: il loro
numero si scrive alla fine, perche' «nessun segreto» non vuol dire «guardato tutto».

Dentro una cartella .claude salta le cartelle del programma e dei plugin
(plugins, cache, tmp, ...) e le sessioni (projects): le sessioni si guardano
solo con --con-sessioni, oppure indicando direttamente ~/.claude/projects/<cartella>,
e solo con il consenso della persona.

Uso:
  cerca_segreti.py <cartella-o-file> [altre...] [--max-mb 2] [--riassunto]
                   [--con-sessioni] [--escludi nome1,nome2]

  --riassunto     stampa solo il totale per file (file:conteggio), utile per le
                  sessioni di Claude Code (~/.claude/projects/<cartella>/*.jsonl).
  --con-sessioni  dentro ~/.claude guarda anche projects/ (le sessioni).
  --escludi       nomi di cartelle in piu' da saltare, separati da virgola.

Alla fine scrive su stderr un riassunto: righe trovate, file con il nome
sospetto, documenti non letti.

Codici di uscita: 0 nessun segreto, 1 trovato qualcosa, 2 errore.
Solo libreria standard di Python 3. Funziona su Mac, Windows e Linux.
"""
import html
import os
import re
import sys
import zipfile

SALTA_CARTELLE = {
    ".git", "node_modules", ".venv", "venv", "__pycache__", ".cache",
    ".Trash", "$RECYCLE.BIN", ".npm", ".cargo", "site-packages",
}
# Dentro una cartella .claude: file del programma, dei plugin e copie temporanee.
SALTA_IN_CLAUDE = {
    "plugins", "cache", "file-history", "shell-snapshots", "tmp", "backups", "todos",
    "statsig", "debug", "ide", "paste-cache", "session-env", "telemetry", "projects",
}
SALTA_ESTENSIONI = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".zip", ".gz",
    ".tar", ".7z", ".mp3", ".mp4", ".mov", ".wav", ".m4a", ".ogg", ".woff",
    ".woff2", ".ttf", ".otf", ".exe", ".dll", ".so", ".dylib", ".bin",
    ".sqlite", ".db", ".pyc", ".class", ".jar", ".psd", ".ai", ".heic",
}
OFFICE = {".docx", ".xlsx", ".pptx", ".odt", ".ods", ".odp", ".docm", ".xlsm"}
NON_LETTI = {".pdf", ".doc", ".xls", ".ppt", ".rtf", ".pages", ".numbers", ".key"}

# Nome del file che fa pensare a credenziali: la parola e' la prima o l'ultima del nome
# («password.txt», «Accessi.docx», «elenco-password.md»), non in mezzo a un titolo.
_PAROLE_FILE = r"(?:password|passwords|passw|pwd|credenziali|credenziale|credentials?|accessi|chiavi|chiave|keys|secrets?|segreti)"
NOME_FILE_SOSPETTO = re.compile(
    r"^" + _PAROLE_FILE + r"(?:[-_ .]|$)|[-_ ]" + _PAROLE_FILE + r"$|\.kdbx$|^id_rsa$|^id_ed25519$|\.pem$|"
    r"^\.env(?:\.(?!example|sample|template)\w+)?$", re.I)


def nome_sospetto(nome_file):
    radice = nome_file if nome_file.startswith(".env") else os.path.splitext(nome_file)[0]
    return bool(NOME_FILE_SOSPETTO.search(radice) or NOME_FILE_SOSPETTO.search(nome_file))


# Forme riconoscibili: (tipo, espressione). L'espressione non viene mai stampata.
FORME = [
    ("chiave-privata", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP |ENCRYPTED )?PRIVATE KEY")),
    ("chiave-anthropic", re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}")),
    ("chiave-openai", re.compile(r"\bsk-(?!ant-)(?:proj-|svcacct-)?[A-Za-z0-9_\-]{32,}")),
    ("token-github", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{40,}")),
    ("token-slack", re.compile(r"\bxox[abprse]-[A-Za-z0-9\-]{10,}")),
    ("chiave-aws", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("chiave-google", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("chiave-stripe", re.compile(r"\b[sr]k_live_[0-9A-Za-z]{20,}")),
    ("token-notion", re.compile(r"\b(?:secret|ntn)_[A-Za-z0-9]{30,}")),
    ("token-jwt", re.compile(r"\beyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}")),
    ("url-con-password", re.compile(r"[a-z][a-z0-9+.\-]*://[^/\s:@]+:[^/\s:@]{3,}@[^\s]+", re.I)),
]

# Parole che annunciano un segreto. Si cercano OVUNQUE nella riga (anche dentro
# un JSON, un URL o il testo di una sessione), non solo all'inizio.
NOME_SENSIBILE = re.compile(
    r"(api[_\-.]?key|apikey|secret|token|passw(?:or)?d|passwd|passcode|password|"
    r"(?<![A-Za-z])pass(?![A-Za-z])|(?<![A-Za-z])passw(?![A-Za-z])|(?<![A-Za-z])pwd(?![A-Za-z])|(?<![A-Za-z])psw(?![A-Za-z])|"
    r"(?<![A-Za-z])pin(?![A-Za-z])|parola d'ordine|parola[_\-.]?chiave|private[_\-.]?key|"
    r"access[_\-.]?key|client[_\-.]?secret|auth[_\-.]?key|bearer|credenzial\w*|"
    r"(?<![A-Za-z])wi-?fi(?![A-Za-z])|codice di accesso|home[ _\-]?banking|internet[ _\-]?banking)",
    re.I)
# parole dove un valore di sole lettere puo' essere una password vera
TIPO_PASSWORD = re.compile(r"(pass|pwd|psw|parola|wi-?fi|codice|pin)", re.I)

# Dopo il nome: qualche parola (max 25 caratteri), poi : = => e il valore.
DOPO_SEPARATORE = re.compile(r"""^[^\n:=()]{0,25}?(?:=>|[:=])\s*["'`]?(?P<v>[^\s"'`,;&<>()\[\]{}]+)""")
# Password per app di Google: quattro gruppi di 4 lettere.
APP_PASSWORD = re.compile(r"""^[^\n:=()]{0,25}?[:=]\s*["']?(?P<v>[a-z]{4} [a-z]{4} [a-z]{4} [a-z]{4})\b""")
# Prosa: «la password del CRM è X», «password di wordpress è X», «my password is X».
IN_PROSA = re.compile(
    r"""^\s+(?:(?:del|della|dello|dei|di|da|per|of|for|the|il|la|lo|mia|mio|my|nuova|new)\s+(?:\S+\s+)?){0,2}"""
    r"""(?:è|\\u00e8|e'|e`|é|is|vale|era|was)\s+["'`]?(?P<v>\S+)""", re.I)
# Subito dopo, senza separatore: la parola, uno spazio e il valore (oppure «Bearer» e il token).
SUBITO = re.compile(r"""^\s+["'`]?(?P<v>\S{8,})""")

SEGNAPOSTO = re.compile(
    r"^(<.*|\$\{?.*|\{\{.*|%.*%|x{3,}.*|\*{3,}.*|•+|your[_\-].*|tuo[_\-].*|tua[_\-].*|example.*|esempio.*|"
    r"changeme|change_me|placeholder|dummy|test|none|null|nil|true|false|undefined|string|str|int|"
    r"process\.env.*|os\.environ.*|getenv.*|env\(.*|\.\.\..*|…|redacted.*|oscurat.*|\[oscurat.*|"
    r"required|optional|obbligatori.*|facoltativ.*|vuot.*|empty|segreto|secret|password|token)$",
    re.I)
PUNTEGGIATURA_FINALE = ".,;:!?)]}\"'`"


def sembra_valore(v, solo_lettere_ok=False):
    v = v.rstrip(PUNTEGGIATURA_FINALE) if len(v.rstrip(PUNTEGGIATURA_FINALE)) >= 6 else v
    if SEGNAPOSTO.match(v):
        return False
    if len(v) < 8:
        return False
    ha_cifre = any(c.isdigit() for c in v)
    ha_lettere = any(c.isalpha() for c in v)
    if ha_cifre and ha_lettere:
        return True
    # lungo ma fatto di parole con trattini (uno slug, un nome di file): non e' un segreto
    if len(v) >= 20 and not re.fullmatch(r"[a-z]+(?:[-_.][a-z]+)+", v):
        return True
    # per le password: anche solo lettere, ma almeno 8 e senza aria di parola comune
    return solo_lettere_ok and v.isalpha() and len(v) >= 8


def nome_variabile(riga, m):
    """Il nome intero che contiene la parola sensibile (OPENAI_API_KEY, db_pass...)."""
    i, j = m.start(), m.end()
    while i > 0 and (riga[i - 1].isalnum() or riga[i - 1] in "_-."):
        i -= 1
    while j < len(riga) and (riga[j].isalnum() or riga[j] in "_-."):
        j += 1
    nome = riga[i:j].strip("_-.")
    if not nome or " " in m.group(0):
        nome = m.group(0)
    if nome.islower() or not re.search(r"[_A-Z]", nome):
        nome = nome.lower()
    return nome[:60]


def _pezzo_con_segreto(pezzo):
    """True se il nome di un file o di una cartella contiene un'assegnazione con un valore
    («password=Fint0…», «token_ab12…»): la forma riconoscibile da sola la copre FORME."""
    radice = os.path.splitext(pezzo)[0] if not pezzo.startswith(".") else pezzo
    return bool(nomi_in_riga(radice) or nomi_in_riga(pezzo))


def segreto_nel_percorso(p):
    """True se il percorso (nomi di cartelle o del file) contiene un segreto riconoscibile."""
    if any(espr.search(p) for _, espr in FORME):
        return True
    return any(_pezzo_con_segreto(x) for x in re.split(r"[\\/]", p) if x)


def percorso_sicuro(p):
    """Il percorso con le parti che sembrano segreti sostituite da [OSCURATO]."""
    for _, espr in FORME:
        p = espr.sub("[OSCURATO]", p)
    # un nome con «password=valore» o simili: si oscura tutto quel pezzo del percorso
    pezzi = re.split(r"([\\/])", p)
    return "".join("[OSCURATO]" if x not in ("/", "\\") and x and _pezzo_con_segreto(x) else x
                   for x in pezzi)


def nomi_in_riga(riga):
    trovati = []
    for tipo, espr in FORME:
        if espr.search(riga):
            trovati.append(tipo)
    for m in NOME_SENSIBILE.finditer(riga):
        resto = riga[m.end():]
        pw = bool(TIPO_PASSWORD.search(m.group(0)))
        ok = False
        a = DOPO_SEPARATORE.match(resto)
        if a and sembra_valore(a.group("v"), solo_lettere_ok=pw):
            ok = True
        elif APP_PASSWORD.match(resto):
            ok = True
        else:
            b = IN_PROSA.match(resto)
            if b and sembra_valore(b.group("v")):
                ok = True
            else:
                c = SUBITO.match(resto)
                if c and (pw or m.group(0).lower() == "bearer") and sembra_valore(c.group("v")) \
                        and any(ch.isdigit() for ch in c.group("v")):
                    ok = True
        if ok:
            trovati.append(nome_variabile(riga, m))
    visti, fuori = set(), []
    for t in trovati:
        if t.lower() not in visti:
            visti.add(t.lower())
            fuori.append(t)
    return fuori


def _testo_xml(xml, a_capo):
    xml = re.sub(a_capo, "\n", xml)
    xml = re.sub(r"<(?:w:tab|w:br|text:tab|text:line-break)[^>]*/>", " ", xml)
    testo = re.sub(r"<[^>]+>", "", xml)
    return html.unescape(testo)


def righe_office(percorso):
    """Testo di un documento Office/OpenDocument, una riga per paragrafo o riga del foglio."""
    est = os.path.splitext(percorso)[1].lower()
    with zipfile.ZipFile(percorso) as z:
        nomi = z.namelist()
        if est in (".docx", ".docm"):
            parti = [n for n in nomi if re.match(r"word/(document|header\d*|footer\d*|footnotes|comments)\.xml$", n)]
            testo = "".join(_testo_xml(z.read(n).decode("utf-8", "replace"), r"</w:p>") + "\n" for n in parti)
            return testo.splitlines()
        if est == ".pptx":
            parti = sorted(n for n in nomi if re.match(r"ppt/(slides/slide|notesSlides/notesSlide)\d+\.xml$", n))
            testo = "".join(_testo_xml(z.read(n).decode("utf-8", "replace"), r"</a:p>") + "\n" for n in parti)
            return testo.splitlines()
        if est in (".xlsx", ".xlsm"):
            condivise = []
            if "xl/sharedStrings.xml" in nomi:
                xml = z.read("xl/sharedStrings.xml").decode("utf-8", "replace")
                for si in re.findall(r"<si>(.*?)</si>", xml, re.S):
                    condivise.append(html.unescape(re.sub(r"<[^>]+>", "", si)))
            righe = []
            for n in sorted(x for x in nomi if re.match(r"xl/worksheets/sheet\d+\.xml$", x)):
                xml = z.read(n).decode("utf-8", "replace")
                for riga in re.findall(r"<row[^>]*>(.*?)</row>", xml, re.S):
                    celle = []
                    for attr, dentro in re.findall(r"<c([^>]*)>(.*?)</c>", riga, re.S):
                        v = re.search(r"<v>(.*?)</v>", dentro, re.S)
                        t = re.search(r"<t[^>]*>(.*?)</t>", dentro, re.S)
                        if 't="s"' in attr and v:
                            try:
                                celle.append(condivise[int(v.group(1))])
                            except (ValueError, IndexError):
                                pass
                        elif t:
                            celle.append(html.unescape(t.group(1)))
                        elif v:
                            celle.append(html.unescape(v.group(1)))
                    # celle vicine unite con «: » cosi' «Password | Venditore88» si riconosce
                    righe.append(" : ".join(celle))
            return righe
        # OpenDocument
        if "content.xml" in nomi:
            return _testo_xml(z.read("content.xml").decode("utf-8", "replace"),
                              r"</text:p>|</text:h>|</table:table-row>").splitlines()
    return []


def file_da_guardare(radice, escludi=(), con_sessioni=False):
    if os.path.isfile(radice):
        yield radice
        return
    salta = SALTA_CARTELLE | set(escludi)
    in_claude = SALTA_IN_CLAUDE - ({"projects"} if con_sessioni else set())
    for cartella, sottocartelle, files in os.walk(radice):
        base = os.path.basename(cartella)
        # di .git si guarda solo config: un token nell'indirizzo del remoto
        # (utente e token prima della chiocciola) sta li' in chiaro
        if ".git" in sottocartelle and ".git" not in escludi:
            conf = os.path.join(cartella, ".git", "config")
            if os.path.isfile(conf):
                yield conf
        sottocartelle[:] = [d for d in sottocartelle
                            if d not in salta and not (base == ".claude" and d in in_claude)]
        for f in files:
            yield os.path.join(cartella, f)


def e_binario(percorso):
    try:
        with open(percorso, "rb") as fh:
            return b"\0" in fh.read(4096)
    except OSError:
        return True


def righe_con_segreti(p, limite=2 * 1024 * 1024, conti=None):
    """Genera (numero_riga, [nomi]) per un file. conti: dizionario per i file non letti."""
    est = os.path.splitext(p)[1].lower()
    if conti is None:
        conti = {}
    if est in NON_LETTI:
        conti["non_letti"] = conti.get("non_letti", 0) + 1
        return
    if est in OFFICE:
        try:
            righe = righe_office(p)
        except (zipfile.BadZipFile, OSError, KeyError, RuntimeError):
            conti["office_rotti"] = conti.get("office_rotti", 0) + 1
            return
        conti["office_letti"] = conti.get("office_letti", 0) + 1
        for n, riga in enumerate(righe, 1):
            nomi = nomi_in_riga(riga)
            if nomi:
                yield n, nomi
        return
    if est in SALTA_ESTENSIONI:
        return
    try:
        dim = os.path.getsize(p)
    except OSError:
        return
    # le sessioni .jsonl sono grandi: le guardiamo comunque, riga per riga
    if dim > limite and not p.endswith(".jsonl"):
        conti["troppo_grandi"] = conti.get("troppo_grandi", 0) + 1
        return
    if e_binario(p):
        return
    try:
        with open(p, encoding="utf-8", errors="replace") as fh:
            colonne = {}
            for n, riga in enumerate(fh, 1):
                nomi = nomi_in_riga(riga)
                if est in (".csv", ".tsv"):
                    sep = "\t" if est == ".tsv" else (";" if riga.count(";") > riga.count(",") else ",")
                    celle = [c.strip().strip('"') for c in riga.rstrip("\r\n").split(sep)]
                    if n == 1:
                        # intestazione: le colonne con un nome sensibile (password, token...)
                        colonne = {i: c for i, c in enumerate(celle)
                                   if NOME_SENSIBILE.search(c) or re.fullmatch(r"pw|psw|pwd", c.strip(), re.I)}
                        continue
                    for i, nome_col in colonne.items():
                        if i < len(celle) and len(celle[i]) >= 4 and not SEGNAPOSTO.match(celle[i]) \
                                and nome_col not in nomi:
                            nomi.append(nome_col[:60])
                if nomi:
                    yield n, nomi
    except OSError:
        return


def main(argv):
    args, max_mb, riassunto, con_sessioni, escludi = [], 2.0, False, False, []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--max-mb" and i + 1 < len(argv):
            try:
                max_mb = float(argv[i + 1])
            except ValueError:
                print("--max-mb vuole un numero", file=sys.stderr)
                return 2
            i += 2
            continue
        if a == "--escludi" and i + 1 < len(argv):
            escludi += [x.strip() for x in argv[i + 1].split(",") if x.strip()]
            i += 2
            continue
        if a == "--riassunto":
            riassunto = True
        elif a == "--con-sessioni":
            con_sessioni = True
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            args.append(a)
        i += 1
    if not args:
        print(__doc__, file=sys.stderr)
        return 2

    righe_trovate, nomi_sospetti, conti = 0, 0, {}
    limite = max_mb * 1024 * 1024
    for radice in args:
        radice = os.path.expanduser(radice)
        if not os.path.exists(radice):
            print("non trovato: " + percorso_sicuro(radice), file=sys.stderr)
            continue
        for p in file_da_guardare(radice, escludi, con_sessioni):
            # il percorso stampato non porta mai un segreto, nemmeno nel nome del file
            ps = percorso_sicuro(p)
            if segreto_nel_percorso(p):
                nomi_sospetti += 1
                if not riassunto:
                    print("%s:0:segreto-nel-nome" % ps)
            elif nome_sospetto(os.path.basename(p)):
                nomi_sospetti += 1
                if not riassunto:
                    print("%s:0:nome-del-file" % ps)
            conteggio = 0
            for n, nomi in righe_con_segreti(p, limite, conti):
                conteggio += 1
                if not riassunto:
                    print("%s:%d:%s" % (ps, n, ",".join(nomi)))
            righe_trovate += conteggio
            if riassunto and conteggio:
                print("%s:%d" % (ps, conteggio))
    note = ["Totale: %d righe con possibili segreti" % righe_trovate]
    if nomi_sospetti:
        note.append("%d file con un nome da credenziali (riga 0): da guardare" % nomi_sospetti)
    if conti.get("office_letti"):
        note.append("%d documenti Office letti" % conti["office_letti"])
    if conti.get("non_letti"):
        note.append("%d file PDF o Office vecchi NON letti: lì dentro non ho guardato" % conti["non_letti"])
    if conti.get("office_rotti"):
        note.append("%d documenti Office che non si aprono: non letti" % conti["office_rotti"])
    if conti.get("troppo_grandi"):
        note.append("%d file sopra %s MB saltati (--max-mb per alzare)" % (conti["troppo_grandi"], max_mb))
    print("; ".join(note) + ".", file=sys.stderr)
    return 1 if (righe_trovate or nomi_sospetti) else 0


def _uscita_utf8():
    for flusso in (sys.stdout, sys.stderr):
        try:
            flusso.reconfigure(encoding="utf-8", errors="backslashreplace")
        except (AttributeError, ValueError):
            pass


if __name__ == "__main__":
    _uscita_utf8()
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        sys.exit(2)
    except Exception as e:  # errore imprevisto: codice 2, mai confuso con «trovato qualcosa»
        print("errore: %s" % e, file=sys.stderr)
        sys.exit(2)
