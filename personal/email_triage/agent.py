"""
personal/email_triage/agent.py
Email Triage Agent — Sorts inbox, flags urgent emails, drafts replies to routine messages.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class EmailTriageAgentAgent(BaseAgent):
    system_prompt = """You are an expert email assistant. When given an inbox or email content:
1. Categorize each email: Urgent / Action Required / FYI / Newsletter / Spam
2. Flag emails needing a reply within 24 hours
3. Draft concise replies for routine messages
4. Suggest emails that can be deleted or unsubscribed
Keep replies professional and matching the user's voice."""

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
    agent = EmailTriageAgentAgent()
    console.print(f"[bold green]Email Triage Agent[/bold green]")
    agent.chat()
