# Pipeline Forecaster Agent

## What it does

- Score each deal's close probability based on stage and engagement
- Apply weighted pipeline math to project monthly revenue
- Identify deals at risk of slipping out of the current period
- Provide commit, best case, and pipeline revenue scenarios
- Flag forecast vs target gaps and suggest corrective actions

## Usage

```bash
python3 sales/pipeline_forecaster/agent.py
```

## Category

`sales`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
