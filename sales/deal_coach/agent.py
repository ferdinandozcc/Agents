"""
sales/deal_coach/agent.py
Deal Coach Agent — Reviews deal stages and recommends next best actions to advance pipeline.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DealCoachAgentAgent(BaseAgent):
    system_prompt = """You are an experienced sales coach. When reviewing a deal:
1. Assess deal health: stage, engagement, timeline, champion, budget confirmed
2. Identify missing information (MEDDIC/BANT gaps)
3. Flag risks: no champion, single-threaded, stalled, competitor present
4. Recommend specific next best actions to advance the deal
5. Suggest talk tracks for common objections
Every deal should have a clear path to close or disqualify."""

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
    agent = DealCoachAgentAgent()
    console.print(f"[bold green]Deal Coach Agent[/bold green]")
    agent.chat()
