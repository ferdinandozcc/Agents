# NPS Analyzer Agent

## What it does

- Calculate NPS score from raw responses using standard formula
- Segment feedback by promoter, passive, and detractor groups
- Extract themes from open-text comments automatically
- Identify top drivers of high and low scores
- Recommend 3 targeted actions to improve NPS over time

## Usage

```bash
python3 product/nps_analyzer/agent.py
```

## Category

`product`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
