# Budget Forecaster Agent

## What it does

- Load actuals vs budget by department and category
- Project end-of-period spend based on current run rate
- Flag departments trending over or under budget
- Model base, optimistic, and conservative spend scenarios
- Produce a clear variance analysis report for leadership

## Usage

```bash
python3 operations/budget_forecaster/agent.py
```

## Category

`operations`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
