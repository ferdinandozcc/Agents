"""
data/cohort_analysis/agent.py
Cohort Analysis Agent — Builds and interprets cohort analyses for retention and engagement.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class CohortAnalysisAgentAgent(BaseAgent):
    system_prompt = """You are a product analytics specialist. You:
1. Define cohorts by acquisition date, channel, or feature usage
2. Calculate retention rates at D1, D7, D30, D90
3. Compare cohort performance over time
4. Identify which cohorts retain best and why
5. Translate cohort data into product recommendations
Retention is the foundation of sustainable growth."""

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
    agent = CohortAnalysisAgentAgent()
    console.print(f"[bold green]Cohort Analysis Agent[/bold green]")
    agent.chat()
