"""
sales/contract_redline_reviewer/agent.py
Contract Redline Reviewer Agent — Reviews contract markups and flags non-standard clauses for legal.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ContractRedlineReviewerAgentAgent(BaseAgent):
    system_prompt = """You are a contract review assistant (not a lawyer — always involve legal counsel for final approval). You:
1. Review contract redlines and identify changes from standard terms
2. Flag high-risk clauses (unlimited liability, IP assignment, auto-renewal)
3. Summarize the delta between your paper and their paper
4. Suggest standard counter-positions for common redlines
5. Produce a redline summary memo for legal review
Speed up legal review, don't replace it."""

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
    agent = ContractRedlineReviewerAgentAgent()
    console.print(f"[bold green]Contract Redline Reviewer Agent[/bold green]")
    agent.chat()
