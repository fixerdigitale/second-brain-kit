"""stato.py: --help never reads or writes, imposta-molti sets several keys in one call
with the same checks as imposta (no secrets, max length), all or nothing."""
import json

import pytest

from conftest import FINTO_GITHUB, FINTO_PASSWORD, SCRIPTS, env_pulito, esegui

SCRIPT = SCRIPTS / "stato.py"


@pytest.fixture
def lavoro(tmp_path, casa):
    w = tmp_path / "lavoro"
    w.mkdir()
    r = esegui(SCRIPT, "--cartella", w, "crea", env=env_pulito(home=casa))
    assert r.returncode == 0, r.stderr
    return w


def stato(cartella, casa, *args):
    return esegui(SCRIPT, "--cartella", cartella, *args, env=env_pulito(home=casa))


def leggi(cartella):
    return json.loads((cartella / "second-brain" / ".onboarding" / "stato.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("args", [["--help"], ["-h"], ["imposta", "--help"], ["leggi", "-h"],
                                  ["imposta-molti", "--help"]])
def test_help_stampa_l_aiuto_e_non_scrive(tmp_path, casa, args):
    vuota = tmp_path / "vuota"
    vuota.mkdir()
    r = esegui(SCRIPT, *args, env=env_pulito(home=casa), cwd=vuota)
    assert r.returncode == 0, r.stderr
    assert "imposta-molti" in r.stdout and "Uso" in r.stdout
    assert "nessuno stato" not in r.stdout + r.stderr
    assert list(vuota.iterdir()) == []


def test_help_con_cartella_non_tocca_lo_stato(lavoro, casa):
    prima = (lavoro / "second-brain" / ".onboarding" / "stato.json").read_bytes()
    r = stato(lavoro, casa, "--help")
    assert r.returncode == 0
    assert (lavoro / "second-brain" / ".onboarding" / "stato.json").read_bytes() == prima


def test_imposta_molti_scrive_tutte_le_chiavi(lavoro, casa):
    r = stato(lavoro, casa, "imposta-molti", "tono=T1", "voti.memoria=2", "voti.sicurezza=0",
              "primo_risultato.descrizione=preventivo da una mail", "flag=true", "lista=[1,2]",
              "lingua=EN")
    assert r.returncode == 0, r.stderr
    assert "7" in r.stdout
    d = leggi(lavoro)
    assert d["tono"] == "T1"
    assert d["voti"]["memoria"] == 2 and d["voti"]["sicurezza"] == 0
    assert d["primo_risultato"]["descrizione"] == "preventivo da una mail"
    assert d["flag"] is True and d["lista"] == [1, 2]
    assert d["lingua"] == "en"


def test_imposta_molti_valore_con_uguale(lavoro, casa):
    r = stato(lavoro, casa, "imposta-molti", "nota=a=b")
    assert r.returncode == 0, r.stderr
    assert leggi(lavoro)["nota"] == "a=b"


@pytest.mark.parametrize("cattiva,codice", [
    ("token=" + FINTO_GITHUB, 2),
    ("nota=password: " + FINTO_PASSWORD, 2),
    ("lungo=" + "x" * 400, 1),
    ("senza-uguale", 2),
    ("=valore", 2),
    ("lingua=fr", 2),
])
def test_imposta_molti_tutto_o_niente(lavoro, casa, cattiva, codice):
    prima = leggi(lavoro)
    r = stato(lavoro, casa, "imposta-molti", "tono=T2", cattiva, "voti.memoria=3")
    assert r.returncode == codice, (r.stdout, r.stderr)
    dopo = leggi(lavoro)
    assert dopo == prima
    assert FINTO_GITHUB not in r.stdout + r.stderr
    assert FINTO_PASSWORD not in json.dumps(dopo)


def test_imposta_molti_rifiuta_una_chiave_che_sembra_un_segreto(lavoro, casa):
    prima = leggi(lavoro)
    r = stato(lavoro, casa, "imposta-molti", "tono=T2", FINTO_GITHUB + "=1")
    assert r.returncode == 2
    assert leggi(lavoro) == prima


def test_imposta_molti_senza_coppie_e_errore_d_uso(lavoro, casa):
    r = stato(lavoro, casa, "imposta-molti")
    assert r.returncode == 2


def test_imposta_valore_troppo_lungo_esce_con_1_come_prima(lavoro, casa):
    r = stato(lavoro, casa, "imposta", "nota", "x" * 400)
    assert r.returncode == 1
    assert "troppo lungo" in r.stderr
