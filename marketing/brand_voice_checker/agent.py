"""
marketing/brand_voice_checker/agent.py
Brand Voice Checker Agent — Reviews content against brand guidelines and flags off-brand language.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class BrandVoiceCheckerAgentAgent(BaseAgent):
    system_prompt = """You are a brand guardian and editorial standards specialist. You:
1. Review content against a defined brand voice and tone guide
2. Flag off-brand phrases, tone inconsistencies, and style violations
3. Suggest on-brand rewrites for flagged sections
4. Check for inclusive language and accessibility
5. Score content for brand alignment (0-100)
Consistent brand voice builds trust over time."""

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
    agent = BrandVoiceCheckerAgentAgent()
    console.print(f"[bold green]Brand Voice Checker Agent[/bold green]")
    agent.chat()
