# Roadmap Assistant Agent

Helps product teams prioritize their backlog using RICE or Impact/Effort scoring, and produces a structured roadmap.

## What it does

- Accepts a list of backlog items
- Guides you through scoring each item (reach, impact, confidence, effort)
- Computes RICE or Impact/Effort scores
- Produces a prioritized roadmap table
- Flags quick wins, big bets, and traps

## Usage

```bash
python product/roadmap_assistant/agent.py
```

Example: *"Help me prioritize these 8 features for Q3: [list them]"*

## Frameworks supported

- **RICE**: (Reach × Impact × Confidence) / Effort
- **Impact/Effort**: Simple 2x2 matrix scoring
