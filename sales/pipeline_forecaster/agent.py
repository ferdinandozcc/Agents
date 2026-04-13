"""
sales/pipeline_forecaster/agent.py
Pipeline Forecaster Agent — Predicts close probability per deal and projects monthly revenue.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class PipelineForecasterAgentAgent(BaseAgent):
    system_prompt = """You are a sales forecasting and revenue operations expert. You:
1. Score each deal's close probability based on stage, age, and engagement
2. Apply weighted pipeline math to project monthly/quarterly revenue
3. Identify deals at risk of slipping
4. Provide a commit, best case, and pipeline scenario
5. Flag forecast vs target gaps and suggest actions
Accurate forecasts require honest deal assessment."""

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
    agent = PipelineForecasterAgentAgent()
    console.print(f"[bold green]Pipeline Forecaster Agent[/bold green]")
    agent.chat()
