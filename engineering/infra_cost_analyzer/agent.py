"""
engineering/infra_cost_analyzer/agent.py
Infrastructure Cost Analyzer Agent — Reviews cloud spend and recommends rightsizing and cost optimizations.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class InfrastructureCostAnalyzerAgentAgent(BaseAgent):
    system_prompt = """You are a FinOps and cloud cost optimization specialist. You:
1. Analyze cloud spend by service, team, and environment
2. Identify over-provisioned resources (oversized instances, idle resources)
3. Flag dev/test resources left running in prod-like configs
4. Recommend reserved instance or savings plan purchases
5. Project cost savings from recommended changes
Cloud bills grow silently — shine a light on them."""

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
    agent = InfrastructureCostAnalyzerAgentAgent()
    console.print(f"[bold green]Infrastructure Cost Analyzer Agent[/bold green]")
    agent.chat()
