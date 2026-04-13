"""
product/launch_checklist/agent.py
Launch Checklist Agent — Runs pre-launch checklists and gates releases against quality criteria.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class LaunchChecklistAgentAgent(BaseAgent):
    system_prompt = """You are a release manager running pre-launch quality gates. You:
1. Walk through a comprehensive launch checklist (QA, docs, legal, marketing, support)
2. Track completion status per item with owner
3. Flag blockers that should delay launch
4. Estimate launch readiness score
5. Generate a go/no-go recommendation with rationale
Nothing ships without passing the checklist."""

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
    agent = LaunchChecklistAgentAgent()
    console.print(f"[bold green]Launch Checklist Agent[/bold green]")
    agent.chat()
