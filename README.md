# AI Comparison

A consumer's database of AI tools: what they cost, what they're good at, what to watch out for, and how they handle your data. Last updated **2 October 2026**, covering 77 tools in 10 categories:

General assistants · Search & research · Images · Video · Music, voice & dictation · Coding · No-code app builders · AI browsers · Writing, notes & meetings · Phone & home assistants

## Where to look

| File | Use it for |
|---|---|
| [DATABASE.md](DATABASE.md) | The readable guide: quick picks, 2026 changes, feature matrix, prices (US$ and ~A$), privacy table |
| [index.html](index.html) | Searchable, filterable version — open it in a browser |
| [data/tools.csv](data/tools.csv) | Open in Excel / Google Sheets |
| [data/tools.json](data/tools.json) | The source data — edit this one |

## Updating

Edit `data/tools.json`, then run:

```sh
python3 scripts/build.py
```

That regenerates `DATABASE.md`, `data/tools.csv` and `index.html`. See "How to update this database" in DATABASE.md for the field reference.
