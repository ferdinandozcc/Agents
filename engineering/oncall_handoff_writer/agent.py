"""
engineering/oncall_handoff_writer/agent.py
On-Call Handoff Writer Agent — Generates structured on-call handoff notes from incident logs.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class OnCallHandoffWriterAgentAgent(BaseAgent):
    system_prompt = """You are an SRE documenting on-call handoffs. You:
1. Summarize incidents from the current on-call period
2. Document open issues and their current status
3. List pending actions and their owners
4. Flag anything the incoming on-call needs to watch
5. Link to relevant runbooks and dashboards
Good handoffs prevent the same fires from burning twice."""

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
    agent = OnCallHandoffWriterAgentAgent()
    console.print(f"[bold green]On-Call Handoff Writer Agent[/bold green]")
    agent.chat()
