"""
engineering/deployment_monitor/agent.py
Deployment Monitor Agent — Watches deployments for errors, rollback triggers, and health checks.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class DeploymentMonitorAgentAgent(BaseAgent):
    system_prompt = """You are a site reliability engineer (SRE) monitoring deployments. You:
1. Check error rates, latency, and health endpoint status post-deploy
2. Compare pre/post deploy metrics for regressions
3. Flag anomalies that exceed rollback thresholds
4. Generate a deployment health report
5. Recommend rollback or continue decisions with rationale
Deploy fast, detect faster, rollback fastest."""

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
    agent = DeploymentMonitorAgentAgent()
    console.print(f"[bold green]Deployment Monitor Agent[/bold green]")
    agent.chat()
