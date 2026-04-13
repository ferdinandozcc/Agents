# Deployment Monitor Agent

## What it does

- Check error rates, latency, and health endpoint status post-deploy
- Compare pre and post deploy metrics for regressions
- Flag anomalies that exceed defined rollback thresholds
- Generate a deployment health report for the team
- Recommend rollback or continue decisions with clear rationale

## Usage

```bash
python3 engineering/deployment_monitor/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
