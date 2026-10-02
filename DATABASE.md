# AI Tools Database for Consumers

_Last updated 2 October 2026. 77 tools across 10 categories._

Prices are monthly, in US dollars, for individual plans. The **~A$** figures are rough estimates (US$1 = A$1.44, plus 10% GST); Australian app-store and local prices often differ, so check before you buy. Rows marked _unverified_ come from older sources and weren't re-checked for this update. AI products change monthly, so treat this as a snapshot.

Generated from [`data/tools.json`](data/tools.json) by `scripts/build.py`. Open [`index.html`](index.html) for a searchable, filterable version, or [`data/tools.csv`](data/tools.csv) in a spreadsheet.

## Quick picks

| Need | Pick |
|---|---|
| Best all-rounder | ChatGPT Plus ($20) or Claude Pro ($20) |
| Best value bundle | Google AI Pro ($19.99): Gemini plus storage, Veo video and Gemini Notebook |
| Best free assistant | Gemini free tier; DeepSeek for free reasoning (data stored in China) |
| Cheapest paid assistant | Google AI Plus ($4.99) or ChatGPT Go ($8, has ads) |
| Writing & long documents | Claude |
| Research with sources | Perplexity Pro; Gemini Notebook for your own documents |
| Microsoft Office user | Microsoft 365 Premium ($19.99) — Office, 6 TB and Copilot |
| Privacy first | Mistral Vibe (EU-hosted), Duck.ai, Brave Leo; Claude with training switched off |
| Images | ChatGPT Images 2.5 (quality), Nano Banana (free/fast), Midjourney (style), Ideogram (text) |
| Video | Veo 3.1 via Google AI (realism), Kling 3.0 (value), Runway (control) |
| Music | Suno Pro ($10) |
| Voiceovers | ElevenLabs |
| Coding | Claude Code (in Claude Pro), GitHub Copilot Pro ($10) as the cheap option, Cursor as an editor |
| Build an app without coding | Lovable or Bolt.new ($25); Replit to host it too |
| AI browser | Comet (free agent); Chrome or Edge if you won't switch |
| Meeting notes | Granola (no bot), Plaud (in-person, needs device) |

## Recent changes worth knowing (2026)

- **OpenAI Sora is gone** — app closed 26 Apr 2026, API 24 Sep 2026. ChatGPT no longer makes video.
- **ChatGPT Atlas browser shut down** 9 Aug 2026; use the ChatGPT Chrome extension instead.
- **ChatGPT Pro now has $100, $200 and $500 tiers**; $200 closed to new sign-ups since 10 Sep 2026. Free and Go show ads.
- **Google AI Ultra cut from $249.99 to $99.99** (5x limits); old top tier now $199.99 (20x). AI Plus cut to $4.99.
- **NotebookLM is now Gemini Notebook** (Jul 2026).
- **Siri rebuilt on Gemini-based models** in iOS 27 (14 Sep 2026).
- **Meta launched Muse**, an errand-running agent, free with $20/$100 tiers (US, Sep 2026).
- **Le Chat is now Mistral Vibe**; **Windsurf is now Devin Desktop**.
- **Microsoft Copilot** dropped consumer Deep Research and moved advanced features to usage-based billing (Sep 2026).
- **GitHub Copilot** switched to per-token AI Credits (1 Jun 2026).
- **Kimi** paused new paid subscriptions (20 Jul 2026) due to compute limits.
- **Suno lost a German copyright (GEMA) case**; Udio paused downloads while moving to licensed models.

## Contents

- [General AI assistants](#general-ai-assistants) (13)
- [Search & research](#search--research) (5)
- [Image generation & editing](#image-generation--editing) (11)
- [Video generation](#video-generation) (12)
- [Music, voice & dictation](#music-voice--dictation) (5)
- [Coding assistants](#coding-assistants) (9)
- [No-code app & website builders](#no-code-app--website-builders) (5)
- [AI browsers](#ai-browsers) (7)
- [Writing, notes & meetings](#writing-notes--meetings) (7)
- [Phone & home assistants](#phone--home-assistants) (3)
- [Privacy at a glance](#privacy-at-a-glance)
- [How to update this database](#how-to-update-this-database)

## General AI assistants

_Chatbots you talk to for almost anything: questions, writing, planning, files, images._

### Feature matrix

| Service | Search | Research | Image | Video | Voice | Code | Files | Memory | Agent |
|---|---|---|---|---|---|---|---|---|---|
| ChatGPT | ✓ | ✓ | ✓★ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Claude | ✓ | ✓ | ✗ | ✗ | ✓ | ✓★ | ✓★ | ✓ | ✓ |
| Gemini | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Grok | ✓★ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ~ |
| Perplexity | ✓★ | ✓★ | ✓ | ~ | ✓ | ✗ | ✓ | ✓ | ✓ |
| Microsoft Copilot | ✓ | ~ | ✓ | ✗ | ✓ | ~ | ✓★ | ✓ | ✓ |
| Meta AI / Muse | ✓ | ~ | ✓ | ✓ | ✓ | ✗ | ~ | ✓ | ✓ |
| DeepSeek | ✓ | ~ | ✗ | ✗ | ~ | ✓ | ~ | ✗ | ✗ |
| Mistral Vibe (ex-Le Chat) | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Qwen | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | ✓ | ~ |
| Kimi | ✓ | ✓ | ~ | ✗ | ~ | ✓ | ✓ | ~ | ✓ |

✓ yes · ~ limited · ✗ no · ★ standout. _Agent_ = can carry out multi-step tasks for you (browse, book, fill forms).

### Prices

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [ChatGPT](https://chatgpt.com) | OpenAI | ✓ | $8 | $20 | $500 | ~A$32 | All-rounder: writing, images, agents, voice |
| [Claude](https://claude.ai) | Anthropic | ✓ | $20 | $20 | $200 | ~A$32 | Long writing, coding, documents and agent tasks |
| [Gemini](https://gemini.google.com) | Google | ✓ | $4.99 | $19.99 | $199.99 | ~A$32 | Google Workspace / Android users; best value bundle |
| [Grok](https://grok.com) | xAI | ✓ | $8 | $30 | $300 | ~A$48 | Live X/Twitter news; video with sound |
| [Perplexity](https://www.perplexity.ai) | Perplexity AI | ✓ | $20 | $20 | $200 | ~A$32 | Researching with citations |
| [Microsoft Copilot](https://copilot.microsoft.com) | Microsoft | ✓ | $9.99 | $19.99 | $19.99 | ~A$32 | Word, Excel, PowerPoint and Outlook users |
| [Meta AI / Muse](https://muse.ai) | Meta | ✓ | $20 | $20 | $100 | ~A$32 | Casual use inside WhatsApp/Instagram; everyday errands |
| [DeepSeek](https://chat.deepseek.com) | DeepSeek | ✓ | — | — | — | — | Free strong reasoning and maths |
| [Mistral Vibe (ex-Le Chat)](https://chat.mistral.ai) | Mistral AI | ✓ | $5.99 | $14.99 | $29.99 | ~A$24 | Privacy-minded users wanting a cheaper all-rounder |
| [Qwen](https://chat.qwen.ai) | Alibaba | ✓ | — | — | — | — | Free reports, slides and coding |
| [Kimi](https://www.kimi.com) ⏸ sign-ups paused | Moonshot AI | ✓ | $19 | $19 | $199 | ~A$30 | Long documents and agentic slides/research (free tier) |
| [Poe](https://poe.com) | Quora | ✓ | $5 | $20 | $250 | ~A$32 | Trying many models (GPT, Claude, Gemini, Grok, image/video) in one app |
| [Duck.ai](https://duck.ai) | DuckDuckGo | ✓ | $9.99 | $9.99 | $9.99 | ~A$16 | Private, anonymous chat |

<details><summary>Details for each tool</summary>

**ChatGPT**
- Plans: Go $8 (ads) · Plus $20 · Pro $100 / $200 / $500 (Pro $200 closed to new sign-ups since 10 Sep 2026) · Business $25/seat · Free: GPT-6 Luna; ads in the US and 31 European markets
- Strengths: GPT-6 family (Astra, Sol, Luna); Images 2.5 is the top-ranked image model; agent mode; Codex for coding included; biggest app ecosystem
- Watch out: No video since Sora shut down (app Apr 2026, API 24 Sep 2026); agent mode capped at 40 msgs/month on Plus; ChatGPT Atlas browser shut down Aug 2026
- Platforms: Web, Windows, macOS, iOS, Android, Chrome extension
- Privacy: Trains on chats by default; one-tap opt-out ('Improve the model for everyone'); Temporary Chat not used for training (data region: US)

**Claude**
- Plans: Pro $20 ($17/mo annual) · Max 5x $100 · Max 20x $200 · Team $25 / Premium $125 per seat · Free: Daily caps; the strictest free limits of the big three
- Strengths: Claude Opus 5.5 and Fable 5.1; Claude Code included from Pro; Docs, Slides and Design built into chats; lowest hallucination rate in several reviews; ad-free
- Watch out: No native image or video generation; no budget tier below $20
- Platforms: Web, Windows, macOS, iOS, Android, Chrome extension
- Privacy: You choose whether chats train models; with training off, deleted chats are gone within 30 days (data region: US)

**Gemini**
- Plans: AI Plus $4.99 (400 GB) · AI Pro $19.99 (storage + Veo) · AI Ultra $99.99 (5x, 20 TB, YouTube Premium) · Ultra $199.99 (20x) · Free: Most generous free tier; Gemini Flash with search, image generation
- Strengths: Nano Banana image editing; Veo and Gemini Omni video; Gemini Notebook (ex-NotebookLM); Google storage bundled; now powers Siri on iOS 27
- Watch out: Chats reviewed by humans and kept up to 3 years unless you turn activity off; agent features often US-only first
- Platforms: Web, Windows app, Android, iOS, Chrome, Workspace
- Privacy: Trains by default with human review; turn off 'Keep Activity' to stop (data region: US)

**Grok**
- Plans: X Premium $8 · SuperGrok Lite $10 · SuperGrok $30 · Plus $100 · Heavy $300 (annual ~17% off) · Free: Basic chat; no image/video generation since Mar 2026
- Strengths: Real-time X data; Grok Imagine 1080p video with audio; Grok 4.7 (Sep 2026)
- Watch out: Priciest standard tier ($30); xAI hasn't said which tier gets Grok 4.7; trails rivals on reasoning benchmarks
- Platforms: Web, iOS, Android, inside X
- Privacy: Trains by default, including on public X posts; opt-out in settings (data region: US)

**Perplexity**
- Plans: Pro $20 ($200/yr) · Max $200 ($2,000/yr) · Enterprise Pro $40/seat · Free: 3 Pro searches/day; 1 Research query/month
- Strengths: Every answer cited; pick between frontier models (GPT, Claude, Gemini); Labs for sheets/dashboards; Comet browser free for all; Perplexity Health
- Watch out: Moved to weekly usage limits; Computer credits mostly on Max; not great as a general creative chatbot
- Platforms: Web, Windows, macOS, iOS, Android, Comet browser
- Privacy: 'AI data retention' on by default; switch off in settings (data region: US)

**Microsoft Copilot**
- Plans: M365 Personal $9.99 · Family $12.99 · M365 Premium $19.99 (Office + 6 TB) · Code/Autopilot usage-based from Sep 2026 · Free: Free chat, image and voice
- Strengths: Built into Office and Windows; Premium bundles Office + storage for the same $20; new Code and Autopilot (always-on agents) sections
- Watch out: Consumer Deep Research, podcasts and group chats removed Aug 2026; usage-based billing for advanced features is new and hard to predict
- Platforms: Windows, web, iOS, Android, Edge, Office apps
- Privacy: Opt-out toggle for model training on conversations (data region: US)

**Meta AI / Muse**
- Plans: Free · Muse Power $20 · Muse Maximum $100 (more agent usage) · Free: Free in WhatsApp, Instagram, Messenger and the Muse app
- Strengths: Muse agent (Sep 2026) books appointments, fills forms; Muse Spark model; Vibes video; already in apps you use
- Watch out: Muse agent US-only at launch; weakest privacy controls of the majors; least suited to serious work
- Platforms: WhatsApp, Instagram, Messenger, web, iOS, Android, Ray-Ban glasses
- Privacy: No meaningful conversation-level training opt-out for US users (data region: US)

**DeepSeek**
- Plans: Free app and web; developers pay per token (API) · Free: Completely free, no message cap
- Strengths: V4-Pro and V4-Flash; 1M-token context; three thinking-effort levels
- Watch out: No image generation; voice only in limited testing; data stored in China; censors politically sensitive topics
- Platforms: Web, iOS, Android
- Privacy: Data stored in China; trains on inputs; limited user controls (data region: China)

**Mistral Vibe (ex-Le Chat)**
- Plans: Student $5.99 · Pro $14.99 (€17.99) · Team €29.99/seat · Free: Generous free tier
- Strengths: EU-hosted; Work Mode and Code Mode in one agent; deep research, voice, 100+ connectors; cheapest full-featured paid tier
- Watch out: Models a step behind the US frontier; no video
- Platforms: Web, iOS, Android
- Privacy: EU (GDPR) hosting; training opt-out available (data region: EU)

**Qwen**
- Plans: Free · Free: Free
- Strengths: Capable Qwen 3.8 models; deep research, image, slides; Wan video models from the same lab
- Watch out: Integrations mostly China-based (Taobao, Alipay, Amap); data stored in China
- Platforms: Web, iOS, Android
- Privacy: Data stored in China (data region: China)

**Kimi** ⏸ sign-ups paused
- Plans: Plus / Pro / Max / Ultra $19–$199 (new subscriptions paused since 20 Jul 2026) · Free: Free 'Adagio' tier
- Strengths: Kimi K3 (Jul 2026), strong at agentic tasks and long context
- Watch out: New paid sign-ups paused due to compute shortage; data stored in China
- Platforms: Web, iOS, Android
- Privacy: Data stored in China (data region: China)

**Poe** _(unverified)_
- Plans: Points-based subscriptions from about $5 to $250/month · Free: Daily points
- Strengths: One subscription for dozens of models and image/video generators
- Watch out: Points burn fast on top models; fewer features than each vendor's own app
- Platforms: Web, iOS, Android, desktop
- Privacy: Data passes to each model provider (data region: US)

**Duck.ai** _(unverified)_
- Plans: Free · higher limits/models with DuckDuckGo subscription (~$9.99) · Free: Free, no account
- Strengths: No account; chats anonymised and not used for training
- Watch out: Smaller models on free tier; few features (no agents, limited files)
- Platforms: Web, DuckDuckGo browser
- Privacy: Anonymised; providers contractually barred from training on chats (data region: US)

</details>

## Search & research

_Tools built around finding, citing and working through sources._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [Gemini Notebook (ex-NotebookLM)](https://notebooklm.google.com) | Google | ✓ | $4.99 | $19.99 | $199.99 | ~A$32 | Studying and summarising your own documents; audio overviews |
| [Google AI Mode](https://www.google.com/search?udm=50) | Google | ✓ | — | — | — | — | Quick answers with links without leaving Google |
| [Kagi Assistant](https://kagi.com/assistant) | Kagi | ✗ | $10 | $25 | $25 | ~A$40 | Ad-free search with access to multiple frontier models |
| [Consensus](https://consensus.app) | Consensus | ✓ | $15 | $15 | $15 | ~A$24 | What do peer-reviewed studies actually say? |
| [Elicit](https://elicit.com) | Elicit | ✓ | $12 | $12 | $49 | ~A$19 | Literature reviews and extracting data from papers |

<details><summary>Details for each tool</summary>

**Gemini Notebook (ex-NotebookLM)**
- Plans: Free · higher limits via Google AI Plus/Pro/Ultra · Free: Free with a Google account
- Strengths: Answers only from your sources; podcasts, video overviews, 11 output formats; runs code in a cloud computer
- Watch out: Renamed Jul 2026; compute-based limits since 2 Sep 2026
- Platforms: Web, iOS, Android
- Privacy: Google says uploads aren't used to train models (data region: US)

**Google AI Mode** _(unverified)_
- Plans: Free (higher limits with Google AI Pro/Ultra) · Free: Free in Google Search
- Strengths: Free, fast, uses Google's index; follow-up questions
- Watch out: Less transparent citations than Perplexity; ads
- Platforms: Web, Google app, Chrome
- Privacy: Tied to Google account activity settings (data region: US)

**Kagi Assistant** _(unverified)_
- Plans: Assistant included with Kagi Ultimate (~$25); search plans from ~$10
- Strengths: No ads, no tracking; choose GPT, Claude, Gemini and others
- Watch out: Paid only; a niche product
- Platforms: Web, iOS, Android, browser extensions
- Privacy: Doesn't train on or sell data (data region: US)

**Consensus** _(unverified)_
- Plans: Free · Pro ~$15/month · Free: Limited Pro searches
- Strengths: Searches 200M+ academic papers; 'consensus meter' on yes/no questions
- Watch out: Academic sources only
- Platforms: Web

**Elicit** _(unverified)_
- Plans: Free · Plus ~$12 · Pro ~$49 · Free: Basic plan
- Strengths: Systematic-review workflows, tables across many papers
- Watch out: Overkill for everyday questions
- Platforms: Web

</details>

## Image generation & editing

_Make or edit pictures from a text description or a reference photo._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [ChatGPT Images 2.5](https://chatgpt.com/images) | OpenAI | ✓ | $8 | $20 | $200 | ~A$32 | Best overall image quality and prompt-following |
| [Nano Banana 2 / Pro (Gemini)](https://gemini.google.com) | Google | ✓ | $4.99 | $19.99 | $199.99 | ~A$32 | Fast photo edits and realistic images; best free option |
| [Midjourney V8.2](https://www.midjourney.com) | Midjourney | ✗ | $10 | $30 | $120 | ~A$48 | Art direction, mood and distinctive style |
| [Ideogram 4.0](https://ideogram.ai) | Ideogram | ✓ | $20 | $20 | $20 | ~A$32 | Posters, logos, packaging — anything with text |
| [Adobe Firefly](https://firefly.adobe.com) | Adobe | ✓ | $9.99 | $19.99 | $19.99 | ~A$32 | Photoshop/Express users; commercially safe output |
| [FLUX.2](https://bfl.ai) | Black Forest Labs | ✗ | — | — | — | — | Tinkerers, local generation, editing with references |
| [Grok Imagine](https://grok.com/imagine) | xAI | ✗ | $10 | $30 | $300 | ~A$48 | Quick concept batches and short video with sound |
| [Krea](https://www.krea.ai) | Krea | ✓ | $9 | $9 | — | ~A$14 | One workspace for many image and video models |
| [Leonardo.ai](https://leonardo.ai) | Canva | ✓ | $10 | $24 | $60 | ~A$38 | Game art and consistent characters |
| [Canva AI](https://www.canva.com/ai) | Canva | ✓ | $15 | $15 | — | ~A$24 | Social posts, presentations and designs with AI help |
| [Recraft](https://www.recraft.ai) | Recraft | ✓ | $12 | $12 | — | ~A$19 | Icons, vector illustrations and brand assets |

<details><summary>Details for each tool</summary>

**ChatGPT Images 2.5**
- Plans: Included in ChatGPT plans · Free: Limited daily images
- Strengths: #1 on LMArena text-to-image (Sep 2026); accurate text in images; precise edits by chat
- Watch out: Slower than Nano Banana; strict content rules
- Platforms: ChatGPT apps
- Privacy: As ChatGPT (data region: US)

**Nano Banana 2 / Pro (Gemini)**
- Plans: Free · more with Google AI plans · Free: Free in the Gemini app
- Strengths: Most convincing photoreal output in tests; consistent characters; 4–30 s per image
- Watch out: Visible/invisible SynthID watermark
- Platforms: Gemini apps, Google Photos, Firefly, many third-party apps
- Privacy: As Gemini (data region: US)

**Midjourney V8.2**
- Plans: Basic $10 · Standard $30 · Pro $60 · Mega $120
- Strengths: Best aesthetics; personalisation learns your taste; instruction-based edit model (Aug 2026); video mode
- Watch out: No free tier; no public API; less literal with prompts
- Platforms: Web, Discord
- Privacy: Images public by default unless Pro/Mega Stealth mode (data region: US)

**Ideogram 4.0**
- Plans: Free · Plus $20 · Free: Weekly slow credits
- Strengths: Best typography and layout; open-weights option
- Watch out: Less photoreal than Nano Banana / ChatGPT
- Platforms: Web, iOS
- Privacy: Free-tier images public (data region: US)

**Adobe Firefly**
- Plans: Standard $9.99 (2,000 credits) · Pro $19.99 · included in Creative Cloud · Free: Limited daily generations
- Strengths: Firefly Image 5 (4 MP) trained on licensed data; also runs Nano Banana, FLUX, Veo; video too
- Watch out: Partner models cost more credits
- Platforms: Web, Photoshop, Express, iOS, Android
- Privacy: Adobe says customer content isn't used to train Firefly (data region: US)

**FLUX.2**
- Plans: Pay per image (~$0.07 for Max); open-weight versions free to run locally
- Strengths: Open-weight models run on your own PC; multi-reference editing up to 4 MP
- Watch out: No first-party consumer app worth recommending; use via Krea, Firefly, Leonardo etc.
- Platforms: API, local, third-party apps
- Privacy: Fully private when run locally (data region: EU)

**Grok Imagine**
- Plans: Included in SuperGrok plans
- Strengths: Fast; image + 1080p video with voice; seven-reference scene control
- Watch out: Looser content moderation has caused controversy
- Platforms: Grok apps, X
- Privacy: As Grok (data region: US)

**Krea**
- Plans: Free · Basic $9 ($5 annual) · higher tiers · Free: 100 units/day
- Strengths: Real-time generation, upscaling, 3D, video; runs FLUX, Nano Banana, Kling, Veo
- Watch out: Credit costs vary by model
- Platforms: Web, iOS

**Leonardo.ai** _(unverified)_
- Plans: Free · paid from ~$10 · Free: Daily tokens
- Strengths: Many fine-tuned styles; owned by Canva
- Watch out: Interface busy for beginners
- Platforms: Web, iOS, Android
- Privacy: Free images public (data region: AU)

**Canva AI** _(unverified)_
- Plans: Free · Canva Pro ~$15 (more AI uses) · Free: Limited AI uses on free plan
- Strengths: AI inside a full design tool; templates; Australian company
- Watch out: Not the best raw image model
- Platforms: Web, Windows, macOS, iOS, Android
- Privacy: Training opt-out in settings (data region: AU)

**Recraft** _(unverified)_
- Plans: Free · paid from ~$12 · Free: Daily credits
- Strengths: Exports real SVG vectors; brand style consistency
- Watch out: Less suited to photos
- Platforms: Web
- Privacy: Free images public (data region: US)

</details>

## Video generation

_Short clips from text or images, plus talking-avatar video._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [Google Veo 3.1 / Flow](https://labs.google/flow) | Google | ✗ | $19.99 | $19.99 | $199.99 | ~A$32 | Cinematic realism with native sound |
| [Kling 3.0](https://kling.ai) | Kuaishou | ✓ | $10 | $37 | $180 | ~A$59 | Realistic people and motion at a good price |
| [Runway Gen-4.5](https://runwayml.com) | Runway | ✓ | $15 | $35 | $95 | ~A$55 | Hands-on filmmaking control and editing |
| [Seedance 2.5 (Dreamina / CapCut)](https://dreamina.capcut.com) | ByteDance | ✓ | $5 | $11 | $70 | ~A$17 | Ads and reference-heavy scenes; longest single clips |
| [Luma Dream Machine (Ray 3.2)](https://lumalabs.ai) | Luma AI | ✓ | $30 | $30 | $300 | ~A$48 | Fast brainstorming; HDR output |
| [Pika 2.5](https://pika.art) | Pika | ✓ | $10 | $10 | — | ~A$16 | Fun effects for TikTok/Reels |
| [Hailuo / MiniMax H3](https://hailuoai.video) | MiniMax | ✓ | $10 | — | — | — | Cheap, fast clips with sound |
| [Higgsfield](https://higgsfield.ai) | Higgsfield | ✗ | $9 | $43 | $129 | ~A$68 | Many video models under one subscription; ads and UGC-style clips |
| [OpenArt](https://openart.ai) | OpenArt | ✓ | $14 | $34 | $56 | ~A$54 | Telling a story across many shots with the same characters |
| [HeyGen](https://www.heygen.com) | HeyGen | ✓ | $29 | $29 | — | ~A$46 | Talking-avatar videos of you; translating videos |
| [Synthesia](https://www.synthesia.io) | Synthesia | ✓ | $29 | $29 | — | ~A$46 | Training and explainer videos in many languages |
| [Sora](https://openai.com/sora) ✖ discontinued | OpenAI | ✗ | — | — | — | — | — |

<details><summary>Details for each tool</summary>

**Google Veo 3.1 / Flow**
- Plans: Via Google AI Pro $19.99 (limited) · full access on AI Ultra from $99.99
- Strengths: Veo 3.1 4K with synced audio; Gemini Omni Flash tops blind-vote leaderboards (Sep 2026); Flow editor
- Watch out: 8-second clips (extendable); Quality mode eats credits
- Platforms: Gemini, Flow (web), YouTube Shorts
- Privacy: As Gemini (data region: US)

**Kling 3.0**
- Plans: Standard ~$10 · Pro ~$37 · Premier ~$92 · Ultra ~$180 · Free: Daily free credits
- Strengths: Native 4K, up to 15 s, multi-shot storyboards, optional audio
- Watch out: Chinese company; queue times on free tier
- Platforms: Web, iOS, Android
- Privacy: Chinese company (data region: China)

**Runway Gen-4.5**
- Plans: Standard $15 ($12 annual) · Pro $35 · Max $95 · Free: 125 one-time credits
- Strengths: Deepest editing toolkit; also runs Seedance, Kling, Veo, Wan
- Watch out: $15 plan buys only ~52 s of Gen-4.5 video/month
- Platforms: Web, iOS

**Seedance 2.5 (Dreamina / CapCut)**
- Plans: Dreamina Standard ~$5 (promo) · Pro $11 · Max $42 · Advanced $70 · Free: Some free credits
- Strengths: 30-second clips with sound; up to 50 references; strong prompt adherence
- Watch out: ByteDance (TikTok) ownership; credit math is confusing
- Platforms: Web, CapCut, iOS, Android
- Privacy: ByteDance (data region: China/Singapore)

**Luma Dream Machine (Ray 3.2)**
- Plans: Plus $30 ($25 annual) · Pro $90 · Ultra $300 · Free: Limited monthly generations
- Strengths: Quick, good physics and skin; keyframes; HDR/EXR export
- Watch out: No native audio
- Platforms: Web, iOS

**Pika 2.5**
- Plans: Starter $10 ($8 annual) · higher tiers · Free: Free, no monthly credits
- Strengths: Quick stylised clips, effects, lip sync
- Watch out: Not for realistic or long footage
- Platforms: Web, iOS

**Hailuo / MiniMax H3**
- Plans: Free · paid from ~$10 · Free: Free credits
- Strengths: MiniMax H3 is top-4 for video with audio; open weights; quick turnaround
- Watch out: Chinese company
- Platforms: Web, iOS, Android
- Privacy: Chinese company (data region: China)

**Higgsfield**
- Plans: Basic $9 · Pro $43 ($23 annual) · Ultra $129
- Strengths: Runs Seedance, Veo, Kling and 25+ others; character consistency and camera controls
- Watch out: Aggregator markup; aggressive marketing
- Platforms: Web, iOS

**OpenArt**
- Plans: Starter $14 · Plus $34 · Pro $56 · Free: 7-day trial
- Strengths: Director mode builds videos up to 5 minutes; Seedance, Veo, Kling, Wan in one place
- Watch out: Aggregator; credits vary by model
- Platforms: Web

**HeyGen**
- Plans: Free · Creator $29 ($24 annual) · Free: 3 videos/month
- Strengths: Avatars, voice cloning and translation into 175+ languages
- Watch out: Cloning your own likeness needs care
- Platforms: Web, iOS
- Privacy: Biometric (face/voice) data (data region: US)

**Synthesia**
- Plans: Free · Starter $29 ($18 annual) · Free: 10 min/month
- Strengths: 160+ languages from one script; business-grade
- Watch out: Avatars look corporate
- Platforms: Web

**Sora** ✖ discontinued
- Plans: Discontinued
- Watch out: App and web shut 26 Apr 2026; API removed 24 Sep 2026. Use Veo, Kling or Seedance instead

</details>

## Music, voice & dictation

_Songs, voiceovers, voice cloning and speech-to-text._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [Suno v5.5](https://suno.com) | Suno | ✓ | $10 | $10 | $30 | ~A$16 | Full songs with vocals and lyrics |
| [Udio](https://www.udio.com) | Udio | ✓ | $10 | $10 | $30 | ~A$16 | Polished electronic/ambient tracks; cleanest licensing |
| [ElevenLabs](https://elevenlabs.io) | ElevenLabs | ✓ | $6 | $22 | $299 | ~A$35 | Voiceovers, audiobooks, voice cloning, licensed music |
| [AIVA](https://www.aiva.ai) | AIVA | ✓ | $15 | $15 | $49 | ~A$24 | Orchestral and film-style instrumental music |
| [Wispr Flow](https://wisprflow.ai) | Wispr | ✓ | $15 | $15 | $15 | ~A$24 | Dictating instead of typing, in any app |

<details><summary>Details for each tool</summary>

**Suno v5.5**
- Plans: Pro $10 ($8 annual) · Premier $30 ($24 annual) · Free: 50 credits/day (~10 songs), non-commercial
- Strengths: Most natural vocals; songs up to 8 min; stems; Suno Studio; voice cloning on Pro
- Watch out: Lost a German (GEMA) copyright case Jul 2026 — care with commercial release in Europe
- Platforms: Web, iOS, Android

**Udio**
- Plans: Standard $10 · Pro $30 · Free: 10 credits/day + 100/month
- Strengths: Licensing deal with UMG
- Watch out: Song downloads paused while it moves to a licensed model
- Platforms: Web, iOS

**ElevenLabs**
- Plans: Starter $6 · Creator $22 · Pro $99 · Scale $299 · Business $990 · Free: Small monthly allowance
- Strengths: Most realistic text-to-speech; voice cloning; ElevenLabs Music v2.5 cleared for commercial use; dubbing
- Watch out: Character credits run out quickly on long audio
- Platforms: Web, iOS, Android, ElevenReader app
- Privacy: Voice data is biometric — clone only your own voice (data region: US/UK)

**AIVA**
- Plans: Standard $15 · Pro $49 (full copyright) · Free: Limited rights
- Strengths: MIDI export; you own the copyright on Pro
- Watch out: No vocals
- Platforms: Web, desktop

**Wispr Flow**
- Plans: Pro $15 ($12 annual) · Free: 2,000 words/week
- Strengths: Cleans up filler words and formats as you speak; works everywhere on desktop and phone
- Watch out: Audio processed in the cloud
- Platforms: macOS, Windows, iOS, Android
- Privacy: Cloud processing; privacy mode available (data region: US)

</details>

## Coding assistants

_AI that writes, edits and reviews code in your editor or terminal._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [Claude Code](https://claude.com/product/claude-code) | Anthropic | ✗ | $20 | $20 | $200 | ~A$32 | Big multi-file changes and long agent tasks |
| [OpenAI Codex](https://openai.com/codex) | OpenAI | ✓ | $8 | $20 | $200 | ~A$32 | ChatGPT subscribers; cloud sandboxes |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub (Microsoft) | ✓ | $10 | $10 | $100 | ~A$16 | Cheapest serious option; works in any editor |
| [Cursor](https://cursor.com) | Anysphere | ✓ | $20 | $20 | $200 | ~A$32 | An AI-first editor for everyday coding |
| [Devin Desktop (ex-Windsurf)](https://devin.ai) | Cognition | ✓ | $20 | $20 | $200 | ~A$32 | Cursor alternative with Devin agent built in |
| [Kiro](https://kiro.dev) | Amazon (AWS) | ✓ | $20 | $20 | $200 | ~A$32 | Planning requirements before writing code |
| [Google Antigravity](https://antigravity.google) | Google | ✓ | $19.99 | $19.99 | $199.99 | ~A$32 | Free agent-first coding with Gemini |
| [Zed](https://zed.dev) | Zed Industries | ✓ | $10 | $10 | — | ~A$16 | Fast, lightweight editor with AI |
| [Cline / OpenCode](https://opencode.ai) | Open source | ✓ | — | — | — | — | No subscription; use any model, including local ones |

<details><summary>Details for each tool</summary>

**Claude Code**
- Plans: Included in Claude Pro $20 · Max $100/$200
- Strengths: Top of most agentic-coding benchmarks; terminal, VS Code, JetBrains, web, mobile
- Watch out: Pro limits run out fast on heavy use; Claude models only
- Platforms: Terminal, VS Code, JetBrains, web, iOS, Android
- Privacy: As Claude (data region: US)

**OpenAI Codex**
- Plans: Included in ChatGPT Go/Plus/Pro/Business · Free: Limited, with ChatGPT Free
- Strengths: GPT-6.1 Sol/Astra; open-source CLI; runs tasks in isolated cloud sandboxes
- Watch out: Usage metered per 5-hour window
- Platforms: Terminal, IDE, web, ChatGPT app
- Privacy: As ChatGPT (data region: US)

**GitHub Copilot**
- Plans: Pro $10 ($15 credits) · Pro+ $39 ($70) · Max $100 ($200) · Business $19/seat · Free: 2,000 completions + limited chat/month
- Strengths: Unlimited completions on paid plans; choose Claude, GPT, Gemini, Grok; runs Claude Code and Codex agents
- Watch out: Switched to per-token AI Credits on 1 Jun 2026 — heavy agent use can overrun
- Platforms: VS Code, JetBrains, Neovim, Xcode, CLI, github.com
- Privacy: Individuals can opt out of training (data region: US)

**Cursor**
- Plans: Pro $20 · Pro+ $60 (3x) · Ultra $200 (20x) · Teams $40/seat · Free: Hobby: limited agent + tab
- Strengths: Polished VS Code-based editor; many models; background agents; CLI
- Watch out: Usage-based overages after the included allowance
- Platforms: Windows, macOS, Linux, CLI
- Privacy: Privacy mode available (data region: US)

**Devin Desktop (ex-Windsurf)**
- Plans: Pro $20 · Max $200 · Teams $40/seat · Free: Unlimited tab, light agent quota
- Strengths: Generous free autocomplete
- Watch out: Renamed from Windsurf 2 Jun 2026
- Platforms: Windows, macOS, Linux, JetBrains plugin

**Kiro**
- Plans: Pro $20 · up to $200 · Free: 50 credits
- Strengths: Spec-driven development
- Watch out: AWS-flavoured
- Platforms: Windows, macOS, Linux

**Google Antigravity**
- Plans: Free · higher limits with Google AI plans · Free: Free with weekly compute cap
- Strengths: Multiple agents across your codebase; CLI version
- Watch out: Gemini Code Assist individual tier closed Jun 2026
- Platforms: Windows, macOS, Linux, CLI
- Privacy: As Google (data region: US)

**Zed**
- Plans: Pro $10 · Free: 2,000 edit predictions/month
- Strengths: Very fast; open source; bring your own keys
- Watch out: Smaller extension ecosystem than VS Code
- Platforms: macOS, Linux, Windows
- Privacy: Open source (data region: US)

**Cline / OpenCode**
- Plans: Free (bring your own API key or local model) · Free: Free; pay your model provider
- Strengths: Open source; provider-independent
- Watch out: API bills can exceed a flat subscription
- Platforms: VS Code (Cline), terminal (OpenCode)
- Privacy: Fully local possible (data region: —)

</details>

## No-code app & website builders

_Describe an app or site in plain English and get a working one._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [Lovable](https://lovable.dev) | Lovable | ✓ | $25 | $25 | $50 | ~A$40 | Best-looking web app prototypes |
| [Bolt.new](https://bolt.new) | StackBlitz | ✓ | $25 | $25 | $200 | ~A$40 | Fastest prompt-to-prototype |
| [Replit](https://replit.com) | Replit | ✓ | $20 | $20 | $100 | ~A$32 | Build and host an app in one place |
| [v0](https://v0.app) | Vercel | ✓ | $20 | $30 | $100 | ~A$48 | Website and UI design generation |
| [Base44](https://base44.com) | Wix | ✓ | $16 | $20 | — | ~A$32 | Cheapest capable app builder |

<details><summary>Details for each tool</summary>

**Lovable**
- Plans: Pro $25 · Business $50 · Free: 5 messages/day
- Strengths: Polished design out of the box; Supabase backend; GitHub export
- Watch out: Hosting and in-app AI now share your credit balance
- Platforms: Web

**Bolt.new**
- Plans: Pro $25 · up to $200 · Teams $30/member · Free: 1M tokens/month
- Strengths: Runs full-stack apps in the browser; export or GitHub
- Watch out: Token usage climbs fast when fixing bugs
- Platforms: Web

**Replit**
- Plans: Core $20 ($18 annual) · Pro $100 · Free: Daily agent credits, 1 published app
- Strengths: Agent builds, tests and deploys; database and hosting included
- Watch out: Effort-based agent pricing; heavy users report $100–300/month extra
- Platforms: Web, iOS, Android

**v0**
- Plans: Premium $20 · Team $30/user · Business $100/user · Free: $5 credits/month
- Strengths: Best-in-class React UI; one-click Vercel deploy
- Watch out: Front-end focused
- Platforms: Web

**Base44**
- Plans: From $16 (annual) / $20 monthly · Free: 25 messages/month
- Strengths: Backend, login and database built in
- Watch out: Web apps only
- Platforms: Web

</details>

## AI browsers

_Web browsers with an assistant built in, some able to click around for you._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [Comet](https://www.perplexity.ai/comet) | Perplexity | ✓ | — | — | — | — | Best free agentic browser |
| [Chrome with Gemini](https://www.google.com/chrome/) | Google | ✓ | $19.99 | $19.99 | $199.99 | ~A$32 | Staying on Chrome |
| [Microsoft Edge](https://www.microsoft.com/edge) | Microsoft | ✓ | — | — | — | — | Microsoft 365 users |
| [Dia](https://www.diabrowser.com) | The Browser Company (Atlassian) | ✓ | $20 | $20 | $20 | ~A$32 | Mac users who want the most polished design |
| [Brave Leo](https://brave.com/leo/) | Brave | ✓ | $14.99 | $14.99 | $14.99 | ~A$24 | Privacy first |
| [Opera Neon](https://www.operaneon.com) | Opera | ✗ | $19.90 | $19.90 | $19.90 | ~A$32 | Running several web agents at once |
| [ChatGPT Atlas](https://chatgpt.com/atlas) ✖ discontinued | OpenAI | ✗ | — | — | — | — | — |

<details><summary>Details for each tool</summary>

**Comet**
- Plans: Free (more with Perplexity Pro/Max) · Free: Free, including the agent
- Strengths: Agent clicks through sites for you; research and shopping; Mac, Windows, iOS, Android
- Watch out: Most-studied for prompt-injection attacks — don't let it near banking
- Platforms: macOS, Windows, iOS, Android
- Privacy: As Perplexity (data region: US)

**Chrome with Gemini**
- Plans: Free · 'auto browse' agent needs AI Pro/Ultra (US only) · Free: Gemini in Chrome free
- Strengths: Biggest extension ecosystem; Gemini knows your tabs
- Watch out: The agent that completes tasks is paywalled and US-only
- Platforms: Windows, macOS, Linux, Android, iOS
- Privacy: As Google (data region: US)

**Microsoft Edge**
- Plans: Free · Free: Free
- Strengths: Copilot built in: multi-tab reasoning, Journeys, voice and vision
- Watch out: Copilot Mode retired as a separate mode in May 2026; weaker at completing tasks than Comet
- Platforms: Windows, macOS, Linux, iOS, Android
- Privacy: As Microsoft (data region: US)

**Dia**
- Plans: Free · $20 for unlimited AI · Free: Free
- Strengths: Arc's sidebar and tab features with AI chat and reusable 'Skills'
- Watch out: macOS only (Windows 'coming soon')
- Platforms: macOS

**Brave Leo**
- Plans: Free · Leo Premium $14.99 · Free: Free
- Strengths: No account needed; chats not stored or used for training
- Watch out: Doesn't complete tasks for you
- Platforms: Windows, macOS, Linux, iOS, Android
- Privacy: Best in category (data region: US)

**Opera Neon**
- Plans: $19.90/month
- Strengths: Agentic tasks run in parallel
- Watch out: Only paid AI browser; desktop only
- Platforms: Windows, macOS

**ChatGPT Atlas** ✖ discontinued
- Plans: Discontinued
- Watch out: Stopped working 9 Aug 2026; replaced by the ChatGPT Chrome extension

</details>

## Writing, notes & meetings

_Grammar help, meeting notes, email and note-taking with AI._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [Grammarly](https://www.grammarly.com) | Superhuman (ex-Grammarly) | ✓ | $12 | $30 | $30 | ~A$48 | Grammar and tone everywhere you type |
| [Notion AI](https://www.notion.com/product/ai) | Notion | ✓ | $20 | $20 | — | ~A$32 | AI over your own notes, docs and wikis |
| [Granola](https://www.granola.ai) | Granola | ✓ | $14 | $14 | $35 | ~A$22 | Meeting notes without a bot joining the call |
| [Otter.ai](https://otter.ai) | Otter.ai | ✓ | $16.99 | $16.99 | $30 | ~A$27 | Live transcripts of Zoom/Teams/Meet |
| [Fathom](https://fathom.video) | Fathom | ✓ | $20 | $20 | $34 | ~A$32 | Free meeting recorder |
| [Plaud Note](https://www.plaud.ai) | Plaud | ✓ | $17.99 | $17.99 | $29.99 | ~A$28 | In-person meetings, site visits and phone calls |
| [Superhuman Mail](https://superhuman.com) | Superhuman | ✗ | $30 | $30 | $40 | ~A$48 | Email power users |

<details><summary>Details for each tool</summary>

**Grammarly**
- Plans: Pro $30 monthly or $144/yr ($12/mo) · Free: Basic grammar and spelling
- Strengths: Works in every app and browser; AI rewrites; plagiarism and AI detection
- Watch out: Monthly billing is 2.5x the annual price
- Platforms: Windows, macOS, browsers, iOS, Android
- Privacy: Says it doesn't sell data (data region: US)

**Notion AI** _(unverified)_
- Plans: Full AI included with Business (~$20/user) · Free: Limited trial
- Strengths: Search across Notion and connected apps; meeting notes; agents
- Watch out: Full AI no longer sold as a cheap add-on
- Platforms: Web, Windows, macOS, iOS, Android
- Privacy: No training on customer data (data region: US)

**Granola**
- Plans: Business $14/user · Enterprise $35/user · Free: Basic free
- Strengths: Records from your computer; you add notes, AI fills them in
- Watch out: You still need participants' consent
- Platforms: macOS, Windows, iOS, Android, web
- Privacy: No bot; audio not stored (data region: UK/US)

**Otter.ai**
- Plans: Pro $16.99 · Business $30/user · Free: Limited minutes
- Strengths: Bot joins and transcribes; searchable archive
- Watch out: Bot in meetings can annoy people
- Platforms: Web, macOS, Windows, iOS, Android

**Fathom**
- Plans: Premium $20 · Team $19 · Business $34 · Free: Generous free plan
- Strengths: Strong free tier; summaries and action items
- Watch out: Desktop only (iPhone app on waitlist)
- Platforms: macOS, Windows
- Privacy: Shows recording notice (data region: US)

**Plaud Note**
- Plans: Device from $159 · Pro $17.99 · Unlimited $29.99 · Free: 300 min/month with device
- Strengths: Pocket hardware recorder; summaries by AI
- Watch out: Requires buying the device
- Platforms: Device + iOS, Android, web, desktop
- Privacy: ISO 27001; EU storage option (data region: US/EU)

**Superhuman Mail**
- Plans: $30–33/user · Business $40
- Strengths: AI drafts in your voice; Ask AI over your inbox; very fast
- Watch out: Expensive for email
- Platforms: Web, macOS, Windows, iOS, Android

</details>

## Phone & home assistants

_Voice assistants built into your phone or smart speaker._

| Tool | Maker | Free? | Cheapest paid | Typical | Top tier | ~A$ typical | Best for |
|---|---|---|---|---|---|---|---|
| [Siri (Apple Intelligence, iOS 27)](https://www.apple.com/apple-intelligence/) | Apple | ✓ | — | — | — | — | iPhone users: actions across your apps, messages and photos |
| [Gemini on Android](https://gemini.google) | Google | ✓ | $4.99 | $19.99 | $199.99 | ~A$32 | Android users |
| [Alexa+](https://www.amazon.com/alexa-plus) | Amazon | ✗ | $19.99 | $19.99 | $19.99 | ~A$32 | Echo / smart-home households |

<details><summary>Details for each tool</summary>

**Siri (Apple Intelligence, iOS 27)**
- Plans: Free (iPhone 15 Pro or newer, M-series Macs/iPads) · Free: Free on supported devices
- Strengths: Rebuilt Siri (14 Sep 2026) on Gemini-based models; personal context, on-screen awareness, app actions
- Watch out: Third-party Siri Extensions (Claude, Gemini) not live yet; older iPhones excluded
- Platforms: iPhone, iPad, Mac
- Privacy: Apple: on-device or Private Cloud Compute (data region: US)

**Gemini on Android** _(unverified)_
- Plans: Free · Google AI plans for more · Free: Free
- Strengths: Replaces Google Assistant; Gemini Live camera/screen sharing; controls apps
- Watch out: Some old Assistant routines missing
- Platforms: Android, Wear OS, Google TV, Nest
- Privacy: As Gemini (data region: US)

**Alexa+** _(unverified)_
- Plans: Free with Amazon Prime · $19.99/month without
- Strengths: Natural conversation; books services; controls smart home
- Watch out: Limited outside the US; check availability in Australia
- Platforms: Echo devices, Alexa app, web
- Privacy: Voice recordings processed in the cloud (data region: US)

</details>

## Privacy at a glance

| Assistant | Trains on your chats? | Where data lives |
|---|---|---|
| ChatGPT | Trains on chats by default; one-tap opt-out ('Improve the model for everyone'); Temporary Chat not used for training | US |
| Claude | You choose whether chats train models; with training off, deleted chats are gone within 30 days | US |
| Gemini | Trains by default with human review; turn off 'Keep Activity' to stop | US |
| Grok | Trains by default, including on public X posts; opt-out in settings | US |
| Perplexity | 'AI data retention' on by default; switch off in settings | US |
| Microsoft Copilot | Opt-out toggle for model training on conversations | US |
| Meta AI / Muse | No meaningful conversation-level training opt-out for US users | US |
| DeepSeek | Data stored in China; trains on inputs; limited user controls | China |
| Mistral Vibe (ex-Le Chat) | EU (GDPR) hosting; training opt-out available | EU |
| Qwen | Data stored in China | China |
| Kimi | Data stored in China | China |
| Poe | Data passes to each model provider | US |
| Duck.ai | Anonymised; providers contractually barred from training on chats | US |

Turning training off stops _future_ use only. Never paste passwords, ID numbers, or client data you aren't allowed to share into any consumer chatbot.

## How to update this database

1. Edit `data/tools.json` (one object per tool; add categories in `data/categories.json`).
2. Set `verified` to the month you checked it (e.g. `2026-10`) and add the page you checked to `sources`.
3. If the exchange rate has moved, update `USD_TO_AUD` and `AS_OF` in `scripts/build.py`.
4. Run `python3 scripts/build.py` to regenerate this file, the CSV and `index.html`.

### Field reference

| Field | Meaning |
|---|---|
| `status` | `active`, `paused` (new sign-ups closed) or `discontinued` |
| `free / free_note` | Whether there's a usable free tier, and its main limit |
| `from / standard / top` | Cheapest paid, most common, and most expensive individual plan in USD/month (`null` = none) |
| `features` | Assistants only: `yes`, `star`, `partial` or `no` for each capability |
| `privacy / region` | Training default and opt-out; where the company stores data |
| `verified` | Month the details were last checked; `older` = not re-checked |

## Sources

- https://aitoolsreview.co.uk/insights/gemini-notebook
- https://aiweekly.co/learning-ai/generative-ai/best-ai-coding-tools-compared
- https://assindo.com/news/ios-27-siri-extensions-best-ai-assistant-iphone
- https://automateall.co/en/blog/mistral-le-chat-vibe/
- https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/
- https://blog.google/products/search/
- https://consensus.app/pricing/
- https://costbench.com/software/ai-productivity/superhuman/
- https://costbench.com/software/ai-voice-tools/elevenlabs/
- https://duckduckgo.com/duckduckgo-help-pages/duckai/
- https://efficient.app/best/browser
- https://elicit.com/pricing
- https://en.wikipedia.org/wiki/DeepSeek_(chatbot)
- https://felloai.com/ai-pricing-comparison/
- https://felloai.com/best-ai-music-generators/
- https://gemini.google/release-notes/
- https://higgsfield.ai/blog/best-ai-video-generators-2026
- https://kagi.com/pricing
- https://leonardo.ai/pricing
- https://openart.ai/blog/best-ai-video-generators/
- https://overchat.ai/ai-hub/best-ai-image-generators
- https://pinggy.io/blog/best_ai_tools_for_coding/
- https://poe.com
- https://releasebot.io/updates/perplexity-ai
- https://sessionwatcher.com/guides/how-much-does-cursor-cost
- https://support.claude.com/en/articles/12138966-release-notes
- https://tech-insider.org/chatgpt-vs-claude-vs-gemini-vs-grok-subscription-pricing-2026/
- https://techcrunch.com/2026/03/24/openais-sora-was-the-creepiest-app-on-your-phone-now-its-shutting-down/
- https://techcrunch.com/2026/08/13/microsoft-kills-off-unsuccessful-ai-features-while-merging-its-separate-copilot-apps/
- https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/
- https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/
- https://www.aboutamazon.com/news/devices/new-alexa-generative-artificial-intelligence
- https://www.ai-toolbox.co/grok-models/grok-pricing-plans-api-2026
- https://www.alibabacloud.com/blog/alibaba-launches-qwen-app-to-boost-its-consumer-ai-efforts_602672
- https://www.appypie.com/blog/best-ai-app-builders
- https://www.canva.com/pricing/
- https://www.cloudzero.com/blog/gemini-pricing/
- https://www.cloudzero.com/blog/perplexity-pricing/
- https://www.cnbc.com/2026/09/21/meta-muse-personal-ai-agent-downloads.html
- https://www.commercepundit.com/blog/best-ai-browsers/
- https://www.digitaltrends.com/phones/siri-ai-ios-27-launch/
- https://www.eesel.ai/blog/grammarly-pricing
- https://www.gosearch.ai/blog/microsoft-copilot-pricing/
- https://www.heise.de/en/news/Mistral-s-chatbot-is-now-called-Vibe-and-gains-new-capabilities-11311685.html
- https://www.layer3labs.io/comparisons/replit-alternatives
- https://www.layer3labs.io/guides/best-ai-video-generators
- https://www.layer3labs.io/guides/suno-explained
- https://www.meetjamie.ai/blog/best-ai-note-takers-for-students
- https://www.morphllm.com/codex-pricing
- https://www.neoteo.com/en/deepseek-tests-voice-replies-and-four-profiles-for-some-app-users
- https://www.nocode.mba/articles/github-copilot-pricing
- https://www.notion.com/pricing
- https://www.pymnts.com/news/artificial-intelligence/2026/moonshot-halts-new-kimi-k3-subscriptions-demand-overwhelms-compute/
- https://www.recraft.ai/pricing
- https://www.teamday.ai/blog/best-ai-image-models-2026
- https://www.teamday.ai/blog/best-ai-video-models-2026
- https://www.techtimes.com/articles/322670/20260802/grok-imagine-video-update-adds-1080p-voice-cloning-seven-reference-scene-control.htm
- https://www.therundown.ai/tools/codeium-windsurf
- https://www.tomsguide.com/ai/i-checked-the-privacy-settings-of-every-major-ai-chatbot-heres-how-they-actually-compare
- https://www.totalum.app/blog/replit-alternative-2026
- https://zackproser.com/blog/wisprflow-pricing-guide-2026
