"""The catalog index, the catalog READMEs and the numbers written in the READMEs are up to date."""
from conftest import SCRIPTS, esegui

SCRIPT = SCRIPTS / "genera_indice_catalogo.py"


def test_controlla_esce_0():
    r = esegui(SCRIPT, "--controlla", timeout=120)
    assert r.returncode == 0, "genera_indice_catalogo.py --controlla failed:\n" + r.stdout + r.stderr
