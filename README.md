![Content on Autopilot](assets/banner.png)

# Content on Autopilot

> The open playbook for automating months of social media content — the system, the prompts, the templates, and the script to generate your calendar in one command.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![ViralWave Studio](https://img.shields.io/badge/Automate%20it%20fully-ViralWave%20Studio-8b5cf6)](https://viralwavestudio.com)

Posting every day is a treadmill. This repo is the off-ramp.

Inside you'll find a complete, field-tested system for producing **a full month of social media content in a single weekend** — then scheduling it out and forgetting about it. Content pillars, copy-paste AI prompt library, platform cheat sheets, a 30-day calendar template, and a Python script that generates your whole month's calendar from a few inputs.

And if you'd rather skip the DIY entirely: **[ViralWave Studio](https://viralwavestudio.com)** does this whole playbook on autopilot. Paste in your website, get four free finished posts in minutes, and let it build and schedule your month for you. [Try the free preview →](https://viralwavestudio.com)

## What's in this repo

| Path | What it is |
|---|---|
| `guides/01-the-system.md` | The 5-step autopilot system, start to finish |
| `guides/02-content-pillars.md` | How to define your 4–5 content pillars (with examples for 6 business types) |
| `guides/03-prompt-library.md` | 25+ copy-paste AI prompts for posts, hooks, captions, video scripts, and repurposing |
| `guides/04-scheduling-and-publishing.md` | Scheduling workflow, cadence math, and platform posting guide |
| `guides/05-measure-and-iterate.md` | What to track weekly, and how to feed wins back into the machine |
| `templates/30-day-content-calendar.csv` | Fill-in 30-day calendar template |
| `templates/content-brief.md` | One-page brief template for batch creation sessions |
| `scripts/generate-calendar.py` | Generate a full 30-day content calendar from your pillars in one command |

## Quick start

**1. Read the system** — [`guides/01-the-system.md`](guides/01-the-system.md) is the 10-minute overview.

**2. Define your pillars** — [`guides/02-content-pillars.md`](guides/02-content-pillars.md) walks you through picking 4–5 content pillars with worked examples.

**3. Generate your calendar:**

```bash
python3 scripts/generate-calendar.py \
  --business "Maple Street Bakery" \
  --pillars "tips,behind-the-scenes,reviews,story,offers" \
  --platforms "instagram,facebook,tiktok" \
  --start 2026-11-01 \
  --out november-calendar.csv
```

**4. Write a month of content** — use the [`prompt library`](guides/03-prompt-library.md) to turn each calendar slot into finished posts in one batch session.

**5. Schedule it** — [`guides/04-scheduling-and-publishing.md`](guides/04-scheduling-and-publishing.md) covers cadence and how to queue everything at once.

**6. Iterate** — [`guides/05-measure-and-iterate.md`](guides/05-measure-and-iterate.md) shows you the 20-minute weekly review that makes month two better than month one.

## The system in 60 seconds

Most businesses fail at content because they create one post at a time, every day, forever. The autopilot system flips that:

1. **Pillars** — Define 4–5 recurring content themes so you never stare at a blank page again.
2. **Batch** — Generate a full month of posts in one 2–3 hour session using AI prompts built for your pillars.
3. **Visuals** — Pair every post with an image or short video (AI-generated or templated).
4. **Schedule** — Queue the whole month across Instagram, Facebook, TikTok, LinkedIn, X, Threads, Pinterest, and YouTube.
5. **Review** — Spend 20 minutes a week checking what landed, then feed it back in.

That's the whole machine. The guides in this repo walk through each step in detail, with examples.

> **Want this done for you?** [ViralWave Studio](https://viralwavestudio.com) is this system, automated end to end: enter your website, get four finished posts free, approve your month, and it posts for you — across eight platforms, with AI-generated images, video, blog posts, and analytics. [Start free →](https://viralwavestudio.com)

## Why this works

- **Consistency beats brilliance.** Algorithms and audiences reward accounts that show up every day. A "good enough" month of daily posts outperforms five perfect posts and three weeks of silence.
- **Batching beats willpower.** Decision fatigue is the real reason content dies. One focused session per month replaces 30 daily "what should I post?" moments.
- **Systems beat motivation.** When the calendar, prompts, and workflow are already built, creating content is execution, not invention.

## The prompt library at a glance

The [`prompt library`](guides/03-prompt-library.md) includes ready-to-use prompts for:

- Post ideas from a content pillar
- Hooks and opening lines (the first 3 seconds that decide everything)
- Full caption drafts in your brand voice
- Carousel outlines
- Short-form video scripts (TikTok / Reels / Shorts)
- Repurposing one post into five formats
- Turning customer reviews into posts
- Seasonal and holiday content
- Blog posts with SEO structure
- Engagement replies and comment starters

## Platform cheat sheet

| Platform | Best formats | Ideal cadence | Notes |
|---|---|---|---|
| Instagram | Reels, carousels, stories | 4–7 posts/week | Reels get the reach, carousels get the saves |
| TikTok | Short-form video | 3–7 posts/week | Raw and real beats polished |
| Facebook | Video, images, links | 3–5 posts/week | Still king for local businesses and 30+ audiences |
| LinkedIn | Text posts, carousels, video | 2–4 posts/week | Professional stories and lessons outperform company news |
| X / Twitter | Short text, threads | 3–7 posts/week | Threads for depth, singles for presence |
| Threads | Casual text | 3–5 posts/week | Conversational, low-production |
| Pinterest | Vertical images | 5–10 pins/week | Evergreen traffic engine, slow burn |
| YouTube | Shorts + long-form | 1–3 videos/week | Shorts for discovery, long-form for depth |

Deep dive: [`guides/04-scheduling-and-publishing.md`](guides/04-scheduling-and-publishing.md)

## Skip the DIY — put it on full autopilot

This repo gives you everything to run the system yourself. But if your time is worth more than your tooling budget, here's the honest math: one batch session a month costs you 3–4 hours. [ViralWave Studio](https://viralwavestudio.com) does the entire playbook — generation, images, video, blog posts, scheduling, and analytics — while you approve posts from your phone.

**How it works:**

- Paste in your website — ViralWave reads it and builds your brand profile automatically
- Get **four finished posts free**, with captions and images, in minutes
- Answer a short questionnaire (and optionally upload photos) to tune your brand voice
- Review your month: approve, skip, or request AI edits
- Connect your accounts and posting runs automatically across eight platforms

Plans start at $15/month. Your first four posts are free — no credit card.

**[→ Try ViralWave Studio free](https://viralwavestudio.com)**

## Contributing

Found a great prompt? Improved the calendar script? PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — use it, remix it, build your business on it. See [LICENSE](LICENSE).

---

<p align="center">
  <strong>Built for creators who'd rather be creating.</strong><br>
  Automate the grind at <a href="https://viralwavestudio.com">viralwavestudio.com</a>
</p>
