#!/usr/bin/env python3
"""Build DATABASE.md, data/tools.csv and index.html from data/*.json.

Usage:
  python3 scripts/build.py                      # regenerate everything
  python3 scripts/build.py --fragment OUT.html  # also write the page body only
"""
import csv
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

TITLE = "The AI Price Guide"
SITE_URL = "https://tommehhs.github.io/ai-price-guide/"
DESCRIPTION = ("What every major AI tool costs in Australia: ChatGPT, Claude, Gemini, Copilot and 97 more. "
               "Plan-by-plan prices in A$, free features, usage limits and coding tools compared. Independent.")
DISCLAIMER = ("Not affiliated with, endorsed by or sponsored by any company listed. Product names and trademarks belong to their owners. Prices, plans and limits change often and may differ from what you see at checkout; always confirm on the company's own site before paying. This guide is general information only, not financial, legal or professional advice, and is provided as is without any guarantee of accuracy.")
# Update these together when refreshing prices.
AS_OF = "2 October 2026"
AS_OF_ISO = "2026-10-02"
STALE_DAYS = 60  # entries checked longer ago than this are flagged
USD_TO_AUD = 1.44  # mid-market, 2 Oct 2026 (1 AUD = 0.695 USD)
GST = 1.10

FEATURES = ["search", "research", "image", "video", "voice", "code", "files", "memory", "agent"]
MARK = {"yes": "✓", "star": "✓★", "partial": "~", "no": "✗"}
STATUS_LABEL = {"active": "", "paused": " ⏸ sign-ups paused", "discontinued": " ✖ discontinued",
                "upcoming": " ◷ coming soon"}
SCORE_KEYS = ["quality", "value", "ease", "privacy"]
BILLING_SUFFIX = {"monthly": "", "yearly": "/yr", "one-off": " once"}
RUNS_LABEL = {"terminal": "Terminal", "vscode": "VS Code", "jetbrains": "JetBrains", "other-ides": "Other IDEs",
              "own-editor": "Own editor", "desktop": "Desktop app", "web": "Web", "mobile": "Mobile"}
CODING_ABILITIES = [("multi_file", "Multi-file edits"), ("run_commands", "Runs commands & tests"),
                    ("cloud", "Cloud agents"), ("pull_requests", "Opens pull requests"), ("code_review", "Code review")]
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
        for p in t.get("plans", []):
            for k in ("name", "usd", "aud", "aud_src", "billing", "includes", "limits"):
                assert k in p, f"{t['id']} plan {p.get('name')}: missing {k}"
            assert p["aud_src"] in (None, "official"), f"{t['id']} plan {p['name']}: bad aud_src"
        t["stale"] = is_stale(t["verified"])
        if t.get("aud_from") is None:  # use the official A$ price of the cheapest paid plan, if published
            paid = [p for p in t.get("plans", []) if p["usd"] and p["usd"] == t["from"] and p["aud_src"] == "official"]
            if paid:
                t["aud_from"] = paid[0]["aud"]
    bench = json.loads((DATA / "benchmarks.json").read_text())
    bench["guide"] = json.loads((DATA / "coding_guide.json").read_text())
    return cats, tools, bench


def is_stale(verified):
    """'older' or a YYYY-MM month more than STALE_DAYS before AS_OF_ISO."""
    if verified == "older":
        return True
    checked = dt.date.fromisoformat(verified + "-28")  # assume late in the month
    return (dt.date.fromisoformat(AS_OF_ISO) - checked).days > STALE_DAYS


def plan_aud(p):
    if p["aud_src"] == "official":
        return "Free" if p["aud"] == 0 else f"A${p['aud']:,}".replace(".00", "")
    if p["usd"] == 0:
        return "Free"
    return f"≈A${aud_est(p['usd']):,} (est.)"


def plan_usd(p):
    return "Free" if p["usd"] == 0 else f"US${p['usd']:,}".replace(".00", "")


def usd(v, billing="monthly"):
    if v is None:
        return "—"
    return f"${v:,.2f}".replace(".00", "") + BILLING_SUFFIX[billing]


def aud_est(v):
    return None if v is None else round(v * USD_TO_AUD * GST)


def aud_cell(t):
    if t.get("aud_from") is not None:
        return f"A${t['aud_from']:,}".replace(".00", "")
    v = aud_est(t["from"])
    return ("Free" if t["free"] else "—") if v is None else f"≈A${v:,}{BILLING_SUFFIX[t['billing']]}"


def stars(n):
    return "●" * n + "○" * (5 - n)


def overall(t):
    s = t["scores"]
    return round((s["quality"] * 2 + s["value"] + s["ease"] + s["privacy"]) / 5, 1)


def anchor(name):
    keep = "".join(ch for ch in name.lower() if ch.isalnum() or ch in " -")
    return keep.replace(" ", "-")


def build_markdown(cats, tools, bench):
    out = []
    w = out.append
    by_cat = {c["id"]: [t for t in tools if t["category"] == c["id"]] for c in cats}
    live = [t for t in tools if t["status"] != "discontinued"]

    w(f"# {TITLE}")
    w("")
    w("What every major AI tool costs in Australia, what you get on each plan, and how much you can use it.")
    w("")
    w(f"_Last updated {AS_OF}. {len(tools)} tools across {len(cats)} categories, "
      f"{sum(1 for t in live if t['free'])} with a usable free tier._")
    w("")
    w("**Prices are in Australian dollars first.** **A$** = the company's own Australian price. **≈A$** = our estimate "
      f"for tools that charge in US dollars (US$1 = A${USD_TO_AUD}, plus 10% GST). US$ prices are shown alongside. "
      "Prices are monthly for individual plans unless marked _/yr_ (yearly) or _once_ (hardware).")
    w("")
    w(f"> **Disclaimer:** {DISCLAIMER}")
    w("")
    w("**Independent.** No sponsorships, affiliate links or paid placements. Ratings and picks are this guide's own "
      "judgement, explained in [How the ratings work](#how-the-ratings-work). Entries checked more than "
      f"{STALE_DAYS} days ago are marked _needs re-check_. AI products change monthly, so treat this as a snapshot.")
    w("")
    w("Generated from [`data/tools.json`](data/tools.json) by `scripts/build.py`. "
      "Open [`index.html`](index.html) for the interactive version with search, plan-by-plan comparison, a "
      "\"help me choose\" picker and a shortlist that totals your monthly cost. "
      "[`data/tools.csv`](data/tools.csv) opens in any spreadsheet.")
    w("")

    w("## Contents")
    w("")
    w("- [Start here: quick picks](#start-here-quick-picks)")
    w("- [Best in each category](#best-in-each-category)")
    w("- [Recent changes (2026)](#recent-changes-2026)")
    w("- [Prices in Australia](#prices-in-australia)")
    w("- [Plans in detail: what you get on each tier](#plans-in-detail-what-you-get-on-each-tier)")
    w("- [What you get free](#what-you-get-free)")
    w("- [Coding tools compared](#coding-tools-compared)")
    w("- [Coding benchmarks, explained](#coding-benchmarks-explained)")
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
        ("I only want one subscription", "ChatGPT Plus (A$30) or Claude Pro (US$20 + GST, ≈A$32). Google AI Pro (A$32.99) if you also want 5 TB storage"),
        ("I don't want to pay", "Gemini free + ChatGPT free; Gemini Notebook for study; Comet as a free agent browser"),
        ("Cheapest paid upgrade", "Google AI Plus (A$7.99) or ChatGPT Go (A$13, has ads)"),
        ("I write a lot", "Claude; Grammarly or Wispr Flow alongside"),
        ("I live in Word/Excel/Outlook", "Microsoft 365 Premium (A$33): Office, 6 TB and Copilot in one"),
        ("I'm on iPhone / Android", "Siri in iOS 27 is free and much better; on Android, Gemini is now the assistant"),
        ("Privacy matters most", "Mistral Vibe (EU), Duck.ai, Brave Leo, or LM Studio to run AI offline"),
        ("Research with sources", "Perplexity Pro; Consensus for science; Gemini Notebook for your own files"),
        ("Pictures", "ChatGPT Images (quality), Gemini Nano Banana (free), Midjourney (style), Canva (designs)"),
        ("Fix my photos", "Google Photos (free), Photoshop (serious), Topaz (upscaling)"),
        ("Video", "Veo 3.1 via Google AI (realism), Kling 3.0 (value), Runway (control)"),
        ("Music / voiceovers", "Suno Pro (US$10, ≈A$16) / ElevenLabs"),
        ("Coding", "Claude Code (in Claude Pro); GitHub Copilot Pro (US$10, ≈A$16) as the cheap option; Cursor as an editor. See [Coding tools compared](#coding-tools-compared)"),
        ("Make an app or website", "Lovable or Bolt.new (US$25, ≈A$40); Replit to host it too"),
        ("Hand off whole tasks", "ChatGPT agent if you're on Plus; Manus for long hands-off jobs"),
        ("Kids' homework help", "Khanmigo (US$4) or ChatGPT Study Mode (free)"),
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
    w("Prices from each company's Australian pricing page (GST included). Tools not listed charge in US dollars; "
      f"this guide estimates those at US$1 = A${USD_TO_AUD} + GST, and your bank may add a foreign transaction fee.")
    w("")
    w("| Tool | Australian price | Notes |")
    w("|---|---|---|")
    for t in tools:
        if t.get("aud") or t.get("au"):
            w(f"| {t['name']} | {t.get('aud', '—')} | {t.get('au', '')} |")
    w("")

    planned = [t for t in tools if t.get("plans")]
    w("## Plans in detail: what you get on each tier")
    w("")
    w("Every individual plan for the main assistants and coding tools. Limits use the company's exact numbers where "
      "published; otherwise we quote their wording and say _not published_.")
    w("")
    for t in planned:
        w(f"### {t['name']}")
        w("")
        w("| Plan | A$ / month | US$ / month | What you get | Limits |")
        w("|---|---|---|---|---|")
        for p in t["plans"]:
            inc = "<br>".join(p["includes"])
            lim = "<br>".join(p["limits"])
            name = p["name"] + (f"<br>_{p['note']}_" if p.get("note") else "")
            w(f"| **{name}** | {plan_aud(p)} | {plan_usd(p)} | {inc} | {lim} |")
        w("")
        w(f"_Checked {t['verified']}. Sources: " + ", ".join(f"[{i + 1}]({u})" for i, u in enumerate(t["sources"][:3])) + "_")
        w("")

    w("## What you get free")
    w("")
    w("The free tier of each tool above, side by side.")
    w("")
    w("| Tool | Free plan includes | Free limits |")
    w("|---|---|---|")
    for t in planned:
        free = next((p for p in t["plans"] if p["usd"] == 0), None)
        if free:
            w(f"| **{t['name']}** | {'; '.join(free['includes'])} | {'; '.join(free['limits'])} |")
        else:
            w(f"| **{t['name']}** | No free plan | — |")
    w("")

    coders = [t for t in tools if t.get("coding")]
    w("## Coding tools compared")
    w("")
    w("### Where it runs")
    w("")
    w("| Tool | " + " | ".join(RUNS_LABEL.values()) + " |")
    w("|---|" + "---|" * len(RUNS_LABEL))
    for t in coders:
        runs = t["coding"]["runs"]
        w(f"| {t['name']} | " + " | ".join("✓" if k in runs else "" for k in RUNS_LABEL) + " |")
    w("")
    w("### What the agent can do")
    w("")
    w("| Tool | " + " | ".join(lbl for _, lbl in CODING_ABILITIES) + " | Models | Context |")
    w("|---|" + "---|" * (len(CODING_ABILITIES) + 2))
    for t in coders:
        c = t["coding"]
        w(f"| {t['name']} | " + " | ".join(MARK[c[k]] for k, _ in CODING_ABILITIES) + f" | {c['models']} | {c['context']} |")
    w("")
    w("✓ yes · ~ limited, add-on or not clearly documented · ✗ no. Plan-by-plan limits are in "
      "[Plans in detail](#plans-in-detail-what-you-get-on-each-tier).")
    w("")
    w("### How usage is counted, and what happens when you run out")
    w("")
    w("| Tool | How usage is counted | When you hit the limit | Spending cap |")
    w("|---|---|---|---|")
    for t in coders:
        c = t["coding"]
        cap = {"yes": "✓ ", "unknown": "", "no": "✗ "}[c["spend_cap"]] + c["spend_cap_note"]
        w(f"| {t['name']} | {c['usage_model']} | {c['at_limit']} | {cap} |")
    w("")
    w("### Your code and privacy")
    w("")
    for tip in bench["guide"]["privacy_tips"]:
        w(f"- {tip}")
    w("")
    w("| Tool | Trains on your code? | Private option | Local / offline models |")
    w("|---|---|---|---|")
    for t in coders:
        c = t["coding"]
        w(f"| {t['name']} | {c['trains_on_code']} | {c['private_option']} | {MARK[c['local_models']]} {c['local_note']} |")
    w("")
    w("### Which coding setup is right for you?")
    w("")
    w("| You are… | Pick | Monthly cost | Why |")
    w("|---|---|---|---|")
    for g in bench["guide"]["personas"]:
        cost = g.get("aud_note") or ("Free" if g["aud"] == 0 else ("≈" if g.get("aud_est") else "") + f"A${g['aud']}")
        w(f"| **{g['who']}** | {g['pick']} | {cost} | {g['why']} |")
    w("")
    w("### Cheapest way in")
    w("")
    w("| Tool | Free tier | Cheapest paid | Heavy use |")
    w("|---|---|---|---|")
    for t in coders:
        paid = [p for p in t["plans"] if p["usd"]]
        free = next((p for p in t["plans"] if p["usd"] == 0), None)
        w(f"| {t['name']} | {'; '.join(free['limits']) if free else 'None'} | "
          f"{paid[0]['name']}: {plan_aud(paid[0])} ({plan_usd(paid[0])}) | {paid[-1]['name']}: {plan_aud(paid[-1])} ({plan_usd(paid[-1])}) |")
    w("")

    w("## Coding benchmarks, explained")
    w("")
    w("Benchmarks give a rough idea of how capable the underlying AI model is at programming. Read them with care:")
    w("")
    for n in bench["notes"]:
        w(f"- {n}")
    w("")
    kind = {"vendor": "Company-reported", "independent": "Independent", "reported": "Published results"}
    for b in bench["benchmarks"]:
        rows = sorted((r for r in bench["scores"] if r["bench"] == b["id"]), key=lambda r: -r["score"])
        w(f"### {b['name']}")
        w("")
        w(f"_{b['plain']}_")
        w("")
        w("| Model | Maker | Score | Source type |")
        w("|---|---|---|---|")
        for r in rows:
            w(f"| {r['model']} | {r['maker']} | {r['score']}% | [{kind[r['type']]}]({r['source']}) |")
        w("")
    w(f"_Scores as of {bench['as_of']}._")
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
        w("| Tool | Free? | From (A$) | From (US$) | Typical (US$) | Top (US$) | Rating | Best for |")
        w("|---|---|---|---|---|---|---|---|")
        for t in items:
            name = f"[{t['name']}]({t['url']}){STATUS_LABEL[t['status']]}"
            if t.get("pick"):
                name += f" 🏅 _{t['pick']}_"
            b = t["billing"]
            rating = "—" if t["status"] == "discontinued" else f"{overall(t)}/5"
            if t["stale"] and t["status"] != "discontinued":
                name += " ⚠ _needs re-check_"
            w(f"| {name} | {'✓' if t['free'] else '✗'} | {aud_cell(t)} | {usd(t['from'], b)} | {usd(t['standard'], b)} | "
              f"{usd(t['top'], b)} | {rating} | {t['best_for']} |")
        w("")
        w("<details><summary>Details for each tool</summary>")
        w("")
        for t in items:
            tag = " _(needs re-check)_" if t["stale"] else ""
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
    w("No company pays to be included, rated or picked, and there are no affiliate links.")
    w("")

    w("## How to update this database")
    w("")
    w("1. Edit `data/tools.json` (one object per tool; categories live in `data/categories.json`).")
    w("2. Set `verified` to the month you checked it (e.g. `2026-10`) and add the page you checked to `sources`.")
    w("3. If the exchange rate has moved, update `USD_TO_AUD`, `AS_OF` and `AS_OF_ISO` in `scripts/build.py`.")
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
        ("verified", f"Month the details were last checked (`YYYY-MM`); flagged _needs re-check_ after {STALE_DAYS} days"),
        ("plans", "Optional list of plan tiers: `name`, `usd`, `aud` (with `aud_src: official`, or `null` to estimate), `includes`, `limits`"),
        ("coding", "Coding tools only: where it runs, agent abilities (`yes` / `partial` / `no`), models, context"),
    ]:
        w(f"| `{k}` | {v} |")
    w("Coding benchmark scores live in `data/benchmarks.json`.")
    w("")
    w("## Disclaimer")
    w("")
    w(DISCLAIMER)
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


ICON = ("data:image/svg+xml," + __import__("urllib.parse").parse.quote(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1b5e8c"/>'
    '<text x="32" y="43" font-family="Arial,Helvetica,sans-serif" font-size="28" font-weight="700" fill="#fff" '
    'text-anchor="middle">A$</text></svg>'))


def h(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def tool_from_text(t):
    """Short 'from' price, A$ first."""
    if t["status"] == "discontinued":
        return "Discontinued"
    if t.get("aud_from") is not None:
        return f"A${t['aud_from']:g}"
    if t["from"] is None:
        return "Free" if t["free"] else "Pay as you go"
    return f"≈A${aud_est(t['from'])}{BILLING_SUFFIX[t['billing']]}"


def build_tool_pages(cats, tools, bench):
    out_dir = ROOT / "tools"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("*.html"):
        old.unlink()
    tpl = (ROOT / "scripts" / "tool_page.html").read_text()
    cat = {c["id"]: c for c in cats}
    month = dt.date.fromisoformat(AS_OF_ISO).strftime("%B %Y")
    for t in tools:
        c = cat[t["category"]]
        frm = tool_from_text(t)
        free = "free plan available" if t["free"] else "no free plan"
        title = f"{t['name']} price in Australia ({month}): plans, limits & free tier | The AI Price Guide"
        if t["status"] == "discontinued":
            title = f"{t['name']} has been discontinued ({month}) | The AI Price Guide"
        desc = (f"{t['name']} costs {frm.lower() if frm == 'Free' else 'from ' + frm} a month in Australia ({free}). "
                f"{t['best_for']}. Every plan, usage limits, privacy and alternatives, checked {t['verified']}.")[:300]
        facts = [("From", frm), ("Free plan", "Yes" if t["free"] else "No")]
        if t["status"] != "discontinued":
            facts.append(("Rating", f"{overall(t)}/5"))
        facts.append(("Checked", t["verified"] if t["verified"] != "older" else "needs re-check"))
        facts_html = '<div class="facts">' + "".join(f"<div><span>{k}</span><b>{h(v)}</b></div>" for k, v in facts) + "</div>"
        b = []
        if t.get("pick"):
            b.append(f'<p><span class="award">★ {h(t["pick"])} · {h(c["name"])}</span></p>')
        if t["status"] != "active":
            b.append(f'<p class="warn">{h(STATUS_LABEL[t["status"]].strip())}: {h(t["watch_out"])}</p>')
        if t.get("plans"):
            b.append("<h2>Every plan</h2>")
            b.append('<div class="tbl"><table><thead><tr><th>Plan</th><th>A$ / month</th><th>US$</th><th>What you get</th><th>Limits</th></tr></thead><tbody>')
            for p in t["plans"]:
                note = f'<p class="small">{h(p["note"])}</p>' if p.get("note") else ""
                b.append(f"<tr><td><strong>{h(p['name'])}</strong></td><td class=\"price\">{h(plan_aud(p))}</td><td class=\"price\">{h(plan_usd(p))}</td>"
                         f"<td><ul>{''.join(f'<li>{h(i)}</li>' for i in p['includes'])}</ul>{note}</td>"
                         f"<td><ul>{''.join(f'<li>{h(i)}</li>' for i in p['limits'])}</ul></td></tr>")
            b.append("</tbody></table></div>")
            b.append('<p class="small">Limits use the company\'s exact numbers where published; otherwise we quote its wording.</p>')
        else:
            b.append("<h2>Plans and prices</h2>")
            b.append(f"<p>{h(t['pricing'])}</p>")
            if t.get("aud"):
                b.append(f"<p><strong>In Australia:</strong> {h(t['aud'])}</p>")
            elif t["from"] is not None:
                b.append(f'<p class="small">Charged in US dollars. Estimated Australian cost from ≈A${aud_est(t["from"])}'
                         f'{BILLING_SUFFIX[t["billing"]]} including GST; your bank may add a foreign transaction fee.</p>')
        b.append("<h2>At a glance</h2><dl>")
        rows = [("Best for", t["best_for"]), ("Free plan", t.get("free_note") if t["free"] else "None"),
                ("Strengths", t["strengths"]), ("Watch out", t["watch_out"]), ("Australia", t.get("au")),
                ("Runs on", t["platforms"]), ("Privacy", f"{t['privacy']} (data: {t['region']})"), ("Maker", t["maker"])]
        for k, v in rows:
            if v and v != "—":
                b.append(f"<dt>{k}</dt><dd>{h(v)}</dd>")
        b.append("</dl>")
        if t.get("coding"):
            cd = t["coding"]
            b.append("<h2>For coders</h2><dl>")
            for k, v in [("Runs in", ", ".join(RUNS_LABEL[r] for r in cd["runs"])), ("Models", cd["models"]), ("Context", cd["context"]),
                         ("Usage counted", cd["usage_model"]), ("At the limit", cd["at_limit"]), ("Spending cap", cd["spend_cap_note"]),
                         ("Trains on your code?", cd["trains_on_code"]), ("Private option", cd["private_option"]), ("Local models", cd["local_note"])]:
                b.append(f"<dt>{k}</dt><dd>{h(v)}</dd>")
            b.append("</dl>")
        if t["status"] != "discontinued":
            sc = t["scores"]
            b.append("<h2>Our rating</h2><p>" + " · ".join(f"{k.title()} {sc[k]}/5" for k in SCORE_KEYS)
                     + f" → <strong>{overall(t)}/5</strong> overall</p>")
        alts = sorted((a for a in tools if a["category"] == t["category"] and a["id"] != t["id"] and a["status"] != "discontinued"),
                      key=lambda a: -overall(a))[:6]
        if alts:
            b.append(f"<h2>Alternatives in {h(c['name'])}</h2><ul class=\"alts\">"
                     + "".join(f'<li><a href="{a["id"]}.html">{h(a["name"])} · {h(tool_from_text(a))}</a></li>' for a in alts) + "</ul>")
        b.append("<h2>Sources</h2><ul class=\"small\">" + "".join(f'<li><a href="{h(u)}" rel="nofollow noopener">{h(u)}</a></li>' for u in t["sources"]) + "</ul>")
        lede = f"{t['best_for']}. From {frm} a month" if frm not in ("Free", "Discontinued", "Pay as you go") else f"{t['best_for']}."
        page = (tpl.replace("{{title}}", h(title)).replace("{{description}}", h(desc))
                .replace("{{canonical}}", f"{SITE_URL}tools/{t['id']}.html").replace("{{icon}}", ICON)
                .replace("{{category_id}}", c["id"]).replace("{{category}}", h(c["name"]))
                .replace("{{h1}}", h(f"{t['name']} price in Australia" if t["status"] != "discontinued" else f"{t['name']} (discontinued)"))
                .replace("{{lede}}", h(lede + (", " + ("with a free plan." if t["free"] else "no free plan.") if lede.endswith("month") else "")))
                .replace("{{facts}}", facts_html).replace("{{body}}", "\n  ".join(b))
                .replace("{{rate}}", str(USD_TO_AUD)).replace("{{disclaimer}}", h(DISCLAIMER)).replace("{{count}}", str(len(tools))))
        (out_dir / f"{t['id']}.html").write_text(page)
    urls = [SITE_URL] + [f"{SITE_URL}tools/{t['id']}.html" for t in tools]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                       + "".join(f"  <url><loc>{u}</loc><lastmod>{AS_OF_ISO}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")


def build_plans_csv(tools, path):
    with path.open("w", newline="") as fh:
        wr = csv.writer(fh)
        wr.writerow(["tool", "plan", "aud", "aud_source", "usd", "billing", "includes", "limits", "verified"])
        for t in tools:
            for p in t.get("plans", []):
                aud = p["aud"] if p["aud_src"] == "official" else (0 if p["usd"] == 0 else aud_est(p["usd"]))
                wr.writerow([t["name"], p["name"], aud, "official" if p["aud_src"] else "estimate", p["usd"], p["billing"],
                             "; ".join(p["includes"]), "; ".join(p["limits"]), t["verified"]])


def page_body(cats, tools, bench):
    template = (ROOT / "scripts" / "template.html").read_text()
    payload = json.dumps({"title": TITLE, "disclaimer": DISCLAIMER, "siteUrl": SITE_URL, "asOf": AS_OF, "rate": USD_TO_AUD, "gst": GST, "staleDays": STALE_DAYS,
                          "categories": cats, "tools": tools, "bench": bench},
                         ensure_ascii=False).replace("</", "<\\/")
    return template.replace("/*__DATA__*/null", payload)


def build_html(body, path):
    head = ('<!doctype html>\n<html lang="en-AU">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<meta name="description" content="{h(DESCRIPTION)}">\n'
            f'<link rel="canonical" href="{SITE_URL}">\n'
            '<meta property="og:type" content="website">\n'
            f'<meta property="og:title" content="{TITLE}">\n'
            f'<meta property="og:description" content="{h(DESCRIPTION)}">\n'
            f'<meta property="og:url" content="{SITE_URL}">\n'
            '<meta name="twitter:card" content="summary">\n'
            f'<link rel="icon" href="{ICON}">\n')
    title_end = body.index("</title>") + len("</title>")
    path.write_text(head + body[:title_end] + "\n</head>\n<body>\n" + body[title_end:] + "\n</body>\n</html>\n")


def main():
    cats, tools, bench = load()
    (ROOT / "DATABASE.md").write_text(build_markdown(cats, tools, bench))
    build_csv(cats, tools, DATA / "tools.csv")
    build_plans_csv(tools, DATA / "plans.csv")
    body = page_body(cats, tools, bench)
    build_html(body, ROOT / "index.html")
    build_tool_pages(cats, tools, bench)
    # Optional: page body only (no <html>/<head>), for hosts that add their own skeleton.
    if len(sys.argv) > 2 and sys.argv[1] == "--fragment":
        Path(sys.argv[2]).write_text(body)
    stale = [t["name"] for t in tools if t["stale"] and t["status"] != "discontinued"]
    print(f"Built {len(tools)} tools in {len(cats)} categories; "
          f"{sum(len(t.get('plans', [])) for t in tools)} plans; {len(stale)} need re-checking"
          + (f": {', '.join(stale)}" if stale else "."))


if __name__ == "__main__":
    main()
