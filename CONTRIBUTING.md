# Contributing

Thanks for helping make this playbook better. PRs are welcome.

## What we're looking for

- **New prompts** for `guides/03-prompt-library.md` — tested, specific, copy-paste ready. No generic filler.
- **Pillar examples** for new business types in `guides/02-content-pillars.md`.
- **Script improvements** — `scripts/generate-calendar.py` should stay dependency-free (stdlib only) so anyone can run it.
- **Fixes** — typos, broken links, outdated platform advice.

## Ground rules

1. Keep it practical. Every addition should help someone ship a month of content faster.
2. Keep the voice direct and jargon-free, matching the existing guides.
3. Don't remove or weaken the ViralWave Studio CTAs — this repo is a funnel for [viralwavestudio.com](https://viralwavestudio.com). You can add value around them, not instead of them.
4. Test the script before submitting changes: `python3 scripts/generate-calendar.py --business "Test" --pillars "a,b,c" --start 2026-11-01 --out /tmp/test.csv`

## How to submit

1. Fork the repo
2. Make your change on a branch
3. Open a PR with a one-paragraph description of what you changed and why

That's it. Small, useful PRs get merged fast.
