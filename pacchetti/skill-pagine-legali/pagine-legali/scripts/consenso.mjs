#!/usr/bin/env node
// consenso.mjs: apre una pagina in un browser pulito e mostra cookie, archivio locale e
// richieste a terze parti in tre momenti: prima di qualsiasi scelta, dopo "Rifiuta",
// dopo "Accetta". Serve per i controlli D1-D6 di checklist.md e per riempire la tabella
// della cookie policy con i cookie veri.
//
// Scritto nell'ottobre 2026 per la skill "pagine-legali". Non deriva dal codice di
// gricyk/claude-skill-eu-web-compliance: ne applica il metodo (controllo nel browser,
// sezione 5 della sua eprivacy-checklist).
//
// Uso:
//   node consenso.mjs https://esempio.it [opzioni]
//
// Opzioni:
//   --rifiuta [SELETTORE]  clicca "Rifiuta" (o la X), poi ricarica e visita le --pagina
//   --accetta [SELETTORE]  in una sessione nuova clicca "Accetta tutti" e mostra cosa compare
//   --pagina URL           altra pagina da visitare prima e dopo la scelta (si può ripetere)
//   --dominio DOMINIO      dominio da considerare "di prima parte" oltre a quello della pagina
//   --attesa MS            attesa dopo ogni caricamento e ogni clic (predefinita 6000)
//   --mobile               schermo da iPhone 15 Pro (393x852, DPR 3)
//   --foto FILE.png        salva lo schermo al primo caricamento, per guardare il banner
//   --salva-html CARTELLA  salva l'HTML generato della pagina e delle --pagina, da passare a scan.py
//   --json                 stampa il risultato in JSON
//
// SELETTORE è un selettore CSS (es. '#cc-main [data-role="necessary"]') oppure
// testo:"Rifiuta tutto". Senza selettore lo script prova i pulsanti di vanilla-cookieconsent
// e poi i testi più comuni. I banner dentro un iframe non vengono trovati: passa il selettore.
//
// Serve Playwright con Chromium (npm i -g playwright && npx playwright install chromium). Se non lo trova,
// imposta PLAYWRIGHT_MODULE con il percorso del pacchetto.

import { createRequire } from "module";
import { execSync } from "child_process";
import fs from "fs";
import path from "path";

const require = createRequire(import.meta.url);

function loadPlaywright() {
  const candidates = [process.env.PLAYWRIGHT_MODULE, "playwright"];
  try {
    candidates.push(path.join(execSync("npm root -g", { encoding: "utf8" }).trim(), "playwright"));
  } catch {}
  for (const c of candidates.filter(Boolean)) {
    try {
      return require(c);
    } catch {}
  }
  console.error("Playwright non trovato. Imposta PLAYWRIGHT_MODULE con il percorso del pacchetto playwright.");
  process.exit(1);
}

// Strumenti riconosciuti dall'host. "tracciamento" = non deve partire prima del consenso.
// "terza parte" = riceve almeno l'indirizzo IP: serve il consenso o una ragione scritta.
const HOSTS = [
  [/(^|\.)connect\.facebook\.net$|(^|\.)facebook\.com$/, "Meta Pixel", "tracciamento"],
  [/(^|\.)clarity\.ms$/, "Microsoft Clarity", "tracciamento"],
  [/(^|\.)bing\.com$/, "Microsoft (Clarity o Ads)", "tracciamento"],
  [/(^|\.)google-analytics\.com$|(^|\.)analytics\.google\.com$/, "Google Analytics", "tracciamento"],
  [/(^|\.)doubleclick\.net$|(^|\.)googleadservices\.com$|(^|\.)googlesyndication\.com$/, "Google Ads", "tracciamento"],
  [/(^|\.)licdn\.com$|(^|\.)ads\.linkedin\.com$/, "LinkedIn Insight", "tracciamento"],
  [/(^|\.)tiktok\.com$/, "TikTok Pixel", "tracciamento"],
  [/(^|\.)hotjar\.(com|io)$/, "Hotjar", "tracciamento"],
  [/(^|\.)googletagmanager\.com$/, "Google Tag Manager / gtag", "terza parte"],
  [/(^|\.)fonts\.googleapis\.com$|(^|\.)fonts\.gstatic\.com$/, "Google Fonts", "terza parte"],
  [/(^|\.)youtube(-nocookie)?\.com$|(^|\.)ytimg\.com$|(^|\.)googlevideo\.com$/, "YouTube", "terza parte"],
  [/(^|\.)vimeo\.com$|(^|\.)vimeocdn\.com$/, "Vimeo", "terza parte"],
  [/(^|\.)leadconnectorhq\.com$|(^|\.)msgsndr\.com$|(^|\.)gohighlevel\.com$/, "GoHighLevel / LeadConnector", "terza parte"],
  [/^calendar\.google\.com$|^calendar\.app\.google$/, "Google Calendar", "terza parte"],
  [/(^|\.)calendly\.com$/, "Calendly", "terza parte"],
  [/(^|\.)mediadelivery\.net$|(^|\.)b-cdn\.net$/, "Bunny", "terza parte"],
  [/(^|\.)whatsapp\.(com|net)$/, "WhatsApp", "terza parte"],
  [/(^|\.)recaptcha\.net$/, "Google reCAPTCHA", "terza parte"],
  [/(^|\.)jsdelivr\.net$|^cdnjs\.cloudflare\.com$|(^|\.)unpkg\.com$/, "CDN pubblico", "terza parte"],
];

// Cookie con nome documentato dal fornitore (fonti in riferimenti.md).
const COOKIES = [
  [/^_ga$|^_ga_/, "Google Analytics", "tracciamento"],
  [/^_fbp$|^_fbc$/, "Meta Pixel", "tracciamento"],
  [/^_clck$|^_clsk$|^CLID$|^ANONCHK$|^MR$|^SM$|^MUID$/, "Microsoft Clarity", "tracciamento"],
  [/^cc_cookie$/, "vanilla-cookieconsent (memorizza la scelta)", "tecnico"],
];

const REJECT_DEFAULT = ['#cc-main [data-role="necessary"]', "#cc-main .cm__btn--close"];
const ACCEPT_DEFAULT = ['#cc-main [data-role="all"]'];
const REJECT_TEXT = [/rifiuta tutt|rifiuta|solo (i )?(cookie )?(necessari|tecnici)|continua senza accettare|nega|reject all|reject|decline/i];
const ACCEPT_TEXT = [/accetta tutt|accept all|consenti tutt/i, /^\s*(accetta|accetto|acconsento|accept|ok)\s*$/i];
const PREFS_TEXT = /preferenze (dei )?cookie|impostazioni (dei )?cookie|gestisci (i )?cookie|rivedi le (tue )?scelte|modifica (le )?preferenze/i;

function parseArgs(argv) {
  const o = { url: null, rifiuta: null, accetta: null, pagine: [], domini: [], attesa: 6000, mobile: false,
              foto: null, salvaHtml: null, json: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    const next = () => (argv[i + 1] && !argv[i + 1].startsWith("--") ? argv[++i] : "");
    if (a === "--rifiuta") o.rifiuta = next();
    else if (a === "--accetta") o.accetta = next();
    else if (a === "--pagina") o.pagine.push(argv[++i]);
    else if (a === "--dominio") o.domini.push(argv[++i]);
    else if (a === "--attesa") o.attesa = parseInt(argv[++i], 10) || 6000;
    else if (a === "--mobile") o.mobile = true;
    else if (a === "--foto") o.foto = argv[++i];
    else if (a === "--salva-html") o.salvaHtml = argv[++i];
    else if (a === "--json") o.json = true;
    else if (a === "-h" || a === "--help") o.help = true;
    else if (!a.startsWith("--") && !o.url) o.url = a;
    else { console.error(`Opzione sconosciuta: ${a}`); process.exit(1); }
  }
  return o;
}

function baseDomain(host) {
  if (/^[\d.]+$/.test(host) || host.includes(":") || !host.includes(".")) return host; // IP o localhost
  const parts = host.replace(/^www\./, "").split(".");
  return parts.slice(-2).join(".");
}

function classifyHost(host) {
  for (const [re, name, kind] of HOSTS) if (re.test(host)) return { name, kind };
  return { name: "non riconosciuto", kind: "terza parte" };
}

function classifyCookie(name) {
  for (const [re, tool, kind] of COOKIES) if (re.test(name)) return { tool, kind };
  return { tool: "da classificare", kind: "da classificare" };
}

function duration(expires) {
  if (!expires || expires < 0) return "sessione";
  const days = Math.round((expires * 1000 - Date.now()) / 86400000);
  return days >= 1 ? `${days} giorni` : "meno di un giorno";
}

class Recorder {
  constructor(ownDomains) {
    this.own = ownDomains;
    this.requests = [];
  }
  attach(context) {
    context.on("request", (req) => {
      let host;
      try { host = new URL(req.url()).hostname; } catch { return; }
      if (!host || this.own.some((d) => host === d || host.endsWith("." + d))) return;
      this.requests.push({ host, url: req.url(), at: Date.now() });
    });
  }
  hostsSince(t0) {
    const map = new Map();
    for (const r of this.requests) if (r.at >= t0) map.set(r.host, (map.get(r.host) || 0) + 1);
    return [...map.entries()].sort().map(([host, count]) => ({ host, count, ...classifyHost(host) }));
  }
}

async function snapshot(context, page, own) {
  const cookies = (await context.cookies()).map((c) => {
    const host = c.domain.replace(/^\./, "");
    const firstParty = own.some((d) => host === d || host.endsWith("." + d));
    return { name: c.name, domain: c.domain, duration: duration(c.expires), party: firstParty ? "prima parte" : "terza parte",
             httpOnly: c.httpOnly, ...classifyCookie(c.name) };
  });
  let storage = { localStorage: [], sessionStorage: [] };
  try {
    storage = await page.evaluate(() => ({ localStorage: Object.keys(localStorage), sessionStorage: Object.keys(sessionStorage) }));
  } catch {}
  return { cookies, storage };
}

async function bannerInfo(page) {
  return page.evaluate(() => {
    const visible = (el) => !!el && !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
    const size = (el) => (el ? Math.round(el.getBoundingClientRect().width) + "x" + Math.round(el.getBoundingClientRect().height) : null);
    const cc = document.querySelector("#cc-main .cm");
    if (visible(cc)) {
      const btn = (r) => document.querySelector(`#cc-main .cm [data-role="${r}"]`);
      return { visto: true, tipo: "vanilla-cookieconsent", x: visible(document.querySelector("#cc-main .cm__btn--close")),
               accetta: size(btn("all")), rifiuta: size(btn("necessary")) };
    }
    // Altri banner: un blocco fisso o sticky che parla di cookie e ha pulsanti di scelta.
    const choice = /accett|rifiut|consent|accept|reject|chiudi/i;
    for (const el of document.querySelectorAll("body *")) {
      const pos = getComputedStyle(el).position;
      if ((pos !== "fixed" && pos !== "sticky") || !visible(el)) continue;
      const text = el.textContent || "";
      if (!/cookie/i.test(text) || !choice.test(text)) continue;
      const buttons = [...el.querySelectorAll("button, a, [role=button]")].filter(visible);
      return { visto: true, tipo: "altro banner", pulsanti: buttons.slice(0, 6).map((b) => `${(b.textContent || b.getAttribute("aria-label") || "").trim().slice(0, 30)} ${size(b)}`) };
    }
    return { visto: false, tipo: "nessuno" };
  });
}

async function clickChoice(page, selector, defaults, texts) {
  const tryLocator = async (loc, label) => {
    try {
      if ((await loc.count()) > 0 && (await loc.first().isVisible())) {
        await loc.first().click({ timeout: 5000 });
        return label;
      }
    } catch {}
    return null;
  };
  if (selector) {
    const loc = selector.startsWith("testo:")
      ? page.getByRole("button", { name: selector.slice(6).replace(/^"|"$/g, "") }).or(page.getByRole("link", { name: selector.slice(6).replace(/^"|"$/g, "") }))
      : page.locator(selector);
    return tryLocator(loc, selector);
  }
  for (const css of defaults) {
    const used = await tryLocator(page.locator(css), css);
    if (used) return used;
  }
  for (const re of texts) {
    const used = await tryLocator(page.getByRole("button", { name: re }).or(page.getByRole("link", { name: re })), `testo ${re}`);
    if (used) return used;
  }
  return null;
}

// Cerca il link per riaprire le scelte (di solito nel piè di pagina), lo clicca e guarda cosa si apre.
async function preferencesCheck(page) {
  const loc = page.locator('[data-cc="show-preferencesModal"]')
    .or(page.getByRole("link", { name: PREFS_TEXT })).or(page.getByRole("button", { name: PREFS_TEXT }));
  if (!(await loc.count())) return { trovato: false };
  const el = loc.first();
  try {
    await el.scrollIntoViewIfNeeded({ timeout: 3000 });
    if (!(await el.isVisible())) return { trovato: true, visibile: false };
    await el.click({ timeout: 5000 });
  } catch {
    return { trovato: true, visibile: false };
  }
  await page.waitForTimeout(1500);
  return page.evaluate(() => {
    const vis = (e) => !!e && !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
    const pm = document.querySelector("#cc-main .pm");
    if (vis(pm)) {
      const interruttori = [...pm.querySelectorAll("input[type=checkbox]")]
        .map((i) => ({ nome: i.value, attivo: i.checked, fisso: i.disabled }));
      return { trovato: true, visibile: true, apre: true, tipo: "vanilla-cookieconsent", interruttori };
    }
    const dialog = [...document.querySelectorAll("[role=dialog], [aria-modal=true]")].find(vis);
    return { trovato: true, visibile: true, apre: !!dialog, tipo: dialog ? "finestra di dialogo" : "nessuna finestra vista" };
  });
}

async function newSession(browser, o) {
  const device = o.mobile
    ? { viewport: { width: 393, height: 852 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true,
        userAgent: "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1" }
    : { viewport: { width: 1366, height: 900 },
        userAgent: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36" };
  const context = await browser.newContext({ locale: "it-IT", timezoneId: "Europe/Rome", ...device });
  // vanilla-cookieconsent (hideFromBots) nasconde il banner se navigator.webdriver è vero.
  await context.addInitScript(() => Object.defineProperty(Navigator.prototype, "webdriver", { get: () => false }));
  return context;
}

async function visit(page, url, wait) {
  await page.goto(url, { waitUntil: "load", timeout: 60000 });
  await page.waitForTimeout(wait);
}

function warnings(state, phase) {
  const w = [];
  const trackers = state.hosts.filter((h) => h.kind === "tracciamento").map((h) => `${h.name} (${h.host})`);
  if (trackers.length) w.push(`${phase}: richieste di tracciamento: ${trackers.join(", ")}`);
  const ck = state.cookies.filter((c) => c.kind === "tracciamento").map((c) => `${c.name} (${c.tool})`);
  if (ck.length) w.push(`${phase}: cookie di tracciamento: ${ck.join(", ")}`);
  const third = state.cookies.filter((c) => c.party === "terza parte").map((c) => `${c.name} @ ${c.domain}`);
  if (third.length) w.push(`${phase}: cookie di terze parti: ${third.join(", ")}`);
  return w;
}

function printState(title, s) {
  console.log(`\n${title}`);
  console.log(`  Cookie (${s.cookies.length}):`);
  for (const c of s.cookies)
    console.log(`    - ${c.name} | ${c.domain} | ${c.duration} | ${c.party} | ${c.tool}${c.kind !== "da classificare" ? " (" + c.kind + ")" : ""}`);
  const keys = [...s.storage.localStorage.map((k) => "local:" + k), ...s.storage.sessionStorage.map((k) => "session:" + k)];
  console.log(`  Archivio locale (${keys.length}): ${keys.join(", ") || "vuoto"}`);
  console.log(`  Host di terze parti contattati (${s.hosts.length}):`);
  for (const h of s.hosts) console.log(`    - ${h.host} | ${h.name} | ${h.kind} | ${h.count} richieste`);
}

async function main() {
  const o = parseArgs(process.argv.slice(2));
  if (o.help || !o.url) {
    const lines = fs.readFileSync(new URL(import.meta.url), "utf8").split("\n").slice(1);
    const head = lines.slice(0, lines.findIndex((l) => !l.startsWith("//")));
    console.log(head.map((l) => l.replace(/^\/\/ ?/, "")).join("\n"));
    process.exit(o.url ? 0 : 1);
  }
  const { chromium } = loadPlaywright();
  const pageHost = new URL(o.url).hostname;
  const own = [...new Set([baseDomain(pageHost), ...o.domini])];
  const browser = await chromium.launch({ headless: true, args: ["--disable-blink-features=AutomationControlled"] });
  const report = { url: o.url, data: new Date().toISOString(), schermo: o.mobile ? "iPhone 15 Pro 393x852" : "desktop 1366x900",
                   primaParte: own, fasi: {}, avvisi: [] };
  try {
    // 1. Prima di qualsiasi scelta.
    let context = await newSession(browser, o);
    let rec = new Recorder(own);
    rec.attach(context);
    let page = await context.newPage();
    let t0 = Date.now();
    await visit(page, o.url, o.attesa);
    report.banner = await bannerInfo(page);
    // Lo scorrimento non è consenso (linee guida del Garante, par. 6.1): scorri e guarda se parte qualcosa.
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight)).catch(() => {});
    await page.waitForTimeout(1500);
    await page.evaluate(() => window.scrollTo(0, 0)).catch(() => {});
    if (o.foto) await page.screenshot({ path: o.foto });
    report.htmlSalvato = [];
    const saveHtml = async (url) => {
      if (!o.salvaHtml) return;
      fs.mkdirSync(o.salvaHtml, { recursive: true });
      const u = new URL(url);
      const name = (u.hostname + u.pathname).replace(/\.html?$/i, "").replace(/[^a-z0-9.-]+/gi, "_").replace(/_+$/, "") + ".html";
      fs.writeFileSync(path.join(o.salvaHtml, name), await page.content());
      report.htmlSalvato.push(path.join(o.salvaHtml, name));
    };
    await saveHtml(o.url);
    for (const p of o.pagine) { // ancora nessuna scelta
      await visit(page, p, o.attesa);
      await saveHtml(p);
    }
    const before = { ...(await snapshot(context, page, own)), hosts: rec.hostsSince(t0) };
    report.fasi.primaDellaScelta = before;
    report.avvisi.push(...warnings(before, "Prima della scelta"));
    if (!report.banner.visto && (before.hosts.length || before.cookies.length))
      report.avvisi.push("Nessun banner visto, ma la pagina usa cookie o contatta terze parti: controlla a mano.");

    // 2. Dopo "Rifiuta": stessa sessione, poi ricarica e altre pagine.
    if (o.rifiuta !== null) {
      t0 = Date.now();
      const used = await clickChoice(page, o.rifiuta, REJECT_DEFAULT, REJECT_TEXT);
      if (!used) report.avvisi.push("Pulsante \"Rifiuta\" o X non trovato: passa il selettore con --rifiuta.");
      await page.waitForTimeout(o.attesa);
      await visit(page, o.url, o.attesa);
      for (const p of o.pagine) await visit(page, p, o.attesa);
      const snap = await snapshot(context, page, own);
      const known = new Set(before.cookies.map((c) => c.name + "@" + c.domain));
      const after = { selettore: used, cookies: snap.cookies.filter((c) => !known.has(c.name + "@" + c.domain)),
                      storage: snap.storage, hosts: rec.hostsSince(t0) };
      report.fasi.dopoRifiuta = after;
      report.avvisi.push(...warnings(after, "Dopo il rifiuto"));
      if (used && (await bannerInfo(page)).visto)
        report.avvisi.push("Dopo il rifiuto e una ricarica il banner si ripresenta: la scelta non viene ricordata.");
      const pref = await preferencesCheck(page);
      after.preferenze = pref;
      if (!pref.trovato) report.avvisi.push("Link per riaprire le scelte sui cookie (\"Preferenze cookie\") non trovato nella pagina.");
      else if (!pref.visibile) report.avvisi.push("Link \"Preferenze cookie\" presente ma non visibile o non cliccabile.");
      else if (!pref.apre) report.avvisi.push("Il link \"Preferenze cookie\" non apre nessuna finestra di scelta.");
      const accesi = (pref.interruttori || []).filter((t) => t.attivo && !t.fisso).map((t) => t.nome);
      if (accesi.length) report.avvisi.push(`Dopo il rifiuto risultano attive: ${accesi.join(", ")}.`);
    }
    await context.close();

    // 3. Dopo "Accetta": sessione nuova.
    if (o.accetta !== null) {
      context = await newSession(browser, o);
      rec = new Recorder(own);
      rec.attach(context);
      page = await context.newPage();
      await visit(page, o.url, o.attesa);
      t0 = Date.now();
      const used = await clickChoice(page, o.accetta, ACCEPT_DEFAULT, ACCEPT_TEXT);
      if (!used) report.avvisi.push("Pulsante \"Accetta\" non trovato: passa il selettore con --accetta.");
      await page.waitForTimeout(o.attesa);
      await visit(page, o.url, o.attesa);
      for (const p of o.pagine) await visit(page, p, o.attesa);
      report.fasi.dopoAccetta = { selettore: used, ...(await snapshot(context, page, own)), hosts: rec.hostsSince(0) };
      await context.close();
    }
  } finally {
    await browser.close();
  }

  if (o.json) {
    console.log(JSON.stringify(report, null, 2));
    return;
  }
  console.log(`Pagina: ${report.url}`);
  console.log(`Data: ${report.data} | Schermo: ${report.schermo} | Prima parte: ${own.join(", ")}`);
  const b = report.banner;
  console.log(`Banner al primo caricamento: ${b.visto ? "sì" : "no"} (${b.tipo})` +
    (b.tipo === "vanilla-cookieconsent" ? ` | X: ${b.x ? "sì" : "no"} | pulsante Accetta ${b.accetta} | pulsante Rifiuta ${b.rifiuta}` : "") +
    (b.pulsanti ? ` | pulsanti: ${b.pulsanti.join(" / ")}` : ""));
  if (report.htmlSalvato.length) console.log(`HTML salvato: ${report.htmlSalvato.join(", ")}`);
  printState("1) Prima di qualsiasi scelta (compreso lo scorrimento della pagina)", report.fasi.primaDellaScelta);
  if (report.fasi.dopoRifiuta) {
    const r = report.fasi.dopoRifiuta;
    printState(`2) Dopo il rifiuto (clic su: ${r.selettore || "nessun pulsante"}; cookie nuovi e host contattati dopo il clic)`, r);
    const p = r.preferenze || {};
    console.log(`  Link "Preferenze cookie": ${!p.trovato ? "non trovato" : !p.visibile ? "presente ma non visibile" : p.apre ? "apre " + p.tipo : "non apre nulla"}` +
      (p.interruttori ? " | interruttori: " + p.interruttori.map((t) => `${t.nome}=${t.fisso ? "fisso" : t.attivo ? "acceso" : "spento"}`).join(", ") : ""));
  }
  if (report.fasi.dopoAccetta) printState(`3) Dopo l'accettazione (clic su: ${report.fasi.dopoAccetta.selettore || "nessun pulsante"}): usa questi dati per la tabella della cookie policy`, report.fasi.dopoAccetta);
  console.log("\nEsito:");
  if (report.avvisi.length) for (const a of report.avvisi) console.log(`  ATTENZIONE - ${a}`);
  else console.log("  Nessun tracciamento riconosciuto prima del consenso o dopo il rifiuto.");
  if (!b.visto && !report.avvisi.length)
    console.log("  Nessun banner: va bene solo se il sito usa esclusivamente cookie tecnici (linee guida del Garante, par. 7.1).");
  console.log("  I cookie \"da classificare\" e gli host \"non riconosciuto\" vanno classificati a mano (SKILL.md, passo 3).");
}

main().catch((e) => {
  console.error(`Errore: ${e.message}`);
  process.exit(1);
});
