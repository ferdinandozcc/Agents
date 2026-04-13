"""
data/sql_query_writer/agent.py
SQL Query Writer Agent — Converts natural language questions into optimized SQL queries.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class SQLQueryWriterAgentAgent(BaseAgent):
    system_prompt = """You are a data analyst and SQL expert. You:
1. Understand the business question being asked
2. Identify the relevant tables and joins needed
3. Write clean, readable, optimized SQL
4. Add comments explaining logic for complex queries
5. Suggest indexes if performance is a concern
Always ask for clarification on ambiguous business logic before writing."""

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
    agent = SQLQueryWriterAgentAgent()
    console.print(f"[bold green]SQL Query Writer Agent[/bold green]")
    agent.chat()
