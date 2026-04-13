"""
sales/follow_up_automator/agent.py
Follow-Up Automator Agent — Drafts and schedules follow-up messages based on call outcomes.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class FollowUpAutomatorAgentAgent(BaseAgent):
    system_prompt = """You are a sales follow-up specialist. After a sales interaction:
1. Draft a same-day follow-up email summarizing the call
2. Confirm next steps and commitments made
3. Attach relevant resources mentioned
4. Schedule reminder for follow-up if no response in N days
5. Write a multi-touch follow-up sequence for unresponsive prospects
Speed and relevance win in follow-up."""

    tools = [WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

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
    agent = FollowUpAutomatorAgentAgent()
    console.print(f"[bold green]Follow-Up Automator Agent[/bold green]")
    agent.chat()
