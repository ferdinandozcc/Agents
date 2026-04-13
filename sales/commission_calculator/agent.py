"""
sales/commission_calculator/agent.py
Commission Calculator Agent — Computes commissions, SPIFs, and quota attainment per rep.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class CommissionCalculatorAgentAgent(BaseAgent):
    system_prompt = """You are a sales compensation and RevOps assistant. You:
1. Calculate base commission from closed deals against plan rules
2. Apply accelerators for over-quota attainment
3. Compute SPIFs and bonuses for qualifying deals
4. Produce per-rep attainment summaries
5. Model payout scenarios for pipeline deals
Accurate comp calculations build trust with the sales team."""

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
    agent = CommissionCalculatorAgentAgent()
    console.print(f"[bold green]Commission Calculator Agent[/bold green]")
    agent.chat()
