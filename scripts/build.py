#!/usr/bin/env python3
"""Build DATABASE.md, data/tools.csv and index.html from data/*.json.

Usage:
  python3 scripts/build.py                      # regenerate everything
  python3 scripts/build.py --fragment OUT.html  # also write the page body only
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
STATUS_LABEL = {"active": "", "paused": " ⏸ sign-ups paused", "discontinued": " ✖ discontinued",
                "upcoming": " ◷ coming soon"}
SCORE_KEYS = ["quality", "value", "ease", "privacy"]
BILLING_SUFFIX = {"monthly": "", "yearly": "/yr", "one-off": " once"}
REQUIRED = ["id", "name", "maker", "category", "status", "url", "free", "billing", "pricing", "best_for",
            "strengths", "watch_out", "platforms", "privacy", "region", "scores", "tags", "verified", "sources"]


def load():
    cats = json.loads((DATA / "categories.json").read_text())
    tools = json.loads((DATA / "tools.json").read_text())
    ids = [t["id"] for t in tools]
    assert len(ids) == len(set(ids)), "duplicate tool ids"
    cat_ids = {c["id"] for c in cats}
    for t in tools:
        missing = [k for k in REQUIRED if k not in t]
        assert not missing, f"{t['id']}: missing {missing}"
        assert t["category"] in cat_ids, f"{t['id']}: unknown category {t['category']}"
        assert t["status"] in STATUS_LABEL, f"{t['id']}: bad status"
        assert t["billing"] in BILLING_SUFFIX, f"{t['id']}: bad billing"
        assert all(1 <= t["scores"][k] <= 5 for k in SCORE_KEYS), f"{t['id']}: bad scores"
        for k in ("from", "standard", "top"):
            t.setdefault(k, None)
    return cats, tools


def usd(v, billing="monthly"):
    if v is None:
        return "—"
    return f"${v:,.2f}".replace(".00", "") + BILLING_SUFFIX[billing]


def aud_est(v):
    return None if v is None else round(v * USD_TO_AUD * GST)


def aud_cell(t):
    if t.get("aud"):
        return t["aud"]
    v = aud_est(t["standard"])
    return "—" if v is None else f"~A${v:,}{BILLING_SUFFIX[t['billing']]}"


def stars(n):
    return "●" * n + "○" * (5 - n)


def overall(t):
    s = t["scores"]
    return round((s["quality"] * 2 + s["value"] + s["ease"] + s["privacy"]) / 5, 1)


def anchor(name):
    keep = "".join(ch for ch in name.lower() if ch.isalnum() or ch in " -")
    return keep.replace(" ", "-")


def build_markdown(cats, tools):
    out = []
    w = out.append
    by_cat = {c["id"]: [t for t in tools if t["category"] == c["id"]] for c in cats}
    live = [t for t in tools if t["status"] != "discontinued"]

    w("# AI Tools Database for Consumers")
    w("")
    w(f"_Last updated {AS_OF}. {len(tools)} tools across {len(cats)} categories, "
      f"{sum(1 for t in live if t['free'])} with a usable free tier._")
    w("")
    w("Prices are monthly, in US dollars, for individual plans unless marked _/yr_ (yearly) or _once_ (hardware). "
      "Where an Australian price has been published it's shown as **A$**; otherwise **~A$** is an estimate "
      f"(US$1 = A${USD_TO_AUD}, plus 10% GST). Ratings are this guide's own judgement, explained in "
      "[How the ratings work](#how-the-ratings-work). AI products change monthly, so treat this as a snapshot.")
    w("")
    w("Generated from [`data/tools.json`](data/tools.json) by `scripts/build.py`. "
      "Open [`index.html`](index.html) for the interactive version with search, filters, a "
      "\"help me choose\" picker and a shortlist that totals your monthly cost. "
      "[`data/tools.csv`](data/tools.csv) opens in any spreadsheet.")
    w("")

    w("## Contents")
    w("")
    w("- [Start here: quick picks](#start-here-quick-picks)")
    w("- [Best in each category](#best-in-each-category)")
    w("- [Recent changes (2026)](#recent-changes-2026)")
    w("- [Prices in Australia](#prices-in-australia)")
    w("- Categories:")
    for c in cats:
        w(f"  - [{c['name']}](#{anchor(c['name'])}) ({len(by_cat[c['id']])})")
    w("- [Privacy at a glance](#privacy-at-a-glance)")
    w("- [Ways to pay less](#ways-to-pay-less)")
    w("- [Staying safe](#staying-safe)")
    w("- [Jargon buster](#jargon-buster)")
    w("- [How the ratings work](#how-the-ratings-work)")
    w("- [How to update this database](#how-to-update-this-database)")
    w("")

    w("## Start here: quick picks")
    w("")
    picks = [
        ("I only want one subscription", "ChatGPT Plus or Claude Pro ($20). Gemini via Google AI Pro if you also want storage"),
        ("I don't want to pay", "Gemini free + ChatGPT free; Gemini Notebook for study; Comet as a free agent browser"),
        ("Cheapest paid upgrade", "Google AI Plus ($4.99) or ChatGPT Go (A$13, has ads)"),
        ("I write a lot", "Claude; Grammarly or Wispr Flow alongside"),
        ("I live in Word/Excel/Outlook", "Microsoft 365 Premium (A$33): Office, 6 TB and Copilot in one"),
        ("I'm on iPhone / Android", "Siri in iOS 27 is free and much better; on Android, Gemini is now the assistant"),
        ("Privacy matters most", "Mistral Vibe (EU), Duck.ai, Brave Leo, or LM Studio to run AI offline"),
        ("Research with sources", "Perplexity Pro; Consensus for science; Gemini Notebook for your own files"),
        ("Pictures", "ChatGPT Images (quality), Gemini Nano Banana (free), Midjourney (style), Canva (designs)"),
        ("Fix my photos", "Google Photos (free), Photoshop (serious), Topaz (upscaling)"),
        ("Video", "Veo 3.1 via Google AI (realism), Kling 3.0 (value), Runway (control)"),
        ("Music / voiceovers", "Suno Pro ($10) / ElevenLabs"),
        ("Coding", "Claude Code (in Claude Pro); GitHub Copilot Pro ($10) as the cheap option; Cursor as an editor"),
        ("Make an app or website", "Lovable or Bolt.new ($25); Replit to host it too"),
        ("Hand off whole tasks", "ChatGPT agent if you're on Plus; Manus for long hands-off jobs"),
        ("Kids' homework help", "Khanmigo ($4) or ChatGPT Study Mode (free)"),
        ("Travel", "Google Translate (offline, camera), DeepL for documents, Ray-Ban Meta for live translation"),
        ("Smart home", "Alexa+ (free with Prime; Early Access in Australia)"),
    ]
    w("| I want… | Pick |")
    w("|---|---|")
    for need, pick in picks:
        w(f"| {need} | {pick} |")
    w("")

    w("## Best in each category")
    w("")
    w("| Category | Pick | Why | From |")
    w("|---|---|---|---|")
    for c in cats:
        for t in by_cat[c["id"]]:
            if t.get("pick"):
                paid = usd(t["from"], t["billing"]) if t["from"] is not None else ""
                price = ("Free" + (f", paid from {paid}" if paid else "")) if t["free"] else paid
                w(f"| {c['name']} | **{t['name']}** | {t['pick']} | {price} |")
    w("")

    w("## Recent changes (2026)")
    w("")
    for line in [
        "**OpenAI Sora is gone**: app closed 26 Apr 2026, API 24 Sep 2026. ChatGPT no longer makes video.",
        "**ChatGPT Atlas browser shut down** 9 Aug 2026; use the ChatGPT Chrome extension instead.",
        "**ChatGPT Pro now has $100, $200 and $500 tiers**; $200 closed to new sign-ups since 10 Sep 2026. Free and Go show ads.",
        "**Google AI Ultra cut from $249.99 to $99.99** (5x limits); old top tier now $199.99 (20x). AI Plus cut to $4.99.",
        "**Gemini fully replaced Google Assistant** on Android phones, watches and cars (from 4 Sep 2026).",
        "**NotebookLM is now Gemini Notebook** (Jul 2026).",
        "**Siri rebuilt on Gemini-based models** in iOS 27 (14 Sep 2026).",
        "**Alexa+ reached Australia** in Early Access (6 Aug 2026): free with Prime, A$29.99 without after 30 Nov.",
        "**Meta launched Muse**, an errand-running agent, free with $20/$100 tiers (US only, Sep 2026). Cheaper Meta Glasses from $299.",
        "**Le Chat is now Mistral Vibe**; **Windsurf is now Devin Desktop**.",
        "**Microsoft Copilot** dropped consumer Deep Research and moved advanced features to usage-based billing (Sep 2026).",
        "**GitHub Copilot** switched to per-token AI Credits (1 Jun 2026).",
        "**Kimi** paused new paid subscriptions (20 Jul 2026) due to compute limits.",
        "**Poe** cut its free allowance by ~90% (Mar 2026).",
        "**Character.AI** settled wrongful-death lawsuits (Jan 2026) and restricted under-18s.",
        "**Suno lost a German (GEMA) copyright case**; Udio paused downloads while moving to licensed models.",
    ]:
        w(f"- {line}")
    w("")

    w("## Prices in Australia")
    w("")
    w("Published or widely reported Australian prices (GST included). Everything else in this guide "
      f"shows an estimate at US$1 = A${USD_TO_AUD} + GST.")
    w("")
    w("| Tool | Australian price | Notes |")
    w("|---|---|---|")
    for t in tools:
        if t.get("aud") or t.get("au"):
            w(f"| {t['name']} | {t.get('aud', '—')} | {t.get('au', '')} |")
    w("")

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
                if f:
                    w(f"| {t['name']} | " + " | ".join(MARK[f[k]] for k in FEATURES) + " |")
            w("")
            w("✓ yes · ~ limited · ✗ no · ★ standout. _Agent_ = can carry out multi-step tasks for you (browse, book, fill forms).")
            w("")
            w("### Prices and ratings")
            w("")
        w("| Tool | Free? | From | Typical | Top | A$ | Rating | Best for |")
        w("|---|---|---|---|---|---|---|---|")
        for t in items:
            name = f"[{t['name']}]({t['url']}){STATUS_LABEL[t['status']]}"
            if t.get("pick"):
                name += f" 🏅 _{t['pick']}_"
            b = t["billing"]
            rating = "—" if t["status"] == "discontinued" else f"{overall(t)}/5"
            w(f"| {name} | {'✓' if t['free'] else '✗'} | {usd(t['from'], b)} | {usd(t['standard'], b)} | "
              f"{usd(t['top'], b)} | {aud_cell(t)} | {rating} | {t['best_for']} |")
        w("")
        w("<details><summary>Details for each tool</summary>")
        w("")
        for t in items:
            tag = "" if t["verified"] != "older" else " _(unverified)_"
            w(f"**{t['name']}** ({t['maker']}){tag}{STATUS_LABEL[t['status']]}")
            w(f"- Plans: {t['pricing']}" + (f" · Free: {t['free_note']}" if t["free"] and t.get("free_note") else ""))
            if t["strengths"] != "—":
                w(f"- Strengths: {t['strengths']}")
            w(f"- Watch out: {t['watch_out']}")
            if t.get("au"):
                w(f"- Australia: {t['au']}")
            if t["platforms"] != "—":
                w(f"- Platforms: {t['platforms']}")
            if t["privacy"] not in ("—", "Standard"):
                w(f"- Privacy: {t['privacy']} (data: {t['region']})")
            if t["status"] != "discontinued":
                s = t["scores"]
                w("- Ratings: " + " · ".join(f"{k} {stars(s[k])}" for k in SCORE_KEYS))
            w(f"- Checked: {t['verified']} · Sources: " + ", ".join(f"[{i + 1}]({u})" for i, u in enumerate(t["sources"])))
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
    w("Most privacy-friendly overall: **LM Studio / Ollama / Jan** (nothing leaves your computer), "
      "**Duck.ai** and **Brave Leo** (anonymised, no training), **Mistral Vibe** (EU law), and **Claude** with "
      "training switched off. Turning training off stops _future_ use only.")
    w("")

    w("## Ways to pay less")
    w("")
    for line in [
        "**Pay yearly** when you're sure: Claude Pro is A$340/yr vs A$34/mo; Beautiful.ai and Grammarly are 2.5–4x dearer month-to-month.",
        "**Count the bundle**: Google AI Pro includes extra Google storage; Microsoft 365 Premium includes Office and 6 TB; Alexa+ is free with Prime (A$9.99/mo). If you already pay for storage or Office, the AI is close to free.",
        "**One assistant, not three**: the $20 assistants overlap heavily. Use free tiers of the others for second opinions.",
        "**Try budget tiers first**: Google AI Plus ($4.99), ChatGPT Go (A$13), Mistral Vibe Student ($5.99).",
        "**Creators: use an aggregator** (Krea, OpenArt, Higgsfield, Poe) if you'd otherwise pay for several image/video tools.",
        "**Watch credit systems**: video, agents and app builders charge per use. Set spending caps where offered.",
        "**Cancel trials** on the day you sign up; app-store subscriptions are cancelled in your phone's settings, not the app.",
        "**Apple App Store / Google Play prices** are often higher than paying on the website.",
    ]:
        w(f"- {line}")
    w("")

    w("## Staying safe")
    w("")
    for line in [
        "Don't paste passwords, tax file numbers, Medicare or bank details into any chatbot.",
        "AI makes things up confidently. Check anything medical, legal, financial or safety-related with a real source or professional.",
        "Agents and AI browsers can be tricked by hidden text on web pages (prompt injection). Don't give them access to banking or let them pay without checking.",
        "Voice-clone scams are common: agree a family code word for urgent money requests.",
        "Companion apps: check age ratings, and watch for emotional over-reliance, especially for teens.",
        "Commercial use: free tiers of image, music and video tools usually don't allow selling what you make.",
    ]:
        w(f"- {line}")
    w("")

    w("## Jargon buster")
    w("")
    for term, meaning in [
        ("Agent", "AI that carries out a multi-step task for you (browsing, filling forms, building a file) rather than just replying."),
        ("Credits / points / tokens", "Usage units. Bigger models, longer videos and agent runs use more of them."),
        ("Context window", "How much text the AI can keep in mind at once. 1M tokens ≈ 750,000 words."),
        ("Deep research", "The AI searches dozens of sources for several minutes and writes a cited report."),
        ("Model", "The underlying AI (e.g. GPT-6, Claude Opus 5.5, Gemini 3.5). Apps often let you pick one."),
        ("Open weights / local", "Models you can download and run on your own computer, offline."),
        ("BYOK", "Bring your own key: you pay the AI company directly per use instead of a subscription."),
        ("Prompt injection", "Hidden instructions on a web page or file that trick an AI into doing something you didn't ask."),
        ("Hallucination", "When AI states something false as fact."),
    ]:
        w(f"- **{term}**: {meaning}")
    w("")

    w("## How the ratings work")
    w("")
    w("Each tool gets 1–5 on four things. These are this guide's judgement from the sources listed, not lab tests.")
    w("")
    w("- **Quality**: how good the results are compared with the best in its category.")
    w("- **Value**: what you get for the money, including the free tier.")
    w("- **Ease**: how quickly a non-technical person gets good results.")
    w("- **Privacy**: training defaults, opt-outs, data location (5 = stays on your device or anonymised; 1 = no real opt-out or stored where you have little legal recourse).")
    w("")
    w("The overall rating weights quality double: (2×quality + value + ease + privacy) ÷ 5.")
    w("")

    w("## How to update this database")
    w("")
    w("1. Edit `data/tools.json` (one object per tool; categories live in `data/categories.json`).")
    w("2. Set `verified` to the month you checked it (e.g. `2026-10`) and add the page you checked to `sources`.")
    w("3. If the exchange rate has moved, update `USD_TO_AUD` and `AS_OF` in `scripts/build.py`.")
    w("4. Run `python3 scripts/build.py`. It checks every entry has the required fields, then regenerates this file, the CSV and `index.html`.")
    w("")
    w("### Field reference")
    w("")
    w("| Field | Meaning |")
    w("|---|---|")
    for k, v in [
        ("status", "`active`, `paused` (new sign-ups closed), `upcoming` or `discontinued`"),
        ("pick", "Optional award label shown as the category's recommendation"),
        ("free / free_note", "Whether there's a usable free tier, and its main limit"),
        ("billing", "`monthly` (default), `yearly` or `one-off` (hardware)"),
        ("from / standard / top", "Cheapest paid, most common and most expensive individual plan in USD (`null` = none)"),
        ("aud / aud_from / au", "Published Australian prices (text, and the cheapest plan as a number); Australian availability notes"),
        ("features", "Assistants only: `yes`, `star`, `partial` or `no` for each capability"),
        ("scores", "`quality`, `value`, `ease`, `privacy`, each 1–5"),
        ("tags", "Use-case keywords that drive the picker and search"),
        ("privacy / region", "Training default and opt-out; where data is stored"),
        ("verified", "Month the details were last checked; `older` = not re-checked"),
    ]:
        w(f"| `{k}` | {v} |")
    w("")
    return "\n".join(out)


def build_csv(cats, tools, path):
    cat_name = {c["id"]: c["name"] for c in cats}
    cols = ["name", "maker", "category", "status", "pick", "free", "free_note", "billing", "from_usd", "standard_usd",
            "top_usd", "aud_published", "standard_aud_est", "au_notes", "pricing", "best_for", "strengths", "watch_out",
            "platforms", "privacy", "region", *[f"score_{k}" for k in SCORE_KEYS], "overall",
            *[f"feat_{f}" for f in FEATURES], "tags", "verified", "url", "sources"]
    with path.open("w", newline="") as fh:
        wr = csv.writer(fh)
        wr.writerow(cols)
        for t in tools:
            f = t.get("features", {})
            wr.writerow([
                t["name"], t["maker"], cat_name[t["category"]], t["status"], t.get("pick", ""),
                "yes" if t["free"] else "no", t.get("free_note", ""), t["billing"], t["from"], t["standard"], t["top"],
                t.get("aud", ""), aud_est(t["standard"]), t.get("au", ""), t["pricing"], t["best_for"], t["strengths"],
                t["watch_out"], t["platforms"], t["privacy"], t["region"], *[t["scores"][k] for k in SCORE_KEYS],
                overall(t), *[f.get(k, "") for k in FEATURES], " ".join(t["tags"]), t["verified"], t["url"],
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
