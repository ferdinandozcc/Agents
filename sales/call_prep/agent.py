"""
sales/call_prep/agent.py
Call Prep Agent — Researches prospects and preps talking points before sales calls.
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


class CallPrepAgentAgent(BaseAgent):
    system_prompt = """You are a sales enablement assistant specializing in pre-call preparation. Before a call:
1. Research the company: size, industry, recent news, funding, tech stack
2. Research the contact: role, background, LinkedIn activity
3. Identify likely pain points and priorities
4. Prepare 3-5 tailored discovery questions
5. Anticipate likely objections with prepared responses
Great calls are won in the preparation."""

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
    agent = CallPrepAgentAgent()
    console.print(f"[bold green]Call Prep Agent[/bold green]")
    agent.chat()
