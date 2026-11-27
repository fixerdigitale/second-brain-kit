#!/usr/bin/env python3
"""Genera l'indice del catalogo che usano l'onboarding, il piano e mappa-vault.

Legge le schede in <repo>/catalogo/<area>/<slug>.md (frontmatter + testo) e scrive:
  - <plugin>/catalogo-indice.json            (per le skill piano-upgrade e installa)
  - <plugin>/skills/mappa-vault/catalogo.md  (elenco leggibile per mappa-vault)

Aggiunge a ogni scheda: area dell'onboarding (le 8 aree), gruppo del piano
(non perdere / non rispiegare / non rifare / delegare), tono minimo, e i segni
da cui si capisce che la persona ce l'ha gia'.

Uso:
  genera_indice_catalogo.py [--repo <cartella-della-repo>] [--controlla]

  --controlla  non scrive niente: esce con 1 se l'indice su disco non e' aggiornato
               o se una scheda rimanda a un pacchetto che non esiste.
Solo libreria standard di Python 3.
"""
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.realpath(os.path.join(QUI, ".."))

# Schede fuse in altre: restano fuori dall'indice anche se il file c'e' ancora.
FUSE = {
    "canali-archivio-call": "ricerca-call-trascritte",
    "memoria-revisore-serale": "memoria-revisore-notturno",
    "agenti-archivista-fine-giornata": "memoria-revisore-notturno",
    "memoria-archivista-correzioni": "memoria-archivista-correzioni-agli-agenti",
    "agenti-smistamento-per-taglia": "agenti-regia-e-smistamento",
    "agenti-regia-delega-con-controllo": "agenti-regia-e-smistamento",
    "hook-avviso-contesto": "hook-contesto-avviso-e-compressione",
    "hook-compressione-automatica": "hook-contesto-avviso-e-compressione",
    "hook-tempo-per-progetto": "hook-tempo-per-task",
    "canali-pagine-dietro-login": "canali-report-pagine",
    "sicurezza-regola-3-2-1": "sicurezza-backup-notturno",
}

AREA_PREDEFINITA = {
    "memoria": "memoria", "ricerca": "ricerca", "agenti": "metodo", "automazioni": "automazioni_canali",
    "canali": "automazioni_canali", "sicurezza": "sicurezza_ripristino", "impara": "correzioni", "skill": "mestiere",
}
AREA_SCHEDA = {
    "memoria-claude-md-a-sezioni": "contesto",
    "memoria-handoff-e-sistema": "contesto",
    "memoria-indice-e-regole-doro": "correzioni",
    "memoria-feedback-why-how": "correzioni",
    "memoria-revisore-notturno": "correzioni",
    "memoria-archivista-correzioni-agli-agenti": "correzioni",
    "hook-contesto-avviso-e-compressione": "contesto",
    "hook-handoff-prima-compressione": "contesto",
    "hook-statusline-contesto": "contesto",
    "hook-stato-a-inizio-sessione": "contesto",
    "hook-guardia-comandi": "sicurezza_ripristino",
    "hook-guardia-email": "sicurezza_ripristino",
    "hook-smistatore-procedure": "metodo",
    "hook-domanda-breve": "metodo",
    "hook-plugin-claude-council": "metodo",
    "skill-contro-parere": "metodo",
    "skill-pipeline-di-lavoro": "metodo",
    "skill-roadmap-lavoro": "metodo",
    "skill-stile-risposte": "metodo",
    "skill-grilling": "metodo",
    "skill-triage": "metodo",
    "skill-cerca-strumento": "sicurezza_ripristino",
    "skill-sicurezza-codice": "sicurezza_ripristino",
    "skill-web-research": "ricerca",
    "canali-board-task": "metodo",
}
GRUPPO_AREA = {
    "sicurezza_ripristino": "1-non-perdere",
    "contesto": "2-non-rispiegare", "memoria": "2-non-rispiegare",
    "correzioni": "2-non-rispiegare", "ricerca": "2-non-rispiegare",
    "metodo": "3-non-rifare", "mestiere": "3-non-rifare",
    "automazioni_canali": "4-delegare",
}
GRUPPO_SCHEDA = {
    "agenti-esecutore-costruttore": "4-delegare",
    "agenti-regia-e-smistamento": "4-delegare",
    "agenti-lavori-lunghi-codex": "4-delegare",
    "agenti-squadra-per-ruolo": "4-delegare",
    "agenti-sistemista-settimanale": "4-delegare",
}
TONO_LIVELLO = {"base": "T0", "medio": "T1", "avanzato": "T2"}

# Segni (verificabili dai file) che la persona ha gia' la cosa, in tutto o in parte.
SEGNI = {
    "memoria-claude-md-a-sezioni": "CLAUDE.md con almeno 3 titoli ## (chi sono, come rispondere, dove stanno le cose, regole)",
    "memoria-indice-e-regole-doro": "MEMORY.md o indice.md che elenca le note, con un blocco di regole d'oro con un tetto",
    "memoria-feedback-why-how": "file di correzione con un perche' e un come si applica (Why / How to apply, Perche' / Come)",
    "memoria-fatti-vs-correzioni": "fatti (clienti, progetti) e correzioni su come lavorare in due posti diversi",
    "memoria-vault-etichette-alla-nascita": "note con frontmatter coerente (tipo:, cliente:, tags:) nella gran parte delle note",
    "memoria-handoff-e-sistema": "file HANDOFF.md o SISTEMA.md (o simili: STATO.md, NOTE-PROGETTO.md) nelle cartelle dei lavori lunghi",
    "memoria-riordino-handoff": "uno script o una skill che sposta i fatti stabili dagli HANDOFF a una scheda",
    "memoria-raccolta-sessioni": "un riepilogo periodico delle sessioni passate (file datati generati da uno script)",
    "memoria-revisore-notturno": "un giro programmato (cron, timer, Utilita' di pianificazione) che rilegge le sessioni",
    "memoria-fatti-da-chat-e-vocali": "esportazioni di chat o trascrizioni di vocali portate nel vault",
    "ricerca-qmd-sul-pc": "QMD o un'altra ricerca per significato installata (server MCP di ricerca nelle note)",
    "ricerca-basic-memory": "Basic Memory fra i server MCP",
    "ricerca-archivio-soluzioni": "una cartella soluzioni/ o simile con problemi risolti e la loro causa",
    "ricerca-inventario-notturno": "un INVENTARIO.md o simile, rigenerato da uno script",
    "ricerca-call-trascritte": "trascrizioni di call in Markdown nel vault (cartella Call/ o simile)",
    "agenti-esecutore-costruttore": "sotto-agenti in .claude/agents/ con un modello piu' piccolo (haiku, sonnet)",
    "agenti-regia-e-smistamento": "una skill o una regola che dice chi fa quale lavoro e chi controlla la consegna",
    "agenti-revisore-prima-di-mandare": "un sotto-agente o una skill di revisione prima di pubblicare o mandare",
    "hook-contesto-avviso-e-compressione": "autoCompactWindow o un hook che avvisa sul contesto in settings.json",
    "hook-handoff-prima-compressione": "un hook PreCompact in settings.json",
    "hook-statusline-contesto": "statusLine in settings.json",
    "hook-guardia-comandi": "un hook PreToolUse che ferma comandi",
    "hook-suono-fine-lavoro": "un hook Stop o Notification che fa un suono o una notifica",
    "hook-stato-a-inizio-sessione": "un hook SessionStart che aggiunge contesto",
    "skill-contro-parere": "una skill o una regola contro il dare ragione per forza",
    "skill-pipeline-di-lavoro": "procedure scritte a passi per i lavori che si ripetono (pipeline/, procedure/)",
    "skill-stile-risposte": "regole di stile delle risposte nel CLAUDE.md o in una skill",
    "sicurezza-permessi-deny-ask": "permissions.deny in settings.json con i file dei segreti",
    "sicurezza-backup-notturno": "git con un remoto e un salvataggio negli ultimi 7 giorni, o un altro backup fuori dal PC",
    "sicurezza-prova-ripristino": "una data di prova di ripristino scritta da qualche parte",
    "sicurezza-copie-datate": "file .bak-AAAAMMGG accanto ai file importanti, o una regola che le chiede",
    "sicurezza-versioni-locali": "git locale nella cartella di lavoro",
    "sicurezza-niente-password-in-chat": "nessun segreto in chiaro nelle note (cerca-segreti pulito)",
    "sicurezza-segreti-file-unico": "un solo file di segreti fuori dalle note, ignorato da git",
    "sicurezza-copia-settimanale": "una copia datata della cartella di lavoro fuori dal PC (cloud, chiavetta) negli ultimi 14 giorni, o un backup automatico",
    "sicurezza-chiave-finita-online": "cerca-segreti pulito sui file seguiti da git con un remoto e nelle cartelle sincronizzate",
}


def frontmatter(testo):
    if not testo.startswith("---"):
        return {}, testo
    fine = testo.find("\n---", 3)
    if fine < 0:
        return {}, testo
    campi = {}
    for riga in testo[3:fine].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", riga.strip())
        if m:
            v = m.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            campi[m.group(1)] = v
    return campi, testo[fine + 4:]


def sezione(corpo, etichetta, limite):
    m = re.search(r"\*\*" + re.escape(etichetta) + r"\.?\*\*\s*(.+?)(?:\n\s*\n|\Z)", corpo, re.S)
    if not m:
        return ""
    t = " ".join(m.group(1).split())
    return t if len(t) <= limite else t[: limite - 1].rsplit(" ", 1)[0] + "…"


def costruisci(repo):
    cat = os.path.join(repo, "catalogo")
    schede, avvisi = [], []
    for area in sorted(os.listdir(cat)):
        d = os.path.join(cat, area)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md"):
                continue
            with open(os.path.join(d, f), encoding="utf-8") as fh:
                fm, corpo = frontmatter(fh.read())
            slug = fm.get("slug") or f[:-3]
            if slug in FUSE:
                avvisi.append("fusa, fuori dall'indice: %s -> %s (il file catalogo/%s/%s si puo' togliere)" % (slug, FUSE[slug], area, f))
                continue
            pacchetto = fm.get("pacchetto", "")
            ha_pacchetto = pacchetto.startswith("pacchetti/")
            if ha_pacchetto and not os.path.isfile(os.path.join(repo, pacchetto, "LEGGIMI.md")):
                avvisi.append("pacchetto mancante per %s: %sLEGGIMI.md" % (slug, pacchetto))
            area_ob = AREA_SCHEDA.get(slug, AREA_PREDEFINITA.get(fm.get("area", area), "metodo"))
            livello = fm.get("livello", "medio")
            tono = TONO_LIVELLO.get(livello, "T1")
            if fm.get("dove_gira") == "server":
                tono = "T3"
            titolo_en, scheda_en = "", ""
            p_en = os.path.join(repo, "catalog", area, f)
            if os.path.isfile(p_en):
                with open(p_en, encoding="utf-8") as fh:
                    titolo_en = frontmatter(fh.read())[0].get("title", "")
                scheda_en = "catalog/%s/%s" % (area, f)
            schede.append({
                "slug": slug,
                "titolo": fm.get("titolo", slug),
                "titolo_en": titolo_en,
                "famiglia": fm.get("area", area),
                "area_onboarding": area_ob,
                "gruppo_piano": GRUPPO_SCHEDA.get(slug, GRUPPO_AREA[area_ob]),
                "dove_gira": fm.get("dove_gira", "PC"),
                "livello": livello,
                "tono_minimo": tono,
                "costo": fm.get("costo", ""),
                "stato_da_me": fm.get("stato", ""),
                "pacchetto": pacchetto if ha_pacchetto else "",
                "tipo": "pacchetto" if ha_pacchetto else (pacchetto or "nessuno"),
                "scheda": "catalogo/%s/%s" % (area, f),
                "scheda_en": scheda_en,
                "problema": sezione(corpo, "Il problema", 260),
                "quando_non_serve": sezione(corpo, "Quando non ti serve", 220),
                "segni_che_ce_l_hai": SEGNI.get(slug, ""),
            })
    for s in SEGNI:
        if s not in {x["slug"] for x in schede}:
            avvisi.append("segni scritti per una scheda che non c'e': %s" % s)
    # una sola versione di cerca_segreti: quella del pacchetto deve essere uguale a quella del plugin
    a = os.path.join(PLUGIN, "scripts", "cerca_segreti.py")
    b = os.path.join(repo, "pacchetti", "sicurezza-niente-password-in-chat", "cerca_segreti.py")
    if os.path.isfile(a) and os.path.isfile(b) and open(a, "rb").read() != open(b, "rb").read():
        avvisi.append("pacchetto diverso dal plugin: pacchetti/sicurezza-niente-password-in-chat/cerca_segreti.py "
                      "(copia lo script del plugin)")
    return schede, avvisi


NOMI_AREE = {
    "contesto": "Contesto", "memoria": "Memoria", "correzioni": "Correzioni", "metodo": "Metodo",
    "mestiere": "Mestiere", "ricerca": "Ricerca", "automazioni_canali": "Automazioni e canali",
    "sicurezza_ripristino": "Sicurezza e ripristino",
}


def catalogo_md(schede):
    righe = [
        "# Catalogo «Cosa uso io» — elenco da cui si sceglie",
        "",
        "File generato da `scripts/genera_indice_catalogo.py`: non modificarlo a mano, rilancia lo script.",
        "Formato: `slug` (dove gira, livello, tono minimo): titolo. La scheda intera sta in `catalogo/<famiglia>/<slug>.md`",
        "della repo del kit; il pacchetto, quando c'e', in `pacchetti/<slug>/LEGGIMI.md`.",
        "",
        "Dove gira: **PC** = sono file, funziona anche a PC spento; **PC acceso** = gira solo quando il PC è acceso;",
        "**server** = serve un computer sempre acceso (per queste c'è solo l'idea, niente pacchetto).",
        "",
    ]
    for area, nome in NOMI_AREE.items():
        gruppo = [s for s in schede if s["area_onboarding"] == area]
        if not gruppo:
            continue
        righe.append("## " + nome)
        for s in gruppo:
            extra = "" if s["pacchetto"] else " — senza pacchetto (%s)" % s["tipo"]
            righe.append("- `%s` (%s, %s, %s): %s%s" % (s["slug"], s["dove_gira"], s["livello"], s["tono_minimo"], s["titolo"], extra))
        righe.append("")
    righe += [
        "## Segnale → scheda (scorciatoia)",
        "",
        "| Cosa vedi o senti | Scheda da considerare |",
        "|---|---|",
        "| Nessuna copia fuori dal PC, chi inizia o spegne il PC | `sicurezza-copia-settimanale` |",
        "| Nessun remoto git, ultimo salvataggio vecchio, una sola copia | `sicurezza-backup-notturno` |",
        "| Una chiave in un file salvato online (git con remoto, cartella sincronizzata) | `sicurezza-chiave-finita-online` |",
        "| Backup mai riaperto | `sicurezza-prova-ripristino` |",
        "| Chiavi o password dentro le note | `sicurezza-niente-password-in-chat`, `sicurezza-segreti-file-unico` |",
        "| Permessi tutti liberi o tutti da chiedere | `sicurezza-permessi-deny-ask` |",
        "| Modifiche fatte senza una copia prima | `sicurezza-copie-datate`, `sicurezza-versioni-locali` |",
        "| «Glielo ripeto ogni volta» | `memoria-indice-e-regole-doro`, `memoria-feedback-why-how` |",
        "| Correzioni dette tante volte ma mai fissate | `impara-regole-proposte-con-ok`, `memoria-revisore-notturno` |",
        "| CLAUDE.md lungo, disordinato o contraddittorio | `memoria-claude-md-a-sezioni` |",
        "| Fatti e correzioni mescolati, memoria che cresce senza ordine | `memoria-fatti-vs-correzioni` |",
        "| Lavori lunghi rispiegati a ogni sessione | `memoria-handoff-e-sistema`, `hook-handoff-prima-compressione` |",
        "| HANDOFF enormi, fatti stabili sepolti | `memoria-riordino-handoff` |",
        "| «Non trovo più quella nota» | `memoria-vault-etichette-alla-nascita`, `ricerca-qmd-sul-pc` |",
        "| Lo stesso problema tecnico risolto due volte | `ricerca-archivio-soluzioni` |",
        "| «Non ce l'ho» detto su cose che ci sono | `ricerca-inventario-notturno` |",
        "| Impegni presi in call e persi | `ricerca-call-trascritte` |",
        "| Smistamento personale/azienda che sbaglia cartella | `memoria-vault-etichette-alla-nascita`, `hook-smistatore-procedure` |",
        "| Sessioni lunghe che si perdono | `hook-contesto-avviso-e-compressione`, `hook-statusline-contesto` |",
        "| Claude dà sempre ragione | `skill-contro-parere` |",
        "| Risposte troppo lunghe | `skill-stile-risposte` |",
        "| Consumi alti per lavori semplici | `agenti-esecutore-costruttore`, `agenti-regia-e-smistamento` |",
        "| Correzioni che si perdono fra un lavoro e l'altro | `skill-pipeline-di-lavoro` |",
        "",
        "Quello che ho provato e lasciato, con il motivo: `catalogo/scartati.md`.",
        "",
    ]
    return "\n".join(righe)


def main(argv):
    repo = os.path.realpath(os.path.join(PLUGIN, "..", ".."))
    controlla = "--controlla" in argv
    if "--repo" in argv:
        repo = os.path.realpath(os.path.expanduser(argv[argv.index("--repo") + 1]))
    if not os.path.isdir(os.path.join(repo, "catalogo")):
        print("catalogo non trovato in " + repo, file=sys.stderr)
        return 2
    schede, avvisi = costruisci(repo)
    indice = {"generato_da": "scripts/genera_indice_catalogo.py", "schede": schede}
    testo_json = json.dumps(indice, ensure_ascii=False, indent=1) + "\n"
    testo_md = catalogo_md(schede)
    p_json = os.path.join(PLUGIN, "catalogo-indice.json")
    p_md = os.path.join(PLUGIN, "skills", "mappa-vault", "catalogo.md")
    for a in avvisi:
        print("avviso: " + a, file=sys.stderr)
    if controlla:
        vecchio = open(p_json, encoding="utf-8").read() if os.path.exists(p_json) else ""
        mancanti = [a for a in avvisi if a.startswith(("pacchetto mancante", "pacchetto diverso"))]
        if vecchio != testo_json:
            print("indice non aggiornato: rilancia lo script", file=sys.stderr)
            return 1
        return 1 if mancanti else 0
    with open(p_json, "w", encoding="utf-8") as fh:
        fh.write(testo_json)
    with open(p_md, "w", encoding="utf-8") as fh:
        fh.write(testo_md)
    print("%d schede -> %s e %s" % (len(schede), os.path.relpath(p_json, repo), os.path.relpath(p_md, repo)))
    return 0


if __name__ == "__main__":
    for _f in (sys.stdout, sys.stderr):
        try:
            _f.reconfigure(encoding="utf-8", errors="backslashreplace")
        except (AttributeError, ValueError):
            pass
    sys.exit(main(sys.argv[1:]))
