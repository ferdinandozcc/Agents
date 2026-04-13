# Risk Register Manager Agent

## What it does

- Capture risks with description, category, owner, and date
- Score each risk by likelihood multiplied by impact on a 1-5 scale
- Track mitigation actions and residual risk per item
- Prioritize top risks for leadership review each week
- Flag risks with no mitigation plan or overdue actions

## Usage

```bash
python3 operations/risk_register_manager/agent.py
```

## Category

`operations`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
