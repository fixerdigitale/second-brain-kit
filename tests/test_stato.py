"""stato.py crea refuses folders that must never become the work folder."""
import json
import sys

import pytest

from conftest import REPO, SCRIPTS, env_pulito, esegui

SCRIPT = SCRIPTS / "stato.py"


def crea(cartella, casa, *extra):
    return esegui(SCRIPT, "--cartella", cartella, "crea", *extra, env=env_pulito(home=casa))


@pytest.mark.parametrize("relativa", ["", "Desktop", "Documents", "Downloads", ".claude",
                                      ".claude/projects", ".ssh"])
def test_rifiuta_cartelle_personali(casa, relativa):
    cartella = casa / relativa if relativa else casa
    r = crea(cartella, casa)
    assert r.returncode == 2, (r.stdout, r.stderr)
    assert r.stderr.startswith("Rifiuto: "), r.stderr
    assert not (cartella / "second-brain").exists()


def test_rifiuta_la_cartella_che_contiene_la_home(casa):
    r = crea(casa.parent, casa)
    assert r.returncode == 2


@pytest.mark.parametrize("relativa", ["", "catalogo", "plugin/second-brain/scripts"])
def test_rifiuta_la_cartella_del_kit(casa, relativa):
    cartella = REPO / relativa if relativa else REPO
    r = crea(cartella, casa)
    assert r.returncode == 2
    assert "cartella del kit" in r.stderr
    assert not (cartella / "second-brain" / ".onboarding").exists()


def test_cartella_del_kit_in_inglese(casa):
    r = crea(REPO, casa, "--lingua", "en")
    assert r.returncode == 2
    assert r.stderr.startswith("Refused: ") and "kit folder" in r.stderr


@pytest.mark.parametrize("nuvola", ["OneDrive", "OneDrive - Studio", "Dropbox", "Dropbox (Personal)",
                                    "Google Drive", "iCloudDrive"])
def test_rifiuta_le_radici_cloud(casa, nuvola):
    radice = casa / nuvola
    radice.mkdir()
    r = crea(radice, casa)
    assert r.returncode == 2, (nuvola, r.stdout, r.stderr)
    assert "cloud" in r.stderr
    # a dedicated subfolder of the same cloud is fine
    sotto = radice / "Lavoro"
    sotto.mkdir()
    r = crea(sotto, casa)
    assert r.returncode == 0, (nuvola, r.stderr)
    assert (sotto / "second-brain" / ".onboarding" / "stato.json").is_file()


def test_rifiuta_cloudstorage_del_mac(casa):
    cs = casa / "Library" / "CloudStorage"
    gd = cs / "GoogleDrive-qualcuno@example.com"
    (gd / "My Drive").mkdir(parents=True)
    for c in (cs, gd, gd / "My Drive"):
        assert crea(c, casa).returncode == 2, c


def test_nome_simile_a_una_nuvola_va_bene(casa):
    c = casa / "Dropboxer"
    c.mkdir()
    assert crea(c, casa).returncode == 0


def test_cartella_dedicata_va_bene_e_non_sovrascrive(casa):
    lavoro = casa / "Documents" / "Lavoro"
    lavoro.mkdir()
    r = crea(lavoro, casa, "--lingua", "en")
    assert r.returncode == 0, r.stderr
    p = lavoro / "second-brain" / ".onboarding" / "stato.json"
    dati = json.loads(p.read_text(encoding="utf-8"))
    assert dati["lingua"] == "en"
    prima = p.read_bytes()
    r = crea(lavoro, casa)
    assert r.returncode == 0 and "esiste gia'" in r.stdout
    assert p.read_bytes() == prima


def test_lingua_sbagliata_codice_2(casa):
    lavoro = casa / "Lavoro"
    lavoro.mkdir()
    assert crea(lavoro, casa, "--lingua").returncode == 2
    assert crea(lavoro, casa, "--lingua", "fr").returncode == 2


def test_lo_stato_rifiuta_i_segreti(casa):
    from conftest import FINTO_GITHUB
    lavoro = casa / "Lavoro"
    lavoro.mkdir()
    assert crea(lavoro, casa).returncode == 0
    env = env_pulito(home=casa)
    r = esegui(SCRIPT, "--cartella", lavoro, "imposta", "misure.nota", "token " + FINTO_GITHUB, env=env)
    assert r.returncode == 2
    testo = (lavoro / "second-brain" / ".onboarding" / "stato.json").read_text(encoding="utf-8")
    assert FINTO_GITHUB not in testo


@pytest.mark.skipif(sys.platform.startswith("win"), reason="POSIX root path")
def test_rifiuta_la_radice_del_disco(casa):
    assert crea("/", casa).returncode == 2
