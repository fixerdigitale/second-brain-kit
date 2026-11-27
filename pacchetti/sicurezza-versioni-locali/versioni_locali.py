#!/usr/bin/env python3
"""Versioni locali di pagine e documenti, senza GitHub.

Ogni volta che gira fa un commit di quello che è cambiato nelle cartelle che scegli (pagine HTML,
report, documenti in Markdown). Nessun remoto, nessun push: la storia resta sul tuo PC.
Il .git sta FUORI dalla cartella (in CARTELLA_STORIA), così non finisce in un sito pubblicato
né nella sincronizzazione di Drive o OneDrive.

Uso:
  python3 versioni_locali.py                       commit di tutte le cartelle (lo lancia il pianificatore)
  python3 versioni_locali.py "messaggio"           commit a mano, con un messaggio tuo
  python3 versioni_locali.py storia <nome> <file>  le versioni di un file (nome = chiave in CARTELLE)
  python3 versioni_locali.py recupera <nome> <commit> <file> <dove-salvarlo>
                                                   salva una versione vecchia accanto, senza toccare l'originale
Su Windows: py versioni_locali.py ...
"""
import datetime
import pathlib
import subprocess
import sys

# --- da configurare -------------------------------------------------------
CARTELLE = {
    "pagine": pathlib.Path("~/<cartella-pagine>").expanduser(),
    "documenti": pathlib.Path("~/<cartella-documenti>").expanduser(),
}
CARTELLA_STORIA = pathlib.Path("~/.versioni-locali").expanduser()
ESTENSIONI = {".html", ".htm", ".css", ".js", ".json", ".md", ".svg", ".txt", ".csv", ".yaml", ".yml"}
MAX_MB = 5
# ---------------------------------------------------------------------------

ESCLUSI = {".git", "node_modules", ".obsidian", "__pycache__", ".trash"}
NOMI_VIETATI = (".env", ".pem", ".key", "id_rsa", "credentials", "secrets")


def git(nome, *argomenti):
    opz = [f"--git-dir={CARTELLA_STORIA / (nome + '.git')}", f"--work-tree={CARTELLE[nome]}"]
    return subprocess.run(["git", *opz, *argomenti], capture_output=True, text=True)


def prepara(nome):
    git_dir = CARTELLA_STORIA / (nome + ".git")
    if not git_dir.exists():
        CARTELLA_STORIA.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "init", "-q", "--bare", str(git_dir)], check=True)
        subprocess.run(["git", f"--git-dir={git_dir}", "config", "core.bare", "false"], check=True)
    if git(nome, "remote").stdout.strip():
        return "ha un remoto: questo repo non deve andare online, toglilo con `git remote remove`"
    return ""


def file_da_tenere(radice):
    for f in radice.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in ESTENSIONI:
            continue
        rel = f.relative_to(radice)
        if ESCLUSI & set(rel.parts) or any(v in f.name.lower() for v in NOMI_VIETATI):
            continue
        if f.stat().st_size > MAX_MB * 1024 * 1024:
            continue
        yield rel.as_posix()


def commit(nome, messaggio):
    radice = CARTELLE[nome]
    if not radice.is_dir():
        return f"{nome}: cartella non trovata ({radice}), salto", True
    problema = prepara(nome)
    if problema:
        return f"{nome}: FERMATO, {problema}", False
    git(nome, "add", "-u")  # registra i file cancellati o cambiati già seguiti
    elenco = list(file_da_tenere(radice))
    for i in range(0, len(elenco), 200):  # a gruppi, per non superare la lunghezza massima del comando
        git(nome, "add", "--", *elenco[i:i + 200])
    if git(nome, "diff", "--cached", "--quiet").returncode == 0:
        return f"{nome}: niente di nuovo", True
    r = git(nome, "-c", "user.name=Versioni locali", "-c", "user.email=versioni@localhost",
            "commit", "-q", "-m", messaggio)
    if r.returncode != 0:
        return f"{nome}: commit FALLITO: {r.stderr.strip()[:200]}", False
    stat = git(nome, "show", "--stat", "--format=", "HEAD").stdout.strip().splitlines()
    return f"{nome}: {git(nome, 'log', '-1', '--format=%h').stdout.strip()} {stat[-1] if stat else ''}", True


def main() -> int:
    a = sys.argv[1:]
    if a and a[0] == "storia" and len(a) == 3:
        print(git(a[1], "log", "--format=%h  %ad  %s", "--date=format:%d/%m/%Y %H:%M", "--", a[2]).stdout
              or "Nessuna versione per questo file.")
        return 0
    if a and a[0] == "recupera" and len(a) == 5:
        r = git(a[1], "show", f"{a[2]}:{a[3]}")
        if r.returncode != 0:
            print("Non trovo quella versione: " + r.stderr.strip()[:200])
            return 1
        dest = pathlib.Path(a[4]).expanduser()
        if dest.exists():
            print(f"{dest} esiste già: scegli un altro nome, non sovrascrivo.")
            return 1
        dest.write_text(r.stdout, encoding="utf-8")
        print(f"Versione {a[2]} salvata in {dest}. L'originale non è stato toccato.")
        return 0
    messaggio = a[0] if a else f"versioni automatiche {datetime.datetime.now():%d/%m/%Y %H:%M}"
    ok = True
    for nome in CARTELLE:
        riga, esito = commit(nome, messaggio)
        print(riga)
        ok = ok and esito
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
