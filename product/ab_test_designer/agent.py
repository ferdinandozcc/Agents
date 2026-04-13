"""
product/ab_test_designer/agent.py
A/B Test Designer Agent — Designs experiments, calculates sample sizes, and interprets results.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, dispatch_common_tool


class ABTestDesignerAgentAgent(BaseAgent):
    system_prompt = """You are a product experimentation expert. Help teams:
1. Define a clear hypothesis and primary metric
2. Calculate required sample size for statistical power
3. Design control and variant conditions
4. Define guardrail metrics to prevent regressions
5. Interpret results including statistical significance and practical significance
Always ask: what decision will this experiment inform?"""

    tools = [WRITE_FILE_TOOL]

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
    agent = ABTestDesignerAgentAgent()
    console.print(f"[bold green]A/B Test Designer Agent[/bold green]")
    agent.chat()
