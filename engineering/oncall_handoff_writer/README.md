# On-Call Handoff Writer Agent

## What it does

- Summarize incidents from the current on-call period
- Document open issues and their current resolution status
- List pending actions and their assigned owners
- Flag anything the incoming on-call needs to watch closely
- Link to relevant runbooks and monitoring dashboards

## Usage

```bash
python3 engineering/oncall_handoff_writer/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
