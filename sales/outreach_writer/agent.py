"""
sales/outreach_writer/agent.py
Outreach Writer Agent — Writes personalized cold emails and LinkedIn messages for prospects.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import SEARCH_TOOL, WRITE_FILE_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class OutreachWriterAgentAgent(BaseAgent):
    system_prompt = """You are an expert B2B outreach copywriter. You write:
1. Cold emails: subject line, opener, value prop, CTA — under 100 words
2. LinkedIn connection requests: personalized, not generic
3. Follow-up sequences (day 3, day 7, day 14)
4. Multi-channel cadences (email + LinkedIn + phone)
Research the prospect before writing — personalization wins.
Never use: 'I hope this email finds you well' or 'touching base'."""

    tools = [SEARCH_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL]

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
    agent = OutreachWriterAgentAgent()
    console.print(f"[bold green]Outreach Writer Agent[/bold green]")
    agent.chat()
