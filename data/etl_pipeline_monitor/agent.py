"""
data/etl_pipeline_monitor/agent.py
ETL Pipeline Monitor Agent — Monitors data pipelines for failures, delays, and data anomalies.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class ETLPipelineMonitorAgentAgent(BaseAgent):
    system_prompt = """You are a data engineering and pipeline reliability specialist. You:
1. Check pipeline run status and detect failures
2. Flag pipelines running late against their SLA
3. Validate row counts and data volumes against expectations
4. Alert on schema changes in source tables
5. Produce a daily pipeline health report
Data consumers depend on reliable pipelines — treat them like production services."""

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
    agent = ETLPipelineMonitorAgentAgent()
    console.print(f"[bold green]ETL Pipeline Monitor Agent[/bold green]")
    agent.chat()
