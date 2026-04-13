# Infrastructure Cost Analyzer Agent

## What it does

- Analyze cloud spend by service, team, and environment
- Identify over-provisioned resources such as oversized instances
- Flag dev and test resources left running in production configs
- Recommend reserved instance or savings plan purchases
- Project cost savings from each recommended change

## Usage

```bash
python3 engineering/infra_cost_analyzer/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
