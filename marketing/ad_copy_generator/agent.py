"""
marketing/ad_copy_generator/agent.py
Ad Copy Generator Agent — Writes A/B variants of ad copy for Google, Meta, and LinkedIn.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, dispatch_common_tool


class AdCopyGeneratorAgentAgent(BaseAgent):
    system_prompt = """You are a performance ad copywriter. You write:
1. Google Search ads: headlines (30 chars), descriptions (90 chars), 3 variants
2. Meta/Facebook ads: primary text, headline, description — image and video formats
3. LinkedIn Sponsored Content: professional tone, lead-gen focused
4. Multiple angle variants: pain / benefit / social proof / urgency
5. Ad copy QA: character limits, policy compliance, clarity check
Great ad copy is specific, not generic."""

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
    agent = AdCopyGeneratorAgentAgent()
    console.print(f"[bold green]Ad Copy Generator Agent[/bold green]")
    agent.chat()
