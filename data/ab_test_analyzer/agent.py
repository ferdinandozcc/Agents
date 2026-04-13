"""
data/ab_test_analyzer/agent.py
A/B Test Analyzer Agent — Calculates statistical significance and interprets experiment results.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ABTestAnalyzerAgentAgent(BaseAgent):
    system_prompt = """You are a data scientist specializing in experimentation and causal inference. You:
1. Validate experiment setup: randomization, sample ratio mismatch, pre-experiment trends
2. Calculate statistical significance (p-value, confidence intervals)
3. Measure practical significance (effect size, minimum detectable effect)
4. Check for novelty effects and segment interactions
5. Produce a clear ship / no-ship recommendation with rationale
Statistical significance ≠ practical significance — always check both."""

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
    agent = ABTestAnalyzerAgentAgent()
    console.print(f"[bold green]A/B Test Analyzer Agent[/bold green]")
    agent.chat()
