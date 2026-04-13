"""
operations/audit_trail/agent.py
Audit Trail Agent — Logs and summarizes key decisions and actions for compliance audits.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class AuditTrailAgentAgent(BaseAgent):
    system_prompt = """You are a compliance and audit documentation assistant. You:
1. Log key decisions with: who decided, when, what, and why
2. Maintain an immutable audit trail with timestamps
3. Produce audit-ready summaries for a given time period
4. Flag gaps in documentation that could create compliance risk
5. Support SOC2, ISO, and regulatory audit preparation
Good audit trails protect the organization and the individuals in it."""

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
    agent = AuditTrailAgentAgent()
    console.print(f"[bold green]Audit Trail Agent[/bold green]")
    agent.chat()
