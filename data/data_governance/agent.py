"""
data/data_governance/agent.py
Data Governance Agent — Enforces data access policies, tags PII, and manages data lineage.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DataGovernanceAgentAgent(BaseAgent):
    system_prompt = """You are a data governance and compliance specialist. You:
1. Classify data assets by sensitivity (public, internal, confidential, restricted)
2. Identify and tag PII, PHI, and PCI fields
3. Enforce data access policies and flag violations
4. Document data lineage from source to consumption
5. Produce compliance-ready data inventory reports
Data governance enables innovation safely."""

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
    agent = DataGovernanceAgentAgent()
    console.print(f"[bold green]Data Governance Agent[/bold green]")
    agent.chat()
