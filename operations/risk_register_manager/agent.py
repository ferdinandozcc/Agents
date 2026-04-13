"""
operations/risk_register_manager/agent.py
Risk Register Manager Agent — Maintains a live risk register with likelihood, impact, and mitigations.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class RiskRegisterManagerAgentAgent(BaseAgent):
    system_prompt = """You are a risk management advisor. You:
1. Capture risks with description, category, owner, and date identified
2. Score each risk: likelihood (1-5) × impact (1-5) = risk score
3. Track mitigation actions and residual risk
4. Prioritize top risks for leadership review
5. Flag risks with no mitigation plan or overdue actions
Risks untracked are risks unmanaged."""

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
    agent = RiskRegisterManagerAgentAgent()
    console.print(f"[bold green]Risk Register Manager Agent[/bold green]")
    agent.chat()
