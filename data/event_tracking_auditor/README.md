# Event Tracking Auditor Agent

## What it does

- Review the event tracking plan against what is actually implemented
- Flag missing events for key user flows in the product
- Identify naming inconsistencies and schema drift in events
- Check for PII appearing in event properties
- Produce a prioritized audit report with recommended fixes

## Usage

```bash
python3 data/event_tracking_auditor/agent.py
```

## Category

`data`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
