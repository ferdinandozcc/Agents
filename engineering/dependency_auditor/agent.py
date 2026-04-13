"""
engineering/dependency_auditor/agent.py
Dependency Auditor Agent — Scans package dependencies for outdated versions and CVEs.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class DependencyAuditorAgentAgent(BaseAgent):
    system_prompt = """You are a software supply chain security and hygiene expert. You:
1. Parse package manifests (requirements.txt, package.json, etc.)
2. Identify outdated dependencies and available updates
3. Flag known CVEs using public vulnerability data
4. Prioritize updates by severity and ease of upgrade
5. Produce an upgrade plan with estimated effort
Keeping dependencies current is boring but essential."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL, SEARCH_TOOL]

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
    agent = DependencyAuditorAgentAgent()
    console.print(f"[bold green]Dependency Auditor Agent[/bold green]")
    agent.chat()
