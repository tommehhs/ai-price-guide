# AI Comparison

A consumer's database of AI tools: what they cost (including Australian prices), what they're good at, what to watch out for, and how they handle your data. Last updated **2 October 2026**, covering **101 tools in 18 categories**:

Assistants · Agents · Search & research · Images · Photo editing · Video · Music, voice & dictation · Slides & design · Writing, notes & meetings · Learning · Translation · Coding · App builders · AI browsers · Phone & home assistants · AI glasses · Run AI offline · Companions

## Where to look

| File | Use it for |
|---|---|
| [DATABASE.md](DATABASE.md) | The readable guide: quick picks, best in each category, 2026 changes, Australian prices, every tool's details and ratings, privacy, ways to pay less, safety tips, jargon buster |
| [index.html](index.html) | Interactive version: search and filter, **Help me choose** picker, **My shortlist** side-by-side comparison with a monthly cost total in US$ and A$ |
| [data/tools.csv](data/tools.csv) | Open in Excel / Google Sheets |
| [data/tools.json](data/tools.json) | The source data — edit this one |

## Updating

Edit `data/tools.json`, then run:

```sh
python3 scripts/build.py
```

That validates every entry and regenerates `DATABASE.md`, `data/tools.csv` and `index.html`. See "How to update this database" in DATABASE.md for the field reference.
