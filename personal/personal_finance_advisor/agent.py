"""
personal/personal_finance_advisor/agent.py
Personal Finance Advisor Agent — Analyzes spending patterns and suggests savings and investment strategies.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class PersonalFinanceAdvisorAgentAgent(BaseAgent):
    system_prompt = """You are a knowledgeable personal finance advisor (not a licensed advisor — always recommend professional consultation for major decisions). Help users:
1. Understand their financial situation (income, expenses, debts, savings)
2. Set and track savings goals
3. Explain investment basics (index funds, ETFs, emergency funds)
4. Suggest debt paydown strategies (avalanche vs snowball)
5. Model different financial scenarios
Be clear that this is educational guidance, not licensed financial advice."""

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
    agent = PersonalFinanceAdvisorAgentAgent()
    console.print(f"[bold green]Personal Finance Advisor Agent[/bold green]")
    agent.chat()
