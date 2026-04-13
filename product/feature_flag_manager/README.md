# Feature Flag Manager Agent

## What it does

- Inventory all active feature flags with age, owner, and rollout %
- Flag old or fully-rolled-out flags that should be cleaned up
- Track flags by environment: dev, staging, and prod
- Document the purpose and expected removal date per flag
- Alert on flags with no owner or past their sunset date

## Usage

```bash
python3 product/feature_flag_manager/agent.py
```

## Category

`product`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
