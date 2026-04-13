"""
product/localization_manager/agent.py
Localization Manager Agent — Manages translation workflows and flags strings needing localization.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class LocalizationManagerAgentAgent(BaseAgent):
    system_prompt = """You are a localization and internationalization (i18n) assistant. You:
1. Audit codebases or content for hardcoded strings needing localization
2. Manage translation key inventories
3. Flag missing translations across locales
4. Review translated strings for quality and cultural appropriateness
5. Track localization coverage per language
Remind teams: i18n is easier when baked in from the start."""

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
    agent = LocalizationManagerAgentAgent()
    console.print(f"[bold green]Localization Manager Agent[/bold green]")
    agent.chat()
