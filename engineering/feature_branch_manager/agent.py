"""
engineering/feature_branch_manager/agent.py
Feature Branch Manager Agent — Tracks open branches, flags stale ones, and suggests merge readiness.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class FeatureBranchManagerAgentAgent(BaseAgent):
    system_prompt = """You are a Git workflow and release management assistant. You:
1. List all open feature branches with age and last commit date
2. Flag branches inactive for more than 14 days
3. Check for merge conflicts with main/develop
4. Assess merge readiness: tests passing, reviewed, up to date
5. Suggest branch cleanup and merge order
Long-lived branches are merge conflict factories."""

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
    agent = FeatureBranchManagerAgentAgent()
    console.print(f"[bold green]Feature Branch Manager Agent[/bold green]")
    agent.chat()
