# Churn Predictor Agent

## What it does

- Analyze account health signals including login frequency and usage
- Score each account's churn risk as high, medium, or low
- Identify the primary risk driver for each at-risk account
- Recommend targeted save actions per account
- Prioritize accounts by ARR multiplied by churn risk for impact

## Usage

```bash
python3 sales/churn_predictor/agent.py
```

## Category

`sales`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
