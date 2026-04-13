"""
marketing/email_copywriter/agent.py
Email Copywriter Agent — Writes subject lines, body copy, and CTAs for marketing emails.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, dispatch_common_tool


class EmailCopywriterAgentAgent(BaseAgent):
    system_prompt = """You are an email marketing copywriter specializing in conversion. You write:
1. Subject lines: 3 variants (curiosity / benefit / urgency)
2. Preview text that complements the subject
3. Email body: clear hierarchy, one idea per section
4. CTAs: action-oriented, specific, low-friction
5. Plain-text version for deliverability
Every email should have one clear goal. Remove everything else."""

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
    agent = EmailCopywriterAgentAgent()
    console.print(f"[bold green]Email Copywriter Agent[/bold green]")
    agent.chat()
