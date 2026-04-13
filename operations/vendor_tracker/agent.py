"""
operations/vendor_tracker/agent.py
Vendor & Contract Tracker — monitors renewals, SLAs, and vendor deliverables with proactive alerts.
"""

import sys
import os
import json
from datetime import datetime, timedelta
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

VENDORS_FILE = Path(__file__).parent / "vendors.json"

GET_VENDORS_TOOL = {
    "name": "get_vendors",
    "description": "Get all tracked vendors and their contract details.",
    "input_schema": {"type": "object", "properties": {}, "required": []},
}

ADD_VENDOR_TOOL = {
    "name": "add_vendor",
    "description": "Add or update a vendor in the tracker.",
    "input_schema": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "category": {"type": "string", "description": "e.g., SaaS, Infrastructure, Professional Services"},
            "contract_end_date": {"type": "string", "description": "ISO date format YYYY-MM-DD"},
            "annual_value": {"type": "number"},
            "sla_uptime_pct": {"type": "number", "default": 99.9},
            "renewal_notice_days": {"type": "integer", "default": 60},
            "owner": {"type": "string"},
            "notes": {"type": "string", "default": ""},
        },
        "required": ["name", "contract_end_date"],
    },
}

CHECK_ALERTS_TOOL = {
    "name": "check_renewal_alerts",
    "description": "Check which vendors have contracts expiring soon or SLA concerns.",
    "input_schema": {
        "type": "object",
        "properties": {
            "alert_window_days": {"type": "integer", "default": 90},
        },
        "required": [],
    },
}

DEFAULT_VENDORS = [
    {
        "name": "AWS",
        "category": "Infrastructure",
        "contract_end_date": (datetime.now() + timedelta(days=45)).strftime("%Y-%m-%d"),
        "annual_value": 120000,
        "sla_uptime_pct": 99.99,
        "renewal_notice_days": 60,
        "owner": "Engineering",
        "notes": "Enterprise agreement — negotiate reserved instances",
    },
    {
        "name": "Salesforce",
        "category": "SaaS",
        "contract_end_date": (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d"),
        "annual_value": 48000,
        "sla_uptime_pct": 99.9,
        "renewal_notice_days": 90,
        "owner": "Sales Ops",
        "notes": "Consider adding Marketing Cloud",
    },
    {
        "name": "Figma",
        "category": "SaaS",
        "contract_end_date": (datetime.now() + timedelta(days=20)).strftime("%Y-%m-%d"),
        "annual_value": 12000,
        "sla_uptime_pct": 99.5,
        "renewal_notice_days": 30,
        "owner": "Design",
        "notes": "Auto-renews — confirm seat count before renewal",
    },
]


def load_vendors() -> list:
    if VENDORS_FILE.exists():
        return json.loads(VENDORS_FILE.read_text())
    return DEFAULT_VENDORS


def save_vendors(vendors: list):
    VENDORS_FILE.write_text(json.dumps(vendors, indent=2))


class VendorTrackerAgent(BaseAgent):
    system_prompt = """You are an operations and procurement assistant managing vendor relationships and contracts.

Your responsibilities:
1. **Renewal alerts**: Flag contracts expiring within 90 days and recommend action
2. **SLA monitoring**: Track uptime commitments and flag violations
3. **Cost visibility**: Summarize annual vendor spend by category
4. **Negotiation prep**: Surface renewal leverage points and benchmarks
5. **Risk assessment**: Identify single points of failure or over-dependence

Proactive report format:
## Vendor Dashboard

### 🔴 Urgent (< 30 days to renewal)
### 🟡 Upcoming (30-90 days)
### 🟢 Stable (> 90 days)

### Spend Summary by Category
### Recommendations

Always recommend who should own each renewal negotiation and what to watch out for."""

    tools = [GET_VENDORS_TOOL, ADD_VENDOR_TOOL, CHECK_ALERTS_TOOL, GET_CURRENT_TIME_TOOL, WRITE_FILE_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result

        if tool_name == "get_vendors":
            return json.dumps(load_vendors(), indent=2)

        if tool_name == "add_vendor":
            vendors = load_vendors()
            existing = next((v for v in vendors if v["name"] == tool_input["name"]), None)
            if existing:
                existing.update(tool_input)
            else:
                vendors.append(tool_input)
            save_vendors(vendors)
            return f"Vendor '{tool_input['name']}' saved."

        if tool_name == "check_renewal_alerts":
            vendors = load_vendors()
            window = tool_input.get("alert_window_days", 90)
            today = datetime.now().date()
            alerts = {"urgent": [], "upcoming": [], "stable": []}
            for v in vendors:
                try:
                    end = datetime.strptime(v["contract_end_date"], "%Y-%m-%d").date()
                    days_left = (end - today).days
                    v["days_until_renewal"] = days_left
                    if days_left < 30:
                        alerts["urgent"].append(v)
                    elif days_left < window:
                        alerts["upcoming"].append(v)
                    else:
                        alerts["stable"].append(v)
                except ValueError:
                    pass
            return json.dumps(alerts, indent=2)

        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = VendorTrackerAgent()
    console.print("[bold green]Vendor Tracker Agent[/bold green]")
    response = agent.run("Run a vendor health check and flag anything urgent.")
    from rich.markdown import Markdown
    console.print(Markdown(response))
