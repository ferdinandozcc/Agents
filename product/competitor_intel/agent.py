"""
product/competitor_intel/agent.py
Competitor Intel Agent — monitors competitor signals across web sources.
"""

import sys
import os
import json
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import FETCH_URL_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

COMPETITORS_FILE = Path(__file__).parent / "competitors.json"

GET_COMPETITORS_TOOL = {
    "name": "get_competitors",
    "description": "Get the list of configured competitors and their URLs to monitor.",
    "input_schema": {"type": "object", "properties": {}, "required": []},
}

SAVE_INTEL_TOOL = {
    "name": "save_intel_report",
    "description": "Save a competitor intelligence report to a file.",
    "input_schema": {
        "type": "object",
        "properties": {
            "report": {"type": "string"},
            "competitor": {"type": "string"},
        },
        "required": ["report", "competitor"],
    },
}

DEFAULT_COMPETITORS = {
    "competitors": [
        {
            "name": "Competitor A",
            "website": "https://example-competitor-a.com",
            "blog": "https://example-competitor-a.com/blog",
            "changelog": "https://example-competitor-a.com/changelog",
            "linkedin": "https://linkedin.com/company/example-a",
        }
    ]
}


class CompetitorIntelAgent(BaseAgent):
    system_prompt = """You are a competitive intelligence analyst. Your job is to monitor competitor 
activity and surface strategic insights.

For each competitor, analyze:
1. **Product updates**: New features, pricing changes, UI changes
2. **Messaging shifts**: How their positioning or value prop is evolving
3. **Hiring signals**: What roles they're hiring (signals future investment)
4. **Content strategy**: What topics they're publishing about
5. **Customer sentiment**: Any public feedback or reviews

Structure your output as:
## Competitor: [Name]
### What's new
### Strategic signals
### Opportunities for us
### Watch list

Be analytical — connect dots and surface implications, not just raw facts."""

    tools = [GET_COMPETITORS_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, SAVE_INTEL_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "get_competitors":
            if COMPETITORS_FILE.exists():
                return COMPETITORS_FILE.read_text()
            return json.dumps(DEFAULT_COMPETITORS, indent=2)
        if tool_name == "save_intel_report":
            path = f"outputs/intel_{tool_input['competitor'].replace(' ', '_')}.md"
            Path("outputs").mkdir(exist_ok=True)
            Path(path).write_text(tool_input["report"])
            return f"Report saved to {path}"
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = CompetitorIntelAgent()
    console.print("[bold green]Competitor Intel Agent[/bold green]")
    console.print("Which competitor would you like to analyze? Or type 'all' for a sweep.\n")
    agent.chat()
