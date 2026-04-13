"""
marketing/newsletter_writer/agent.py
Newsletter Writer Agent — Writes weekly newsletters from a brief, with subject line variants.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class NewsletterWriterAgentAgent(BaseAgent):
    system_prompt = """You are a newsletter editor and writer. You produce:
1. Subject line: 3 variants (personalized, curiosity, value)
2. Opening hook: 1-2 sentences that compel reading
3. Main story or insight (300-500 words)
4. Supporting sections: quick links, tips, or community updates
5. CTA: one clear next step for the reader
Newsletter voice should feel like a smart friend, not a press release."""

    tools = [WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

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
    agent = NewsletterWriterAgentAgent()
    console.print(f"[bold green]Newsletter Writer Agent[/bold green]")
    agent.chat()
