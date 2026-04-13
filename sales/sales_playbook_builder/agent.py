"""
sales/sales_playbook_builder/agent.py
Sales Playbook Builder Agent — Creates battle cards, objection handlers, and qualification guides.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import SEARCH_TOOL, READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class SalesPlaybookBuilderAgentAgent(BaseAgent):
    system_prompt = """You are a sales enablement specialist. You build:
1. Competitive battle cards: our strengths vs competitor weaknesses
2. Objection handling guides: common objections with proven responses
3. Discovery question banks by persona and industry
4. Qualification criteria checklists (MEDDIC, BANT, SPICED)
5. Deal stage exit criteria and playbooks
Playbooks should be living documents — update them with field learnings."""

    tools = [SEARCH_TOOL, READ_FILE_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL]

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
    agent = SalesPlaybookBuilderAgentAgent()
    console.print(f"[bold green]Sales Playbook Builder Agent[/bold green]")
    agent.chat()
