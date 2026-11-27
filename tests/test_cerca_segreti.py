"""cerca_segreti.py finds keys and passwords and prints only file:line:TYPE, never the value."""
import re

import pytest

from conftest import (FINTO_ANTHROPIC, FINTO_AWS, FINTO_GITHUB, FINTO_OPENAI, FINTO_PASSWORD,
                      PACCHETTI, SCRIPTS, esegui)

SCRIPT = SCRIPTS / "cerca_segreti.py"
RIGA = re.compile(r"^.+:\d+:[A-Za-z0-9_.,\-]+$")
VALORI = [FINTO_GITHUB, FINTO_ANTHROPIC, FINTO_OPENAI, FINTO_AWS, FINTO_PASSWORD]


def _controlla_niente_valori(r):
    testo = r.stdout + r.stderr
    for v in VALORI:
        assert v not in testo
        assert v[-12:] not in testo, "a piece of the value was printed"


@pytest.mark.parametrize("riga, tipo", [
    ("token = " + FINTO_GITHUB, "token-github"),
    ("ANTHROPIC_API_KEY=" + FINTO_ANTHROPIC, "chiave-anthropic"),
    ('{"openai": "' + FINTO_OPENAI + '"}', "chiave-openai"),
    ("aws " + FINTO_AWS, "chiave-aws"),
    ("-----BEGIN OPENSSH PRIVATE KEY-----", "chiave-privata"),
])
def test_trova_le_forme_note(tmp_path, riga, tipo):
    f = tmp_path / "note.md"
    f.write_text("prima riga normale\n" + riga + "\n", encoding="utf-8")
    r = esegui(SCRIPT, tmp_path)
    assert r.returncode == 1, r.stderr
    righe = r.stdout.splitlines()
    assert righe, "nothing reported"
    assert all(RIGA.match(x) for x in righe), righe
    assert any(":2:" in x and tipo in x.rsplit(":", 1)[1].split(",") for x in righe), righe
    _controlla_niente_valori(r)


def test_password_in_italiano(tmp_path):
    (tmp_path / "appunti.txt").write_text("la password del CRM è " + FINTO_PASSWORD + "\n", encoding="utf-8")
    r = esegui(SCRIPT, tmp_path)
    assert r.returncode == 1
    assert re.search(r"appunti\.txt:1:password$", r.stdout, re.M), r.stdout
    _controlla_niente_valori(r)


def test_una_riga_per_riga_sospetta(tmp_path):
    (tmp_path / "x.env.md").write_text("GITHUB_TOKEN=" + FINTO_GITHUB + "\n", encoding="utf-8")
    r = esegui(SCRIPT, tmp_path / "x.env.md")
    assert r.returncode == 1
    assert len([x for x in r.stdout.splitlines() if ":1:" in x]) == 1, r.stdout
    _controlla_niente_valori(r)


def test_nome_del_file_da_credenziali(tmp_path):
    (tmp_path / "password.txt").write_text("niente di strano qui\n", encoding="utf-8")
    r = esegui(SCRIPT, tmp_path)
    assert r.returncode == 1
    assert re.search(r"password\.txt:0:nome-del-file$", r.stdout, re.M), r.stdout


def test_segreto_nel_nome_del_file_si_oscura(tmp_path):
    (tmp_path / (FINTO_GITHUB + ".txt")).write_text("ciao\n", encoding="utf-8")
    r = esegui(SCRIPT, tmp_path)
    assert r.returncode == 1
    assert "[OSCURATO]" in r.stdout
    _controlla_niente_valori(r)


@pytest.mark.parametrize("testo", [
    "la password è sbagliata, la cambio domani\n",
    "uso un password manager per tutto\n",
    "API_KEY=<la-tua-chiave>\n",
    "token: ${GITHUB_TOKEN}\n",
    "Riunione alle 10, poi pranzo.\n",
])
def test_frasi_normali_non_segnalate(tmp_path, testo):
    (tmp_path / "nota.md").write_text(testo, encoding="utf-8")
    r = esegui(SCRIPT, tmp_path)
    assert r.returncode == 0, r.stdout
    assert r.stdout == ""


def test_errore_d_uso_codice_2(tmp_path):
    assert esegui(SCRIPT).returncode == 2


def test_copie_nei_pacchetti_uguali_al_plugin():
    """Every package that ships its own copy of cerca_segreti.py ships the plugin's one, unchanged."""
    originale = SCRIPT.read_bytes()
    copie = sorted(PACCHETTI.rglob("cerca_segreti.py"))
    assert copie, "no copy found"
    diverse = [str(c.relative_to(PACCHETTI)) for c in copie if c.read_bytes() != originale]
    assert not diverse, "copies differ from plugin/second-brain/scripts/cerca_segreti.py: %s" % diverse
