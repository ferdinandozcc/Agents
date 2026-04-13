"""
sales/lead_qualifier/agent.py
Lead Qualifier Agent — Scores inbound leads against ICP criteria and routes to the right rep.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class LeadQualifierAgentAgent(BaseAgent):
    system_prompt = """You are a sales development expert and lead qualification specialist. You:
1. Score leads against ICP criteria (company size, industry, role, intent signals)
2. Assign a lead grade: A (hot) / B (warm) / C (cold) / D (disqualify)
3. Recommend the best rep or team to route each lead to
4. Draft a personalized intro message for A and B leads
5. Flag leads that need more research before outreach
Quality over quantity — protect rep time."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL, SEARCH_TOOL]

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
    agent = LeadQualifierAgentAgent()
    console.print(f"[bold green]Lead Qualifier Agent[/bold green]")
    agent.chat()
