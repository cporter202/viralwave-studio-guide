#!/usr/bin/env python3
"""Generate a 30-day content calendar CSV from your content pillars.

Usage:
    python3 generate-calendar.py --business "Maple Street Bakery" \\
        --pillars "behind-the-scenes,tips,offers,community,story" \\
        --platforms "instagram,facebook,tiktok" \\
        --start 2026-11-01 --out november-calendar.csv

The rotation balances pillars across the month (see guides/02-content-pillars.md):
Teach/Show carry the month, Sell stays near ~13%.
"""

import argparse
import csv
import datetime
import sys

# 30-day pillar rotation: (pillar, default format, default platforms)
ROTATION = [
    ("Teach", "Carousel", "Instagram,Facebook,LinkedIn"),
    ("Show", "Short video", "TikTok,Instagram,Facebook"),
    ("Prove", "Single image", "Instagram,Facebook"),
    ("Human", "Text post", "LinkedIn,Threads,X"),
    ("Teach", "Short video", "TikTok,Instagram,YouTube"),
    ("Show", "Single image", "Instagram,Facebook"),
    ("Sell", "Single image", "Instagram,Facebook"),
    ("Teach", "Carousel", "Instagram,LinkedIn,Pinterest"),
    ("Show", "Stories", "Instagram,Facebook"),
    ("Human", "Short video", "TikTok,Instagram"),
    ("Teach", "Text post", "LinkedIn,Threads,X"),
    ("Prove", "Carousel", "Instagram,Facebook"),
    ("Show", "Short video", "TikTok,Instagram,Facebook"),
    ("Sell", "Single image", "Instagram,Facebook,Threads"),
    ("Teach", "Blog post", "Website,Pinterest,LinkedIn"),
    ("Human", "Single image", "Instagram,Facebook"),
    ("Show", "Short video", "TikTok,Instagram,YouTube"),
    ("Teach", "Carousel", "Instagram,Facebook"),
    ("Prove", "Short video", "TikTok,Instagram,Facebook"),
    ("Human", "Text post", "LinkedIn,Threads,X"),
    ("Sell", "Short video", "TikTok,Instagram,Facebook"),
    ("Teach", "Single image", "Instagram,Pinterest"),
    ("Show", "Carousel", "Instagram,Facebook"),
    ("Prove", "Text post", "LinkedIn,X"),
    ("Teach", "Short video", "TikTok,Instagram,YouTube"),
    ("Human", "Stories", "Instagram,Facebook"),
    ("Show", "Single image", "Instagram,Facebook"),
    ("Sell", "Carousel", "Instagram,Facebook,LinkedIn"),
    ("Teach", "Text post", "Threads,X,LinkedIn"),
    ("Human", "Short video", "TikTok,Instagram,Facebook"),
]

PILLAR_BRIEFS = {
    "Teach": "Teach the audience something useful. Tip, how-to, or mistake to avoid. End with a save-worthy takeaway.",
    "Show": "Behind the scenes. Film or photograph the real process, workspace, or team. Raw and honest beats polished.",
    "Prove": "Social proof. Review, testimonial, before/after, or result. Show the transformation, name the starting point.",
    "Sell": "Offer post. Lead with the buyer outcome, include genuine urgency, one clear CTA. Keep under 120 words.",
    "Human": "Story and values. Your why, a lesson learned, community involvement. Specific and honest, no filler.",
}


# Canonical pillar order. Your --pillars list maps onto these by position:
#   1st = your Teach pillar, 2nd = Show, 3rd = Prove, 4th = Human, 5th = Sell.
CANONICAL_ORDER = ["Teach", "Show", "Prove", "Human", "Sell"]


def build_calendar(business, pillars, platforms, start, days=30):
    pillar_list = [p.strip() for p in pillars.split(",") if p.strip()]
    if len(pillar_list) < 3:
        sys.exit("error: give at least 3 pillars, comma-separated")
    platform_list = [p.strip() for p in platforms.split(",") if p.strip()]

    rows = []
    for i in range(days):
        date = start + datetime.timedelta(days=i)
        pillar, fmt, default_plats = ROTATION[i % len(ROTATION)]
        # map the canonical rotation slot onto the user's own pillar names
        user_pillar = pillar_list[CANONICAL_ORDER.index(pillar) % len(pillar_list)]
        # prefer user's platforms, fall back to rotation defaults
        plats = ",".join(platform_list[:2]) if platform_list else default_plats
        rows.append({
            "Day": i + 1,
            "Date": date.isoformat(),
            "Pillar": user_pillar,
            "Format": fmt,
            "Platforms": plats,
            "Hook": "",
            "Brief": PILLAR_BRIEFS.get(pillar, ""),
            "Visual": "",
            "Caption_Draft": "",
            "Status": "todo",
        })
    return rows


def main():
    ap = argparse.ArgumentParser(description="Generate a 30-day content calendar.")
    ap.add_argument("--business", required=True, help="Business name (used in output header comment)")
    ap.add_argument("--pillars", required=True,
                        help="Comma-separated pillar names in canonical order: "
                             "teach,show,prove,human,sell — e.g. "
                             "\"tips,behind-the-scenes,reviews,offers,story\"")
    ap.add_argument("--platforms", default="instagram,facebook,tiktok", help="Comma-separated platforms")
    ap.add_argument("--start", required=True, help="Start date YYYY-MM-DD")
    ap.add_argument("--days", type=int, default=30, help="Number of days (default 30)")
    ap.add_argument("--out", required=True, help="Output CSV path")
    args = ap.parse_args()

    try:
        start = datetime.date.fromisoformat(args.start)
    except ValueError:
        sys.exit("error: --start must be YYYY-MM-DD")

    rows = build_calendar(args.business, args.pillars, args.platforms, start, args.days)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["Day", "Date", "Pillar", "Format", "Platforms",
                                          "Hook", "Brief", "Visual", "Caption_Draft", "Status"])
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {args.days}-day content calendar for {args.business} to {args.out}")
    print("Next: fill in Hook + Caption_Draft using guides/03-prompt-library.md,")
    print("then schedule everything per guides/04-scheduling-and-publishing.md.")
    print("Or skip the DIY: https://viralwavestudio.com")


if __name__ == "__main__":
    main()
