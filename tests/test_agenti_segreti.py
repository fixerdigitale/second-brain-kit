"""Regression for the secrets blocker found in the end-to-end test: the `revisore` subagent
must never open (Read, or Grep with content) the files that cerca_segreti flagged.

The check is on the agent's instructions, so it runs without a model. It looks for a stable
key phrase, plus an explicit ban on Read and content Grep."""

from conftest import REPO

AGENTI = REPO / "plugin" / "second-brain" / "agents"
FRASE = "file segnalati da cerca_segreti"


def _testo(nome):
    """Text on one line, without Markdown backticks or bold, cerca-segreti spelled as the script."""
    t = (AGENTI / nome).read_text(encoding="utf-8")
    t = t.replace("`", "").replace("**", "").replace("cerca-segreti", "cerca_segreti")
    return " ".join(t.split())


def test_revisore_non_apre_i_file_segnalati():
    t = _testo("revisore.md")
    assert FRASE in t, "revisore.md must name the %r it receives" % FRASE
    basso = t.lower()
    # the prohibition must be explicit: no Read and no Grep on the content of those files
    assert "read" in basso and "grep" in basso
    assert "output_mode: count" in t or 'output_mode: "count"' in t
    assert any(p in basso for p in ("non aprire", "non leggere", "mai read", "mai sui file"))


def test_ogni_agente_che_legge_ha_il_file_md():
    # sanity: the agents folder exists and revisore.md is there, so the test above is meaningful
    assert (AGENTI / "revisore.md").is_file()
    assert [p.name for p in AGENTI.glob("*.md")]
