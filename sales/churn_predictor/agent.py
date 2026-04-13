"""
sales/churn_predictor/agent.py
Churn Predictor Agent — Identifies at-risk accounts using usage and engagement signals.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class ChurnPredictorAgentAgent(BaseAgent):
    system_prompt = """You are a customer success and churn prevention specialist. You:
1. Analyze account health signals: login frequency, feature usage, support tickets, NPS
2. Score each account's churn risk (high / medium / low)
3. Identify the primary risk driver for each at-risk account
4. Recommend targeted save actions per account
5. Prioritize accounts by ARR × churn risk for maximum impact
Prevention is 10x cheaper than win-back."""

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
    agent = ChurnPredictorAgentAgent()
    console.print(f"[bold green]Churn Predictor Agent[/bold green]")
    agent.chat()
