"""Shared helpers for the kit tests.

The tests are fast and never use the network: every vault, home folder and git remote
is a fake one created under pytest's tmp_path.

Fake secrets are built at runtime (prefix + filler) so that this file never contains
something that looks like a real key, for GitHub push protection and for cerca_segreti.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / "plugin" / "second-brain" / "scripts"
PACCHETTI = REPO / "pacchetti"

# Fake secrets: valid shape for the regexes, obviously not real.
FINTO_GITHUB = "ghp" + "_" + "A1b2C3d4" * 5          # 40 chars after the prefix
FINTO_ANTHROPIC = "sk-" + "ant-" + "api03-" + "x9Y8z7W6" * 4
FINTO_OPENAI = "sk-" + "proj-" + "Q1w2E3r4" * 5
FINTO_AWS = "AKIA" + "ABCDEFGH12345678"
FINTO_PASSWORD = "Fint0" + "Segreto" + "42"


def env_pulito(home=None, **extra):
    """A copy of the environment without keys, cloud variables or CLAUDE_CONFIG_DIR, with a fake HOME if given.

    CLAUDE_CONFIG_DIR is dropped so that the runner's own Claude Code config never leaks
    into a test; the tests that need it pass it again through **extra."""
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(("ANTHROPIC_", "OneDrive", "ONEDRIVE")) and k != "CLAUDE_CONFIG_DIR"}
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    if home is not None:
        env["HOME"] = str(home)
        env["USERPROFILE"] = str(home)
    env.update({k: str(v) for k, v in extra.items()})
    return env


def esegui(script, *args, env=None, cwd=None, stdin=None, timeout=60):
    """Run a Python script with the current interpreter and return the CompletedProcess."""
    return subprocess.run([sys.executable, str(script), *map(str, args)], input=stdin,
                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                          env=env or env_pulito(), cwd=cwd, timeout=timeout)


def trova_bash():
    """Bash for second-brain.sh: Git Bash on Windows (never the WSL launcher), bash elsewhere."""
    if sys.platform.startswith("win"):
        for p in (r"C:\Program Files\Git\bin\bash.exe", r"C:\Program Files\Git\usr\bin\bash.exe"):
            if os.path.isfile(p):
                return p
        return None
    return shutil.which("bash")


@pytest.fixture
def casa(tmp_path):
    """A fake home folder with the usual personal folders."""
    h = tmp_path / "casa"
    for d in ("Desktop", "Documents", "Downloads", ".claude/projects", ".ssh"):
        (h / d).mkdir(parents=True)
    return h
