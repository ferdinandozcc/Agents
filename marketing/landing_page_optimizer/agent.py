"""
marketing/landing_page_optimizer/agent.py
Landing Page Optimizer Agent — Reviews landing pages and suggests copy, layout, and CTA improvements.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import FETCH_URL_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class LandingPageOptimizerAgentAgent(BaseAgent):
    system_prompt = """You are a conversion rate optimization (CRO) specialist. You:
1. Review landing page copy for clarity and persuasion
2. Assess visual hierarchy and CTA placement
3. Check for friction points in the conversion flow
4. Suggest A/B test hypotheses ranked by potential impact
5. Review social proof, trust signals, and objection handling
Every element on a landing page should earn its place."""

    tools = [FETCH_URL_TOOL, WRITE_FILE_TOOL]

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
    agent = LandingPageOptimizerAgentAgent()
    console.print(f"[bold green]Landing Page Optimizer Agent[/bold green]")
    agent.chat()
