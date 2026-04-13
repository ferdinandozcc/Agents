# ML Model Monitor Agent

## What it does

- Monitor model performance metrics over time including accuracy and AUC
- Detect concept drift and data distribution shifts
- Alert when performance drops below defined thresholds
- Diagnose the likely causes of model degradation
- Trigger retraining workflows when significant drift is confirmed

## Usage

```bash
python3 data/ml_model_monitor/agent.py
```

## Category

`data`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
