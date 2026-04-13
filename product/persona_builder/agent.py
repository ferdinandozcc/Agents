"""
product/persona_builder/agent.py
Persona Builder Agent — Creates detailed user personas from research data and interviews.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class PersonaBuilderAgentAgent(BaseAgent):
    system_prompt = """You are a UX researcher specializing in persona development. You:
1. Synthesize qualitative data (interviews, surveys, support tickets)
2. Identify distinct user archetypes based on behaviors and goals
3. Build detailed personas with: demographics, goals, frustrations, behaviors, quotes
4. Suggest which persona to prioritize for a given feature
5. Keep personas grounded in data, not assumptions
Output personas in a structured, shareable format."""

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
    agent = PersonaBuilderAgentAgent()
    console.print(f"[bold green]Persona Builder Agent[/bold green]")
    agent.chat()
