"""
operations/budget_forecaster/agent.py
Budget Forecaster Agent — Projects spend vs budget across departments and flags variances.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class BudgetForecasterAgentAgent(BaseAgent):
    system_prompt = """You are a financial planning and analysis (FP&A) assistant. You:
1. Load actuals vs budget by department and category
2. Project end-of-period spend based on run rate
3. Flag departments trending over or under budget
4. Model different spend scenarios (base / optimistic / conservative)
5. Produce a variance analysis report
Keep forecasts grounded in actuals, not wishful thinking."""

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
    agent = BudgetForecasterAgentAgent()
    console.print(f"[bold green]Budget Forecaster Agent[/bold green]")
    agent.chat()
