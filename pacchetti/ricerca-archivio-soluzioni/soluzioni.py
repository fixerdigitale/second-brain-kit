#!/usr/bin/env python3
"""Archivio delle soluzioni: cosa si e' rotto, perche', come si e' aggiustato.

Una scheda markdown per problema, in una cartella del tuo vault. Solo libreria standard,
funziona su Mac, Windows e Linux con Python 3.9 o piu' recente.

Dove sta l'archivio (il primo che trova):
  1. la variabile d'ambiente SOLUZIONI_DIR
  2. <cartella-vault>/soluzioni, se imposti VAULT_DIR
  3. ~/vault/soluzioni

Uso:
  python3 soluzioni.py cerca <parole>     cerca nelle schede, le piu' pertinenti per prime
  python3 soluzioni.py mostra <slug>      stampa una scheda intera
  python3 soluzioni.py elenco [tag]       elenca le schede, eventualmente filtrate per tag
  python3 soluzioni.py nuova <slug>       crea una scheda nuova dal modello
  python3 soluzioni.py indice             rigenera INDICE.md
"""
import getpass
import os
import re
import sys
from datetime import date
from pathlib import Path

QUI = Path(__file__).resolve().parent


def archivio():
    if os.environ.get('SOLUZIONI_DIR'):
        return Path(os.environ['SOLUZIONI_DIR']).expanduser()
    if os.environ.get('VAULT_DIR'):
        return Path(os.environ['VAULT_DIR']).expanduser() / 'soluzioni'
    return Path.home() / 'vault' / 'soluzioni'


ARCHIVIO = archivio()
INDICE = ARCHIVIO / 'INDICE.md'

MODELLO_DI_RISERVA = """---
slug: {slug}
titolo: {slug}
data: {oggi}
autore: {autore}
sistemi: []
tag: []
---

## Sintomo

## Causa

## Come si riconosce

## Soluzione

## Verifica

## Vicoli ciechi

## Riusabile per
"""


def modello():
    p = QUI / 'modello-scheda.md'
    return p.read_text(encoding='utf-8') if p.is_file() else MODELLO_DI_RISERVA


def schede():
    if not ARCHIVIO.is_dir():
        return []
    return sorted(p for p in ARCHIVIO.glob('*.md') if p.name != 'INDICE.md')


def frontmatter(testo):
    dati = {}
    m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n', testo, re.S)
    if not m:
        return dati
    for riga in m.group(1).splitlines():
        if ':' in riga:
            chiave, valore = riga.split(':', 1)
            dati[chiave.strip()] = valore.strip().strip('"').strip("'")
    return dati


def corpo(testo):
    return re.sub(r'^---\r?\n.*?\r?\n---\r?\n', '', testo, flags=re.S)


def campo_lista(valore):
    return [v.strip() for v in valore.strip('[]').split(',') if v.strip()]


def leggi(p):
    return p.read_text(encoding='utf-8', errors='replace')


def cerca(parole):
    if not parole:
        print('Serve almeno una parola da cercare.')
        return 1
    termini = [p.lower() for p in parole]
    risultati = []
    for p in schede():
        testo = leggi(p)
        basso = testo.lower()
        fm = frontmatter(testo)
        titolo = fm.get('titolo', p.stem)
        # Le parole nel titolo, nei tag e nel nome del file pesano 5 volte quelle nel testo.
        testa = ' '.join([titolo, fm.get('tag', ''), fm.get('sistemi', ''), p.stem]).lower()
        punti, contesti = 0, []
        for t in termini:
            nel_corpo = basso.count(t)
            punti += nel_corpo + 5 * testa.count(t)
            if nel_corpo:
                for riga in corpo(testo).splitlines():
                    if t in riga.lower() and riga.strip() and not riga.startswith('#'):
                        contesti.append(riga.strip()[:160])
                        break
        if punti:
            risultati.append((punti, p.stem, titolo, fm.get('data', ''), contesti[:2]))
    if not risultati:
        print('Nessuna scheda trovata per: ' + ' '.join(parole))
        print('Se poi lo risolvi, scrivila:  python3 soluzioni.py nuova <slug>')
        return 1
    risultati.sort(reverse=True)
    print('%d schede pertinenti:\n' % len(risultati))
    for punti, slug, titolo, data, contesti in risultati[:15]:
        print('  %s  [%s]' % (titolo, slug))
        print('    data %s - rilevanza %d' % (data or '?', punti))
        for c in contesti:
            print('    - ' + c)
        print()
    return 0


def mostra(slug):
    p = ARCHIVIO / (slug.removesuffix('.md') + '.md')
    if not p.is_file():
        print('Scheda non trovata: %s' % slug)
        return 1
    print(leggi(p))
    return 0


def elenco(tag=None):
    righe = []
    for p in schede():
        fm = frontmatter(leggi(p))
        tags = campo_lista(fm.get('tag', ''))
        if tag and tag.lower() not in [t.lower() for t in tags]:
            continue
        righe.append((fm.get('data', ''), p.stem, fm.get('titolo', p.stem), tags))
    if not righe:
        print('Archivio vuoto.' if not tag else 'Nessuna scheda con tag "%s".' % tag)
        return 0
    righe.sort(reverse=True)
    for data, slug, titolo, tags in righe:
        print('%s  %-42s  %s' % (data or '?', slug, titolo))
        if tags:
            print('%s  %s' % (' ' * 10, ' '.join('#' + t for t in tags)))
    print('\n%d schede in %s' % (len(righe), ARCHIVIO))
    return 0


def nuova(slug):
    slug = re.sub(r'[^a-z0-9-]+', '-', slug.lower().removesuffix('.md')).strip('-')
    if not slug:
        print('Slug non valido.')
        return 1
    ARCHIVIO.mkdir(parents=True, exist_ok=True)
    p = ARCHIVIO / (slug + '.md')
    if p.exists():
        print("Esiste gia': %s" % p)
        return 1
    try:
        autore = getpass.getuser()
    except Exception:
        autore = 'io'
    p.write_text(modello().format(slug=slug, oggi=date.today().isoformat(), autore=autore),
                 encoding='utf-8')
    print('Creata: %s' % p)
    print('Compilala, poi lancia:  python3 soluzioni.py indice')
    return 0


def indice():
    ARCHIVIO.mkdir(parents=True, exist_ok=True)
    voci = []
    for p in schede():
        fm = frontmatter(leggi(p))
        voci.append((fm.get('data', ''), p.name, fm.get('titolo', p.stem),
                     campo_lista(fm.get('sistemi', ''))))
    voci.sort(reverse=True)
    testo = ['# Archivio soluzioni', '',
             "Cosa si e' rotto, perche' e come si e' aggiustato. Una scheda per problema.", '',
             '| Data | Scheda | Problema | Sistemi |', '| --- | --- | --- | --- |']
    for data, nome, titolo, sistemi in voci:
        testo.append('| %s | [%s](%s) | %s | %s |' % (
            data or '?', nome[:-3], nome, titolo, ', '.join(sistemi) or '-'))
    testo += ['', '_Rigenerato da `soluzioni.py indice`. %d schede._' % len(voci), '']
    INDICE.write_text('\n'.join(testo), encoding='utf-8')
    print('Indice aggiornato: %s (%d schede)' % (INDICE, len(voci)))
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print('Archivio in uso: %s' % ARCHIVIO)
        return 0
    cmd, resto = sys.argv[1], sys.argv[2:]
    if cmd in ('cerca', 'search'):
        return cerca(resto)
    if cmd in ('mostra', 'show'):
        return mostra(resto[0]) if resto else (print('Serve lo slug.') or 1)
    if cmd in ('elenco', 'list'):
        return elenco(resto[0] if resto else None)
    if cmd in ('nuova', 'new'):
        return nuova(resto[0]) if resto else (print('Serve lo slug.') or 1)
    if cmd in ('indice', 'index'):
        return indice()
    print(__doc__)
    return 1


if __name__ == '__main__':
    sys.exit(main())
