"""
operations/incident_responder/agent.py
Incident Responder Agent — guides triage, assigns owners, tracks resolution, writes post-mortems.
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

DECLARE_INCIDENT_TOOL = {
    "name": "declare_incident",
    "description": "Officially declare an incident and assign it a severity level.",
    "input_schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "description": {"type": "string"},
            "severity": {"type": "string", "enum": ["SEV1", "SEV2", "SEV3"], "description": "SEV1=critical, SEV2=major, SEV3=minor"},
            "reporter": {"type": "string"},
        },
        "required": ["title", "severity"],
    },
}

LOG_UPDATE_TOOL = {
    "name": "log_incident_update",
    "description": "Add a timestamped update to the incident log.",
    "input_schema": {
        "type": "object",
        "properties": {
            "incident_id": {"type": "string"},
            "update": {"type": "string"},
            "author": {"type": "string"},
        },
        "required": ["incident_id", "update"],
    },
}

RESOLVE_INCIDENT_TOOL = {
    "name": "resolve_incident",
    "description": "Mark an incident as resolved and capture resolution details.",
    "input_schema": {
        "type": "object",
        "properties": {
            "incident_id": {"type": "string"},
            "root_cause": {"type": "string"},
            "resolution": {"type": "string"},
            "duration_minutes": {"type": "integer"},
        },
        "required": ["incident_id", "root_cause", "resolution"],
    },
}

INCIDENTS_FILE = Path(__file__).parent / "incidents.json"


def load_incidents() -> dict:
    if INCIDENTS_FILE.exists():
        return json.loads(INCIDENTS_FILE.read_text())
    return {"incidents": {}, "counter": 0}


def save_incidents(data: dict):
    INCIDENTS_FILE.write_text(json.dumps(data, indent=2))


class IncidentResponderAgent(BaseAgent):
    system_prompt = """You are an incident response coordinator. Your role is to guide teams through incidents efficiently.

**During an active incident:**
1. Help declare and classify the incident (SEV1/2/3)
2. Suggest immediate triage steps based on the symptoms
3. Recommend who to page / notify
4. Track updates in the incident log
5. Suggest investigation commands or checks
6. Guide toward resolution

**After resolution:**
Write a post-mortem following this template:
## Post-Mortem: [Incident Title]
- **Severity**: 
- **Duration**: 
- **Impact**: 
### Timeline
### Root Cause
### Contributing Factors
### What Went Well
### What Went Wrong
### Action Items (with owners and due dates)

Keep communication clear, calm, and factual. Don't assign blame — focus on systems and processes."""

    tools = [DECLARE_INCIDENT_TOOL, LOG_UPDATE_TOOL, RESOLVE_INCIDENT_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result

        data = load_incidents()

        if tool_name == "declare_incident":
            data["counter"] += 1
            incident_id = f"INC-{data['counter']:04d}"
            data["incidents"][incident_id] = {
                "id": incident_id,
                "title": tool_input["title"],
                "description": tool_input.get("description", ""),
                "severity": tool_input["severity"],
                "reporter": tool_input.get("reporter", "unknown"),
                "declared_at": datetime.now().isoformat(),
                "status": "active",
                "updates": [],
            }
            save_incidents(data)
            return f"Incident {incident_id} declared: {tool_input['severity']} — {tool_input['title']}"

        if tool_name == "log_incident_update":
            iid = tool_input["incident_id"]
            if iid in data["incidents"]:
                data["incidents"][iid]["updates"].append({
                    "timestamp": datetime.now().isoformat(),
                    "author": tool_input.get("author", "unknown"),
                    "update": tool_input["update"],
                })
                save_incidents(data)
                return f"Update logged to {iid}."
            return f"Incident {iid} not found."

        if tool_name == "resolve_incident":
            iid = tool_input["incident_id"]
            if iid in data["incidents"]:
                data["incidents"][iid].update({
                    "status": "resolved",
                    "resolved_at": datetime.now().isoformat(),
                    "root_cause": tool_input["root_cause"],
                    "resolution": tool_input["resolution"],
                    "duration_minutes": tool_input.get("duration_minutes"),
                })
                save_incidents(data)
                return f"Incident {iid} resolved. Root cause: {tool_input['root_cause']}"
            return f"Incident {iid} not found."

        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = IncidentResponderAgent()
    console.print("[bold green]Incident Responder Agent[/bold green]")
    console.print("Describe the incident and I'll help you triage and respond.\n")
    agent.chat()
