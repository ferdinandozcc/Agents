"""
personal/budget_tracker/agent.py
Budget Tracker Agent — Monitors spending, categorizes transactions, and flags budget overruns.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class BudgetTrackerAgentAgent(BaseAgent):
    system_prompt = """You are a personal finance and budget coach. Help users:
1. Log and categorize transactions (food, transport, entertainment, etc.)
2. Track spending against monthly budgets per category
3. Alert when a category is over budget
4. Produce weekly spending summaries with trends
5. Suggest areas to cut back
Be encouraging and non-judgmental about spending."""

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
    agent = BudgetTrackerAgentAgent()
    console.print(f"[bold green]Budget Tracker Agent[/bold green]")
    agent.chat()
