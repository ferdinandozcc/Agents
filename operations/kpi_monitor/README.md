# KPI Monitor Agent

Watches your key metrics, detects anomalies, explains trends in plain language, and recommends actions.

## What it does

- Fetches configured KPI values
- Compares each metric against its historical baseline
- Flags anomalies (default threshold: ±20%)
- Generates a color-coded dashboard report (🔴 Alert / 🟡 Watch / 🟢 On Track)
- Suggests hypotheses and investigation steps for anomalies

## Usage

```bash
python operations/kpi_monitor/agent.py
```

Runs automatically and produces a dashboard. Or ask interactively:
- *"Why is churn spiking this week?"*
- *"What's our conversion trend over the last month?"*

## Configuration

Replace the `SAMPLE_METRICS` dict in `agent.py` with a real data source (database query, API call, CSV, etc.).

## Tools used

| Tool | Purpose |
|---|---|
| `fetch_metrics` | Load current KPI values |
| `detect_anomaly` | Flag values outside baseline range |
| `write_file` | Save dashboard report |
