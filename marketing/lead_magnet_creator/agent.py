"""
marketing/lead_magnet_creator/agent.py
Lead Magnet Creator Agent — Designs and writes lead magnet content (guides, checklists, templates).
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, dispatch_common_tool


class LeadMagnetCreatorAgentAgent(BaseAgent):
    system_prompt = """You are a lead generation content strategist. You create:
1. Topic selection: identify high-value problems your ICP wants solved
2. Format recommendation: guide, checklist, template, calculator, swipe file
3. Outline and full content for the chosen lead magnet
4. Landing page copy and thank-you page messaging
5. Email nurture sequence triggered by the download
Lead magnets should deliver immediate, specific value."""

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
    agent = LeadMagnetCreatorAgentAgent()
    console.print(f"[bold green]Lead Magnet Creator Agent[/bold green]")
    agent.chat()
