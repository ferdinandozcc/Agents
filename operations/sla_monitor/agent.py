"""
operations/sla_monitor/agent.py
SLA Monitor Agent — Tracks SLA compliance across teams and alerts on approaching breaches.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class SLAMonitorAgentAgent(BaseAgent):
    system_prompt = """You are an operations SLA compliance monitor. You:
1. Track open tickets/requests against their SLA deadlines
2. Alert when an item is within 20% of its SLA window
3. Flag breached SLAs with time-over and responsible team
4. Produce daily SLA compliance reports by team
5. Trend SLA performance over time
SLA breaches should never come as a surprise."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

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
    agent = SLAMonitorAgentAgent()
    console.print(f"[bold green]SLA Monitor Agent[/bold green]")
    agent.chat()
