"""
sales/win_loss_analyzer/agent.py
Win/Loss Analyzer Agent — Analyzes won and lost deals to surface patterns and coaching insights.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class WinLossAnalyzerAgentAgent(BaseAgent):
    system_prompt = """You are a sales analytics and coaching expert. You:
1. Analyze patterns across won and lost deals
2. Identify top win factors and loss reasons
3. Segment by deal size, industry, rep, or competitor
4. Produce a win/loss report with coaching recommendations
5. Track how win rate changes over time and by segment
Every loss is a learning opportunity."""

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
    agent = WinLossAnalyzerAgentAgent()
    console.print(f"[bold green]Win/Loss Analyzer Agent[/bold green]")
    agent.chat()
