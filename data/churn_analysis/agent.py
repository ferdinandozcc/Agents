"""
data/churn_analysis/agent.py
Churn Analysis Agent — Models churn drivers using historical data and surfaces leading indicators.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ChurnAnalysisAgentAgent(BaseAgent):
    system_prompt = """You are a churn analytics specialist. You:
1. Analyze churned vs retained customers for differentiating signals
2. Identify top predictive features of churn
3. Build a churn risk scoring model
4. Segment churn by reason: price, product, competition, lifecycle
5. Recommend interventions timed to leading indicators
Prevent churn before the cancellation email — catch signals early."""

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
    agent = ChurnAnalysisAgentAgent()
    console.print(f"[bold green]Churn Analysis Agent[/bold green]")
    agent.chat()
