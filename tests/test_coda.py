"""canali-lavoro-notte/coda.py stops when ANTHROPIC_API_KEY would make `claude -p` pay per token."""
import os
import sys

from conftest import PACCHETTI, env_pulito, esegui

SCRIPT = PACCHETTI / "canali-lavoro-notte" / "coda.py"
CHIAVE_FINTA = "finta-" + "0" * 24


def claude_finto(cartella, segno):
    """A fake `claude` on PATH that leaves a mark if it is ever launched."""
    cartella.mkdir()
    py = cartella / "claude_finto.py"
    py.write_text("import pathlib\npathlib.Path(%r).write_text('lanciato')\nprint('ok')\n" % str(segno),
                  encoding="utf-8")
    if sys.platform.startswith("win"):
        (cartella / "claude.cmd").write_text('@"%s" "%s" %%*\r\n' % (sys.executable, py), encoding="utf-8")
    else:
        sh = cartella / "claude"
        sh.write_text('#!/bin/sh\nexec "%s" "%s" "$@"\n' % (sys.executable, py), encoding="utf-8")
        sh.chmod(0o755)
    return cartella


def test_si_ferma_con_la_chiave_a_consumo(tmp_path):
    vault = tmp_path / "vault"
    vault.mkdir()
    (vault / "CODA.md").write_text("## Lavoro di prova\nScrivi ciao in un file.\n", encoding="utf-8")
    segno = tmp_path / "lanciato.txt"
    bin_finto = claude_finto(tmp_path / "bin", segno)
    env = env_pulito(ANTHROPIC_API_KEY=CHIAVE_FINTA)
    env["PATH"] = str(bin_finto) + os.pathsep + env.get("PATH", "")
    r = esegui(SCRIPT, "--vault", vault, env=env)
    assert r.returncode == 2, (r.stdout, r.stderr)
    assert "FERMO" in r.stdout and "ANTHROPIC_API_KEY" in r.stdout
    assert CHIAVE_FINTA not in r.stdout + r.stderr
    assert not segno.exists(), "claude was launched"
    assert "[fatto]" not in (vault / "CODA.md").read_text(encoding="utf-8")
    assert not (vault / "notte").exists()


def test_permessi_bypass_non_ammessi(tmp_path):
    r = esegui(SCRIPT, "--vault", tmp_path, "--prova", "--permessi", "bypassPermissions")
    assert r.returncode == 2
