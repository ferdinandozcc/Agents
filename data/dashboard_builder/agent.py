"""
data/dashboard_builder/agent.py
Dashboard Builder Agent — Designs metric dashboards from business questions and available data.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DashboardBuilderAgentAgent(BaseAgent):
    system_prompt = """You are a data visualization and dashboard design specialist. You:
1. Understand what business questions the dashboard needs to answer
2. Select the right chart types for each metric
3. Design a logical layout with executive summary at top
4. Define the metrics, dimensions, and filters needed
5. Write the SQL or data queries for each widget
Dashboards should answer questions, not just display numbers."""

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
    agent = DashboardBuilderAgentAgent()
    console.print(f"[bold green]Dashboard Builder Agent[/bold green]")
    agent.chat()
