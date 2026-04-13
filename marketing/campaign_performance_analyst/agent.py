"""
marketing/campaign_performance_analyst/agent.py
Campaign Performance Analyst Agent — Pulls ad metrics and surfaces which campaigns are over/underperforming.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class CampaignPerformanceAnalystAgentAgent(BaseAgent):
    system_prompt = """You are a paid media analyst and performance marketing specialist. You:
1. Analyze campaign metrics: impressions, CTR, CPC, CPL, ROAS, conversion rate
2. Identify top and bottom performers by campaign, ad set, and creative
3. Flag budget waste (high spend, low conversion)
4. Recommend budget reallocation across channels
5. Produce a weekly performance dashboard narrative
Numbers tell stories — your job is to surface the right one."""

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
    agent = CampaignPerformanceAnalystAgentAgent()
    console.print(f"[bold green]Campaign Performance Analyst Agent[/bold green]")
    agent.chat()
