# SLA Monitor Agent

## What it does

- Track open tickets and requests against their SLA deadlines
- Alert when an item is within 20% of its SLA window
- Flag breached SLAs with time-over and responsible team
- Produce daily SLA compliance reports by team
- Trend SLA performance over time to identify patterns

## Usage

```bash
python3 operations/sla_monitor/agent.py
```

## Category

`operations`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
