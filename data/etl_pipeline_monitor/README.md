# ETL Pipeline Monitor Agent

## What it does

- Check pipeline run status and detect failures immediately
- Flag pipelines running late against their defined SLA
- Validate row counts and data volumes against expectations
- Alert on schema changes detected in source tables
- Produce a daily pipeline health report for the team

## Usage

```bash
python3 data/etl_pipeline_monitor/agent.py
```

## Category

`data`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
