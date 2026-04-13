"""
operations/process_documentation_writer/agent.py
Process Documentation Writer Agent — Interviews team members and produces SOPs and process docs.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, dispatch_common_tool


class ProcessDocumentationWriterAgentAgent(BaseAgent):
    system_prompt = """You are a business analyst and technical writer. You:
1. Interview the user about a process through structured questions
2. Document the process as a step-by-step SOP
3. Include decision points, edge cases, and escalation paths
4. Format in a clear, scannable structure with roles and responsibilities
5. Suggest process improvements spotted during documentation
Good documentation is the foundation of scalable operations."""

    tools = [WRITE_FILE_TOOL]

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
    agent = ProcessDocumentationWriterAgentAgent()
    console.print(f"[bold green]Process Documentation Writer Agent[/bold green]")
    agent.chat()
