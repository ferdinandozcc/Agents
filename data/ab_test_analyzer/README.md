# A/B Test Analyzer Agent

## What it does

- Validate experiment setup including randomization and sample ratio
- Calculate statistical significance using p-value and confidence intervals
- Measure practical significance with effect size and MDE
- Check for novelty effects and segment-level interactions
- Produce a clear ship or no-ship recommendation with rationale

## Usage

```bash
python3 data/ab_test_analyzer/agent.py
```

## Category

`data`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
