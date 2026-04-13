"""
product/sprint_retrospective/agent.py
Sprint Retrospective Agent — Facilitates retros, captures feedback, and tracks action items over time.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class SprintRetrospectiveAgentAgent(BaseAgent):
    system_prompt = """You are an agile coach facilitating sprint retrospectives. You:
1. Run a structured retro (Start / Stop / Continue or 4Ls)
2. Capture all team feedback neutrally
3. Help the team dot-vote on priorities
4. Convert top items into concrete action items with owners
5. Track action items from previous retros and check completion
Keep sessions timeboxed, focused, and psychologically safe."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

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
    agent = SprintRetrospectiveAgentAgent()
    console.print(f"[bold green]Sprint Retrospective Agent[/bold green]")
    agent.chat()
