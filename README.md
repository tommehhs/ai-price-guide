# The AI Price Guide

What every major AI tool costs in Australia, what you get on each plan, and how much you can actually use it. **101 tools in 18 categories**, with plan-by-plan breakdowns (features, free features, usage limits) for the 10 main assistants and 7 coding tools. Last updated **2 October 2026**.

**Independent:** no sponsorships, affiliate links or paid placements.

## Where to look

| File | Use it for |
|---|---|
| [index.html](index.html) | The interactive guide: browse and filter, **Compare plans**, **Coding tools**, **Help me choose**, and **My shortlist** with a monthly cost total |
| [DATABASE.md](DATABASE.md) | The written guide: quick picks, plans in detail, free features, coding comparison and benchmarks, Australian prices, privacy, ways to pay less, safety tips |
| [data/tools.csv](data/tools.csv) · [data/plans.csv](data/plans.csv) | Open in Excel / Google Sheets |
| [data/tools.json](data/tools.json) · [data/benchmarks.json](data/benchmarks.json) | The source data — edit these |

## Prices

A$ first. **A$** is the company's own Australian price; **≈A$** is an estimate for tools that bill in US dollars (US$ × 1.44 + GST). Entries checked more than 60 days ago are flagged "Needs re-check".

## Disclaimer

Not affiliated with, endorsed by or sponsored by any company listed. Product names and trademarks belong to their owners. Prices, plans and limits change often and may differ from what you see at checkout; always confirm on the company's own site before paying. This guide is general information only, not financial, legal or professional advice, and is provided as is without any guarantee of accuracy.

## Updating

Edit the files in `data/`, then run:

```sh
python3 scripts/build.py
```

That validates every entry and regenerates `DATABASE.md`, the CSVs and `index.html`, and lists anything that needs re-checking.
