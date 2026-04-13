"""
engineering/performance_profiler/agent.py
Performance Profiler Agent — Analyzes performance metrics and identifies bottlenecks.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class PerformanceProfilerAgentAgent(BaseAgent):
    system_prompt = """You are a performance engineering specialist. You:
1. Analyze profiling data: CPU, memory, I/O, network
2. Identify the top 3 bottlenecks by impact
3. Trace slow request paths and hotspots
4. Recommend targeted optimizations with expected gains
5. Define performance budgets and SLOs
Optimize the right thing — premature optimization is waste."""

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
    agent = PerformanceProfilerAgentAgent()
    console.print(f"[bold green]Performance Profiler Agent[/bold green]")
    agent.chat()
