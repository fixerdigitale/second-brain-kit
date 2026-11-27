#!/usr/bin/env python3
"""Legge le impostazioni di Claude Code senza far passare i segreti nella chat.

~/.claude.json e ~/.claude/settings.json possono contenere token (negli URL dei
connettori, nelle variabili d'ambiente, negli header) e, ~/.claude.json, anche la
cronologia delle richieste. Per questo l'onboarding non li apre con Read: usa
questo script, che stampa solo nomi, conteggi e impostazioni dei permessi.

Uso:
  config_claude.py nomi [--claude-json <file>] [--settings <file>]... [--json]
      Server MCP (connettori): nome, locale o remoto, quante variabili o header ha
      (mai i valori). Impostazioni: chiavi presenti, eventi degli hook, numero di
      regole allow/deny/ask, defaultMode, regole allow larghe, NOMI delle
      variabili d'ambiente.

  config_claude.py aggiungi-deny [--settings <file>] [--sistema auto|mac|windows|linux] [--prova]
      Aggiunge le regole deny del patto a permissions.deny senza togliere niente:
      copia datata <file>.bak-AAAAMMGG-second-brain (con -HHMM se esiste gia'),
      controllo che il file sia JSON valido, scrittura, rilettura. Non stampa mai
      il contenuto del file. --prova mostra solo quante regole aggiungerebbe.

Codici di uscita: 0 fatto, 1 file non valido o non trovato, 2 errore d'uso.
Solo libreria standard di Python 3.
"""
import datetime as dt
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cerca_segreti import percorso_sicuro  # noqa: E402  (anche i nomi passano dall'oscuramento)

COMUNI = [
    "Read(~/.ssh/**)", "Read(~/.aws/**)", "Read(~/.gnupg/**)", "Read(~/.config/gcloud/**)",
    "Read(~/.config/gh/**)", "Read(~/.kube/**)", "Read(~/.docker/config.json)",
    "Read(~/.netrc)", "Read(~/.npmrc)", "Read(**/.env)", "Read(**/.env.*)",
]
PER_SISTEMA = {
    "mac": [
        "Read(~/Library/Keychains/**)",
        "Read(~/Library/Application Support/Google/Chrome/**)",
        "Read(~/Library/Application Support/Firefox/Profiles/**)",
        "Read(~/Library/Safari/**)",
    ],
    "windows": [
        "Read(~/AppData/Local/Google/Chrome/User Data/**)",
        "Read(~/AppData/Local/Microsoft/Edge/User Data/**)",
        "Read(~/AppData/Roaming/Mozilla/Firefox/Profiles/**)",
        "Read(~/AppData/Roaming/Microsoft/Credentials/**)",
    ],
    "linux": [
        "Read(~/.config/google-chrome/**)",
        "Read(~/.mozilla/firefox/**)",
    ],
}
LARGHE = ("Bash(*)", "Bash", "Bash(rm:*)", "Bash(rm *)", "Bash(git push:*)", "Bash(git push *)",
          "Bash(cat:*)", "Bash(cat *)", "Bash(curl:*)", "Bash(curl *)", "Write(**)", "Edit(**)", "Read(**)")


def carica(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def server_mcp(blocco):
    fuori = []
    for nome, cfg in sorted((blocco or {}).items()):
        if not isinstance(cfg, dict):
            continue
        remoto = bool(cfg.get("url")) or cfg.get("type") in ("http", "sse")
        n_segreti = len(cfg.get("env") or {}) + len(cfg.get("headers") or {})
        url = str(cfg.get("url") or "")
        if "?" in url and any(k in url.lower() for k in ("token", "key", "secret", "auth")):
            n_segreti += 1
        fuori.append({"nome": percorso_sicuro(str(nome)), "tipo": "remoto" if remoto else "locale",
                      "variabili_o_header": n_segreti})
    return fuori


def nomi(argv):
    claude_json = os.path.expanduser("~/.claude.json")
    settings, come_json = [], False
    i = 0
    while i < len(argv):
        a, v = argv[i], (argv[i + 1] if i + 1 < len(argv) else None)
        if a == "--claude-json" and v:
            claude_json = os.path.expanduser(v); i += 2; continue
        if a == "--settings" and v:
            settings.append(os.path.expanduser(v)); i += 2; continue
        if a == "--json":
            come_json = True
        i += 1
    if not settings:
        settings = [os.path.expanduser("~/.claude/settings.json")]
        cwd = os.getcwd()
        for f in ("settings.json", "settings.local.json"):
            settings.append(os.path.join(cwd, ".claude", f))
    uscita = {"connettori": [], "connettori_per_progetto": 0, "impostazioni": []}
    if os.path.isfile(claude_json):
        try:
            d = carica(claude_json)
            uscita["connettori"] = server_mcp(d.get("mcpServers"))
            for _, prog in (d.get("projects") or {}).items():
                if isinstance(prog, dict):
                    uscita["connettori_per_progetto"] += len(prog.get("mcpServers") or {})
        except (OSError, ValueError):
            uscita["errore_claude_json"] = "non e' JSON valido o non si legge"
    for p in settings:
        if not os.path.isfile(p):
            continue
        r = {"file": p}
        try:
            d = carica(p)
        except (OSError, ValueError):
            r["errore"] = "non e' JSON valido"
            uscita["impostazioni"].append(r)
            continue
        perm = d.get("permissions") or {}
        r["chiavi"] = sorted(d.keys())
        r["hook_per_evento"] = {k: len(v or []) for k, v in (d.get("hooks") or {}).items()}
        r["allow"] = len(perm.get("allow") or [])
        r["deny"] = len(perm.get("deny") or [])
        r["ask"] = len(perm.get("ask") or [])
        r["defaultMode"] = perm.get("defaultMode") or d.get("defaultMode")
        r["allow_larghe"] = [x for x in (perm.get("allow") or []) if x in LARGHE]
        r["deny_su_env"] = any(".env" in x for x in (perm.get("deny") or []))
        r["deny_su_ssh"] = any(".ssh" in x for x in (perm.get("deny") or []))
        r["nomi_variabili_env"] = sorted(percorso_sicuro(str(k)) for k in (d.get("env") or {}).keys())
        r["statusLine"] = "statusLine" in d
        r["plugin_attivi"] = len(d.get("enabledPlugins") or {})
        r["mcp_nel_file"] = server_mcp(d.get("mcpServers"))
        uscita["impostazioni"].append(r)
    if come_json:
        print(json.dumps(uscita, ensure_ascii=False, indent=1))
        return 0
    print("Connettori (MCP) in ~/.claude.json: %d" % len(uscita["connettori"]))
    for c in uscita["connettori"]:
        print("- %s: %s%s" % (c["nome"], c["tipo"],
                              ", con %d variabili/header o token nell'indirizzo (valori non mostrati)" % c["variabili_o_header"]
                              if c["variabili_o_header"] else ""))
    if uscita["connettori_per_progetto"]:
        print("Connettori legati a singoli progetti: %d" % uscita["connettori_per_progetto"])
    for r in uscita["impostazioni"]:
        print("Impostazioni %s:" % r["file"])
        if r.get("errore"):
            print("  " + r["errore"])
            continue
        print("  hook: %s" % (", ".join("%s=%d" % kv for kv in r["hook_per_evento"].items()) or "nessuno"))
        print("  permessi: allow %d, deny %d, ask %d, defaultMode %s" % (r["allow"], r["deny"], r["ask"], r["defaultMode"]))
        if r["allow_larghe"]:
            print("  allow larghe: %s (con queste il «sì» lo garantisce solo il modello, non il programma)" % ", ".join(r["allow_larghe"]))
        if r["defaultMode"] in ("acceptEdits", "bypassPermissions"):
            print("  attenzione: defaultMode %s, le modifiche ai file passano senza domanda" % r["defaultMode"])
        print("  deny su .env: %s; deny su ~/.ssh: %s" % ("si'" if r["deny_su_env"] else "no", "si'" if r["deny_su_ssh"] else "no"))
        if r["nomi_variabili_env"]:
            print("  variabili d'ambiente (solo nomi): %s" % ", ".join(r["nomi_variabili_env"]))
        if r["statusLine"]:
            print("  statusLine: si'")
        if r["plugin_attivi"]:
            print("  plugin attivi: %d" % r["plugin_attivi"])
    return 0


def sistema_attuale():
    if sys.platform == "darwin":
        return "mac"
    if sys.platform.startswith("win") or os.environ.get("MSYSTEM"):
        return "windows"
    return "linux"


def aggiungi_deny(argv):
    p, sistema, prova = os.path.expanduser("~/.claude/settings.json"), "auto", False
    i = 0
    while i < len(argv):
        a, v = argv[i], (argv[i + 1] if i + 1 < len(argv) else None)
        if a == "--settings" and v:
            p = os.path.expanduser(v); i += 2; continue
        if a == "--sistema" and v:
            sistema = v; i += 2; continue
        if a == "--prova":
            prova = True
        i += 1
    if sistema == "auto":
        sistema = sistema_attuale()
    if sistema not in PER_SISTEMA:
        print("--sistema: mac, windows o linux", file=sys.stderr)
        return 2
    regole = COMUNI + PER_SISTEMA[sistema]
    if os.path.exists(p):
        try:
            dati = carica(p)
        except ValueError:
            print("Fermo: %s non e' JSON valido. Non lo tocco." % p, file=sys.stderr)
            return 1
        if not isinstance(dati, dict):
            print("Fermo: %s non ha la forma attesa. Non lo tocco." % p, file=sys.stderr)
            return 1
    else:
        dati = {}
    perm = dati.setdefault("permissions", {})
    if not isinstance(perm, dict):
        print("Fermo: permissions non ha la forma attesa. Non tocco il file.", file=sys.stderr)
        return 1
    deny = perm.setdefault("deny", [])
    nuove = [r for r in regole if r not in deny]
    if prova or not nuove:
        print("%s: %d regole da aggiungere, %d gia' presenti." % (p, len(nuove), len(regole) - len(nuove)))
        return 0
    copia = None
    if os.path.exists(p):
        oggi = dt.datetime.now()
        copia = "%s.bak-%s-second-brain" % (p, oggi.strftime("%Y%m%d"))
        if os.path.exists(copia):
            copia = "%s.bak-%s-second-brain" % (p, oggi.strftime("%Y%m%d-%H%M"))
        if os.path.exists(copia):
            print("Fermo: la copia %s esiste gia'. Riprova fra un minuto." % copia, file=sys.stderr)
            return 1
        shutil.copy2(p, copia)
    deny.extend(nuove)
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or ".", prefix=".settings-", suffix=".json")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(dati, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, p)
    riletto = carica(p)
    mancanti = [r for r in nuove if r not in riletto.get("permissions", {}).get("deny", [])]
    if mancanti:
        print("Errore: dopo la scrittura mancano %d regole. Rimetti la copia %s." % (len(mancanti), copia), file=sys.stderr)
        return 1
    print("Aggiunte %d regole deny a %s (sistema: %s). Niente tolto." % (len(nuove), p, sistema))
    if copia:
        print("Copia prima della modifica: %s" % copia)
    print("Come si toglie: rimetti la copia, oppure cancella solo le righe aggiunte.")
    return 0


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    if argv[0] == "nomi":
        return nomi(argv[1:])
    if argv[0] == "aggiungi-deny":
        return aggiungi_deny(argv[1:])
    print(__doc__, file=sys.stderr)
    return 2


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
