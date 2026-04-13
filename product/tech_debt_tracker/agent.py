"""
product/tech_debt_tracker/agent.py
Tech Debt Tracker Agent — Catalogs technical debt, estimates impact, and prioritizes paydown.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class TechDebtTrackerAgentAgent(BaseAgent):
    system_prompt = """You are an engineering lead helping teams manage technical debt. You:
1. Catalog debt items with description, location, and type (code, infra, test, docs)
2. Estimate impact: performance, developer velocity, reliability risk
3. Score debt by urgency × impact
4. Recommend a paydown strategy alongside feature work
5. Track debt reduction over time
Help teams make debt visible and manageable, not shameful."""

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
    agent = TechDebtTrackerAgentAgent()
    console.print(f"[bold green]Tech Debt Tracker Agent[/bold green]")
    agent.chat()
