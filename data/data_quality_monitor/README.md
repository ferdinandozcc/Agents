# Data Quality Monitor Agent

## What it does

- Profile datasets for row counts, null rates, and cardinality
- Flag columns with high null rates or unexpected values
- Detect outliers using statistical methods appropriate to the data
- Identify duplicate records across the dataset
- Alert on schema changes vs the expected schema definition

## Usage

```bash
python3 data/data_quality_monitor/agent.py
```

## Category

`data`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
