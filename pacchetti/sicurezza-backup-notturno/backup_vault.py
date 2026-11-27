#!/usr/bin/env python3
"""Backup minimo del vault: commit + push su GitHub privato, poi una copia zip datata nella cartella cloud.

Mac, Windows e Linux, solo libreria standard di Python 3. Configura le tre righe qui sotto.

Cosa fa, in ordine:
  1. git add/commit/push nella cartella del vault (se è un repo git e ci sono modifiche).
     Si ferma se fra i file da salvare ce n'è uno che sembra una chiave (.env, .pem, id_rsa...)
     o se `gh` dice che il repo è pubblico;
  2. crea <cartella-cloud>/vault-AAAAMMGG-HHMM.zip (esclusi .git, node_modules, .obsidian/cache);
  3. tiene solo le ultime COPIE_DA_TENERE copie zip, le più vecchie le cancella;
  4. scrive l'esito in <cartella-cloud>/ultimo-backup.txt.

Lo zip NON è cifrato: va bene per un vault di note senza segreti. Se dentro ci sono dati delicati,
usa restic (vedi LEGGIMI.md) al posto del punto 2.

Uso:  python3 backup_vault.py        (su Windows: py backup_vault.py)
"""
import datetime
import json
import pathlib
import shutil
import subprocess
import sys
import zipfile

# --- da configurare -------------------------------------------------------
CARTELLA_VAULT = pathlib.Path("~/<cartella-vault>").expanduser()
# La cartella sincronizzata da Google Drive / OneDrive / iCloud sul tuo PC, per esempio
# Mac: ~/Library/CloudStorage/GoogleDrive-<account>/Il mio Drive/Backup vault
# Windows: G:/Il mio Drive/Backup vault
CARTELLA_CLOUD = pathlib.Path("<cartella-cloud>/Backup vault").expanduser()
COPIE_DA_TENERE = 7
# ---------------------------------------------------------------------------

ESCLUSI = {".git", "node_modules", ".trash", "__pycache__"}
# File che non devono mai finire nel repo: se sono fra quelli da salvare, il commit si ferma.
NOMI_VIETATI = (".env", ".pem", ".key", "id_rsa", "id_ed25519", "credentials", "secrets")


def file_vietati():
    """File pronti per il commit che sembrano chiavi o credenziali (solo i nomi, mai il contenuto)."""
    r = git("diff", "--cached", "--name-only")
    return [f for f in r.stdout.splitlines()
            if any(v in pathlib.Path(f).name.lower() for v in NOMI_VIETATI)]


def repo_pubblico():
    """True se `gh` dice che il repo remoto è pubblico. Senza `gh` non si può sapere: False."""
    if not shutil.which("gh"):
        return False
    r = subprocess.run(["gh", "repo", "view", "--json", "visibility"], cwd=CARTELLA_VAULT,
                       capture_output=True, text=True)
    try:
        return json.loads(r.stdout).get("visibility", "").upper() == "PUBLIC"
    except ValueError:
        return False


def git(*argomenti):
    return subprocess.run(["git", *argomenti], cwd=CARTELLA_VAULT, capture_output=True, text=True)


def passo_git(righe):
    if not (CARTELLA_VAULT / ".git").exists():
        righe.append("git: la cartella non è un repo, salto")
        return True
    git("add", "-A")
    vietati = file_vietati()
    if vietati:
        git("reset", "-q")  # toglie dal commit quello appena aggiunto; i file restano dove sono
        righe.append("git: FERMATO, file che sembrano chiavi pronti per il commit: " + ", ".join(vietati[:10])
                     + ". Aggiungili a .gitignore e rilancia.")
        return False
    if git("diff", "--cached", "--quiet").returncode == 0:
        righe.append("git: niente di nuovo da salvare")
    else:
        ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        r = git("commit", "-m", f"Backup automatico {ora}")
        if r.returncode != 0:
            righe.append("git commit FALLITO: " + r.stderr.strip()[:300])
            return False
        righe.append("git: commit fatto")
    if repo_pubblico():
        righe.append("git: push FERMATO, il repo su GitHub è PUBBLICO. Rendilo privato e rilancia.")
        return False
    r = git("push")
    if r.returncode != 0:
        righe.append("git push FALLITO: " + r.stderr.strip()[:300])
        return False
    righe.append("git: push fatto")
    return True


def passo_zip(righe):
    CARTELLA_CLOUD.mkdir(parents=True, exist_ok=True)
    nome = CARTELLA_CLOUD / f"vault-{datetime.datetime.now():%Y%m%d-%H%M}.zip"
    n = 0
    with zipfile.ZipFile(nome, "w", zipfile.ZIP_DEFLATED) as z:
        for f in CARTELLA_VAULT.rglob("*"):
            if f.name.lower().startswith(".env") or any(v in f.name.lower() for v in NOMI_VIETATI):
                continue  # le chiavi non vanno nello zip: è in chiaro e finisce sul cloud
            if f.is_file() and not (ESCLUSI & set(f.relative_to(CARTELLA_VAULT).parts)):
                z.write(f, f.relative_to(CARTELLA_VAULT))
                n += 1
    # controllo minimo: lo zip si rilegge senza errori
    with zipfile.ZipFile(nome) as z:
        guasto = z.testzip()
    if guasto:
        righe.append(f"zip ROTTO al file {guasto}")
        return False
    righe.append(f"zip: {nome.name}, {n} file, {nome.stat().st_size // 1024} KB")
    copie = sorted(CARTELLA_CLOUD.glob("vault-*.zip"))
    for vecchia in copie[:-COPIE_DA_TENERE]:
        vecchia.unlink()
        righe.append(f"zip: cancellata la copia vecchia {vecchia.name}")
    return True


def main() -> int:
    if not CARTELLA_VAULT.is_dir():
        print(f"Non trovo il vault: {CARTELLA_VAULT}")
        return 2
    righe = [f"Backup del {datetime.datetime.now():%Y-%m-%d %H:%M}"]
    ok = passo_git(righe)
    ok = passo_zip(righe) and ok
    righe.append("ESITO: OK" if ok else "ESITO: QUALCOSA È FALLITO, leggi sopra")
    testo = "\n".join(righe)
    print(testo)
    try:
        (CARTELLA_CLOUD / "ultimo-backup.txt").write_text(testo + "\n", encoding="utf-8")
    except OSError:
        pass
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
