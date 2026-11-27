#!/usr/bin/env python3
"""Scrive INVENTARIO.md: la mappa di cosa hai davvero installato per Claude Code.

Serve perche' Claude, a inizio sessione, non sa cosa c'e' sul tuo PC: senza una mappa
conclude "non ce l'ho" e ricostruisce uno strumento che esiste gia'. Questo file elenca
skill, agenti, comandi, hook, server MCP, programmi utili e i NOMI delle chiavi nei file
.env (mai i valori).

Solo libreria standard, Python 3.9 o piu' recente, Mac, Windows e Linux.

Uso:
  python3 genera_inventario.py [--progetto <tuo-progetto>] [--uscita <file>] [--env <file.env> ...]
                               [--se-vecchio <ore>]

Senza --uscita scrive <tuo-progetto>/INVENTARIO.md (o ./INVENTARIO.md).
Con --se-vecchio 20 non fa niente se il file ha meno di 20 ore: comodo in un hook SessionStart.
"""
import argparse
import json
import platform
import re
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

HOME = Path.home()
UTENTE_CLAUDE = HOME / '.claude'

# Programmi che vale la pena sapere se ci sono. Aggiungi i tuoi.
PROGRAMMI = ['git', 'gh', 'node', 'npm', 'npx', 'python3', 'python', 'uv', 'uvx', 'docker',
             'ollama', 'qmd', 'basic-memory', 'rg', 'jq', 'ffmpeg', 'pandoc', 'code', 'claude']


def leggi_json(p):
    try:
        return json.loads(Path(p).read_text(encoding='utf-8'))
    except Exception:
        return {}


def descrizione_md(p):
    """La riga description: del frontmatter, accorciata."""
    try:
        testo = Path(p).read_text(encoding='utf-8', errors='replace')
    except Exception:
        return ''
    m = re.search(r'^description:\s*(?:>-?|\|)?\s*(.*?)(?=^\w[\w-]*:|^---)', testo, re.S | re.M)
    if not m:
        return ''
    d = ' '.join(m.group(1).split())
    return (d[:140] + '...') if len(d) > 140 else d


def skill(cartella):
    righe = []
    if cartella.is_dir():
        for d in sorted(cartella.iterdir()):
            f = d / 'SKILL.md'
            if f.is_file():
                desc = descrizione_md(f)
                righe.append('- `%s`%s' % (d.name, ' - ' + desc if desc else ''))
    return righe


def file_md(cartella):
    righe = []
    if cartella.is_dir():
        for f in sorted(cartella.rglob('*.md')):
            desc = descrizione_md(f)
            nome = f.relative_to(cartella).with_suffix('').as_posix()
            righe.append('- `%s`%s' % (nome, ' - ' + desc if desc else ''))
    return righe


def hook(settings):
    righe = []
    for evento, voci in (settings.get('hooks') or {}).items():
        for voce in voci or []:
            filtro = voce.get('matcher') or '*'
            for h in voce.get('hooks') or []:
                comando = str(h.get('command', h.get('type', '?')))
                # Un comando puo' contenere un token scritto in chiaro: lo si copre.
                comando = re.sub(r'[A-Za-z0-9_\-]{24,}', '<nascosto>', comando)
                righe.append('- %s [%s]: `%s`' % (evento, filtro, comando[:120]))
    return righe


def mcp(dati):
    righe = []
    for nome, conf in (dati.get('mcpServers') or {}).items():
        if conf.get('url'):
            dove = 'url remoto'
        else:
            dove = 'comando `%s`' % Path(str(conf.get('command', '?'))).name
        righe.append('- `%s` - %s' % (nome, dove))
    return righe


def chiavi_env(file_env):
    """Solo i nomi delle variabili: i valori non vengono mai letti in uscita."""
    nomi = []
    try:
        for riga in Path(file_env).read_text(encoding='utf-8', errors='replace').splitlines():
            m = re.match(r'^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=', riga)
            if m:
                nomi.append(m.group(1))
    except Exception:
        return []
    return sorted(set(nomi))


def sezione(titolo, righe, vuoto='_niente_'):
    return ['', '## ' + titolo, ''] + (righe or [vuoto])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--progetto', default='.', help='cartella del progetto (con .claude/ e .mcp.json)')
    ap.add_argument('--uscita', help='dove scrivere il file')
    ap.add_argument('--env', action='append', default=[], help='file .env di cui elencare i NOMI')
    ap.add_argument('--se-vecchio', type=float, default=0, help='rigenera solo se piu vecchio di N ore')
    a = ap.parse_args()

    progetto = Path(a.progetto).expanduser().resolve()
    uscita = Path(a.uscita).expanduser() if a.uscita else progetto / 'INVENTARIO.md'
    if a.se_vecchio and uscita.is_file() and time.time() - uscita.stat().st_mtime < a.se_vecchio * 3600:
        return 0

    progetto_claude = progetto / '.claude'
    impostazioni = {
        'utente': leggi_json(UTENTE_CLAUDE / 'settings.json'),
        'progetto': leggi_json(progetto_claude / 'settings.json'),
        'progetto locale': leggi_json(progetto_claude / 'settings.local.json'),
    }

    out = ['# INVENTARIO - cosa c\'e\' davvero su questo PC', '',
           '_Generato da `genera_inventario.py` il %s su %s. Non modificare a mano._' % (
               datetime.now().strftime('%Y-%m-%d %H:%M'), platform.system()),
           '',
           'Leggi questo file prima di concludere che uno strumento non c\'e\' o di costruirne uno nuovo.']

    out += sezione('Skill (utente)', skill(UTENTE_CLAUDE / 'skills'))
    out += sezione('Skill (progetto)', skill(progetto_claude / 'skills'))
    out += sezione('Agenti', file_md(UTENTE_CLAUDE / 'agents') + file_md(progetto_claude / 'agents'))
    out += sezione('Comandi', file_md(UTENTE_CLAUDE / 'commands') + file_md(progetto_claude / 'commands'))

    righe_hook = []
    for dove, s in impostazioni.items():
        righe_hook += [r.replace('- ', '- (%s) ' % dove, 1) for r in hook(s)]
    out += sezione('Hook', righe_hook)

    righe_mcp = []
    for dove, f in [('utente', HOME / '.claude.json'), ('progetto', progetto / '.mcp.json')]:
        righe_mcp += [r.replace('- ', '- (%s) ' % dove, 1) for r in mcp(leggi_json(f))]
    out += sezione('Server MCP', righe_mcp)

    trovati = []
    for p in PROGRAMMI:
        percorso = shutil.which(p)
        if percorso:
            trovati.append('- `%s` - %s' % (p, percorso))
    out += sezione('Programmi', trovati)

    for f in a.env:
        nomi = chiavi_env(f)
        out += sezione('Chiavi in %s (%d, solo nomi)' % (Path(f).name, len(nomi)),
                       ['`%s`' % ', '.join(nomi)] if nomi else [])

    out.append('')
    uscita.parent.mkdir(parents=True, exist_ok=True)
    uscita.write_text('\n'.join(out), encoding='utf-8')
    print('Scritto %s' % uscita)
    return 0


if __name__ == '__main__':
    sys.exit(main())
