#!/usr/bin/env python3
"""Backup minimo del vault: commit + push su GitHub privato, poi una copia zip datata nella cartella cloud.

Mac, Windows e Linux, solo libreria standard di Python 3. Configura le righe qui sotto.

Cosa fa, in ordine:
  1. git add/commit/push nella cartella del vault (se è un repo git e ci sono modifiche).
     Prima del commit controlla i file pronti con cerca_segreti.py (nome E contenuto): se uno
     sembra una chiave, un token o una password, toglie tutto dal commit e si ferma.
     Il push parte solo se `gh` conferma che il repo su GitHub NON è pubblico. Se `gh` non c'è
     o non risponde, il push si ferma, a meno di --push-senza-verifica;
  2. crea <cartella-cloud>/vault-AAAAMMGG-HHMM.zip (esclusi .git, node_modules, .trash).
     Anche qui i file che cerca_segreti.py segnala restano fuori, e l'esito lo dice;
  3. le copie zip oltre COPIE_DA_TENERE le cancella solo con --ruota (o se rispondi «s»
     quando lo lanci a mano); altrimenti le elenca e basta;
  4. scrive l'esito in <cartella-cloud>/ultimo-backup.txt.

Senza cerca_segreti.py (accanto a questo file, o nel plugin second-brain) non salva niente:
meglio nessun backup stanotte che un segreto su GitHub.

Lo zip NON è cifrato: va bene per un vault di note senza segreti. Se dentro ci sono dati delicati,
usa restic (vedi LEGGIMI.md) al posto del punto 2.

Uso:  python3 backup_vault.py [--ruota] [--push-senza-verifica]   (su Windows: py backup_vault.py)
"""
import argparse
import datetime
import importlib.util
import json
import pathlib
import re
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

QUI = pathlib.Path(__file__).resolve().parent
ESCLUSI = {".git", "node_modules", ".trash", "__pycache__"}
# Nomi di file che non devono mai finire nel repo né nello zip (basta che il nome li contenga).
NOMI_VIETATI = (".env", ".pem", ".key", "id_rsa", "id_ed25519", "credentials", "secrets",
                "accessi", "password", "token")
NOME_ZIP = re.compile(r"^vault-\d{8}-\d{4}\.zip$")


def carica_cerca_segreti():
    """Il modulo cerca_segreti: prima accanto a questo file, poi nel plugin second-brain. None se manca."""
    candidati = [QUI / "cerca_segreti.py",
                 QUI.parent.parent / "plugin" / "second-brain" / "scripts" / "cerca_segreti.py"]
    for p in candidati:
        if p.is_file():
            spec = importlib.util.spec_from_file_location("cerca_segreti", p)
            modulo = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(modulo)
            except Exception:
                continue
            if all(hasattr(modulo, f) for f in ("righe_con_segreti", "segreto_nel_percorso",
                                                 "nome_sospetto", "percorso_sicuro")):
                return modulo
    return None


def nome_vietato(nome):
    nome = nome.lower()
    return nome.startswith(".env") or any(v in nome for v in NOMI_VIETATI)


def segnalazioni(cs, percorso, relativo):
    """Righe «file:riga:TIPO» per un file sospetto (mai il valore). Lista vuota se pulito."""
    rel = str(relativo)
    sicuro = cs.percorso_sicuro(rel)
    out = []
    if cs.segreto_nel_percorso(rel):
        out.append(f"{sicuro}:0:segreto-nel-nome")
    elif nome_vietato(percorso.name) or cs.nome_sospetto(percorso.name):
        out.append(f"{sicuro}:0:nome-del-file")
    for n, nomi in cs.righe_con_segreti(str(percorso)):
        out.append(f"{sicuro}:{n}:{','.join(nomi)}")
    return out


def git(*argomenti):
    return subprocess.run(["git", *argomenti], cwd=CARTELLA_VAULT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def visibilita_repo():
    """'PUBLIC', 'PRIVATE', 'INTERNAL' secondo `gh`; None se `gh` manca o non sa rispondere."""
    if not shutil.which("gh"):
        return None
    try:
        r = subprocess.run(["gh", "repo", "view", "--json", "visibility"], cwd=CARTELLA_VAULT,
                           capture_output=True, text=True, timeout=60)
        return (json.loads(r.stdout).get("visibility") or "").upper() or None
    except (ValueError, OSError, subprocess.TimeoutExpired):
        return None


def passo_git(righe, cs, push_senza_verifica):
    if not (CARTELLA_VAULT / ".git").exists():
        righe.append("git: la cartella non è un repo, salto")
        return True
    git("add", "-A")
    pronti = git("diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR").stdout.split("\0")
    trovati = []
    for rel in filter(None, pronti):
        trovati += segnalazioni(cs, CARTELLA_VAULT / rel, pathlib.PurePosixPath(rel))
    if trovati:
        git("reset", "-q")  # toglie dal commit quello appena aggiunto; i file restano dove sono
        righe.append("git: FERMATO, fra i file pronti per il commit qualcosa sembra una chiave o una password "
                     "(file:riga:tipo, il valore non lo stampo):")
        righe += ["  " + t for t in trovati[:20]]
        if len(trovati) > 20:
            righe.append(f"  ... e altre {len(trovati) - 20} righe")
        righe.append("  Togli il segreto dal file (mettilo in un gestore di password) o aggiungi il file "
                     "a .gitignore, poi rilancia.")
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
    vis = visibilita_repo()
    if vis == "PUBLIC":
        righe.append("git: push FERMATO, il repo su GitHub è PUBBLICO. Rendilo privato e rilancia. "
                     "Il commit resta sul PC.")
        return False
    if vis is None and not push_senza_verifica:
        righe.append("git: push FERMATO, non riesco a verificare che il repo sia privato (manca `gh`, "
                     "oppure non hai fatto `gh auth login`, oppure il remote non è su GitHub). Il commit "
                     "resta sul PC. Installa gh e fai il login, oppure, se sei sicuro che il repo è "
                     "privato, rilancia con --push-senza-verifica.")
        return False
    r = git("push")
    if r.returncode != 0:
        righe.append("git push FALLITO: " + r.stderr.strip()[:300])
        return False
    righe.append("git: push fatto" + ("" if vis else " (visibilità del repo NON verificata: --push-senza-verifica)"))
    return True


def chiedi_conferma(domanda):
    if not sys.stdin.isatty():
        return False
    try:
        return input(domanda + " [s/N] ").strip().lower() in ("s", "si", "sì", "y", "yes")
    except EOFError:
        return False


def passo_zip(righe, cs, ruota):
    CARTELLA_CLOUD.mkdir(parents=True, exist_ok=True)
    nome = CARTELLA_CLOUD / f"vault-{datetime.datetime.now():%Y%m%d-%H%M}.zip"
    n, fuori = 0, []
    with zipfile.ZipFile(nome, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(CARTELLA_VAULT.rglob("*")):
            rel = f.relative_to(CARTELLA_VAULT)
            if not f.is_file() or (ESCLUSI & set(rel.parts)):
                continue
            # le chiavi non vanno nello zip: è in chiaro e finisce sul cloud
            trovati = segnalazioni(cs, f, rel.as_posix())
            if trovati:
                fuori += trovati
                continue
            z.write(f, rel)
            n += 1
    # controllo minimo: lo zip si rilegge senza errori
    with zipfile.ZipFile(nome) as z:
        guasto = z.testzip()
    if guasto:
        righe.append(f"zip ROTTO al file {guasto}")
        return False
    righe.append(f"zip: {nome.name}, {n} file, {nome.stat().st_size // 1024} KB")
    ok = True
    if fuori:
        ok = False
        righe.append("zip: ATTENZIONE, lasciati fuori i file che sembrano contenere chiavi o password "
                     "(file:riga:tipo):")
        righe += ["  " + t for t in fuori[:20]]
        if len(fuori) > 20:
            righe.append(f"  ... e altre {len(fuori) - 20} righe")
    copie = sorted(p for p in CARTELLA_CLOUD.iterdir() if p.is_file() and NOME_ZIP.match(p.name))
    vecchie = copie[:-COPIE_DA_TENERE]
    if vecchie:
        if ruota or chiedi_conferma(f"Cancello le {len(vecchie)} copie zip più vecchie delle ultime "
                                    f"{COPIE_DA_TENERE}?"):
            for vecchia in vecchie:
                vecchia.unlink()
                righe.append(f"zip: cancellata la copia vecchia {vecchia.name}")
        else:
            righe.append(f"zip: {len(vecchie)} copie oltre le ultime {COPIE_DA_TENERE}, non cancellate "
                         "(rilancia con --ruota per cancellarle, o toglile a mano)")
    return ok


def main() -> int:
    p = argparse.ArgumentParser(description="Backup del vault: git (commit + push) e zip datato nel cloud.")
    p.add_argument("--ruota", action="store_true",
                   help=f"cancella le copie zip oltre le ultime {COPIE_DA_TENERE} senza chiedere")
    p.add_argument("--push-senza-verifica", action="store_true",
                   help="fa il push anche se gh non può dire se il repo è privato (si ferma comunque se è pubblico)")
    a = p.parse_args()
    if not CARTELLA_VAULT.is_dir():
        print(f"Non trovo il vault: {CARTELLA_VAULT}")
        return 2
    righe = [f"Backup del {datetime.datetime.now():%Y-%m-%d %H:%M}"]
    cs = carica_cerca_segreti()
    if cs is None:
        righe.append("Non trovo cerca_segreti.py (accanto a backup_vault.py o nel plugin second-brain): "
                     "senza il controllo dei segreti non salvo niente. Copialo accanto a questo script e rilancia.")
        ok = False
    else:
        ok = passo_git(righe, cs, a.push_senza_verifica)
        ok = passo_zip(righe, cs, a.ruota) and ok
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
