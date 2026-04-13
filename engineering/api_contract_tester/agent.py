"""
engineering/api_contract_tester/agent.py
API Contract Tester Agent — Validates API responses against OpenAPI specs and flags regressions.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class APIContractTesterAgentAgent(BaseAgent):
    system_prompt = """You are a QA engineer specializing in API testing and contract validation. You:
1. Compare API responses against OpenAPI/Swagger specs
2. Flag fields that are missing, extra, or wrong type
3. Test required vs optional fields
4. Validate error responses and status codes
5. Generate a contract compliance report
API regressions break consumers — catch them before deploy."""

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
    agent = APIContractTesterAgentAgent()
    console.print(f"[bold green]API Contract Tester Agent[/bold green]")
    agent.chat()
