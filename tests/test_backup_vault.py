"""backup_vault.py: no commit and no zip entry for a file with a key; no push without a private repo.

Uses a fake vault, a fake cloud folder and a local bare git remote under tmp_path.
"""
import importlib.util
import subprocess
import zipfile

import pytest

from conftest import FINTO_GITHUB, PACCHETTI

SCRIPT = PACCHETTI / "sicurezza-backup-notturno" / "backup_vault.py"


def git(cartella, *args):
    return subprocess.run(["git", *args], cwd=cartella, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


@pytest.fixture
def bv(tmp_path, monkeypatch):
    """The module, pointed at a fake vault (git repo with a local remote) and a fake cloud folder."""
    casa = tmp_path / "casa"
    casa.mkdir()
    for k, v in {"HOME": casa, "USERPROFILE": casa, "GIT_CONFIG_NOSYSTEM": "1",
                 "GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.com",
                 "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "test@example.com"}.items():
        monkeypatch.setenv(k, str(v))
    monkeypatch.delenv("GIT_DIR", raising=False)
    spec = importlib.util.spec_from_file_location("backup_vault_in_prova", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    vault, cloud, remoto = tmp_path / "vault", tmp_path / "cloud", tmp_path / "remoto.git"
    vault.mkdir()
    assert git(tmp_path, "init", "-q", "--bare", str(remoto)).returncode == 0
    assert git(vault, "init", "-q").returncode == 0
    git(vault, "config", "commit.gpgsign", "false")
    git(vault, "remote", "add", "origin", str(remoto))
    monkeypatch.setattr(m, "CARTELLA_VAULT", vault)
    monkeypatch.setattr(m, "CARTELLA_CLOUD", cloud)
    m.cs = m.carica_cerca_segreti()
    assert m.cs is not None
    return m


def nessun_commit(vault):
    return git(vault, "rev-parse", "--verify", "-q", "HEAD").returncode != 0


def test_chiave_in_stage_ferma_il_commit(bv):
    vault = bv.CARTELLA_VAULT
    (vault / "pulita.md").write_text("una nota qualsiasi\n", encoding="utf-8")
    (vault / "appunti.md").write_text("riga uno\nGITHUB_TOKEN=" + FINTO_GITHUB + "\n", encoding="utf-8")
    righe = []
    assert bv.passo_git(righe, bv.cs, push_senza_verifica=True) is False
    testo = "\n".join(righe)
    assert "FERMATO" in testo
    assert "appunti.md:2:" in testo
    assert FINTO_GITHUB not in testo and FINTO_GITHUB[-12:] not in testo
    assert nessun_commit(vault)
    assert git(vault, "diff", "--cached", "--name-only").stdout.strip() == ""
    # the files stay where they are
    assert (vault / "appunti.md").is_file()


@pytest.mark.parametrize("nome", ["accessi.md", "password-wifi.txt", "token.txt", ".env"])
def test_nomi_vietati_fermano_il_commit(bv, nome):
    (bv.CARTELLA_VAULT / nome).write_text("niente\n", encoding="utf-8")
    righe = []
    assert bv.passo_git(righe, bv.cs, push_senza_verifica=True) is False
    assert nessun_commit(bv.CARTELLA_VAULT)


def test_senza_verifica_della_visibilita_niente_push(bv, monkeypatch):
    monkeypatch.setattr(bv, "visibilita_repo", lambda: None)
    (bv.CARTELLA_VAULT / "nota.md").write_text("ciao\n", encoding="utf-8")
    righe = []
    assert bv.passo_git(righe, bv.cs, push_senza_verifica=False) is False
    testo = "\n".join(righe)
    assert "commit fatto" in testo and "push FERMATO" in testo
    remoto = bv.CARTELLA_VAULT.parent / "remoto.git"
    assert git(remoto, "for-each-ref").stdout.strip() == ""


def test_repo_pubblico_niente_push_neanche_con_l_opzione(bv, monkeypatch):
    monkeypatch.setattr(bv, "visibilita_repo", lambda: "PUBLIC")
    (bv.CARTELLA_VAULT / "nota.md").write_text("ciao\n", encoding="utf-8")
    righe = []
    assert bv.passo_git(righe, bv.cs, push_senza_verifica=True) is False
    assert "PUBBLICO" in "\n".join(righe)
    remoto = bv.CARTELLA_VAULT.parent / "remoto.git"
    assert git(remoto, "for-each-ref").stdout.strip() == ""


def test_lo_zip_lascia_fuori_le_chiavi_e_non_ruota_da_solo(bv, monkeypatch):
    monkeypatch.setattr(bv, "chiedi_conferma", lambda domanda: False)
    vault, cloud = bv.CARTELLA_VAULT, bv.CARTELLA_CLOUD
    (vault / "nota.md").write_text("ciao\n", encoding="utf-8")
    (vault / "chiave.md").write_text("token " + FINTO_GITHUB + "\n", encoding="utf-8")
    cloud.mkdir()
    vecchie = ["vault-2020010%d-0000.zip" % i for i in range(1, 10)]
    for n in vecchie + ["altro.zip"]:
        (cloud / n).write_bytes(b"")
    righe = []
    assert bv.passo_zip(righe, bv.cs, ruota=False) is False
    nuovi = sorted(p for p in cloud.glob("vault-*.zip") if p.name not in vecchie)
    assert len(nuovi) == 1
    with zipfile.ZipFile(nuovi[0]) as z:
        assert z.namelist() == ["nota.md"]
    assert all((cloud / n).exists() for n in vecchie), "rotation without --ruota"
    assert FINTO_GITHUB not in "\n".join(righe)
    # with --ruota only the vault-AAAAMMGG-HHMM.zip copies beyond 7 go away
    assert bv.passo_zip([], bv.cs, ruota=True) is False
    rimaste = sorted(p.name for p in cloud.glob("vault-*.zip"))
    assert len(rimaste) == bv.COPIE_DA_TENERE
    assert (cloud / "altro.zip").exists()
