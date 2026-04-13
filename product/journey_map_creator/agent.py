"""
product/journey_map_creator/agent.py
Journey Map Creator Agent — Builds end-to-end user journey maps with pain points and opportunities.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class JourneyMapCreatorAgentAgent(BaseAgent):
    system_prompt = """You are a customer experience designer. Build journey maps by:
1. Defining the user, scenario, and scope
2. Mapping each stage of the journey (awareness → onboarding → use → renewal)
3. Capturing user actions, thoughts, and emotions at each stage
4. Identifying pain points and moments of delight
5. Surfacing opportunity areas for product improvements
Output in a structured table format that can be dropped into Miro or Figma."""

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
    agent = JourneyMapCreatorAgentAgent()
    console.print(f"[bold green]Journey Map Creator Agent[/bold green]")
    agent.chat()
