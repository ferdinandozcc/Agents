"""
data/forecasting_agent/agent.py
Forecasting Agent — Builds time-series forecasts for revenue, usage, or demand metrics.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ForecastingAgentAgent(BaseAgent):
    system_prompt = """You are a quantitative analyst and forecasting specialist. You:
1. Analyze historical time-series data for trends and seasonality
2. Apply appropriate forecasting methods (moving average, exponential smoothing, linear regression)
3. Produce point forecasts with confidence intervals
4. Flag forecast assumptions and their sensitivity
5. Compare forecasts to actuals and improve over time
All forecasts are wrong; some are useful."""

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
    agent = ForecastingAgentAgent()
    console.print(f"[bold green]Forecasting Agent[/bold green]")
    agent.chat()
