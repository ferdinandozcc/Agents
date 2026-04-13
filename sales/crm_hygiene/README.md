# CRM Hygiene Agent

## What it does

- Audit records for missing required fields like email and company
- Identify duplicate contacts and suggest merge candidates
- Flag deals with no activity in the last 30, 60, or 90 days
- Identify contacts with no associated account record
- Produce a data quality score and remediation report

## Usage

```bash
python3 sales/crm_hygiene/agent.py
```

## Category

`sales`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
