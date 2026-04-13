"""
product/api_documentation_writer/agent.py
API Documentation Writer Agent — Generates clean API docs from code, schemas, or endpoint descriptions.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class APIDocumentationWriterAgentAgent(BaseAgent):
    system_prompt = """You are a technical writer specializing in API documentation. You:
1. Parse OpenAPI specs, code, or verbal descriptions of endpoints
2. Write clear endpoint documentation with: method, path, params, request/response examples
3. Generate SDK usage examples in Python and JavaScript
4. Write authentication and getting-started guides
5. Flag undocumented or ambiguous endpoints
Output in Markdown or OpenAPI YAML format."""

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
    agent = APIDocumentationWriterAgentAgent()
    console.print(f"[bold green]API Documentation Writer Agent[/bold green]")
    agent.chat()
