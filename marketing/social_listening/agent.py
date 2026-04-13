"""
marketing/social_listening/agent.py
Social Listening Agent — Monitors brand mentions and competitor buzz across social channels.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import SEARCH_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class SocialListeningAgentAgent(BaseAgent):
    system_prompt = """You are a social media intelligence analyst. You:
1. Search for brand mentions across public social and web sources
2. Categorize sentiment: positive / neutral / negative
3. Surface trending topics in your category
4. Monitor competitor activity and engagement
5. Flag viral or crisis-potential content requiring immediate response
Listening is the foundation of good social strategy."""

    tools = [SEARCH_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, SEARCH_TOOL]

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
    agent = SocialListeningAgentAgent()
    console.print(f"[bold green]Social Listening Agent[/bold green]")
    agent.chat()
