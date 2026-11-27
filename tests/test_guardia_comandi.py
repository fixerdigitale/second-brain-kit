"""hook-guardia-comandi: the risky forms are flagged, the harmless commands pass."""
import json

import pytest

from conftest import PACCHETTI, esegui

SCRIPT = PACCHETTI / "hook-guardia-comandi" / "guardia_comandi.py"


def decisione(comando, strumento="Bash", entrata=None):
    dati = {"tool_name": strumento, "tool_input": entrata if entrata is not None else {"command": comando}}
    r = esegui(SCRIPT, stdin=json.dumps(dati))
    assert r.returncode == 0, r.stderr
    if not r.stdout.strip():
        return None
    return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"]


@pytest.mark.parametrize("comando, attesa", [
    ("rm -rf build", "ask"),
    ("rm -r -f build", "ask"),
    ("rm -f -r build", "ask"),
    ("rm --recursive --force build", "ask"),
    ("rm -r --force build", "ask"),
    ("git push --force", "deny"),
    ("git push -f origin main", "deny"),
    ("git push -uf origin main", "deny"),
    ("git push origin +main", "deny"),
    ("git -C progetto push --force", "deny"),
    ("git push --force-with-lease; git push -f", "deny"),
    ("cd x && git push --force", "deny"),
    ("git push --force-with-lease --force", "deny"),
])
def test_comandi_segnalati(comando, attesa):
    assert decisione(comando) == attesa


@pytest.mark.parametrize("comando", [
    "ls -la",
    "git push",
    "git push --follow-tags",
    "git push origin feature-fix",
    "git push --force-with-lease",
    "rm -r build",
    "rm -f file.txt",
    "rm file-rf.txt",
    "git status && git log -n 3",
])
def test_comandi_innocui_passano(comando):
    assert decisione(comando) is None


def test_scrittura_in_env_chiede_conferma():
    assert decisione(None, "Write", {"file_path": "progetto/.env", "content": "x"}) == "ask"
    assert decisione(None, "Write", {"file_path": "progetto/nota.md", "content": "x"}) is None


def test_input_rotto_lascia_passare():
    r = esegui(SCRIPT, stdin="non e' json")
    assert r.returncode == 0 and r.stdout == ""
