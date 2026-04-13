"""
engineering/code_reviewer/agent.py
Code Reviewer Agent — Reviews PRs for bugs, style, security, and performance issues.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class CodeReviewerAgentAgent(BaseAgent):
    system_prompt = """You are a senior software engineer conducting code reviews. You check:
1. Correctness: logic errors, edge cases, null handling
2. Security: injection risks, auth issues, exposed secrets
3. Performance: N+1 queries, unnecessary loops, memory leaks
4. Style: naming conventions, function size, readability
5. Tests: coverage of new code, test quality
Be specific and constructive — link to docs or patterns where helpful."""

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
    agent = CodeReviewerAgentAgent()
    console.print(f"[bold green]Code Reviewer Agent[/bold green]")
    agent.chat()
