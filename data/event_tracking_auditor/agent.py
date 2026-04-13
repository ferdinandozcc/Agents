"""
data/event_tracking_auditor/agent.py
Event Tracking Auditor Agent — Audits analytics event taxonomy for coverage gaps and naming issues.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class EventTrackingAuditorAgentAgent(BaseAgent):
    system_prompt = """You are a product analytics and data governance specialist. You:
1. Review the event tracking plan against what's actually implemented
2. Flag missing events for key user flows
3. Identify naming inconsistencies and schema drift
4. Check for PII in event properties
5. Produce a prioritized audit report with recommended fixes
Garbage in, garbage analytics out."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "search_web":
            try:
                from personal.research_assistant.agent import search_web
                return search_web(tool_input["query"], tool_input.get("num_results", 5))
            except Exception as e:
                return f"Search unavailable: {e}"
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = EventTrackingAuditorAgentAgent()
    console.print(f"[bold green]Event Tracking Auditor Agent[/bold green]")
    agent.chat()
