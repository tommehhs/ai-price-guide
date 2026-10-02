#!/usr/bin/env python3
"""Build DATABASE.md, data/tools.csv and index.html from data/*.json.

Usage: python3 scripts/build.py
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Update these together when refreshing prices.
AS_OF = "2 October 2026"
USD_TO_AUD = 1.44  # mid-market, 2 Oct 2026 (1 AUD = 0.695 USD)
GST = 1.10

FEATURES = ["search", "research", "image", "video", "voice", "code", "files", "memory", "agent"]
MARK = {"yes": "✓", "star": "✓★", "partial": "~", "no": "✗"}
STATUS_LABEL = {"active": "", "paused": " ⏸ sign-ups paused", "discontinued": " ✖ discontinued"}


def load():
    cats = json.loads((DATA / "categories.json").read_text())
    tools = json.loads((DATA / "tools.json").read_text())
    ids = [t["id"] for t in tools]
    assert len(ids) == len(set(ids)), "duplicate tool ids"
    cat_ids = {c["id"] for c in cats}
    for t in tools:
        assert t["category"] in cat_ids, f"{t['id']}: unknown category {t['category']}"
    return cats, tools


def usd(v):
    if v is None:
        return "—"
    return f"${v:,.2f}".replace(".00", "")


def aud(v):
    """Rough AUD estimate including GST. Local store prices often differ."""
    if v is None:
        return "—"
    return f"~A${round(v * USD_TO_AUD * GST):,}"


def price_cell(t):
    if t["status"] == "discontinued":
        return "Discontinued"
    if t["from"] is None:
        return "Free" if t["free"] else "Pay as you go"
    return ("Free / " if t["free"] else "") + f"from {usd(t['from'])}"


def build_markdown(cats, tools):
    out = []
    w = out.append
    w("# AI Tools Database for Consumers")
    w("")
    w(f"_Last updated {AS_OF}. {len(tools)} tools across {len(cats)} categories._")
    w("")
    w("Prices are monthly, in US dollars, for individual plans. The **~A$** figures are rough "
      f"estimates (US$1 = A${USD_TO_AUD}, plus 10% GST); Australian app-store and local prices "
      "often differ, so check before you buy. Rows marked _unverified_ come from older sources "
      "and weren't re-checked for this update. AI products change monthly, so treat this as a snapshot.")
    w("")
    w("Generated from [`data/tools.json`](data/tools.json) by `scripts/build.py`. "
      "Open [`index.html`](index.html) for a searchable, filterable version, or "
      "[`data/tools.csv`](data/tools.csv) in a spreadsheet.")
    w("")

    w("## Quick picks")
    w("")
    picks = [
        ("Best all-rounder", "ChatGPT Plus ($20) or Claude Pro ($20)"),
        ("Best value bundle", "Google AI Pro ($19.99): Gemini plus storage, Veo video and Gemini Notebook"),
        ("Best free assistant", "Gemini free tier; DeepSeek for free reasoning (data stored in China)"),
        ("Cheapest paid assistant", "Google AI Plus ($4.99) or ChatGPT Go ($8, has ads)"),
        ("Writing & long documents", "Claude"),
        ("Research with sources", "Perplexity Pro; Gemini Notebook for your own documents"),
        ("Microsoft Office user", "Microsoft 365 Premium ($19.99) — Office, 6 TB and Copilot"),
        ("Privacy first", "Mistral Vibe (EU-hosted), Duck.ai, Brave Leo; Claude with training switched off"),
        ("Images", "ChatGPT Images 2.5 (quality), Nano Banana (free/fast), Midjourney (style), Ideogram (text)"),
        ("Video", "Veo 3.1 via Google AI (realism), Kling 3.0 (value), Runway (control)"),
        ("Music", "Suno Pro ($10)"),
        ("Voiceovers", "ElevenLabs"),
        ("Coding", "Claude Code (in Claude Pro), GitHub Copilot Pro ($10) as the cheap option, Cursor as an editor"),
        ("Build an app without coding", "Lovable or Bolt.new ($25); Replit to host it too"),
        ("AI browser", "Comet (free agent); Chrome or Edge if you won't switch"),
        ("Meeting notes", "Granola (no bot), Plaud (in-person, needs device)"),
    ]
    w("| Need | Pick |")
    w("|---|---|")
    for need, pick in picks:
        w(f"| {need} | {pick} |")
    w("")

    w("## Recent changes worth knowing (2026)")
    w("")
    for line in [
        "**OpenAI Sora is gone** — app closed 26 Apr 2026, API 24 Sep 2026. ChatGPT no longer makes video.",
        "**ChatGPT Atlas browser shut down** 9 Aug 2026; use the ChatGPT Chrome extension instead.",
        "**ChatGPT Pro now has $100, $200 and $500 tiers**; $200 closed to new sign-ups since 10 Sep 2026. Free and Go show ads.",
        "**Google AI Ultra cut from $249.99 to $99.99** (5x limits); old top tier now $199.99 (20x). AI Plus cut to $4.99.",
        "**NotebookLM is now Gemini Notebook** (Jul 2026).",
        "**Siri rebuilt on Gemini-based models** in iOS 27 (14 Sep 2026).",
        "**Meta launched Muse**, an errand-running agent, free with $20/$100 tiers (US, Sep 2026).",
        "**Le Chat is now Mistral Vibe**; **Windsurf is now Devin Desktop**.",
        "**Microsoft Copilot** dropped consumer Deep Research and moved advanced features to usage-based billing (Sep 2026).",
        "**GitHub Copilot** switched to per-token AI Credits (1 Jun 2026).",
        "**Kimi** paused new paid subscriptions (20 Jul 2026) due to compute limits.",
        "**Suno lost a German copyright (GEMA) case**; Udio paused downloads while moving to licensed models.",
    ]:
        w(f"- {line}")
    w("")

    w("## Contents")
    w("")
    for c in cats:
        n = sum(1 for t in tools if t["category"] == c["id"])
        w(f"- [{c['name']}](#{anchor(c['name'])}) ({n})")
    w("- [Privacy at a glance](#privacy-at-a-glance)")
    w("- [How to update this database](#how-to-update-this-database)")
    w("")

    by_cat = {c["id"]: [t for t in tools if t["category"] == c["id"]] for c in cats}

    for c in cats:
        items = by_cat[c["id"]]
        w(f"## {c['name']}")
        w("")
        w(f"_{c['blurb']}_")
        w("")
        if c["id"] == "assistant":
            w("### Feature matrix")
            w("")
            w("| Service | " + " | ".join(f.title() for f in FEATURES) + " |")
            w("|---|" + "---|" * len(FEATURES))
            for t in items:
                f = t.get("features")
                if not f:
                    continue
                w(f"| {t['name']} | " + " | ".join(MARK[f[k]] for k in FEATURES) + " |")
            w("")
            w("✓ yes · ~ limited · ✗ no · ★ standout. _Agent_ = can carry out multi-step tasks for you (browse, book, fill forms).")
            w("")
            w("### Prices")
            w("")
        w("| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |")
        w("|---|---|---|---|---|---|---|---|")
        for t in items:
            name = f"[{t['name']}]({t['url']}){STATUS_LABEL[t['status']]}"
            free = "✓" if t["free"] else "✗"
            w(f"| {name} | {t['maker']} | {free} | {usd(t['from'])} | {usd(t['standard'])} | "
              f"{usd(t['top'])} | {aud(t['standard'])} | {t['best_for']} |")
        w("")
        w("<details><summary>Details for each tool</summary>")
        w("")
        for t in items:
            tag = "" if t["verified"] != "older" else " _(unverified)_"
            w(f"**{t['name']}**{tag}{STATUS_LABEL[t['status']]}")
            w(f"- Plans: {t['pricing']}" + (f" · Free: {t['free_note']}" if t["free"] and t["free_note"] else ""))
            if t["strengths"] != "—":
                w(f"- Strengths: {t['strengths']}")
            w(f"- Watch out: {t['watch_out']}")
            if t["platforms"] != "—":
                w(f"- Platforms: {t['platforms']}")
            if t["privacy"] not in ("—", "Standard"):
                w(f"- Privacy: {t['privacy']} (data region: {t['region']})")
            w("")
        w("</details>")
        w("")

    w("## Privacy at a glance")
    w("")
    w("| Assistant | Trains on your chats? | Where data lives |")
    w("|---|---|---|")
    for t in by_cat["assistant"]:
        w(f"| {t['name']} | {t['privacy']} | {t['region']} |")
    w("")
    w("Turning training off stops _future_ use only. Never paste passwords, ID numbers, or client data "
      "you aren't allowed to share into any consumer chatbot.")
    w("")

    w("## How to update this database")
    w("")
    w("1. Edit `data/tools.json` (one object per tool; add categories in `data/categories.json`).")
    w("2. Set `verified` to the month you checked it (e.g. `2026-10`) and add the page you checked to `sources`.")
    w("3. If the exchange rate has moved, update `USD_TO_AUD` and `AS_OF` in `scripts/build.py`.")
    w("4. Run `python3 scripts/build.py` to regenerate this file, the CSV and `index.html`.")
    w("")
    w("### Field reference")
    w("")
    w("| Field | Meaning |")
    w("|---|---|")
    for k, v in [
        ("status", "`active`, `paused` (new sign-ups closed) or `discontinued`"),
        ("free / free_note", "Whether there's a usable free tier, and its main limit"),
        ("from / standard / top", "Cheapest paid, most common, and most expensive individual plan in USD/month (`null` = none)"),
        ("features", "Assistants only: `yes`, `star`, `partial` or `no` for each capability"),
        ("privacy / region", "Training default and opt-out; where the company stores data"),
        ("verified", "Month the details were last checked; `older` = not re-checked"),
    ]:
        w(f"| `{k}` | {v} |")
    w("")
    w("## Sources")
    w("")
    srcs = sorted({s for t in tools for s in t["sources"]})
    for s in srcs:
        w(f"- {s}")
    w("")
    return "\n".join(out)


def anchor(name):
    keep = "".join(ch for ch in name.lower() if ch.isalnum() or ch in " -")
    return keep.replace(" ", "-")


def build_csv(cats, tools, path):
    cat_name = {c["id"]: c["name"] for c in cats}
    cols = ["name", "maker", "category", "status", "free", "free_note", "from_usd", "standard_usd",
            "top_usd", "standard_aud_est", "pricing", "best_for", "strengths", "watch_out",
            "platforms", "privacy", "region", *[f"feat_{f}" for f in FEATURES], "verified", "url", "sources"]
    with path.open("w", newline="") as fh:
        wr = csv.writer(fh)
        wr.writerow(cols)
        for t in tools:
            f = t.get("features", {})
            wr.writerow([
                t["name"], t["maker"], cat_name[t["category"]], t["status"], "yes" if t["free"] else "no",
                t["free_note"], t["from"], t["standard"], t["top"],
                None if t["standard"] is None else round(t["standard"] * USD_TO_AUD * GST),
                t["pricing"], t["best_for"], t["strengths"], t["watch_out"], t["platforms"],
                t["privacy"], t["region"], *[f.get(k, "") for k in FEATURES], t["verified"], t["url"],
                " ".join(t["sources"]),
            ])


def page_body(cats, tools):
    template = (ROOT / "scripts" / "template.html").read_text()
    payload = json.dumps({"asOf": AS_OF, "rate": USD_TO_AUD, "gst": GST, "categories": cats, "tools": tools},
                         ensure_ascii=False).replace("</", "<\\/")
    return template.replace("/*__DATA__*/null", payload)


def build_html(body, path):
    head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n')
    title_end = body.index("</title>") + len("</title>")
    path.write_text(head + body[:title_end] + "\n</head>\n<body>\n" + body[title_end:] + "\n</body>\n</html>\n")


def main():
    cats, tools = load()
    (ROOT / "DATABASE.md").write_text(build_markdown(cats, tools))
    build_csv(cats, tools, DATA / "tools.csv")
    body = page_body(cats, tools)
    build_html(body, ROOT / "index.html")
    # Optional: page body only (no <html>/<head>), for hosts that add their own skeleton.
    if len(sys.argv) > 2 and sys.argv[1] == "--fragment":
        Path(sys.argv[2]).write_text(body)
    print(f"Built {len(tools)} tools in {len(cats)} categories.")


if __name__ == "__main__":
    main()
