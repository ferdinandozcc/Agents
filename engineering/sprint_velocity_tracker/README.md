# Sprint Velocity Tracker Agent

## What it does

- Track story points completed per sprint accurately
- Calculate rolling average velocity over the last 3 to 6 sprints
- Flag velocity drops and help investigate root causes
- Forecast delivery dates for roadmap items based on velocity
- Capacity plan for upcoming sprints accounting for PTO

## Usage

```bash
python3 engineering/sprint_velocity_tracker/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
