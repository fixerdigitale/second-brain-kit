"""second-brain.sh: refuses personal folders, and `applica` never duplicates the CLAUDE.md block."""
import subprocess

import pytest

from conftest import SCRIPTS, env_pulito, trova_bash

BASH = trova_bash()
SCRIPT = SCRIPTS / "second-brain.sh"
INIZIO = "<!-- second-brain:inizio -->"
FINE = "<!-- second-brain:fine -->"

pytestmark = pytest.mark.skipif(BASH is None, reason="bash (Git Bash on Windows) not found")


def sb(casa, *args):
    return subprocess.run([BASH, str(SCRIPT), *map(str, args)], capture_output=True, text=True,
                          encoding="utf-8", errors="replace",
                          env=env_pulito(home=casa, SECOND_BRAIN_OGGI="2026-01-02"), timeout=120)


@pytest.mark.parametrize("relativa", ["", "Desktop", "Documents", "Downloads", ".claude", ".claude/projects"])
def test_rifiuta_cartelle_personali(casa, relativa):
    cartella = casa / relativa if relativa else casa
    r = sb(casa, "applica", "--cartella", cartella, "--claude", "crea")
    assert r.returncode == 2, (r.stdout, r.stderr)
    assert "Rifiuto:" in r.stderr
    assert not (cartella / "CLAUDE.md").exists()
    assert not (cartella / "memoria").exists()


def _conta(testo):
    return testo.count(INIZIO), testo.count(FINE)


def test_applica_crea_poi_aggiungi_non_duplica(casa):
    lavoro = casa / "Lavoro"
    lavoro.mkdir()
    r = sb(casa, "applica", "--cartella", lavoro, "--claude", "crea")
    assert r.returncode == 0, r.stderr
    claude = lavoro / "CLAUDE.md"
    assert _conta(claude.read_text(encoding="utf-8")) == (1, 1)
    assert (lavoro / "memoria" / "indice.md").is_file()
    prima = claude.read_bytes()
    stato = (lavoro / ".second-brain" / "stato.txt").read_bytes()
    for azione in ("aggiungi", "crea", "aggiorna"):
        r = sb(casa, "applica", "--cartella", lavoro, "--claude", azione)
        assert r.returncode == 0, (azione, r.stdout, r.stderr)
        assert claude.read_bytes() == prima, azione
    assert (lavoro / ".second-brain" / "stato.txt").read_bytes() == stato
    assert not list(lavoro.glob("CLAUDE.md.bak-*"))


def test_applica_aggiungi_su_claude_md_personale(casa):
    lavoro = casa / "Progetti"
    lavoro.mkdir()
    claude = lavoro / "CLAUDE.md"
    claude.write_text("# Le mie regole\n\nScrivi corto.\n", encoding="utf-8")
    r = sb(casa, "applica", "--cartella", lavoro, "--claude", "aggiungi")
    assert r.returncode == 0, r.stderr
    testo = claude.read_text(encoding="utf-8")
    assert testo.startswith("# Le mie regole\n\nScrivi corto.\n")
    assert _conta(testo) == (1, 1)
    copie = list(lavoro.glob("CLAUDE.md.bak-20260102-second-brain*"))
    assert len(copie) == 1
    dopo = claude.read_bytes()
    r = sb(casa, "applica", "--cartella", lavoro, "--claude", "aggiungi")
    assert r.returncode == 0, r.stderr
    assert claude.read_bytes() == dopo
    assert len(list(lavoro.glob("CLAUDE.md.bak-*"))) == 1


def test_applica_non_tocca_i_file_della_persona(casa):
    lavoro = casa / "Lavoro"
    lavoro.mkdir()
    assert sb(casa, "applica", "--cartella", lavoro).returncode == 0
    indice = lavoro / "memoria" / "indice.md"
    indice.write_text("mio indice\n", encoding="utf-8")
    r = sb(casa, "applica", "--cartella", lavoro)
    assert r.returncode == 0, r.stderr
    assert indice.read_text(encoding="utf-8") == "mio indice\n"


def test_marcatore_incompleto_si_ferma(casa):
    lavoro = casa / "Lavoro"
    lavoro.mkdir()
    claude = lavoro / "CLAUDE.md"
    claude.write_text("# Regole\n" + INIZIO + "\nmezzo blocco\n", encoding="utf-8")
    prima = claude.read_bytes()
    r = sb(casa, "applica", "--cartella", lavoro, "--claude", "aggiungi")
    assert r.returncode == 2
    assert claude.read_bytes() == prima
