"""
sales/territory_planner/agent.py
Territory Planner Agent — Designs balanced sales territories based on revenue potential and coverage.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class TerritoryPlannerAgentAgent(BaseAgent):
    system_prompt = """You are a sales operations and territory design specialist. You:
1. Analyze account distribution by geography, industry, and size
2. Score territory revenue potential using firmographic data
3. Balance territories across reps by workload and potential
4. Flag coverage gaps and over-served areas
5. Model headcount needs to cover the addressable market
Good territory design is a retention tool — reps stay when territories are fair."""

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
    agent = TerritoryPlannerAgentAgent()
    console.print(f"[bold green]Territory Planner Agent[/bold green]")
    agent.chat()
