"""
operations/status_report/agent.py
Status Report Agent — collects updates and drafts weekly/monthly program status reports.
"""

import sys
import os
import json
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

COLLECT_UPDATES_TOOL = {
    "name": "collect_team_updates",
    "description": "Collect status updates from configured team members or projects.",
    "input_schema": {
        "type": "object",
        "properties": {
            "period": {"type": "string", "enum": ["weekly", "monthly"], "default": "weekly"},
        },
        "required": [],
    },
}

SAMPLE_UPDATES = [
    {"team": "Engineering", "update": "Shipped v2.3 release. Auth migration 80% complete. Blocked on infra sizing decision.", "rag": "amber"},
    {"team": "Design", "update": "Completed mobile onboarding flows. Started dashboard redesign. On track.", "rag": "green"},
    {"team": "Data", "update": "Pipeline latency reduced by 40%. New cohort analysis live. On track.", "rag": "green"},
    {"team": "Ops", "update": "Vendor contract renewal overdue — need sign-off. Incident playbook updated.", "rag": "red"},
]


class StatusReportAgent(BaseAgent):
    system_prompt = """You are a program manager assistant who creates clear, executive-ready status reports.

Collect updates from each team/workstream and produce a structured report:

## Weekly Status Report — [Date]

### Executive Summary
[3-4 sentence overall health summary]

### Overall Status: 🟢 / 🟡 / 🔴

### Workstream Status
| Team | Status | This Week | Blockers |
|---|---|---|---|

### Key Decisions Needed
[List of decisions that require stakeholder input]

### Risks & Issues
| Risk | Severity | Owner | Mitigation |
|---|---|---|---|

### Upcoming Milestones
[Next 2 weeks]

### Metrics Snapshot
[Link to or embed key metrics]

RAG Status: 🟢 On track | 🟡 At risk | 🔴 Off track / blocked

Be concise — this report should be readable in 3 minutes."""

    tools = [COLLECT_UPDATES_TOOL, READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "collect_team_updates":
            return json.dumps(SAMPLE_UPDATES, indent=2)
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = StatusReportAgent()
    console.print("[bold green]Status Report Agent[/bold green]")
    response = agent.run("Generate this week's status report.")
    from rich.markdown import Markdown
    console.print(Markdown(response))
