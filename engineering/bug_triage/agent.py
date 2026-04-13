"""
engineering/bug_triage/agent.py
Bug Triage Agent — Categorizes incoming bugs by severity, assigns owners, and tracks fixes.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class BugTriageAgentAgent(BaseAgent):
    system_prompt = """You are an engineering triage lead. You:
1. Categorize bug severity: Critical / High / Medium / Low
2. Identify the likely component and owning team
3. Check for duplicate reports and link them
4. Draft a clear, reproducible bug report
5. Track resolution status and time-to-fix SLAs
Good triage keeps engineering focused on what matters most."""

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
    agent = BugTriageAgentAgent()
    console.print(f"[bold green]Bug Triage Agent[/bold green]")
    agent.chat()
