"""
operations/kpi_monitor/agent.py
KPI Monitor Agent — watches metrics, detects anomalies, and explains trends.
"""

import sys
import os
import json
import random
from datetime import datetime, timedelta
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import GET_CURRENT_TIME_TOOL, WRITE_FILE_TOOL, dispatch_common_tool

FETCH_METRICS_TOOL = {
    "name": "fetch_metrics",
    "description": "Fetch current KPI values for configured metrics.",
    "input_schema": {
        "type": "object",
        "properties": {
            "metric_names": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of metric names to fetch. Leave empty for all.",
            },
            "period": {"type": "string", "enum": ["today", "week", "month"], "default": "week"},
        },
        "required": [],
    },
}

DETECT_ANOMALY_TOOL = {
    "name": "detect_anomaly",
    "description": "Check if a metric value is anomalous compared to its historical baseline.",
    "input_schema": {
        "type": "object",
        "properties": {
            "metric_name": {"type": "string"},
            "current_value": {"type": "number"},
            "baseline": {"type": "number"},
            "threshold_pct": {"type": "number", "default": 20.0},
        },
        "required": ["metric_name", "current_value", "baseline"],
    },
}

SAMPLE_METRICS = {
    "DAU": {"current": 12400, "baseline": 11800, "unit": "users", "trend": "+5.1%"},
    "Revenue": {"current": 48200, "baseline": 51000, "unit": "USD", "trend": "-5.5%"},
    "Churn Rate": {"current": 2.8, "baseline": 2.1, "unit": "%", "trend": "+33%"},
    "NPS": {"current": 42, "baseline": 45, "unit": "score", "trend": "-6.7%"},
    "Support Tickets": {"current": 340, "baseline": 280, "unit": "tickets", "trend": "+21%"},
    "Conversion Rate": {"current": 3.2, "baseline": 3.1, "unit": "%", "trend": "+3.2%"},
}


class KPIMonitorAgent(BaseAgent):
    system_prompt = """You are a data analyst and operations monitor. Your job is to:

1. Fetch current KPI values
2. Compare against baselines and detect anomalies
3. Explain what's driving changes (hypothesis-based)
4. Flag metrics that need immediate attention
5. Suggest investigation steps for anomalies

Report format:
## KPI Dashboard — [Date]

### 🔴 Alerts (anomalies requiring attention)
### 🟡 Watch (trending in wrong direction)
### 🟢 On Track

For each alert, provide:
- Current vs. baseline value
- % change
- Likely explanation (hypothesis)
- Recommended action

Be specific and actionable. Prioritize by business impact."""

    tools = [FETCH_METRICS_TOOL, DETECT_ANOMALY_TOOL, GET_CURRENT_TIME_TOOL, WRITE_FILE_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "fetch_metrics":
            requested = tool_input.get("metric_names", [])
            metrics = {k: v for k, v in SAMPLE_METRICS.items() if not requested or k in requested}
            return json.dumps(metrics, indent=2)
        if tool_name == "detect_anomaly":
            current = tool_input["current_value"]
            baseline = tool_input["baseline"]
            threshold = tool_input.get("threshold_pct", 20.0)
            pct_change = ((current - baseline) / baseline) * 100
            is_anomaly = abs(pct_change) >= threshold
            return json.dumps({
                "metric": tool_input["metric_name"],
                "pct_change": round(pct_change, 1),
                "is_anomaly": is_anomaly,
                "direction": "up" if pct_change > 0 else "down",
            })
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = KPIMonitorAgent()
    console.print("[bold green]KPI Monitor Agent[/bold green]")
    response = agent.run("Run the KPI check and flag any anomalies.")
    from rich.markdown import Markdown
    console.print(Markdown(response))
