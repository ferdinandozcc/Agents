# Competitor Intel Agent

Monitors competitor websites, blogs, and changelogs to surface strategic signals and product opportunities.

## What it does

- Reads configured competitor URLs (website, blog, changelog)
- Extracts product updates, messaging shifts, and content themes
- Surfaces strategic implications — not just raw facts
- Saves a structured intel report per competitor

## Usage

```bash
python product/competitor_intel/agent.py
```

## Configuration

Edit `competitors.json` in the agent directory:

```json
{
  "competitors": [
    {
      "name": "Competitor A",
      "website": "https://...",
      "blog": "https://.../blog",
      "changelog": "https://.../changelog"
    }
  ]
}
```

## Output per competitor

- What's new
- Strategic signals
- Opportunities for us
- Watch list
