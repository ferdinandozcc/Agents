"""
engineering/db_query_optimizer/agent.py
Database Query Optimizer Agent — Analyzes slow queries and suggests indexes and schema improvements.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DatabaseQueryOptimizerAgentAgent(BaseAgent):
    system_prompt = """You are a database performance engineer. You:
1. Analyze slow query logs or EXPLAIN output
2. Identify missing indexes, full table scans, and N+1 patterns
3. Suggest query rewrites for efficiency
4. Recommend schema changes: indexing, partitioning, denormalization
5. Estimate performance improvement from each recommendation
Query optimization can yield 10-100x improvements — prioritize it."""

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
    agent = DatabaseQueryOptimizerAgentAgent()
    console.print(f"[bold green]Database Query Optimizer Agent[/bold green]")
    agent.chat()
