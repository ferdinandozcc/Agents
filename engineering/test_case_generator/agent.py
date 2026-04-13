"""
engineering/test_case_generator/agent.py
Test Case Generator Agent — Writes unit and integration tests from function signatures or specs.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class TestCaseGeneratorAgentAgent(BaseAgent):
    system_prompt = """You are a QA engineer and test automation specialist. You:
1. Analyze function signatures, specs, or user stories
2. Generate unit tests covering happy path, edge cases, and errors
3. Write integration tests for API endpoints and services
4. Suggest test data and fixtures
5. Identify untested code paths that need coverage
Tests are documentation that runs."""

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
    agent = TestCaseGeneratorAgentAgent()
    console.print(f"[bold green]Test Case Generator Agent[/bold green]")
    agent.chat()
