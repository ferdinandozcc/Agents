"""
data/data_quality_monitor/agent.py
Data Quality Monitor Agent — Scans datasets for nulls, outliers, duplicates, and schema drift.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DataQualityMonitorAgentAgent(BaseAgent):
    system_prompt = """You are a data quality engineer. You:
1. Profile datasets: row counts, null rates, cardinality, data types
2. Flag columns with high null rates or unexpected values
3. Detect outliers using statistical methods
4. Identify duplicate records
5. Alert on schema changes vs expected schema
Bad data in = bad decisions out. Quality gates matter."""

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
    agent = DataQualityMonitorAgentAgent()
    console.print(f"[bold green]Data Quality Monitor Agent[/bold green]")
    agent.chat()
