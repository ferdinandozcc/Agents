"""
marketing/market_research/agent.py
Market Research Agent — Researches TAM, SAM, SOM, and buyer trends for a target market.
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


class MarketResearchAgentAgent(BaseAgent):
    system_prompt = """You are a market intelligence and research analyst. You:
1. Define and size the TAM, SAM, and SOM for a market
2. Research buyer personas and decision-making behavior
3. Identify market trends, growth drivers, and headwinds
4. Analyze major players and market share
5. Produce a structured market overview report with sources
Ground claims in data — note confidence levels for estimates."""

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
    agent = MarketResearchAgentAgent()
    console.print(f"[bold green]Market Research Agent[/bold green]")
    agent.chat()
