#!/usr/bin/env python3
"""Trasforma le trascrizioni delle call (.txt, .vtt, .srt) in note markdown ricercabili.

Molti strumenti di registrazione (Fathom, Zoom, Meet, Teams, tl;dv...) danno la trascrizione
come file di testo senza titolo, data o partecipanti. Una ricerca nel vault la trova male.
Questo script scrive una nota per call con in testa titolo, data e chi parla, poi la
trascrizione intera. Non tocca i file originali e non riscrive le note gia' fatte.

Solo libreria standard, Python 3.9 o piu' recente, Mac, Windows e Linux.

Uso:
  python3 call_in_markdown.py <cartella-trascrizioni> <cartella-vault>/Call
"""
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

ESTENSIONI = {'.txt', '.vtt', '.srt'}
DATA_NEL_NOME = re.compile(r'(20\d\d)[-_.]?(\d\d)[-_.]?(\d\d)')
TEMPO_VTT = re.compile(r'^\d{1,2}:\d\d(:\d\d)?[.,]\d{3}\s+-->\s+')
PARLANTE = re.compile(r'^(?:\[[\d:]+\]\s*)?([A-Z][\w\'. -]{1,40}):\s')


def slug(testo):
    t = unicodedata.normalize('NFKD', testo).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')[:60].rstrip('-') or 'call'


def pulisci(testo, estensione):
    """Toglie numeri di blocco e tempi dei sottotitoli; il .txt resta com'e'."""
    if estensione == '.txt':
        return testo.strip()
    righe = []
    for r in testo.splitlines():
        r = r.strip()
        if not r or r == 'WEBVTT' or r.isdigit() or TEMPO_VTT.match(r) or '-->' in r:
            continue
        r = re.sub(r'<[^>]+>', '', r)  # tag di voce dei .vtt, es. <v Nome>
        if not righe or righe[-1] != r:
            righe.append(r)
    return '\n'.join(righe)


def data_della_call(p):
    m = DATA_NEL_NOME.search(p.stem)
    if m:
        try:
            return datetime(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            pass
    return datetime.fromtimestamp(p.stat().st_mtime)


def titolo_della_call(p):
    t = DATA_NEL_NOME.sub('', p.stem)
    t = re.sub(r'[-_]+', ' ', t).strip()
    return t[:1].upper() + t[1:] if t else 'Call'


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    sorgente, uscita = Path(sys.argv[1]).expanduser(), Path(sys.argv[2]).expanduser()
    if not sorgente.is_dir():
        print('Cartella delle trascrizioni non trovata: %s' % sorgente)
        return 1
    uscita.mkdir(parents=True, exist_ok=True)
    fatte = saltate = 0
    for p in sorted(sorgente.iterdir()):
        if p.suffix.lower() not in ESTENSIONI or not p.is_file():
            continue
        data, titolo = data_della_call(p), titolo_della_call(p)
        nota = uscita / ('%s-%s.md' % (data.strftime('%Y-%m-%d'), slug(titolo)))
        if nota.exists():
            saltate += 1
            continue
        testo = pulisci(p.read_text(encoding='utf-8', errors='replace'), p.suffix.lower())
        parlanti = []
        for r in testo.splitlines():
            m = PARLANTE.match(r)
            if m and m[1].strip() not in parlanti:
                parlanti.append(m[1].strip())
        contenuto = [
            '---', 'tipo: call', 'data: %s' % data.strftime('%Y-%m-%d'),
            'parlano: [%s]' % ', '.join(parlanti[:12]), 'origine: %s' % p.name, '---', '',
            '# %s' % titolo, '',
            '- Data: %s' % data.strftime('%d/%m/%Y'),
            '- Parlano: %s' % (', '.join(parlanti[:12]) or 'non riconosciuti'), '',
            '## Trascrizione', '', testo, '']
        nota.write_text('\n'.join(contenuto), encoding='utf-8')
        fatte += 1
    print('Note scritte: %d, gia\' presenti: %d, in %s' % (fatte, saltate, uscita))
    return 0


if __name__ == '__main__':
    sys.exit(main())
