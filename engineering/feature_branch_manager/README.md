# Feature Branch Manager Agent

## What it does

- List all open feature branches with age and last commit date
- Flag branches inactive for more than 14 days
- Check for merge conflicts with the main or develop branch
- Assess merge readiness based on tests, reviews, and freshness
- Suggest branch cleanup order and merge sequencing

## Usage

```bash
python3 engineering/feature_branch_manager/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
