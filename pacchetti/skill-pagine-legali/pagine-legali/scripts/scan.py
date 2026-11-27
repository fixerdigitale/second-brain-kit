#!/usr/bin/env python3
# Copyright 2026 Igor Gricyk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# FILE MODIFICATO. L'originale è scripts/scan.py del progetto
# https://github.com/gricyk/claude-skill-eu-web-compliance (commit 5034795).
# Modifiche fatte nell'ottobre 2026 per la skill "pagine-legali" (elenco anche nel file NOTICE):
#   - istruzioni d'uso, aiuto della riga di comando, avvisi e riepilogo tradotti in italiano;
#   - riconoscimento degli strumenti tipici delle landing italiane (Meta Pixel, Microsoft Clarity,
#     Google Analytics e Tag Manager, Google Fonts, YouTube, Vimeo, GoHighLevel, WhatsApp,
#     Google Calendar, Calendly, n8n, NocoDB, Bunny, banner cookie) con lo stato di caricamento;
#   - controlli italiani sulle pagine: P.IVA visibile, link a privacy e cookie policy,
#     link "Preferenze cookie", form senza link all'informativa, consensi accorpati;
#   - richieste dentro <noscript> separate da quelle caricate subito;
#   - parole chiave italiane per i consensi e nuovi host di terze parti.
# Le chiavi JSON dell'originale sono invariate; quelle nuove sono "known_tools",
# "it_checks" e "noscript_requests".
"""
scan.py: scansione veloce, solo libreria standard, del codice di un sito alla ricerca di
segnali utili per privacy, cookie, AI e accessibilità (GDPR, Codice privacy, AI Act, WCAG).

Produce una lista di indizi, non un verdetto. Usa espressioni regolari sul testo dei file:
non esegue JavaScript e non apre le pagine. Quindi può perdere cose (cookie scritti a runtime
da uno script incluso) e può segnalare falsi positivi (un nome dentro un commento o una
stringa). Conferma ogni indizio importante leggendo il file prima di scriverlo in un testo.

Uso:
    python3 scan.py /percorso/del/sito [--domain esempio.it ...] [--exclude MODELLO ...] [--json]

--domain si può ripetere: esclude il dominio del sito (e i suoi sottodomini) dall'elenco
delle richieste esterne.

--exclude si può ripetere: ogni modello glob viene confrontato con il percorso relativo e con
il nome del file o della cartella. Esempi: --exclude public --exclude "design/*".

L'HTML minificato (attributi senza virgolette, attributi booleani come `alt` o `checked`) è
supportato. Per i generatori di siti statici scansiona la cartella generata, non i template.

Per una landing online (GoHighLevel, WordPress, Elementor) salva prima l'HTML della pagina,
per esempio con `node consenso.mjs URL --salva-html cartella` o con curl, e scansiona la
cartella. I form e i calendari dentro un iframe non si vedono: apri l'indirizzo dell'iframe.

Serve solo la libreria standard di Python (3.9 o successivo).
"""

import argparse
import fnmatch
import html
import json
import os
import re
import sys
from urllib.parse import urlparse

SOURCE_EXTENSIONS = {
    ".html", ".htm", ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx", ".vue", ".php", ".astro", ".svelte",
    ".css", ".scss", ".twig", ".liquid", ".hbs", ".njk", ".ejs", ".erb", ".jinja", ".j2",
}
MARKUP_EXTENSIONS = {
    ".html", ".htm", ".php", ".vue", ".astro", ".svelte", ".jsx", ".tsx",
    ".twig", ".liquid", ".hbs", ".njk", ".ejs", ".erb", ".jinja", ".j2",
}
SKIP_DIRS = {"node_modules", ".git", ".next", ".nuxt", ".svelte-kit", "vendor", ".venv", "__pycache__",
             "coverage"}
# Cartelle tipiche dei generatori di siti e dei bundler. Vengono scansionate, ma se stanno accanto
# ai sorgenti si stampa un avviso, perché gli indizi risultano doppi.
BUILD_OUTPUT_DIRS = {"public", "dist", "build", "_site", "out"}

# Tag e attributi. I valori possono essere tra virgolette doppie o singole, senza virgolette
# (HTML minificato), un'espressione JSX tra graffe, oppure mancare (attributo booleano).
# I blocchi di template come {{ if .x }} tra gli attributi vengono saltati.
BRACES = r"\{(?:[^{}]|\{[^{}]*\})*\}"
RE_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
RE_RAW_TEXT = re.compile(r"<(script|style)\b((?:[^>\"']|\"[^\"]*\"|'[^']*')*)>(.*?)</\1\s*>",
                         re.IGNORECASE | re.DOTALL)
RE_TAG = re.compile(r"<([a-zA-Z][\w:.-]*)((?:[^>\"'{}]|\"[^\"]*\"|'[^']*'|" + BRACES + r")*)>")
RE_ATTR = re.compile(r"(" + BRACES + r")|([^\s\"'<>/={}]+)(?:\s*=\s*(\"[^\"]*\"|'[^']*'|" + BRACES +
                     r"|[^\s\"'=<>`]+))?")
RE_LABEL_BLOCK = re.compile(r"<label\b(?:[^>\"']|\"[^\"]*\"|'[^']*')*>.*?</label\s*>", re.IGNORECASE | re.DOTALL)
RE_HEADING = re.compile(r"<h([1-6])(?=[\s>/])", re.IGNORECASE)
RE_NOSCRIPT = re.compile(r"<noscript\b[^>]*>(.*?)</noscript\s*>", re.IGNORECASE | re.DOTALL)
RE_FORM_BLOCK = re.compile(r"<form\b(?:[^>\"']|\"[^\"]*\"|'[^']*')*>.*?</form\s*>", re.IGNORECASE | re.DOTALL)
RE_ANCHOR = re.compile(r"<a\b((?:[^>\"']|\"[^\"]*\"|'[^']*')*)>(.*?)</a\s*>", re.IGNORECASE | re.DOTALL)
RE_ANY_TAG = re.compile(r"<[^>]+>")

RE_CSS_URL = re.compile(r'(?:url\(\s*["\']?|@import\s+["\'])((?:https?:)?//[^"\')\s]+)', re.IGNORECASE)
RE_JS_SRC_ASSIGN = re.compile(r'\.src\s*=\s*["\'`]((?:https?:)?//[^"\'`\s]+)', re.IGNORECASE)

# Tag il cui src viene scaricato da solo al caricamento della pagina.
SRC_TAGS = {"script", "iframe", "frame", "img", "audio", "video", "source", "embed", "track", "input"}
# Valori di <link rel> che fanno contattare l'host dell'href senza clic.
AUTO_LOAD_RELS = {"stylesheet", "preload", "modulepreload", "prefetch", "preconnect", "dns-prefetch", "icon",
                  "apple-touch-icon", "mask-icon", "manifest"}
# Tipi di script che vengono eseguiti; gli altri (JSON-LD, template, text/plain in attesa del consenso) no.
EXECUTABLE_SCRIPT_TYPES = {"", "text/javascript", "application/javascript", "module"}
CONSENT_GATED_SCRIPT_TYPES = {"text/plain"}

# Tipi di input che non hanno mai bisogno di un'etichetta visibile.
UNLABELED_OK_TYPES = {"hidden", "submit", "button", "reset", "image"}
CLICKABLE_NON_BUTTON_TAGS = {"div", "span", "li", "td", "img", "p"}
CLICK_ATTRS = {"onclick", "@click", "v-on:click", "on:click"}

COOKIE_PATTERNS = [
    r"document\.cookie",
    r"\bsetCookie\b",
    r"\blocalStorage\.setItem\b",
    r"\bgtag\s*\(",
    r"google-analytics\.com",
    r"googletagmanager\.com",
    r"\bfbq\s*\(",
    r"connect\.facebook\.net",
    r"_paq\.push",
    r"matomo",
    r"hotjar",
    r"clarity\.ms",
    r"plausible\.io",
    r"segment\.(?:com|io)",
    r"mixpanel",
    r"cookieconsent",
    r"\bcookiebot\b",
    r"onetrust",
    r"usercentrics",
    r"didomi",
    r"iubenda",
    r"klaro",
    r"complianz",
    r"cookieyes",
]

CONSENT_KEYWORDS = [
    r"consent", r"gdpr", r"privacy", r"souhlas", r"datenschutz", r"cookies?\b", r"newsletter",
    r"consenso", r"informativa", r"dati personali", r"trattamento dei dati",
]

# Confrontati solo con le risorse che la pagina carica davvero (vedi embedded_resources): un semplice
# <a href> verso Google Maps o YouTube non conta come contenuto incorporato.
THIRD_PARTY_EMBED_PATTERNS = [
    r"youtube\.com/embed", r"youtube-nocookie\.com", r"player\.vimeo\.com", r"google\.com/maps",
    r"maps\.googleapis\.com", r"fonts\.googleapis\.com", r"fonts\.gstatic\.com", r"platform\.twitter\.com",
    r"instagram\.com/embed", r"facebook\.com/plugins", r"recaptcha", r"hcaptcha\.com",
    r"challenges\.cloudflare\.com", r"leadconnectorhq\.com", r"msgsndr\.com", r"calendar\.google\.com",
    r"calendly\.com", r"mediadelivery\.net",
]

AI_PATTERNS = [
    r"openai\.com", r"\bfrom\s+[\"']openai[\"']", r"anthropic\.com", r"@anthropic-ai/", r"\bchatgpt\b",
    r"\bgpt-\d", r"\bclaude-[a-z0-9]", r"generativelanguage\.googleapis\.com", r"@google/genai",
    r"api\.mistral\.ai", r"api-inference\.huggingface\.co", r"replicate\.com", r"\bchatbot\b",
    r"assistant\b.*widget", r"recommend(?:ation|er)s?\b", r"personali[sz]ation",
    r"openrouter\.ai", r"assistente\s+(?:virtuale|ai|ia)\b",
]

AD_PATTERNS = [
    r"adsbygoogle", r"doubleclick\.net", r"googlesyndication\.com", r"taboola", r"outbrain",
]

TRACKING_PIXEL_PATTERNS = [
    r"facebook\.com/tr", r"px\.ads\.linkedin\.com", r"snap\.licdn\.com", r"bat\.bing\.com",
    r"analytics\.tiktok\.com",
]

USER_CONTENT_PATTERNS = [
    r"type\s*=\s*[\"']?file\b", r"disqus", r"giscus", r"utteranc\.es", r"commento", r"remark42",
    r"comment[-_]?form", r"wp-comments-post",
]

# Strumenti che contano per i testi legali delle landing. Per ogni file si dice se lo strumento è
# attivo al caricamento, bloccato fino al consenso, presente solo in <noscript> o solo come link/testo.
KNOWN_TOOLS = [
    ("Meta Pixel", [r"connect\.facebook\.net", r"facebook\.com/tr\b", r"\bfbq\s*\("]),
    ("Microsoft Clarity", [r"clarity\.ms", r"\bclarity\s*\(\s*[\"'](?:set|consent|consentv2|identify|event)"]),
    ("Google Analytics", [r"google-analytics\.com", r"googletagmanager\.com/gtag", r"\bgtag\s*\(\s*[\"']config"]),
    ("Google Tag Manager", [r"googletagmanager\.com/gtm\.js", r"\bGTM-[A-Z0-9]{4,}"]),
    ("Google Ads", [r"googleadservices\.com", r"doubleclick\.net", r"\bAW-\d{6,}"]),
    ("Google Fonts", [r"fonts\.googleapis\.com", r"fonts\.gstatic\.com"]),
    ("YouTube", [r"youtube\.com/embed", r"youtube-nocookie\.com", r"youtube\.com/iframe_api"]),
    ("Vimeo", [r"player\.vimeo\.com"]),
    ("Bunny (video/CDN)", [r"mediadelivery\.net", r"\.b-cdn\.net"]),
    ("GoHighLevel / LeadConnector", [r"leadconnectorhq\.com", r"msgsndr\.com", r"gohighlevel\.com"]),
    ("WhatsApp", [r"wa\.me/", r"api\.whatsapp\.com", r"web\.whatsapp\.com", r"chat\.whatsapp\.com"]),
    ("Google Calendar", [r"calendar\.google\.com", r"calendar\.app\.google"]),
    ("Calendly", [r"calendly\.com"]),
    ("n8n", [r"https?://[^\s\"'<>]*\bn8n\b[^\s\"'<>]*", r"/webhook(?:-test)?/[\w-]{6,}"]),
    ("NocoDB", [r"https?://[^\s\"'<>]*noco[^\s\"'<>]*", r"/nc/form/", r"/api/v[12]/(?:db/data|tables)/"]),
    ("Google reCAPTCHA", [r"recaptcha"]),
    ("Google Maps", [r"google\.com/maps/embed", r"maps\.googleapis\.com"]),
    ("LinkedIn Insight", [r"snap\.licdn\.com", r"px\.ads\.linkedin\.com"]),
    ("TikTok Pixel", [r"analytics\.tiktok\.com"]),
    ("Hotjar", [r"hotjar"]),
    ("Banner cookieconsent", [r"cookieconsent", r"CookieConsent\.run\s*\(", r"data-cc\s*=\s*[\"']?show-preferencesModal"]),
    ("Altro banner cookie", [r"cdn\.iubenda\.com", r"_iub\.csConfiguration", r"consent\.cookiebot\.com",
                             r"cmplz[_-](?:cookiebanner|banner)", r"cdn-cookieyes\.com", r"cdn\.cookielaw\.org",
                             r"usercentrics\.eu", r"sdk\.privacy-center\.org", r"klaro(?:\.min)?\.js"]),
]
STATUS_ACTIVE = "attivo al caricamento"
STATUS_DATA = "riceve i dati di un form o di uno script"
STATUS_GATED = "bloccato fino al consenso o caricato dopo"
STATUS_NOSCRIPT = "solo in <noscript>"
STATUS_LINK = "solo link o testo"
STATUS_JS = "nel file JS/CSS"
STATUS_PRESENT = "presente nella pagina"
STATUS_ORDER = [STATUS_ACTIVE, STATUS_DATA, STATUS_NOSCRIPT, STATUS_JS, STATUS_GATED, STATUS_LINK, STATUS_PRESENT]
# Strumenti che non si "caricano": ricevono i dati inviati dai form (webhook, database).
DATA_TOOLS = {"n8n", "NocoDB"}
# Per i banner conta solo se ci sono; il controllo vero si fa nel browser con consenso.mjs.
BANNER_TOOLS = {"Banner cookieconsent", "Altro banner cookie"}

# Controlli italiani sulle pagine complete.
RE_PIVA = re.compile(r"(?:\bp\.?\s*i\.?\s*v\.?\s*a\b\.?|\bpartita\s+i\.?v\.?a\b\.?|\bvat(?:\s+(?:number|no\.?|n\.?))?\b)"
                     r"[^0-9a-z]{0,6}(?:(?:n|nr|num|no)\b\.?|n°|nº)?[^0-9a-z]{0,6}(?:it[\s-]*)?(\d{11})\b",
                     re.IGNORECASE)
PREFS_PATTERNS = [
    r"data-cc\s*=\s*[\"']?show-preferencesModal", r"showPreferences\s*\(", r"Cookiebot\.renew",
    r"openPreferences", r"cmplz-manage-consent", r"cky-btn-revisit",
    r"(?:preferenze|impostazioni|gestisci|gestione)\s+(?:dei\s+|i\s+)?cookie", r"rivedi\s+le\s+(?:tue\s+)?scelte",
]
MARKETING_WORDS = r"newsletter|marketing|promozion|offert|comunicazioni\s+commerciali|aggiornamenti|pubblicit"
PRIVACY_WORDS = r"privacy|informativa|trattamento\s+dei\s+dati|dati\s+personali"
COOKIE_POLICY_WORDS = r"cookie[\s_-]*policy|informativa[^.]{0,20}cookie|politica[^.]{0,12}cookie"


def is_excluded(rel_path, exclude):
    rel_path = rel_path.replace(os.sep, "/")
    name = rel_path.rsplit("/", 1)[-1]
    return any(fnmatch.fnmatch(rel_path, pat) or fnmatch.fnmatch(name, pat) for pat in exclude)


def iter_source_files(root, exclude=()):
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        rel_dir = "" if rel_dir == "." else rel_dir + os.sep
        dirnames[:] = sorted(d for d in dirnames
                             if d not in SKIP_DIRS and not d.startswith(".")
                             and not is_excluded(rel_dir + d, exclude))
        for fn in sorted(filenames):
            if fn.endswith((".min.js", ".min.css")) or is_excluded(rel_dir + fn, exclude):
                continue
            ext = os.path.splitext(fn)[1].lower()
            if ext in SOURCE_EXTENSIONS:
                yield os.path.join(dirpath, fn)


def build_output_dirs_next_to_sources(root, exclude=()):
    """Cartelle generate al primo livello che verrebbero scansionate insieme ad altri file."""
    found = [d for d in sorted(BUILD_OUTPUT_DIRS)
             if os.path.isdir(os.path.join(root, d)) and not is_excluded(d, exclude)]
    if not found:
        return []
    for path in iter_source_files(root, exclude):
        top = os.path.relpath(path, root).split(os.sep, 1)[0]
        if top not in found:
            return found
    return []


def read_text(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except OSError:
        return ""


def find_matches(patterns, text):
    hits = []
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            hits.append(pat)
    return hits


def is_own_domain(url, site_domains):
    host = (urlparse(url).hostname or "").lower()
    for d in site_domains:
        d = d.lower().strip(".")
        if host == d or host.endswith("." + d):
            return True
    return False


def parse_attrs(attr_text):
    """Attributi di un tag come {nome minuscolo: valore}; valore None per un attributo booleano."""
    attrs = {}
    for m in RE_ATTR.finditer(attr_text):
        if m.group(1):  # blocco di template tra gli attributi, es. {{ if .x }}
            continue
        name, value = m.group(2).lower(), m.group(3)
        if value is not None and value[:1] in ("\"", "'", "{"):
            value = value[1:-1].strip() if value[0] == "{" else value[1:-1]
            if value[:1] in ("\"", "'") and value[-1:] == value[:1]:  # JSX {"testo"}
                value = value[1:-1]
        attrs.setdefault(name, value)  # vince la prima occorrenza, come nei browser
    return attrs


def split_markup(text):
    """Restituisce (markup, raw_blocks): commenti tolti, corpo di <script>/<style> tolto dal markup e
    restituito a parte come (tag, attributi, corpo), così il contenuto non viene letto come tag."""
    text = RE_COMMENT.sub(" ", text)
    raw_blocks = []

    def keep_open_tag(m):
        raw_blocks.append((m.group(1).lower(), parse_attrs(m.group(2)), m.group(3)))
        return "<%s%s></%s>" % (m.group(1), m.group(2), m.group(1))

    return RE_RAW_TEXT.sub(keep_open_tag, text), raw_blocks


def iter_tags(markup):
    for m in RE_TAG.finditer(markup):
        yield m.group(1).lower(), parse_attrs(m.group(2)), m.start()


def absolute_url(url):
    if not url:
        return None
    url = url.strip()
    if url.startswith("//"):
        url = "https:" + url
    return url if url.lower().startswith(("http://", "https://")) else None


def embedded_resources(tags, extra_text=""):
    """URL che il browser scarica senza azioni dell'utente, e URL trattenuti da uno strumento di consenso."""
    loaded, gated = set(), set()
    for name, attrs, _ in tags:
        urls = []
        if name in SRC_TAGS:
            urls.append(attrs.get("src"))
        if name in ("img", "source") and attrs.get("srcset"):
            urls.extend(part.split()[0] for part in attrs["srcset"].split(",") if part.split())
        if name == "video":
            urls.append(attrs.get("poster"))
        if name == "object":
            urls.append(attrs.get("data"))
        if name == "link" and set((attrs.get("rel") or "").lower().split()) & AUTO_LOAD_RELS:
            urls.append(attrs.get("href"))
        if attrs.get("style"):
            urls.extend(RE_CSS_URL.findall(attrs["style"]))
        target = gated if (name == "script" and (attrs.get("type") or "").lower() in CONSENT_GATED_SCRIPT_TYPES) \
            else loaded
        target.update(u for u in map(absolute_url, urls) if u)
    loaded.update(u for u in map(absolute_url, RE_CSS_URL.findall(extra_text) + RE_JS_SRC_ASSIGN.findall(extra_text))
                  if u)
    return loaded, gated


def external_form_targets(tags, site_domains):
    targets = (absolute_url(attrs.get("action")) for name, attrs, _ in tags if name == "form")
    return sorted({u for u in targets if u and not is_own_domain(u, site_domains)})


def analyze_forms(markup, tags):
    label_fors = {attrs.get("for") or attrs.get("htmlfor") for name, attrs, _ in tags if name == "label"}
    label_spans = [(m.start(), m.end()) for m in RE_LABEL_BLOCK.finditer(markup)]
    form_count = 0
    field_types = []
    unlabeled = 0
    prechecked = 0
    for name, attrs, pos in tags:
        if name == "form":
            form_count += 1
        if name not in ("input", "textarea", "select"):
            continue
        field_type = (attrs.get("type") or "text").lower() if name == "input" else name
        field_types.append(field_type)
        if field_type in ("checkbox", "radio"):
            checked = attrs.get("checked", attrs.get("defaultchecked", False))
            # Attributo booleano o valore letterale vero; una variabile JSX come checked={isOn} non conta.
            if checked is None or (checked is not False and checked.lower() in ("", "checked", "true")):
                prechecked += 1
        if field_type in UNLABELED_OK_TYPES:
            continue
        if (attrs.get("aria-label") or attrs.get("aria-labelledby") or attrs.get("title")
                or (attrs.get("id") and attrs["id"] in label_fors)
                or any(start < pos < end for start, end in label_spans)):
            continue
        unlabeled += 1
    return {
        "count": form_count,
        "field_count": len(field_types),
        "field_types": field_types,
        "fields_without_matching_label": unlabeled,
        "prechecked_checkboxes_or_radios": prechecked,
        "nearby_consent_keywords": find_matches(CONSENT_KEYWORDS, markup),
    }


def heading_skips(markup):
    skips = []
    levels = [int(m) for m in RE_HEADING.findall(markup)]
    for prev, cur in zip(levels, levels[1:]):
        if cur > prev + 1:
            skips.append(f"h{prev}->h{cur}")
    return skips


def visible_text(fragment):
    return re.sub(r"\s+", " ", html.unescape(RE_ANY_TAG.sub(" ", fragment)))


def anchors(fragment):
    """Coppie (href, testo visibile) dei link nel frammento."""
    result = []
    for m in RE_ANCHOR.finditer(fragment):
        href = (parse_attrs(m.group(1)).get("href") or "").lower()
        result.append((href, visible_text(m.group(2)).lower()))
    return result


def real_href(href):
    return bool(href) and not href.startswith(("#", "javascript:"))


def has_privacy_link(links):
    return any((real_href(href) and "privacy" in href) or "privacy" in text
               or ("informativa" in text and "cookie" not in text) for href, text in links)


def has_cookie_policy_link(links):
    return any((real_href(href) and "cookie" in href) or re.search(COOKIE_POLICY_WORDS, text)
               for href, text in links)


def italian_checks(markup):
    """Controlli italiani su una pagina completa: P.IVA, link legali, preferenze cookie, form."""
    links = anchors(markup)
    piva = RE_PIVA.search(visible_text(markup))
    forms = []
    for block in RE_FORM_BLOCK.findall(markup):
        tags = list(iter_tags(block))
        checkboxes = [attrs for name, attrs, _ in tags
                      if name == "input" and (attrs.get("type") or "").lower() == "checkbox"]
        labels = [visible_text(lb).lower() for lb in RE_LABEL_BLOCK.findall(block)]
        block_text = visible_text(block).lower()
        forms.append({
            "privacy_link": has_privacy_link(anchors(block)),
            "checkboxes": len(checkboxes),
            "marketing_checkbox": bool(checkboxes) and bool(re.search(MARKETING_WORDS, block_text)),
            "bundled_consent": any(re.search(PRIVACY_WORDS, lb) and re.search(MARKETING_WORDS, lb) for lb in labels),
        })
    return {
        "piva": piva.group(1) if piva else None,
        "privacy_link": has_privacy_link(links),
        "cookie_link": has_cookie_policy_link(links),
        "cookie_preferences_link": bool(find_matches(PREFS_PATTERNS, markup)),
        "forms": forms,
    }


def tool_status(patterns, active, noscript, gated, anywhere):
    for status, haystack in ((STATUS_ACTIVE, active), (STATUS_NOSCRIPT, noscript), (STATUS_GATED, gated),
                             (STATUS_LINK, anywhere)):
        if find_matches(patterns, haystack):
            return status
    return None


def analyze_file(path, text, site_domains):
    findings = {"file": path}
    ext = os.path.splitext(path)[1].lower()
    is_markup = ext in MARKUP_EXTENSIONS

    noscript_html = ""
    if is_markup:
        markup, raw_blocks = split_markup(text)
        executed = "\n".join(body for tag, attrs, body in raw_blocks
                             if tag == "style" or (attrs.get("type") or "").lower() in EXECUTABLE_SCRIPT_TYPES)
        gated_code = "\n".join(" ".join([body, attrs.get("src") or "", attrs.get("data-src") or ""])
                               for tag, attrs, body in raw_blocks
                               if tag == "script" and (attrs.get("type") or "").lower() in CONSENT_GATED_SCRIPT_TYPES)
        # Il contenuto di <noscript> si carica solo con JavaScript spento: va tenuto a parte.
        noscript_html = "\n".join(RE_NOSCRIPT.findall(markup))
        tags = list(iter_tags(RE_NOSCRIPT.sub(" ", markup))) + list(iter_tags(executed))
    else:
        markup, executed, gated_code = text, text, ""
        tags = list(iter_tags(text))  # tag dentro stringhe JS/CSS, es. iframe inseriti da script

    loaded, gated = embedded_resources(tags, executed)
    external = sorted(u for u in loaded if not is_own_domain(u, site_domains))
    if external:
        findings["external_requests"] = external
    gated_external = sorted(u for u in gated if not is_own_domain(u, site_domains))
    if gated_external:
        findings["consent_gated_requests"] = gated_external
    noscript_loaded, _ = embedded_resources(list(iter_tags(noscript_html)))
    noscript_external = sorted(u for u in noscript_loaded - loaded if not is_own_domain(u, site_domains))
    if noscript_external:
        findings["noscript_requests"] = noscript_external

    embed_text = "\n".join(external) + "\n" + executed if is_markup else text
    for key, patterns, haystack in (
        ("cookie_or_tracking_code", COOKIE_PATTERNS, text),
        ("third_party_embeds", THIRD_PARTY_EMBED_PATTERNS, embed_text),
        ("ad_code", AD_PATTERNS, text),
        ("tracking_pixels", TRACKING_PIXEL_PATTERNS, text),
        ("ai_related_code", AI_PATTERNS, text),
        ("user_content_features", USER_CONTENT_PATTERNS, text),
    ):
        hits = find_matches(patterns, haystack)
        if hits:
            findings[key] = hits

    tools = {}
    if is_markup:
        all_tags = list(iter_tags(markup))
        deferred = " ".join(attrs.get("data-src") or "" for _, attrs, _ in all_tags if attrs.get("data-src"))
        form_actions = " ".join(attrs.get("action") or "" for name, attrs, _ in all_tags if name == "form")
        for name, patterns in KNOWN_TOOLS:
            if name in BANNER_TOOLS:
                status = STATUS_PRESENT if find_matches(patterns, text) else None
            elif name in DATA_TOOLS:
                status = (STATUS_DATA if find_matches(patterns, "\n".join([form_actions, executed, gated_code]))
                          else STATUS_LINK if find_matches(patterns, text) else None)
            else:
                status = tool_status(patterns, "\n".join(external) + "\n" + executed, noscript_html,
                                     "\n".join(gated_external) + "\n" + gated_code + "\n" + deferred, text)
            if status:
                tools[name] = status
    else:
        tools = {name: STATUS_JS for name, patterns in KNOWN_TOOLS if find_matches(patterns, text)}
    if tools:
        findings["known_tools"] = tools

    if not is_markup:
        return findings if len(findings) > 1 else None

    page_tags = list(iter_tags(markup))
    form_targets = external_form_targets(page_tags, site_domains)
    if form_targets:
        findings["external_form_targets"] = form_targets

    if any(name in ("form", "input", "textarea", "select") for name, _, _ in page_tags):
        findings["forms"] = analyze_forms(markup, page_tags)

    missing_alt = sum(1 for name, attrs, _ in page_tags if name == "img" and "alt" not in attrs)
    if missing_alt:
        findings["images_missing_alt"] = missing_alt

    clickable = sum(1 for name, attrs, _ in page_tags
                    if name in CLICKABLE_NON_BUTTON_TAGS and CLICK_ATTRS & set(attrs))
    if clickable:
        findings["clickable_non_button_elements"] = clickable

    skips = heading_skips(markup)
    if skips:
        findings["heading_level_skips"] = skips

    html_tags = [attrs for name, attrs, _ in page_tags if name == "html"]
    if html_tags:
        if not (html_tags[0].get("lang") or "").strip():
            findings["html_missing_lang"] = True
        if not any(name == "meta" and (attrs.get("name") or "").lower() == "viewport"
                   for name, attrs, _ in page_tags):
            findings["missing_viewport_meta"] = True

    # I controlli italiani hanno senso solo sulle pagine complete, non sui frammenti di template.
    if html_tags or any(name == "body" for name, _, _ in page_tags):
        findings["it_checks"] = italian_checks(markup)

    return findings if len(findings) > 1 else None


def scan(root, site_domains, exclude=()):
    results = []
    for path in iter_source_files(root, exclude):
        text = read_text(path)
        if not text:
            continue
        finding = analyze_file(os.path.relpath(path, root), text, site_domains)
        if finding:
            results.append(finding)
    return results


def print_file_list(title, files):
    print(f"{title}: {len(files)}")
    for f in files:
        print(f"  - {f}")


def print_tools(results):
    by_tool = {}
    for r in results:
        for name, status in r.get("known_tools", {}).items():
            by_tool.setdefault(name, {}).setdefault(status, []).append(r["file"])
    print(f"Strumenti riconosciuti: {len(by_tool)}")
    for name, _ in KNOWN_TOOLS:
        if name not in by_tool:
            continue
        print(f"  - {name}")
        for status in STATUS_ORDER:
            files = by_tool[name].get(status)
            if files:
                shown = ", ".join(files[:5]) + (f" e altri {len(files) - 5}" if len(files) > 5 else "")
                print(f"      {status}: {shown}")


def print_italian_checks(results):
    pages = [r for r in results if "it_checks" in r]
    print(f"Controlli italiani sulle pagine complete: {len(pages)}")
    if not pages:
        return
    checks = [
        ("Pagine senza P.IVA visibile (obbligatoria in home page)", lambda c: not c["piva"]),
        ("Pagine senza link alla privacy policy", lambda c: not c["privacy_link"]),
        ("Pagine senza link alla cookie policy", lambda c: not c["cookie_link"]),
        ("Pagine senza link per riaprire le preferenze cookie", lambda c: not c["cookie_preferences_link"]),
    ]
    for title, failed in checks:
        print_file_list("  " + title, [r["file"] for r in pages if failed(r["it_checks"])])
    form_checks = [
        ("Moduli senza link all'informativa privacy", lambda f: not f["privacy_link"]),
        ("Moduli con una casella che unisce privacy e marketing", lambda f: f["bundled_consent"]),
        ("Moduli con caselle e parole di marketing (controlla che il consenso sia separato e facoltativo)",
         lambda f: f["marketing_checkbox"]),
    ]
    for title, failed in form_checks:
        files = [r["file"] for r in pages if any(failed(f) for f in r["it_checks"]["forms"])]
        print_file_list("  " + title, files)
    found = sorted({r["it_checks"]["piva"] for r in pages if r["it_checks"]["piva"]})
    if found:
        print(f"  P.IVA trovate nel testo: {', '.join(found)} (controlla che sia quella giusta)")


def print_summary(root, results):
    if not results:
        print("La scansione veloce non ha trovato indizi. Non significa che il sito sia in regola: "
              "significa solo che questo passaggio non ha nulla da segnalare. Leggi il codice per un "
              "controllo completo e fai il controllo nel browser.")
        return

    def files_with(*keys):
        return [r["file"] for r in results if any(r.get(k) for k in keys)]

    all_external = sorted(set(u for r in results for u in r.get("external_requests", [])))
    external_hosts = sorted(set(urlparse(u).hostname or u for u in all_external))
    gated_hosts = sorted(set(urlparse(u).hostname or u for r in results for u in r.get("consent_gated_requests", [])))
    noscript_hosts = sorted(set(urlparse(u).hostname or u for r in results for u in r.get("noscript_requests", [])))
    form_hosts = sorted(set(urlparse(u).hostname or u for r in results for u in r.get("external_form_targets", [])))
    forms = [r["forms"] for r in results if "forms" in r]

    print(f"Cartella scansionata: {root}")
    print(f"File con indizi: {len(results)}")
    print()
    print(f"Host esterni caricati subito, senza clic: {len(external_hosts)} ({len(all_external)} URL diversi)")
    for h in external_hosts[:40]:
        print(f"  - {h}")
    if len(external_hosts) > 40:
        print(f"  ... e altri {len(external_hosts) - 40}, usa --json per l'elenco completo")
    if gated_hosts:
        print(f"Host esterni trattenuti da uno strumento di consenso (type=text/plain): {len(gated_hosts)}")
        for h in gated_hosts:
            print(f"  - {h}")
    if noscript_hosts:
        print(f"Host dentro <noscript> (partono senza consenso se JavaScript è spento): {len(noscript_hosts)}")
        for h in noscript_hosts:
            print(f"  - {h}")
    print_file_list("Moduli che inviano a host esterni (" + ", ".join(form_hosts) + ")" if form_hosts
                    else "Moduli che inviano a host esterni", files_with("external_form_targets"))
    print()
    print_tools(results)
    print()
    print_file_list("File con codice di cookie, archiviazione, tracciamento o banner di consenso",
                    files_with("cookie_or_tracking_code"))
    print_file_list("File con contenuti di terze parti, font o CAPTCHA (possono inviare l'IP prima del consenso)",
                    files_with("third_party_embeds"))
    print_file_list("File con codice pubblicitario o pixel di tracciamento", files_with("ad_code", "tracking_pixels"))
    print_file_list("File con codice o parole legate all'AI", files_with("ai_related_code"))
    print_file_list("File con commenti o caricamento file (possibili obblighi DSA)",
                    files_with("user_content_features"))
    print()
    print_italian_checks(results)
    print()
    print(f"Moduli trovati: {sum(f['count'] for f in forms)}, "
          f"campi senza <label>/aria-label corrispondente: {sum(f['fields_without_matching_label'] for f in forms)}, "
          f"caselle o radio già selezionati: {sum(f['prechecked_checkboxes_or_radios'] for f in forms)}")
    print(f"Immagini senza attributo alt: {sum(r.get('images_missing_alt', 0) for r in results)}")
    print(f"Elementi cliccabili che non sono pulsanti: {sum(r.get('clickable_non_button_elements', 0) for r in results)}")
    print_file_list("File con livelli di titolo saltati", files_with("heading_level_skips"))
    print_file_list("File con <html> senza attributo lang", files_with("html_missing_lang"))
    print_file_list("File con <html> senza meta viewport", files_with("missing_viewport_meta"))
    print()
    print("Questa è una lista di indizi, non un verdetto. Conferma ogni punto sul codice e nel browser "
          "(scripts/consenso.mjs) prima di scriverlo nelle pagine legali.")


def main():
    parser = argparse.ArgumentParser(
        description="Scansiona il codice di un sito alla ricerca di indizi utili per privacy, cookie, AI e "
                    "accessibilità. Lista di indizi, non verdetto.")
    parser.add_argument("root", help="Cartella con il codice del sito, la cartella generata di un sito statico "
                                     "o la cartella dove hai salvato l'HTML delle pagine")
    parser.add_argument("--domain", action="append", default=[],
                        help="Dominio del sito (con i sottodomini) da escludere dalle richieste esterne. "
                             "Si può ripetere.")
    parser.add_argument("--exclude", action="append", default=[], metavar="MODELLO",
                        help="Modello glob confrontato con il percorso relativo e con il nome di file o cartella, "
                             "es. public, 'design/*', '*.dc.html'. Si può ripetere.")
    parser.add_argument("--json", action="store_true", help="Stampa il JSON grezzo, file per file, invece del riepilogo")
    args = parser.parse_args()

    if not os.path.isdir(args.root):
        print(f"Non è una cartella: {args.root}", file=sys.stderr)
        sys.exit(1)

    build_dirs = build_output_dirs_next_to_sources(args.root, args.exclude)
    if build_dirs:
        names = ", ".join(d + "/" for d in build_dirs)
        print(f"Attenzione: {names} sembra una cartella generata ed è scansionata insieme ai sorgenti, quindi "
              f"gli indizi possono comparire due volte. Per un sito statico scansiona solo la cartella generata "
              f"(scan.py {os.path.join(args.root, build_dirs[0])}) e leggi i template a mano, oppure aggiungi "
              f"--exclude {build_dirs[0]}.", file=sys.stderr)

    results = scan(args.root, args.domain, args.exclude)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print_summary(args.root, results)


if __name__ == "__main__":
    main()
