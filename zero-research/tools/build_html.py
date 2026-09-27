#!/usr/bin/env python3
"""Build stand-alone HTML pages for the Zero synthetic research study.

Usage: python3 zero-research/tools/build_html.py
Sources (Markdown) -> outputs (HTML), all in zero-research/:
  03_synthesis_dashboard.md          -> 03_synthesis_dashboard.html (with charts from the JSON appendix)
  04_real_user_interview_script.md   -> 04_real_user_interview_script.html
  05_business_plan_revisions.md      -> 05_business_plan_revisions.html
No third-party dependencies: a small Markdown subset converter lives here.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CSS = r"""
:root{
  --page:#f3eee4; --surface:#fbf8f2; --surface-2:#f1ebdf; --ink:#1c1a17; --ink-2:#55504a; --muted:#8a847b;
  --line:#e2dbcc; --accent:#b8482a; --accent-soft:#f3dfd5; --code:#efe8da;
  --good:#0ca30c; --good-ink:#006300; --warn:#fab219; --warn-ink:#8a5a00; --crit:#d03b3b; --crit-ink:#a42626;
  --bar:#2a78d6; --bar-2:#86b6ef; --ring:rgba(28,26,23,.10);
  color-scheme:light;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --page:#0f0e0d; --surface:#1a1918; --surface-2:#232120; --ink:#f4f1ea; --ink-2:#c3c0b7; --muted:#8f8a80;
    --line:#34312d; --accent:#e0714f; --accent-soft:#3a2219; --code:#262320;
    --good-ink:#34c534; --warn-ink:#fab219; --crit-ink:#ef7a7a; --bar:#3987e5; --bar-2:#184f95; --ring:rgba(255,255,255,.10);
    color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --page:#0f0e0d; --surface:#1a1918; --surface-2:#232120; --ink:#f4f1ea; --ink-2:#c3c0b7; --muted:#8f8a80;
  --line:#34312d; --accent:#e0714f; --accent-soft:#3a2219; --code:#262320;
  --good-ink:#34c534; --warn-ink:#fab219; --crit-ink:#ef7a7a; --bar:#3987e5; --bar-2:#184f95; --ring:rgba(255,255,255,.10);
  color-scheme:dark;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--page);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}
.wrap{max-width:1080px;margin:0 auto;padding:40px 16px 96px}
header.hero{border-bottom:1px solid var(--line);padding-bottom:28px;margin-bottom:28px}
.eyebrow{font:600 12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.brand{font:600 15px/1 Georgia,"Songti SC",serif;color:var(--ink);display:flex;align-items:center;gap:8px;margin-bottom:20px}
.brand i{width:8px;height:8px;border-radius:50%;background:var(--accent);display:inline-block}
h1{font:600 clamp(28px,4.4vw,44px)/1.15 Georgia,"Songti SC",serif;margin:.35em 0 .3em;letter-spacing:-.01em}
h2{font:600 clamp(22px,3vw,28px)/1.25 Georgia,"Songti SC",serif;margin:2.2em 0 .6em;padding-top:.6em;border-top:1px solid var(--line)}
h3{font-size:18px;line-height:1.35;margin:1.8em 0 .5em}
h4{font-size:16px;margin:1.4em 0 .4em;color:var(--ink-2)}
p,li{color:var(--ink)}
.lede{color:var(--ink-2);font-size:17px;max-width:760px}
a{color:var(--accent)}
strong{font-weight:650}
code{font:13px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--code);padding:1px 5px;border-radius:4px}
ul,ol{padding-left:1.3em}
li{margin:.25em 0}
nav.toc{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:24px 0;font-size:14px}
nav.toc b{display:block;font:600 12px/1 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
nav.toc a{color:var(--ink-2);text-decoration:none;display:inline-block;margin:2px 14px 2px 0}
nav.toc a:hover{color:var(--accent)}
.tbl{overflow-x:auto;margin:14px 0 18px;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{padding:9px 12px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
th{font-weight:600;color:var(--ink-2);background:var(--surface-2);white-space:nowrap}
tr:last-child td{border-bottom:0}
td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
.warnbox{background:var(--accent-soft);border:1px solid var(--accent);border-left-width:5px;border-radius:10px;padding:14px 18px;margin:18px 0}
.warnbox h2,.warnbox h3{margin-top:0;border:0;padding:0}
.callout{border-radius:10px;padding:12px 16px;margin:10px 0;border:1px solid var(--line);background:var(--surface)}
.callout .lbl{display:block;font:600 11px/1.4 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px}
.callout p{margin:.25em 0}
.callout.syn{border-left:4px solid var(--bar)} .callout.syn .lbl{color:var(--bar)}
.callout.val{border-left:4px solid var(--accent)} .callout.val .lbl{color:var(--accent)}
.callout.probe{border-left:4px solid var(--muted)} .callout.probe .lbl{color:var(--muted)}
.callout.rec{border-left:4px solid var(--good)} .callout.rec .lbl{color:var(--good-ink)}
.callout.why{border-left:4px solid var(--warn)} .callout.why .lbl{color:var(--warn-ink)}
.callout.test{border-left:4px solid var(--accent)} .callout.test .lbl{color:var(--accent)}
.badge{display:inline-flex;align-items:center;gap:4px;font:600 12px/1.2 system-ui,sans-serif;padding:4px 8px;border-radius:999px;white-space:nowrap;max-width:100%;border:1px solid transparent}
.badge.v{color:var(--good-ink);background:color-mix(in srgb,var(--good) 14%,transparent);border-color:color-mix(in srgb,var(--good) 40%,transparent)}
.badge.p{color:var(--warn-ink);background:color-mix(in srgb,var(--warn) 18%,transparent);border-color:color-mix(in srgb,var(--warn) 50%,transparent)}
.badge.i{color:var(--crit-ink);background:color-mix(in srgb,var(--crit) 13%,transparent);border-color:color-mix(in srgb,var(--crit) 40%,transparent)}
.badge.n{color:var(--ink-2);background:var(--surface-2);border-color:var(--line)}
.matrix td,.matrix th{text-align:center}
.matrix td:first-child,.matrix th:first-child{text-align:left}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0}
.kpi{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.kpi .k{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
.kpi .kv{font:600 30px/1.1 Georgia,serif;margin:6px 0 2px}
.kpi .s{font-size:13px;color:var(--ink-2)}
.kpi .s .badge{white-space:normal}
.kpi{min-width:0}
.chart{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px 18px 12px;margin:16px 0 22px}
.chart h4{margin:0 0 4px;color:var(--ink)}
.chart .sub{font-size:13px;color:var(--muted);margin:0 0 14px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:13px;color:var(--ink-2);margin:0 0 12px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.sw{width:12px;height:12px;border-radius:3px;display:inline-block}
.row{display:grid;grid-template-columns:minmax(120px,260px) 1fr 104px;gap:12px;align-items:center;margin:8px 0;font-size:14px}
.row .lab{color:var(--ink);line-height:1.3}
.row .lab small{display:block;color:var(--muted);font-size:12px}
.row .val{font-variant-numeric:tabular-nums;color:var(--ink-2);text-align:right;white-space:nowrap}
.track{height:18px;background:var(--surface-2);border-radius:4px;display:flex;gap:2px;overflow:hidden}
.seg{height:100%;border-radius:4px;min-width:0;cursor:default;transition:filter .12s}
.seg:hover{filter:brightness(1.1)}
.seg.v{background:var(--good)} .seg.p{background:var(--warn)} .seg.i{background:var(--crit)}
.seg.b{background:var(--bar)} .seg.b2{background:var(--bar-2)}
.vbars{display:flex;align-items:flex-end;gap:10px;height:190px;padding:0 4px;border-bottom:1px solid var(--line)}
.vcol{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;gap:6px}
.vcol .bar{width:100%;max-width:64px;background:var(--bar);border-radius:4px 4px 0 0}
.vcol .n{font-size:13px;color:var(--ink-2);font-variant-numeric:tabular-nums}
.vlabels{display:flex;gap:10px;padding:6px 4px 0}
.vlabels div{flex:1;text-align:center;font-size:12px;color:var(--muted);line-height:1.3}
.refline{position:relative}
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media (max-width:760px){.twocol{grid-template-columns:1fr}.row{grid-template-columns:1fr;gap:4px}.row .val{text-align:left}}
details.raw{margin:12px 0;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
details.raw summary{cursor:pointer;padding:10px 14px;font-weight:600}
details.raw pre{margin:0;padding:14px;overflow:auto;max-height:420px;font:12px/1.5 ui-monospace,monospace;background:var(--code);border-radius:0 0 10px 10px}
.need{font:500 clamp(19px,2.4vw,24px)/1.4 Georgia,"Songti SC",serif;border-left:4px solid var(--accent);padding:6px 0 6px 16px;margin:14px 0}
#tip{position:fixed;pointer-events:none;z-index:10;background:var(--ink);color:var(--page);font-size:12px;line-height:1.4;padding:6px 9px;border-radius:6px;max-width:280px;opacity:0;transition:opacity .08s}
footer{margin-top:64px;padding-top:18px;border-top:1px solid var(--line);font-size:13px;color:var(--muted)}
.theme-toggle{position:absolute;top:12px;right:16px;background:var(--surface);color:var(--ink-2);border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:12px;cursor:pointer;z-index:5}
@media print{.theme-toggle,nav.toc{display:none}body{background:#fff}}
"""

JS = r"""
(function(){
  var tip=document.getElementById('tip');
  document.addEventListener('mousemove',function(e){
    var t=e.target.closest('[data-tip]');
    if(!t){tip.style.opacity=0;return;}
    tip.textContent=t.getAttribute('data-tip');
    var x=e.clientX+14,y=e.clientY+14;
    if(x+290>innerWidth)x=e.clientX-290;
    tip.style.left=x+'px';tip.style.top=y+'px';tip.style.opacity=1;
  });
  var b=document.querySelector('.theme-toggle'),r=document.documentElement;
  function cur(){return r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');}
  try{var s=localStorage.getItem('zero-theme');if(s)r.setAttribute('data-theme',s);}catch(e){}
  b.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('zero-theme',n);}catch(e){}});
})();
"""

BADGE = {"V": ("v", "✓ Validated"), "P": ("p", "◐ Partial"), "I": ("i", "✕ Invalidated")}
VERDICT_CLASS = {"validated": "v", "partially validated": "p", "invalidated": "i"}


def esc(s):
    return html.escape(s, quote=False)


def inline(s):
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def slug(s):
    s = re.sub(r"<[^>]+>", "", s).lower()
    s = re.sub(r"[^\w\u4e00-\u9fff]+", "-", s).strip("-")
    return s or "section"


def cell(txt):
    t = txt.strip()
    if t in BADGE:
        c, lab = BADGE[t]
        return f'<td><span class="badge {c}">{lab.split(" ")[0]} {t}</span></td>'
    low = t.lower()
    if low in VERDICT_CLASS:
        return f'<td><span class="badge {VERDICT_CLASS[low]}">{esc(t)}</span></td>'
    if re.fullmatch(r"[¥$]?[\d.,]+%?( \(\d+%\))?|\d+ \(\d+%\)", t):
        return f'<td class="num">{inline(t)}</td>'
    return f"<td>{inline(t)}</td>"


CALLOUTS = [
    ("synthetic research suggests", "syn"), ("validate with real humans", "val"), ("probe", "probe"),
    ("recommendation", "rec"), ("evidence", "why"), ("why", "why"), ("validation test", "test"), ("test", "test"),
]


def md_to_html(md, hooks=None):
    """Convert the Markdown subset used in this study. hooks: {heading_text_prefix: html_to_insert_after}."""
    hooks = hooks or {}
    lines = md.split("\n")
    out, toc = [], []
    i = 0
    list_stack = []  # list of (tag, indent)

    def close_lists(to_indent=-1):
        while list_stack and list_stack[-1][1] > to_indent:
            out.append(f"</li></{list_stack.pop()[0]}>")

    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            close_lists()
            lang = ln[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            label = "Machine-readable data (JSON)" if lang == "json" else "Code"
            out.append(f'<details class="raw"><summary>{label}</summary><pre>{esc(chr(10).join(buf))}</pre></details>')
            continue
        m = re.match(r"^(#{1,4}) (.*)$", ln)
        if m:
            close_lists()
            lvl, text = len(m.group(1)), m.group(2).strip()
            sid = slug(text)
            if lvl == 1:
                out.append(f"<h1>{inline(text)}</h1>")
            else:
                out.append(f'<h{lvl} id="{sid}">{inline(text)}</h{lvl}>')
                if lvl == 2:
                    toc.append((sid, re.sub(r"^\d+\.\s*", "", text)))
            for k, v in hooks.items():
                if text.startswith(k):
                    out.append(v)
            i += 1
            continue
        if ln.startswith("|"):
            close_lists()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], [r for r in rows[1:] if not re.fullmatch(r"[\s:\-|]*", "|".join(r))]
            is_matrix = any(c.strip() in BADGE for r in body for c in r[1:])
            cls = ' class="matrix"' if is_matrix else ""
            t = [f"<div class=\"tbl\"><table{cls}><thead><tr>" + "".join(f"<th>{inline(h.strip())}</th>" for h in head) + "</tr></thead><tbody>"]
            for r in body:
                t.append("<tr>" + "".join(cell(c) for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        if ln.startswith(">"):
            close_lists()
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].strip())
                i += 1
            text = " ".join(b for b in buf if b)
            mm = re.match(r"^\*\*([^*]+?):?\*\*:?\s*(.*)$", text)
            kind = "probe"
            if mm:
                label, body = mm.group(1).strip().rstrip(":"), mm.group(2)
                for key, k in CALLOUTS:
                    if label.lower().startswith(key):
                        kind = k
                        break
                if label.lower().startswith(("important", "synthetic data warning", "disclaimer")):
                    out.append(f'<div class="warnbox"><strong>{inline(label)}.</strong> {inline(body)}</div>')
                    continue
                out.append(f'<div class="callout {kind}"><span class="lbl">{inline(label)}</span><p>{inline(body)}</p></div>')
            else:
                out.append(f'<div class="callout probe"><p>{inline(text)}</p></div>')
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.) (.*)$", ln)
        if m:
            indent = len(m.group(1))
            tag = "ol" if m.group(2)[0].isdigit() else "ul"
            if list_stack and list_stack[-1][1] == indent:
                out.append("</li>")
            elif list_stack and list_stack[-1][1] > indent:
                close_lists(indent)
                out.append("</li>")
            if not list_stack or list_stack[-1][1] < indent:
                out.append(f"<{tag}>")
                list_stack.append((tag, indent))
            out.append(f"<li>{inline(m.group(3))}")
            i += 1
            continue
        if not ln.strip():
            if not (i + 1 < len(lines) and re.match(r"^\s+([-*]|\d+\.) ", lines[i + 1])):
                close_lists()
            i += 1
            continue
        close_lists()
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|```|\s*([-*]|\d+\.) )", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    close_lists()
    return "\n".join(out), toc


def page(title, eyebrow, lede, body, toc, description):
    toc_html = ""
    if toc:
        toc_html = '<nav class="toc"><b>Contents</b>' + "".join(f'<a href="#{s}">{esc(t)}</a>' for s, t in toc) + "</nav>"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{html.escape(description)}">
<style>{CSS}</style>
</head>
<body>
<button class="theme-toggle" type="button" aria-label="Toggle light or dark theme">◐ Theme</button>
<div class="wrap">
<header class="hero">
<div class="brand"><i></i>Zero · Synthetic Research</div>
<div class="eyebrow">{esc(eyebrow)}</div>
{lede}
</header>
{toc_html}
{body}
<footer>Synthetic AI research — an exploratory simulation for refining hypotheses and scripts. All findings must be validated through primary interviews with real human end users. Generated for Zero (观界未来) · Disciplined Entrepreneurship framework.</footer>
</div>
<div id="tip" role="tooltip"></div>
<script>{JS}</script>
</body>
</html>
"""


# ---------- Dashboard charts ----------

def dashboard_charts(data):
    A = data["assumptions"]
    W = data["wtp"]
    WS = data["wtp_summary"]
    O = data["objections"]
    P = data["phrases"]
    n = data["meta"]["n"]
    names = {p["id"]: p["name"] for p in data["personas"]}

    counts = {k: sum(1 for a in A if a["verdict"].lower() == k) for k in VERDICT_CLASS}
    kpis = f"""<div class="kpis">
<div class="kpi"><div class="k">Assumptions tested</div><div class="kv">{len(A)}</div><div class="s">{n} synthetic personas</div></div>
<div class="kpi"><div class="k">Validated</div><div class="kv">{counts['validated']}</div><div class="s"><span class="badge v">✓ none cleared ≥6/10</span></div></div>
<div class="kpi"><div class="k">Partially validated</div><div class="kv">{counts['partially validated']}</div><div class="s"><span class="badge p">◐ A1 A2 A4 A6 A8</span></div></div>
<div class="kpi"><div class="k">Invalidated</div><div class="kv">{counts['invalidated']}</div><div class="s"><span class="badge i">✕ A3 A5 A7</span></div></div>
<div class="kpi"><div class="k">Median stated WTP</div><div class="kv">¥{WS['median_rmb']:g}</div><div class="s">mean ¥{WS['mean_rmb']:g} vs ARPU ¥{data['meta']['baseline']['arpu_rmb']:g}</div></div>
<div class="kpi"><div class="k">Pay ¥39 unconditionally</div><div class="kv">{WS['pay_39_unconditionally']}/{n}</div><div class="s">{WS['pay_99_conditionally']}/{n} would pay ¥99 only via substitution</div></div>
</div>"""

    rows = []
    for a in A:
        c = a["counts"]
        segs = ""
        for k, cls, lab in (("V", "v", "Validated"), ("P", "p", "Partial"), ("I", "i", "Invalidated")):
            if c[k]:
                who = ", ".join(p for p, s in a["scores"].items() if s == k)
                segs += f'<div class="seg {cls}" style="width:{c[k] / n * 100}%" data-tip="{a["id"]} · {lab}: {c[k]}/{n} ({c[k] * 10}%) — {who}"></div>'
        vc = VERDICT_CLASS[a["verdict"].lower()]
        rows.append(f'<div class="row"><div class="lab"><b>{a["id"]}</b> {esc(a["name"])}<small><span class="badge {vc}">{esc(a["verdict"])}</span> · confidence {a["confidence"]}</small></div>'
                    f'<div class="track" role="img" aria-label="{a["id"]}: {c["V"]} validated, {c["P"]} partial, {c["I"]} invalidated of {n}">{segs}</div>'
                    f'<div class="val">{c["V"]} / {c["P"]} / {c["I"]}</div></div>')
    scorechart = f"""<div class="chart"><h4>Assumption scorecard — share of 10 personas</h4>
<p class="sub">Each bar is 10 personas. Hover a segment for who. Verdict rule: Validated if V ≥ 6; Invalidated if I ≥ 6 or (V = 0 and I ≥ 5).</p>
<div class="legend"><span><i class="sw" style="background:var(--good)"></i>✓ Validated</span><span><i class="sw" style="background:var(--warn)"></i>◐ Partially validated</span><span><i class="sw" style="background:var(--crit)"></i>✕ Invalidated</span></div>
{''.join(rows)}</div>"""

    mx = max(w["amount_rmb"] for w in W)
    wrows = []
    for w in sorted(W, key=lambda x: -x["amount_rmb"]):
        pct = w["amount_rmb"] / mx * 100
        ceil = w.get("ceiling_rmb", w["amount_rmb"])
        extra = max(0, ceil - w["amount_rmb"]) / mx * 100
        segs = ""
        if w["amount_rmb"]:
            segs += f'<div class="seg b" style="width:{pct}%" data-tip="{w["persona"]} stated ¥{w["amount_rmb"]}/mo — {esc(w["conditions"])}"></div>'
        if extra:
            segs += f'<div class="seg b2" style="width:{extra}%" data-tip="{w["persona"]} conditional ceiling ¥{ceil}/mo"></div>'
        season = " · seasonal" if w.get("seasonal") else ""
        wrows.append(f'<div class="row"><div class="lab"><b>{w["persona"]}</b> {esc(names[w["persona"]])}<small>{esc(w["bucket"])}{season}</small></div>'
                     f'<div class="track">{segs}</div><div class="val">¥{w["amount_rmb"]:g}{" → ¥" + format(ceil, "g") if ceil != w["amount_rmb"] else ""}</div></div>')
    arpu_pct = data["meta"]["baseline"]["arpu_rmb"] / mx * 100
    wtpchart = f"""<div class="chart"><h4>Stated monthly WTP per persona (RMB)</h4>
<p class="sub">Dark = stated amount, light = conditional ceiling. Current ARPU ¥{data['meta']['baseline']['arpu_rmb']:g} sits at {arpu_pct:.0f}% of this axis; P10's ¥144 is a ChatGPT Plus substitution (¥0 incremental).</p>
<div class="legend"><span><i class="sw" style="background:var(--bar)"></i>Stated WTP</span><span><i class="sw" style="background:var(--bar-2)"></i>Conditional ceiling</span></div>
{''.join(wrows)}</div>"""

    bmax = max(b["count"] for b in WS["buckets"])
    cols = "".join(f'<div class="vcol"><span class="n">{b["count"]} · {b["pct"]}%</span><div class="bar" style="height:{b["count"] / bmax * 80}%" data-tip="{esc(b["bucket"])}: {b["count"]} of {n} personas"></div></div>' for b in WS["buckets"])
    labs = "".join(f"<div>{esc(b['bucket'])}</div>" for b in WS["buckets"])
    bucketchart = f"""<div class="chart"><h4>WTP distribution by bucket</h4><p class="sub">Count of 10 personas per monthly bucket.</p>
<div class="vbars">{cols}</div><div class="vlabels">{labs}</div></div>"""

    orows = "".join(
        f'<div class="row"><div class="lab">{esc(o["text"])}</div><div class="track"><div class="seg b" style="width:{o["count"] / n * 100}%" data-tip="{o["count"]}/{n}: {", ".join(o["personas"])}"></div></div><div class="val">{o["count"]}/{n} · {o["count"] * 10}%</div></div>'
        for o in O)
    objchart = f"""<div class="chart"><h4>Objections ranked by frequency</h4><p class="sub">Share of 10 personas raising each objection; hover for who.</p>{orows}</div>"""

    prows = "".join(
        f'<div class="row"><div class="lab">“{esc(p["phrase"])}”</div><div class="track"><div class="seg b" style="width:{p["count"] / n * 100}%" data-tip="{p["count"]} of {n} personas"></div></div><div class="val">{p["count"]}/{n}</div></div>'
        for p in P)
    phrasechart = f"""<div class="chart"><h4>Organic language — personas using each phrase</h4><p class="sub">Starting vocabulary to listen for in real interviews (shared-generator caveat applies).</p>{prows}</div>"""

    need = data["biggest_unmet_need"]
    needblock = f"""<p class="need">“{esc(need['statement'])}”</p>
<div class="kpis"><div class="kpi"><div class="k">Direct match</div><div class="kv">{len(need['direct_match'])}/{n}</div><div class="s">{', '.join(need['direct_match'])}</div></div>
<div class="kpi"><div class="k">Adjacent</div><div class="kv">{len(need['adjacent_match'])}/{n}</div><div class="s">{', '.join(need['adjacent_match'])}</div></div>
<div class="kpi"><div class="k">Different need</div><div class="kv">{len(need['different'])}/{n}</div><div class="s">{', '.join(need['different'])}</div></div></div>"""

    return {
        "1. Executive summary": kpis,
        "2a. Assumption scorecard: summary table": scorechart,
        "2b. Willingness-to-pay distribution: buckets": bucketchart,
        "2b. Willingness-to-pay distribution: per-persona": wtpchart,
        "2c. Top objections": objchart,
        "3b. Recurring organic language": phrasechart,
        "3c. The single biggest unmet need": needblock,
    }


def build_dashboard():
    md = (ROOT / "03_synthesis_dashboard.md").read_text(encoding="utf8")
    data = json.loads(re.search(r"```json\n(.*?)\n```", md, re.S).group(1))
    title_line, rest = md.split("\n", 1)
    body, toc = md_to_html(rest, dashboard_charts(data))
    body = re.sub(r'(<h2 id="disclaimer[^"]*">.*?)(?=<h2 )', r'<div class="warnbox">\1</div>', body, count=1, flags=re.S)
    lede = f'<h1>{inline(title_line.lstrip("# ").strip())}</h1><p class="lede">Ten synthetic end users, eight key assumptions (Disciplined Entrepreneurship Step 20), one synthesis. Scorecard, willingness to pay, objections, verbatims and the biggest unmet need.</p>'
    (ROOT / "03_synthesis_dashboard.html").write_text(
        page("Zero Research Dashboard", "Steps 4–5 · Synthesis dashboard", lede, body, toc,
             "Synthetic primary market research dashboard for Zero: assumption scorecard, WTP, objections and verbatims."),
        encoding="utf8")


def build_simple(src, dst, title, eyebrow, description):
    md = (ROOT / src).read_text(encoding="utf8")
    title_line, rest = md.split("\n", 1)
    lede_m = re.match(r"\s*\n?(_[^\n]+_)\n", rest)
    lede_txt = ""
    if lede_m:
        lede_txt = f'<p class="lede">{inline(lede_m.group(1).strip("_"))}</p>'
        rest = rest[lede_m.end():]
    body, toc = md_to_html(rest)
    lede = f'<h1>{inline(title_line.lstrip("# ").strip())}</h1>{lede_txt}'
    (ROOT / dst).write_text(page(title, eyebrow, lede, body, toc, description), encoding="utf8")


if __name__ == "__main__":
    build_dashboard()
    if (ROOT / "04_real_user_interview_script.md").exists():
        build_simple("04_real_user_interview_script.md", "04_real_user_interview_script.html",
                     "Zero Interview Script", "Step 6 · Real-user interview guide",
                     "Annotated interview script for real-user validation of Zero's key assumptions.")
    if (ROOT / "05_business_plan_revisions.md").exists():
        build_simple("05_business_plan_revisions.md", "05_business_plan_revisions.html",
                     "Zero Plan Revisions", "Step 7 · 24 Steps of Disciplined Entrepreneurship",
                     "Recommended revisions to Zero's end user profile, persona, value proposition and business plan.")
    print("built")
