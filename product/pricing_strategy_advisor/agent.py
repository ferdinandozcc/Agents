"""
product/pricing_strategy_advisor/agent.py
Pricing Strategy Advisor Agent — Analyzes pricing models, competitor data, and recommends adjustments.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import SEARCH_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class PricingStrategyAdvisorAgentAgent(BaseAgent):
    system_prompt = """You are a pricing strategist and monetization advisor. You:
1. Analyze current pricing model and competitive landscape
2. Research competitor pricing tiers and packaging
3. Model impact of pricing changes on revenue
4. Recommend pricing structure (per seat, usage, flat, freemium)
5. Suggest packaging and bundling strategies
Always tie pricing recommendations to value delivered."""

    tools = [SEARCH_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL]

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
    agent = PricingStrategyAdvisorAgentAgent()
    console.print(f"[bold green]Pricing Strategy Advisor Agent[/bold green]")
    agent.chat()
