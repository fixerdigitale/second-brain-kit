#!/usr/bin/env python3
"""Controllo mensile degli strumenti presi da fuori. NON aggiorna niente: scrive una nota con cosa è
cambiato a monte, così decidi tu se e quando aggiornare.

Cosa guarda:
  - ogni cartella installata con git clone (di serie: le skill in ~/.claude/skills/ e le cartelle che
    aggiungi in CARTELLE_EXTRA): commit nuovi a monte e quali file "sensibili" sono cambiati
    (hook, script di installazione, impostazioni, file che lanciano comandi);
  - se c'è npm: i pacchetti installati in globale che hanno una versione nuova (npm outdated -g).

Cosa NON fa: git pull, npm update, installazioni. L'unica cosa che tocca è `git fetch`, che scarica la
storia nuova accanto alla tua senza cambiare i file che usi.

Uso:  python3 controlla_aggiornamenti.py            (Windows: py controlla_aggiornamenti.py)
La nota va in CARTELLA_NOTE/aggiornamenti-AAAA-MM.md.
"""
import datetime
import json
import pathlib
import shutil
import subprocess
import sys

# --- da configurare -------------------------------------------------------
CARTELLA_NOTE = pathlib.Path("~/<cartella-vault>/controlli").expanduser()
CARTELLE_SKILL = pathlib.Path("~/.claude/skills").expanduser()
CARTELLE_EXTRA = [
    # pathlib.Path("~/strumenti/<repo-clonata>").expanduser(),
]
# ---------------------------------------------------------------------------

# Parti di percorso che, se cambiano, chiedono una rilettura prima di aggiornare.
SENSIBILI = ("hook", "setup", "install", "bin/", "scripts/", "settings", ".sh", ".ps1", "package.json",
             "requirements", "pyproject", "mcp", "config")


def git(cartella, *argomenti, timeout=120):
    return subprocess.run(["git", "-C", str(cartella), *argomenti], capture_output=True, text=True,
                          timeout=timeout)


def controlla_repo(cartella):
    righe = [f"## {cartella.name}", ""]
    url = git(cartella, "remote", "get-url", "origin").stdout.strip() or "(nessun remoto)"
    righe.append(f"- Fonte: {url}")
    locale = git(cartella, "rev-parse", "HEAD").stdout.strip()
    f = git(cartella, "fetch", "-q", "origin")
    if f.returncode != 0:
        righe += [f"- Non riesco a leggere la fonte (fetch fallito). Installata: `{locale[:7]}`.", ""]
        return righe, False
    monte = git(cartella, "rev-parse", "@{u}").stdout.strip() or git(cartella, "rev-parse", "FETCH_HEAD").stdout.strip()
    righe.append(f"- Installata: `{locale[:7]}`. A monte: `{monte[:7]}`.")
    if not monte or monte == locale:
        righe += ["- Nessun cambiamento.", ""]
        return righe, False
    nuovi = git(cartella, "rev-list", "--count", f"{locale}..{monte}").stdout.strip() or "?"
    file_cambiati = git(cartella, "diff", "--name-only", locale, monte).stdout.splitlines()
    sensibili = [x for x in file_cambiati if any(s in x.lower() for s in SENSIBILI)]
    righe.append(f"- **Cambiato a monte**: {nuovi} commit nuovi, {len(file_cambiati)} file.")
    if sensibili:
        righe.append("- File da rileggere prima di aggiornare (script, hook, impostazioni):")
        righe += [f"  - `{x}`" for x in sensibili[:30]]
    righe.append(f"- Per vedere cosa cambia: `git -C \"{cartella}\" log --oneline {locale[:7]}..{monte[:7]}`")
    righe.append("")
    return righe, True


def controlla_npm():
    if not shutil.which("npm"):
        return []
    r = subprocess.run(["npm", "outdated", "-g", "--json"], capture_output=True, text=True, timeout=180,
                       shell=sys.platform == "win32")  # su Windows npm è un .cmd; nessun dato esterno nel comando
    try:
        dati = json.loads(r.stdout or "{}")
    except ValueError:
        return ["## Pacchetti npm globali", "", "- Non riesco a leggere l'elenco.", ""]
    righe = ["## Pacchetti npm globali", ""]
    if not dati:
        return righe + ["- Tutti all'ultima versione.", ""]
    for nome, v in sorted(dati.items()):
        righe.append(f"- `{nome}`: hai {v.get('current', '?')}, c'è {v.get('latest', '?')}")
    return righe + [""]


def main() -> int:
    oggi = datetime.date.today()
    repo = []
    if CARTELLE_SKILL.is_dir():
        repo += [d for d in sorted(CARTELLE_SKILL.iterdir()) if (d / ".git").exists()]
    repo += [d for d in CARTELLE_EXTRA if (d / ".git").exists()]

    righe = [f"# Controllo mensile degli strumenti presi da fuori — {oggi:%d/%m/%Y}", "",
             "_Non è stato aggiornato niente. Questa è solo la lista di cosa è cambiato a monte._", ""]
    cambiati = 0
    for d in repo:
        try:
            r, cambiato = controlla_repo(d)
        except subprocess.TimeoutExpired:
            r, cambiato = [f"## {d.name}", "", "- Troppo lento, salto.", ""], False
        righe += r
        cambiati += cambiato
    if not repo:
        righe += ["Nessuna cartella installata con git clone trovata.", ""]
    righe += controlla_npm()
    righe += ["## Prima di aggiornare qualcosa", "",
              "1. Leggi i commit nuovi e i file sensibili elencati sopra.",
              "2. Se cambiano script, hook o impostazioni, rifai il controllo di sicurezza (scheda sicurezza-scan-prima-di-installare).",
              "3. Fai una copia datata o un commit della cartella, poi aggiorna una cosa alla volta.", ""]

    CARTELLA_NOTE.mkdir(parents=True, exist_ok=True)
    nota = CARTELLA_NOTE / f"aggiornamenti-{oggi:%Y-%m}.md"
    nota.write_text("\n".join(righe), encoding="utf-8")
    print(f"Nota scritta: {nota} ({len(repo)} cartelle controllate, {cambiati} cambiate a monte)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
