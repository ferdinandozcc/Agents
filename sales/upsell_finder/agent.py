"""
sales/upsell_finder/agent.py
Upsell Opportunity Finder Agent — Scans customer data for expansion and upsell opportunities.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class UpsellOpportunityFinderAgentAgent(BaseAgent):
    system_prompt = """You are a revenue expansion and account growth specialist. You:
1. Analyze customer usage patterns against their current plan/tier
2. Identify customers approaching usage limits (upgrade triggers)
3. Match customers to relevant add-on products based on their usage
4. Score expansion opportunities by revenue potential and likelihood
5. Draft personalized expansion outreach messages
Expansion revenue is the most efficient revenue."""

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
    agent = UpsellOpportunityFinderAgentAgent()
    console.print(f"[bold green]Upsell Opportunity Finder Agent[/bold green]")
    agent.chat()
