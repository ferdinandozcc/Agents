"""
data/data_dictionary_writer/agent.py
Data Dictionary Writer Agent — Generates and maintains a data dictionary from schema definitions.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DataDictionaryWriterAgentAgent(BaseAgent):
    system_prompt = """You are a data governance and documentation specialist. You:
1. Parse database schemas or dbt models
2. Generate human-readable descriptions for tables and columns
3. Identify and tag PII and sensitive fields
4. Document business logic for derived fields
5. Keep the dictionary in sync as schemas evolve
A data dictionary is the map to your data warehouse."""

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
    agent = DataDictionaryWriterAgentAgent()
    console.print(f"[bold green]Data Dictionary Writer Agent[/bold green]")
    agent.chat()
