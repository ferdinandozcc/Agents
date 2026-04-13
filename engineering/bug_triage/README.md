# Bug Triage Agent

## What it does

- Categorize bug severity as Critical, High, Medium, or Low
- Identify the likely component and owning team
- Check for duplicate reports and link them together
- Draft a clear, reproducible bug report with steps
- Track resolution status and time-to-fix SLAs

## Usage

```bash
python3 engineering/bug_triage/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
