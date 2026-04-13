"""
engineering/documentation_generator/agent.py
Documentation Generator Agent — Generates inline code comments and module-level docs from source.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DocumentationGeneratorAgentAgent(BaseAgent):
    system_prompt = """You are a technical writer and documentation engineer. You:
1. Read source code and generate docstrings / JSDoc / inline comments
2. Write module-level READMEs explaining purpose and usage
3. Generate changelog entries from commit diffs
4. Create architecture decision records (ADRs)
5. Keep docs in sync with code changes
Code without docs is a liability — especially for onboarding."""

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
    agent = DocumentationGeneratorAgentAgent()
    console.print(f"[bold green]Documentation Generator Agent[/bold green]")
    agent.chat()
