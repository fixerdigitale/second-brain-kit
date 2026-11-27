#!/usr/bin/env python3
"""Genera l'indice del catalogo che usano l'onboarding, il piano e mappa-vault.

Legge le schede in <repo>/catalogo/<area>/<slug>.md (frontmatter + testo) e scrive:
  - <plugin>/catalogo-indice.json            (per le skill piano-upgrade e installa)
  - <plugin>/skills/mappa-vault/catalogo.md  (elenco leggibile per mappa-vault)
  - <repo>/catalogo/README.md e <repo>/catalog/README.md (indice del catalogo, IT ed EN,
    con la colonna Stato presa dal campo «stato» delle schede)

Aggiunge a ogni scheda: area dell'onboarding (le 8 aree), gruppo del piano
(non perdere / non rispiegare / non rifare / delegare), tono minimo, e i segni
da cui si capisce che la persona ce l'ha gia'.

Uso:
  genera_indice_catalogo.py [--repo <cartella-della-repo>] [--controlla]

  --controlla  non scrive niente: esce con 1 se l'indice o i README del catalogo su disco
               non sono aggiornati, se una scheda rimanda a un pacchetto che non esiste,
               se una scheda ha uno stato che non si riconosce, o se un numero scritto a
               mano in README.md, README.it.md o CHANGELOG.md (schede, pacchetti, aree,
               scarti, stati) non torna con i file veri.
Solo libreria standard di Python 3.
"""
import argparse
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

# Stato della scheda, in 3 valori: dal campo «stato» (IT) e «status» (EN) delle schede.
# Si riconosce dall'inizio del testo; uno stato nuovo che non torna fa fallire --controlla.
STATI = ("uso", "pc", "proposta")
NOMI_STATO = {
    "it": {"uso": "la uso", "pc": "versione per PC", "proposta": "proposta"},
    "en": {"uso": "I use it", "pc": "PC version", "proposta": "proposal"},
}
INIZI_STATO = (
    ("lo uso", "uso"), ("la uso", "uso"), ("i use it", "uso"),
    ("mi è successo", "uso"), ("it happened to me", "uso"),
    ("versione per pc", "pc"), ("pc version", "pc"),
    # la copia settimanale: la facevo all'inizio, oggi c'e' il backup notturno; e' la forma per PC
    ("lo facevo all'inizio", "pc"), ("what i did at the start", "pc"),
    ("proposta", "proposta"), ("new proposal", "proposta"), ("proposal", "proposta"),
)


def stato_tipo(testo):
    t = (testo or "").strip().lower()
    for inizio, tipo in INIZI_STATO:
        if t.startswith(inizio):
            return tipo
    return ""

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
            titolo_en, scheda_en, stato_en = "", "", ""
            p_en = os.path.join(repo, "catalog", area, f)
            if os.path.isfile(p_en):
                with open(p_en, encoding="utf-8") as fh:
                    fm_en = frontmatter(fh.read())[0]
                titolo_en, stato_en = fm_en.get("title", ""), fm_en.get("status", "")
                scheda_en = "catalog/%s/%s" % (area, f)
            tipo_stato = stato_tipo(fm.get("stato", ""))
            if not tipo_stato:
                avvisi.append("stato non riconosciuto per %s: «%s» (aggiungilo a INIZI_STATO)" % (slug, fm.get("stato", "")))
            elif stato_en and stato_tipo(stato_en) != tipo_stato:
                avvisi.append("stato diverso fra IT ed EN per %s: «%s» / «%s»" % (slug, fm.get("stato", ""), stato_en))
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
                "stato_tipo": tipo_stato,
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


# --- README del catalogo (IT ed EN) -------------------------------------------------

# cartella -> (titolo IT, riga IT, titolo EN, riga EN), nell'ordine del README
AREE_README = (
    ("memoria", "Memoria", "dove tengo fatti, correzioni e lavoro aperto",
     "Memory", "where I keep facts, corrections and open work"),
    ("ricerca", "Ricerca", "come ritrovo le cose",
     "Search", "how I find things again"),
    ("impara", "Impara", "come il sistema migliora dalle correzioni",
     "Learn", "how the system improves from corrections"),
    ("automazioni", "Automazioni e hook", "cose che succedono da sole dentro Claude Code",
     "Automations and hooks", "things that happen on their own inside Claude Code"),
    ("agenti", "Agenti e modelli", "chi fa il lavoro e chi lo controlla",
     "Agents and models", "who does the work and who checks it"),
    ("canali", "Canali e giornata", "da dove arrivano le richieste e dove vanno i risultati",
     "Channels and my day", "where requests come from and where results go"),
    ("skill", "Skill", "metodo e mestiere",
     "Skills", "method and craft"),
    ("sicurezza", "Sicurezza e ripristino", "backup, permessi, segreti",
     "Security and recovery", "backups, permissions, secrets"),
)
ORDINE_LIVELLO = {"base": 0, "medio": 1, "avanzato": 2}
LIVELLO_EN = {"base": "basic", "medio": "intermediate", "avanzato": "advanced"}
DOVE_EN = {"PC": "PC", "PC acceso": "PC on", "server": "server"}

TESTA_IT = """# Catalogo

🇬🇧 [English](../catalog/README.md)

<!-- File generato da plugin/second-brain/scripts/genera_indice_catalogo.py: non modificarlo a mano, rilancia lo script. -->

Tutto quello che uso, come opzione. Ogni scheda racconta il problema che avevo, come l'ho risolto, perché così, e quando invece **non** ti serve. Non c'è un ordine giusto: prendi solo quello che ti risolve un problema che hai già.

> Tutto può girare su un PC; il PC non è sempre online, il server sì. Dove una scheda dice «server» racconto come lo uso io; dove dice «PC acceso», il pezzo funziona solo mentre il computer è acceso.

**Come leggere le colonne.** *Dove gira*: PC, PC acceso (serve il computer acceso a quell'ora) o server (lo uso così io, sul PC va adattato). *Livello*: base, medio, avanzato. *Stato*: «la uso» vuol dire che la uso così; «versione per PC» vuol dire che io la uso in un'altra forma (di solito sul server) e la scheda racconta come la adatterei a un PC; «proposta» vuol dire che non la uso così, è un'idea che metto a disposizione. *Pacchetto*: i file pronti da copiare, quando ci sono; «solo scheda» vuol dire che racconto come lo faccio, senza file.

In tutto **{totale} schede** in {aree} aree: {n_uso} «la uso», {n_pc} «versione per PC», {n_proposta} «proposta».

Quello che ho provato e lasciato sta in [scartati.md](scartati.md).
"""

TESTA_EN = """# Catalog

🇮🇹 [Italiano](../catalogo/README.md)

<!-- Generated by plugin/second-brain/scripts/genera_indice_catalogo.py: don't edit by hand, run the script again. -->

Everything I use, offered as an option. Each card tells the problem I had, how I solved it, why I did it that way, and when you **don't** need it. There's no right order: take only what solves a problem you already have.

> Everything can run on a PC; a PC isn't always online, a server is. Where a card says "server" I describe how I use it; where it says "PC on", the piece only works while the computer is switched on.

**How to read the columns.** *Runs on*: PC, PC on (the computer has to be on at that time) or server (that's how I use it; on a PC it needs adapting). *Level*: basic, intermediate, advanced. *Status*: "I use it" means I use it this way; "PC version" means I use it in another form (usually on the server) and the card describes how I'd adapt it to a PC; "proposal" means I don't use it this way, it's an idea I'm sharing. *Package*: ready-to-copy files, when there are any; "card only" means I describe how I do it, without files.

**{totale} cards** in {aree} areas: {n_uso} "I use it", {n_pc} "PC version", {n_proposta} "proposal". The cards are available in English (this folder) and Italian (catalogo/); the packages' read-me files are in Italian with a short English section. Claude Code can read and explain any of them for you.

What I tried and let go is in [discarded.md](discarded.md).
"""


def _ancora(titolo):
    a = re.sub(r"[^\w\- ]", "", titolo.lower(), flags=re.U)
    return a.replace(" ", "-")


def _chiave_titolo(t):
    return t.strip("«»\"' ").casefold()


def conteggi_stato(schede):
    return {k: sum(1 for x in schede if x["stato_tipo"] == k) for k in STATI}


def readme_catalogo(schede, lingua):
    en = lingua == "en"
    n = conteggi_stato(schede)
    aree_usate = [a for a in AREE_README if any(x["scheda"].split("/")[1] == a[0] for x in schede)]
    righe = [(TESTA_EN if en else TESTA_IT).format(
        totale=len(schede), aree=len(aree_usate), n_uso=n["uso"], n_pc=n["pc"], n_proposta=n["proposta"])]
    righe += ["## Areas" if en else "## Aree", ""]
    for cart, t_it, r_it, t_en, r_en in aree_usate:
        t, r = (t_en, r_en) if en else (t_it, r_it)
        righe.append("- [%s](#%s): %s" % (t, _ancora(t), r))
    righe.append("")
    for cart, t_it, r_it, t_en, r_en in aree_usate:
        t, r = (t_en, r_en) if en else (t_it, r_it)
        gruppo = [x for x in schede if x["scheda"].split("/")[1] == cart]
        titolo = (lambda x: x["titolo_en"] or x["titolo"]) if en else (lambda x: x["titolo"])
        gruppo.sort(key=lambda x: (ORDINE_LIVELLO.get(x["livello"], 1), _chiave_titolo(titolo(x))))
        righe += ["## " + t, "",
                  "%s. %d %s." % (r[0].upper() + r[1:], len(gruppo), ("cards" if en else "schede") if len(gruppo) != 1 else ("card" if en else "scheda")),
                  ""]
        if en:
            righe += ["| Title | Runs on | Level | Status | Link |", "|---|---|---|---|---|"]
        else:
            righe += ["| Titolo | Dove gira | Livello | Stato | Link |", "|---|---|---|---|---|"]
        for x in gruppo:
            file = x["scheda"].split("/", 1)[1]
            link = "[%s](%s)" % ("card" if en else "scheda", file)
            if x["pacchetto"]:
                link += " · [%s](../%sLEGGIMI.md)" % ("package" if en else "pacchetto", x["pacchetto"].rstrip("/") + "/")
            else:
                link += " · " + ("card only" if en else "solo scheda")
            dove = DOVE_EN.get(x["dove_gira"], x["dove_gira"]) if en else x["dove_gira"]
            livello = LIVELLO_EN.get(x["livello"], x["livello"]) if en else x["livello"]
            stato = NOMI_STATO[lingua].get(x["stato_tipo"], "?")
            righe.append("| %s | %s | %s | %s | %s |" % (titolo(x).replace("|", "\\|"), dove, livello, stato, link))
        righe.append("")
    return "\n".join(righe)


# --- numeri scritti a mano nei README e nel CHANGELOG -------------------------------

def numeri_veri(repo, schede):
    pacchetti_dir = os.path.join(repo, "pacchetti")
    try:
        n_pacchetti = sum(1 for d in os.listdir(pacchetti_dir)
                          if os.path.isfile(os.path.join(pacchetti_dir, d, "LEGGIMI.md")))
    except OSError:
        n_pacchetti = 0
    scarti = {}
    for rel in ("catalogo/scartati.md", "catalog/discarded.md"):
        p = os.path.join(repo, rel)
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as fh:
                scarti[rel] = sum(1 for r in fh if r.startswith("### "))
    n = conteggi_stato(schede)
    return {
        "schede": len(schede),
        "schede_con_pacchetto": sum(1 for x in schede if x["pacchetto"]),
        "pacchetti": n_pacchetti,
        "aree": len({x["scheda"].split("/")[1] for x in schede}),
        "scarti": scarti.get("catalogo/scartati.md", 0),
        "scarti_en": scarti.get("catalog/discarded.md", 0),
        "uso": n["uso"], "pc": n["pc"], "proposta": n["proposta"],
    }


# (regex, quale numero vero). Il numero va subito prima delle parole. «per 64 schede» /
# «for 64 cards» sono le schede con un pacchetto; «52 schede su 88» non si controlla.
REGOLE_NUMERI = (
    (r"\b(?:per|for)\s+(\d+)\s+(?:schede|cards)\b", "schede_con_pacchetto"),
    (r"(?<!per )(?<!for )\b(\d+)\s+(?:schede|cards)\b(?!\s+(?:su|out of|of)\b)", "schede"),
    (r"\b(\d+)\s+(?:pacchetti|packages)\b", "pacchetti"),
    (r"\b(\d+)\s+(?:aree|areas)\b", "aree"),
    (r"\b(\d+)\s+(?:voci|strumenti e idee|tools and ideas|cose che ho (?:scartato|lasciato)|things I (?:dropped|let go))\b", "scarti"),
    (r"\b(\d+)\s+(?:«?le uso»?|«?la uso»?|\"?I use(?: it)?\"?)(?=[\s,.;:)»\"]|$)", "uso"),
    (r"\b(\d+)\s+(?:«?version[ei] per PC»?|\"?PC versions?\"?)", "pc"),
    (r"\b(\d+)\s+(?:«?propost[ae]»?|\"?proposals?\"?)(?!\s+(?:di|for|of)\b)", "proposta"),
)
FILE_CON_NUMERI = ("README.md", "README.it.md", "CHANGELOG.md")


def controlla_numeri(repo, veri):
    errori = []
    for rel in FILE_CON_NUMERI:
        p = os.path.join(repo, rel)
        if not os.path.isfile(p):
            continue
        with open(p, encoding="utf-8") as fh:
            righe = fh.read().splitlines()
        for i, riga in enumerate(righe, 1):
            if riga.lstrip().startswith("<!--"):
                continue
            for regex, chiave in REGOLE_NUMERI:
                for m in re.finditer(regex, riga, re.I):
                    scritto = int(m.group(1))
                    if scritto != veri[chiave]:
                        errori.append("%s:%d: scritto %d per «%s», ma i file dicono %d (%s)"
                                      % (rel, i, scritto, m.group(0).strip(), veri[chiave], chiave))
    if veri["scarti"] != veri["scarti_en"]:
        errori.append("scartati.md ha %d voci, discarded.md %d" % (veri["scarti"], veri["scarti_en"]))
    if veri["pacchetti"] != veri["schede_con_pacchetto"]:
        errori.append("cartelle in pacchetti/ con LEGGIMI: %d; schede con un pacchetto: %d"
                      % (veri["pacchetti"], veri["schede_con_pacchetto"]))
    return errori


def leggi_file(p):
    if not os.path.exists(p):
        return ""
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def scrivi_file(p, testo):
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(testo)


def main(argv):
    ap = argparse.ArgumentParser(
        prog="genera_indice_catalogo.py",
        description="Genera catalogo-indice.json, skills/mappa-vault/catalogo.md e i README del catalogo "
                    "(catalogo/README.md, catalog/README.md) dalle schede.")
    ap.add_argument("--repo", help="cartella della repo del kit (di serie: due livelli sopra il plugin)")
    ap.add_argument("--controlla", action="store_true",
                    help="non scrive niente: esce con 1 se i file generati non sono aggiornati, se manca un "
                         "pacchetto, se uno stato non si riconosce o se un numero scritto a mano nei README "
                         "o nel CHANGELOG non torna")
    args = ap.parse_args(argv)
    repo = os.path.realpath(os.path.expanduser(args.repo)) if args.repo else \
        os.path.realpath(os.path.join(PLUGIN, "..", ".."))
    controlla = args.controlla
    if not os.path.isdir(os.path.join(repo, "catalogo")):
        print("catalogo non trovato in " + repo, file=sys.stderr)
        return 2
    schede, avvisi = costruisci(repo)
    indice = {"generato_da": "scripts/genera_indice_catalogo.py", "schede": schede}
    testo_json = json.dumps(indice, ensure_ascii=False, indent=1) + "\n"
    generati = [
        (os.path.join(PLUGIN, "catalogo-indice.json"), testo_json),
        (os.path.join(PLUGIN, "skills", "mappa-vault", "catalogo.md"), catalogo_md(schede)),
        (os.path.join(repo, "catalogo", "README.md"), readme_catalogo(schede, "it")),
    ]
    if os.path.isdir(os.path.join(repo, "catalog")):
        generati.append((os.path.join(repo, "catalog", "README.md"), readme_catalogo(schede, "en")))
    for a in avvisi:
        print("avviso: " + a, file=sys.stderr)
    n = conteggi_stato(schede)
    riepilogo = "stati: %d la uso, %d versione per PC, %d proposta" % (n["uso"], n["pc"], n["proposta"])
    if controlla:
        esito = 0
        for p, testo in generati:
            if leggi_file(p) != testo:
                print("non aggiornato: %s (rilancia lo script)" % os.path.relpath(p, repo), file=sys.stderr)
                esito = 1
        gravi = [a for a in avvisi if a.startswith(("pacchetto mancante", "pacchetto diverso", "stato "))]
        if gravi:
            esito = 1
        for e in controlla_numeri(repo, numeri_veri(repo, schede)):
            print("numero sbagliato: " + e, file=sys.stderr)
            esito = 1
        if esito == 0:
            print("%d schede, tutto aggiornato; %s" % (len(schede), riepilogo))
        return esito
    for p, testo in generati:
        scrivi_file(p, testo)
    print("%d schede -> %s; %s" % (len(schede), ", ".join(os.path.relpath(p, repo) for p, _ in generati), riepilogo))
    for e in controlla_numeri(repo, numeri_veri(repo, schede)):
        print("numero da correggere a mano: " + e, file=sys.stderr)
    return 0


if __name__ == "__main__":
    for _f in (sys.stdout, sys.stderr):
        try:
            _f.reconfigure(encoding="utf-8", errors="backslashreplace")
        except (AttributeError, ValueError):
            pass
    sys.exit(main(sys.argv[1:]))
