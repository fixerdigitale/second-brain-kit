"""CLAUDE_CONFIG_DIR: when it is set, the scripts read and write Claude Code's files there,
not in ~/.claude and ~/.claude.json."""
import json

from conftest import SCRIPTS, env_pulito, esegui

CONFIG = SCRIPTS / "config_claude.py"
TEMI = SCRIPTS / "temi_sessioni.py"
STATO = SCRIPTS / "stato.py"


def _casa_e_config(tmp_path):
    casa = tmp_path / "casa"
    (casa / ".claude").mkdir(parents=True)
    config = tmp_path / "config-altrove"
    config.mkdir()
    return casa, config


def test_aggiungi_deny_scrive_in_claude_config_dir(tmp_path):
    casa, config = _casa_e_config(tmp_path)
    env = env_pulito(home=casa, CLAUDE_CONFIG_DIR=config)
    r = esegui(CONFIG, "aggiungi-deny", "--sistema", "linux", env=env)
    assert r.returncode == 0, r.stderr
    assert (config / "settings.json").is_file()
    assert not (casa / ".claude" / "settings.json").exists()
    deny = json.loads((config / "settings.json").read_text(encoding="utf-8"))["permissions"]["deny"]
    assert "Read(**/.env)" in deny
    # the file did not exist before: the script says so instead of naming a copy
    assert "nessuna copia" in r.stdout
    assert not list(config.glob("settings.json.bak-*"))


def test_aggiungi_deny_senza_variabile_resta_in_home(tmp_path):
    casa, config = _casa_e_config(tmp_path)
    r = esegui(CONFIG, "aggiungi-deny", "--sistema", "linux", env=env_pulito(home=casa))
    assert r.returncode == 0, r.stderr
    assert (casa / ".claude" / "settings.json").is_file()
    assert not (config / "settings.json").exists()


def test_nomi_legge_da_claude_config_dir_e_non_dalla_home(tmp_path):
    casa, config = _casa_e_config(tmp_path)
    # rules and connectors left in the home by another profile must not be counted
    (casa / ".claude" / "settings.json").write_text(
        json.dumps({"permissions": {"deny": ["Read(~/.ssh/**)"] * 13}}), encoding="utf-8")
    (casa / ".claude.json").write_text(json.dumps({"mcpServers": {"vecchio": {"command": "x"}}}),
                                       encoding="utf-8")
    (config / "settings.json").write_text(json.dumps({"permissions": {"deny": []}}), encoding="utf-8")
    (config / ".claude.json").write_text(json.dumps({"mcpServers": {"nuovo": {"command": "y"}}}),
                                         encoding="utf-8")
    lavoro = tmp_path / "lavoro"
    lavoro.mkdir()
    env = env_pulito(home=casa, CLAUDE_CONFIG_DIR=config)
    r = esegui(CONFIG, "nomi", "--json", env=env, cwd=lavoro)
    assert r.returncode == 0, r.stderr
    d = json.loads(r.stdout)
    assert [c["nome"] for c in d["connettori"]] == ["nuovo"]
    file_letti = [x["file"] for x in d["impostazioni"]]
    assert str(config / "settings.json") in file_letti
    assert str(casa / ".claude" / "settings.json") not in file_letti
    assert all(x["deny"] == 0 for x in d["impostazioni"])


def test_nomi_senza_variabile_legge_la_home(tmp_path):
    casa, config = _casa_e_config(tmp_path)
    (casa / ".claude.json").write_text(json.dumps({"mcpServers": {"vecchio": {"command": "x"}}}),
                                       encoding="utf-8")
    (config / ".claude.json").write_text(json.dumps({"mcpServers": {"nuovo": {"command": "y"}}}),
                                         encoding="utf-8")
    lavoro = tmp_path / "lavoro"
    lavoro.mkdir()
    r = esegui(CONFIG, "nomi", "--json", env=env_pulito(home=casa), cwd=lavoro)
    assert r.returncode == 0, r.stderr
    assert [c["nome"] for c in json.loads(r.stdout)["connettori"]] == ["vecchio"]


def _sessione(cartella, testo):
    cartella.mkdir(parents=True)
    riga = {"type": "user", "timestamp": "2026-11-26T10:00:00Z",
            "message": {"role": "user", "content": testo}}
    (cartella / "s.jsonl").write_text(json.dumps(riga) + "\n", encoding="utf-8")


def test_temi_sessioni_usa_claude_config_dir(tmp_path):
    casa, config = _casa_e_config(tmp_path)
    _sessione(casa / ".claude" / "projects" / "p", "preventivo preventivo preventivo")
    _sessione(config / "projects" / "p", "fattura fattura fattura")
    r = esegui(TEMI, "--progetto", "p", "--giorni", "100000", "--json",
               env=env_pulito(home=casa, CLAUDE_CONFIG_DIR=config))
    assert r.returncode == 0, r.stderr
    assert "fattura" in r.stdout
    assert "preventivo" not in r.stdout
    r = esegui(TEMI, "--progetto", "p", "--giorni", "100000", "--json", env=env_pulito(home=casa))
    assert r.returncode == 0, r.stderr
    assert "preventivo" in r.stdout
    assert "fattura" not in r.stdout


def test_stato_rifiuta_claude_config_dir_come_cartella_di_lavoro(tmp_path):
    casa, config = _casa_e_config(tmp_path)
    r = esegui(STATO, "--cartella", config, "crea", env=env_pulito(home=casa, CLAUDE_CONFIG_DIR=config))
    assert r.returncode == 2, (r.stdout, r.stderr)
    assert "CLAUDE_CONFIG_DIR" in r.stderr
    assert not (config / "second-brain").exists()
