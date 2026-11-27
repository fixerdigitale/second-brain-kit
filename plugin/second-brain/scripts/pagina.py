#!/usr/bin/env python3
"""Trasforma MAPPA.md o PIANO-UPGRADE.md in una pagina HTML statica.

La pagina si apre con un doppio clic, senza login e senza internet: niente
script, niente font o immagini presi da fuori.

Uso:
  pagina.py <file.md> [<file.html>] [--lingua it|en]   (di serie: stesso nome, .html)

Capisce titoli, paragrafi, elenchi, tabelle, **grassetto**, `codice` e [link](...).
Solo libreria standard di Python 3.
"""
import html
import os
import re
import sys
import urllib.parse

QUI = os.path.dirname(os.path.abspath(__file__))
MODELLO = os.path.join(QUI, "..", "modelli", "pagina.html")


def a_indirizzo(dest):
    """Un percorso del disco diventa un indirizzo file:/// che il browser apre (spazi compresi)."""
    if re.match(r"^[a-z][a-z0-9+.\-]*://", dest, re.I) or dest.startswith(("#", "mailto:")):
        return dest
    p = dest
    if re.match(r"^[A-Za-z]:[\\/]", p) or p.startswith("/") or p.startswith("~"):
        p = os.path.expanduser(p).replace("\\", "/")
        if not p.startswith("/"):
            p = "/" + p
        return "file://" + urllib.parse.quote(p, safe="/:")
    return urllib.parse.quote(p.replace("\\", "/"), safe="/:#?=&.")


def in_linea(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"<em>\1</em>", t)

    def link(m):
        testo, dest = m.group(1), html.unescape(m.group(2).strip().strip("<>"))
        if re.match(r"^\s*(javascript|data|vbscript):", dest, re.I):
            return testo
        return '<a href="%s">%s</a>' % (html.escape(a_indirizzo(dest), quote=True), testo)
    # il percorso puo' contenere spazi (C:\Users\Nome Cognome\...): si accetta fino alla ) finale
    t = re.sub(r"\[([^\]]+)\]\(([^)\n]+)\)", link, t)
    return t


def converti(md):
    righe = md.replace("\r\n", "\n").split("\n")
    # salta il frontmatter
    if righe and righe[0].strip() == "---":
        for j in range(1, len(righe)):
            if righe[j].strip() == "---":
                righe = righe[j + 1:]
                break
    fuori, i, titolo = [], 0, None
    while i < len(righe):
        r = righe[i]
        s = r.strip()
        if not s:
            i += 1
            continue
        if s.startswith("```"):
            blocco = []
            i += 1
            while i < len(righe) and not righe[i].strip().startswith("```"):
                blocco.append(righe[i])
                i += 1
            fuori.append("<pre><code>%s</code></pre>" % html.escape("\n".join(blocco)))
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            liv = len(m.group(1))
            if liv == 1 and titolo is None:
                titolo = m.group(2)
            fuori.append("<h%d>%s</h%d>" % (liv, in_linea(m.group(2)), liv))
            i += 1
            continue
        if s.startswith("|"):
            tab = []
            while i < len(righe) and righe[i].strip().startswith("|"):
                tab.append(righe[i].strip())
                i += 1
            celle = [[c.strip() for c in t.strip("|").split("|")] for t in tab]
            corpo = [c for c in celle if not all(re.fullmatch(r":?-{2,}:?", x or "--") for x in c)]
            if not corpo:
                continue
            h = "<thead><tr>%s</tr></thead>" % "".join("<th>%s</th>" % in_linea(c) for c in corpo[0])
            b = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % in_linea(c) for c in row) for row in corpo[1:])
            fuori.append('<div class="tab"><table>%s<tbody>%s</tbody></table></div>' % (h, b))
            continue
        if re.match(r"^([-*]|\d+\.)\s+", s):
            ordinata = bool(re.match(r"^\d+\.", s))
            voci = []
            while i < len(righe) and re.match(r"^\s*([-*]|\d+\.)\s+", righe[i]):
                voci.append(re.sub(r"^\s*([-*]|\d+\.)\s+", "", righe[i]))
                i += 1
                while i < len(righe) and righe[i].startswith("  ") and righe[i].strip() and not re.match(r"^\s*([-*]|\d+\.)\s+", righe[i]):
                    voci[-1] += " " + righe[i].strip()
                    i += 1
            tag = "ol" if ordinata else "ul"
            fuori.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % in_linea(v) for v in voci), tag))
            continue
        if s.startswith(">"):
            blocco = []
            while i < len(righe) and righe[i].strip().startswith(">"):
                blocco.append(righe[i].strip()[1:].strip())
                i += 1
            fuori.append("<blockquote>%s</blockquote>" % in_linea(" ".join(blocco)))
            continue
        par = [s]
        i += 1
        while i < len(righe) and righe[i].strip() and not re.match(r"^(#|\||[-*]\s|\d+\.\s|>|```)", righe[i].strip()):
            par.append(righe[i].strip())
            i += 1
        fuori.append("<p>%s</p>" % in_linea(" ".join(par)))
    return titolo or "second-brain", "\n".join(fuori)


def senza_segreti(md):
    """Nessun segreto entra nella pagina: le chiavi riconoscibili diventano [OSCURATO],
    una riga dove resta una password annunciata («Password CRM: ...») si toglie."""
    sys.path.insert(0, QUI)
    try:
        import cerca_segreti
    except ImportError:
        return md, []
    righe, tolte = [], []
    for n, r in enumerate(md.split("\n"), 1):
        for _, espr in cerca_segreti.FORME:
            r = espr.sub("[OSCURATO]", r)
        if cerca_segreti.nomi_in_riga(r):
            tolte.append(n)
            r = "- [riga tolta: sembrava contenere un segreto]"
        righe.append(r)
    return "\n".join(righe), tolte


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    lingua = "it"
    if "--lingua" in argv:
        k = argv.index("--lingua")
        lingua = argv[k + 1] if k + 1 < len(argv) else "it"
        del argv[k:k + 2]
    src = argv[0]
    dst = argv[1] if len(argv) > 1 else os.path.splitext(src)[0] + ".html"
    with open(src, encoding="utf-8") as fh:
        testo, tolte = senza_segreti(fh.read())
    for n in tolte:
        print("riga %d tolta dalla pagina: sembrava contenere una chiave o una password "
              "(controlla anche %s)" % (n, os.path.basename(src)), file=sys.stderr)
    titolo, corpo = converti(testo)
    with open(MODELLO, encoding="utf-8") as fh:
        modello = fh.read()
    pagina = modello.replace("{{TITOLO}}", html.escape(titolo)).replace("{{CONTENUTO}}", corpo).replace("{{LINGUA}}", html.escape(lingua))
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(pagina)
    print(dst)
    return 0


if __name__ == "__main__":
    for _f in (sys.stdout, sys.stderr):
        try:
            _f.reconfigure(encoding="utf-8", errors="backslashreplace")
        except (AttributeError, ValueError):
            pass
    sys.exit(main(sys.argv[1:]))
