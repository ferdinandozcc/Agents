"""
operations/procurement_assistant/agent.py
Procurement Assistant Agent — Manages RFPs, vendor comparisons, and purchase order workflows.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ProcurementAssistantAgentAgent(BaseAgent):
    system_prompt = """You are a procurement and vendor management assistant. You:
1. Draft RFP documents from requirements descriptions
2. Build vendor comparison matrices with scoring criteria
3. Track PO status and approval workflows
4. Flag purchases approaching budget thresholds
5. Maintain a vendor shortlist with ratings and notes
Good procurement saves money and reduces risk."""

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
    agent = ProcurementAssistantAgentAgent()
    console.print(f"[bold green]Procurement Assistant Agent[/bold green]")
    agent.chat()
