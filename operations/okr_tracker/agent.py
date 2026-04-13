"""
operations/okr_tracker/agent.py
OKR Tracker Agent — Tracks OKR progress, scores key results, and flags at-risk objectives.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class OKRTrackerAgentAgent(BaseAgent):
    system_prompt = """You are an OKR coach and tracking assistant. You:
1. Help teams write well-formed Objectives and Key Results
2. Track progress against each KR (0.0 to 1.0 scale)
3. Score OKRs at end of quarter using standard methodology
4. Flag at-risk KRs needing attention mid-quarter
5. Facilitate OKR check-in conversations
OKRs should be ambitious but achievable — 0.7 is a win."""

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
    agent = OKRTrackerAgentAgent()
    console.print(f"[bold green]OKR Tracker Agent[/bold green]")
    agent.chat()
