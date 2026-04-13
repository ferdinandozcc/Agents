"""
sales/crm_hygiene/agent.py
CRM Hygiene Agent — Audits CRM records for missing fields, duplicates, and stale data.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class CRMHygieneAgentAgent(BaseAgent):
    system_prompt = """You are a CRM data quality and operations specialist. You:
1. Audit records for missing required fields (email, company, stage)
2. Identify duplicate contacts and suggest merge candidates
3. Flag deals with no activity in the last 30/60/90 days
4. Identify contacts with no associated account
5. Produce a data quality score and remediation report
Bad CRM data = bad forecasts = bad decisions."""

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
    agent = CRMHygieneAgentAgent()
    console.print(f"[bold green]CRM Hygiene Agent[/bold green]")
    agent.chat()
