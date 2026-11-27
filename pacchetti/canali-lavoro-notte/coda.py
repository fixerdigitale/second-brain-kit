#!/usr/bin/env python3
"""coda.py - fa girare in fila i lavori lasciati per la notte e prepara il foglio del mattino.

Uso:
    python3 coda.py                 # esegue i lavori di CODA.md non ancora fatti
    python3 coda.py --prova         # mostra cosa farebbe, senza lanciare niente

CODA.md (nel vault) ha un lavoro per sezione:

    ## Titolo corto
    Brief completo: obiettivo, file, cosa consegnare.

Ogni lavoro gira con `claude -p`, uno dopo l'altro. Il risultato va in
<vault>/notte/AAAA-MM-GG/<titolo>.md e il riassunto in <vault>/notte/AAAA-MM-GG/DA-RIVEDERE.md,
con una casella si'/no per ogni consegna. Gli eseguiti vengono segnati in CODA.md come [fatto].

Gira solo a PC acceso (e sveglio). Si ferma alle ORA_STOP per non trovarti il PC impegnato.
"""
import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
from pathlib import Path

VAULT = Path("<cartella-vault>")   # cambia qui, o passa --vault
ORA_STOP = 7                        # non parte nessun lavoro nuovo dopo le 7:00
MAX_MINUTI_PER_LAVORO = 45


def leggi_coda(testo: str) -> list:
    lavori = []
    for blocco in re.split(r"^## ", testo, flags=re.M)[1:]:
        titolo, _, brief = blocco.partition("\n")
        if "[fatto]" in titolo:
            continue
        lavori.append((titolo.strip(), brief.strip()))
    return lavori


def segna_fatto(coda: Path, titolo: str) -> None:
    testo = coda.read_text(encoding="utf-8")
    testo = testo.replace(f"## {titolo}\n", f"## {titolo} [fatto]\n", 1)
    coda.write_text(testo, encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--vault", default=str(VAULT))
    p.add_argument("--prova", action="store_true")
    p.add_argument("--permessi", default="acceptEdits", help="default, acceptEdits o plan")
    a = p.parse_args()

    vault = Path(a.vault)
    coda = vault / "CODA.md"
    if not coda.exists():
        print(f"Manca {coda}: crealo con un '## titolo' e il brief sotto per ogni lavoro.")
        return 2
    lavori = leggi_coda(coda.read_text(encoding="utf-8"))
    if not lavori:
        print("Coda vuota.")
        return 0
    oggi = vault / "notte" / dt.date.today().isoformat()
    if a.prova:
        for t, _ in lavori:
            print(f"- farei: {t}")
        return 0
    oggi.mkdir(parents=True, exist_ok=True)
    claude = shutil.which("claude") or "claude"
    righe = []
    for titolo, brief in lavori:
        if dt.datetime.now().hour >= ORA_STOP and dt.datetime.now().hour < 20:
            righe.append(f"- [ ] {titolo}: NON PARTITO, era gia' mattina. Resta in coda.")
            continue
        file_out = oggi / (re.sub(r"[^a-zA-Z0-9]+", "-", titolo.lower()).strip("-")[:40] + ".md")
        try:
            r = subprocess.run([claude, "-p", brief, "--output-format", "text", "--permission-mode", a.permessi],
                               cwd=vault, capture_output=True, text=True, encoding="utf-8",
                               timeout=MAX_MINUTI_PER_LAVORO * 60)
            ok, uscita = r.returncode == 0, (r.stdout.strip() or r.stderr.strip())
        except subprocess.TimeoutExpired:
            ok, uscita = False, f"Fermato dopo {MAX_MINUTI_PER_LAVORO} minuti."
        file_out.write_text(f"# {titolo}\n\n## Brief\n\n{brief}\n\n## Risultato\n\n{uscita}\n", encoding="utf-8")
        if ok:
            segna_fatto(coda, titolo)
        prima = (uscita.splitlines() or [""])[0][:160]
        esito = "fatto" if ok else "NON RIUSCITO, resta in coda"
        righe.append(f"- [ ] **{titolo}** ({esito}): {prima} - [{file_out.name}]({file_out.name})  \n"
                     f"  Va bene? si / no / correggi: ...")
    (oggi / "DA-RIVEDERE.md").write_text(
        f"# Lavoro della notte, {dt.date.today():%d/%m}\n\n"
        "Per ognuno: si' (lo tengo), no (lo butto) o la correzione. Niente e' stato mandato a nessuno.\n\n"
        + "\n".join(righe) + "\n", encoding="utf-8")
    print(f"Fatto. Da rivedere: {oggi / 'DA-RIVEDERE.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
