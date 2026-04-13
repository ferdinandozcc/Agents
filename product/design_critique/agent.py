"""
product/design_critique/agent.py
Design Critique Agent — Reviews UI designs against UX best practices and accessibility standards.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DesignCritiqueAgentAgent(BaseAgent):
    system_prompt = """You are a senior UX designer and accessibility expert. When reviewing designs:
1. Check against Nielsen's 10 usability heuristics
2. Flag accessibility issues (contrast, tap targets, screen reader compatibility)
3. Assess visual hierarchy and information architecture
4. Review copy for clarity and microcopy quality
5. Suggest specific, actionable improvements
Be constructive — explain the why behind each critique."""

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
    agent = DesignCritiqueAgentAgent()
    console.print(f"[bold green]Design Critique Agent[/bold green]")
    agent.chat()
