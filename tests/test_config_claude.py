"""config_claude.py: dated copy before writing, broken JSON left untouched, values never printed."""
import json
import re

from conftest import FINTO_GITHUB, SCRIPTS, esegui

SCRIPT = SCRIPTS / "config_claude.py"


def test_aggiungi_deny_fa_la_copia_datata_e_non_toglie_niente(tmp_path):
    s = tmp_path / "settings.json"
    originale = {"permissions": {"allow": ["Bash(ls:*)"], "deny": ["Read(~/.ssh/**)"]}, "model": "x"}
    s.write_text(json.dumps(originale), encoding="utf-8")
    prima = s.read_bytes()
    r = esegui(SCRIPT, "aggiungi-deny", "--settings", s, "--sistema", "linux")
    assert r.returncode == 0, r.stderr
    copie = [p for p in tmp_path.iterdir() if re.fullmatch(r"settings\.json\.bak-\d{8}-second-brain", p.name)]
    assert len(copie) == 1, list(tmp_path.iterdir())
    assert copie[0].read_bytes() == prima
    dati = json.loads(s.read_text(encoding="utf-8"))
    assert dati["model"] == "x"
    assert dati["permissions"]["allow"] == ["Bash(ls:*)"]
    deny = dati["permissions"]["deny"]
    assert deny.count("Read(~/.ssh/**)") == 1
    assert "Read(**/.env)" in deny


def test_aggiungi_deny_due_volte_non_duplica(tmp_path):
    s = tmp_path / "settings.json"
    s.write_text("{}", encoding="utf-8")
    assert esegui(SCRIPT, "aggiungi-deny", "--settings", s, "--sistema", "mac").returncode == 0
    dopo_la_prima = s.read_bytes()
    r = esegui(SCRIPT, "aggiungi-deny", "--settings", s, "--sistema", "mac")
    assert r.returncode == 0
    assert "0 regole da aggiungere" in r.stdout
    assert s.read_bytes() == dopo_la_prima
    assert len(list(tmp_path.glob("settings.json.bak-*"))) == 1
    deny = json.loads(s.read_text(encoding="utf-8"))["permissions"]["deny"]
    assert len(deny) == len(set(deny))


def test_json_rotto_non_si_tocca(tmp_path):
    s = tmp_path / "settings.json"
    s.write_text('{"permissions": {"deny": [', encoding="utf-8")
    prima = s.read_bytes()
    r = esegui(SCRIPT, "aggiungi-deny", "--settings", s, "--sistema", "windows")
    assert r.returncode == 1
    assert "Non lo tocco" in r.stderr
    assert s.read_bytes() == prima
    assert list(tmp_path.iterdir()) == [s]


def test_prova_non_scrive(tmp_path):
    s = tmp_path / "settings.json"
    s.write_text("{}", encoding="utf-8")
    r = esegui(SCRIPT, "aggiungi-deny", "--settings", s, "--sistema", "linux", "--prova")
    assert r.returncode == 0
    assert s.read_text(encoding="utf-8") == "{}"
    assert list(tmp_path.iterdir()) == [s]


def test_nomi_non_stampa_i_valori(tmp_path):
    cj = tmp_path / "claude.json"
    cj.write_text(json.dumps({"mcpServers": {
        "remoto": {"type": "http", "url": "https://example.com/mcp?token=" + FINTO_GITHUB,
                   "headers": {"Authorization": "Bearer " + FINTO_GITHUB}},
        "locale": {"command": "x", "env": {"API_KEY": FINTO_GITHUB}}}}), encoding="utf-8")
    s = tmp_path / "settings.json"
    s.write_text(json.dumps({"env": {"MY_TOKEN": FINTO_GITHUB}}), encoding="utf-8")
    for extra in ([], ["--json"]):
        r = esegui(SCRIPT, "nomi", "--claude-json", cj, "--settings", s, *extra)
        assert r.returncode == 0, r.stderr
        assert FINTO_GITHUB not in r.stdout + r.stderr
        assert "MY_TOKEN" in r.stdout and "remoto" in r.stdout
