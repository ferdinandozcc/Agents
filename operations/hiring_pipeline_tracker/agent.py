"""
operations/hiring_pipeline_tracker/agent.py
Hiring Pipeline Tracker Agent — Tracks candidates across stages, flags bottlenecks, and sends nudges.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class HiringPipelineTrackerAgentAgent(BaseAgent):
    system_prompt = """You are a recruiting operations assistant. You:
1. Track candidates across hiring stages (applied → screen → interview → offer → hired)
2. Flag candidates stuck at a stage for too long
3. Calculate pipeline metrics: time-to-hire, conversion rates per stage
4. Draft interview scheduling and status update emails
5. Produce weekly hiring funnel reports
Hiring is a two-way sales process — candidate experience matters."""

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
    agent = HiringPipelineTrackerAgentAgent()
    console.print(f"[bold green]Hiring Pipeline Tracker Agent[/bold green]")
    agent.chat()
