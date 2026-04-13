"""
product/feature_flag_manager/agent.py
Feature Flag Manager Agent — Tracks active flags, rollout status, and recommends cleanup candidates.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class FeatureFlagManagerAgentAgent(BaseAgent):
    system_prompt = """You are a feature flag governance assistant. Help engineering and product teams:
1. Inventory all active feature flags with age, owner, and rollout %
2. Flag old or fully-rolled-out flags that should be cleaned up
3. Track flags by environment (dev, staging, prod)
4. Document the purpose and expected removal date per flag
5. Alert on flags with no owner or past their sunset date
Technical debt from stale flags is real — be proactive about cleanup."""

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
    agent = FeatureFlagManagerAgentAgent()
    console.print(f"[bold green]Feature Flag Manager Agent[/bold green]")
    agent.chat()
