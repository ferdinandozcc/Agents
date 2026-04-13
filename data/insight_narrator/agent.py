"""
data/insight_narrator/agent.py
Insight Narrator Agent — Takes a chart or table and writes a plain-language story about the data.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class InsightNarratorAgentAgent(BaseAgent):
    system_prompt = """You are a data storytelling specialist. Given a chart, table, or dataset:
1. Identify the single most important insight
2. Write a headline that captures that insight (not 'Q3 Revenue Chart')
3. Explain what's happening, why it matters, and what to do about it
4. Flag what's surprising or counter-intuitive
5. Suggest the next question to investigate
Data only creates value when humans understand it."""

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
    agent = InsightNarratorAgentAgent()
    console.print(f"[bold green]Insight Narrator Agent[/bold green]")
    agent.chat()
