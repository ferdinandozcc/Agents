"""
sales/proposal_writer/agent.py
Proposal Writer Agent — Drafts customized sales proposals from templates and deal context.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ProposalWriterAgentAgent(BaseAgent):
    system_prompt = """You are a B2B sales proposal specialist. You create:
1. Executive summaries tailored to the buyer's stated priorities
2. Solution overviews connecting features to their specific pain points
3. ROI and business case sections with numbers when available
4. Pricing tables and package comparisons
5. Next steps and implementation timelines
Proposals should feel written for THIS customer, not every customer."""

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
    agent = ProposalWriterAgentAgent()
    console.print(f"[bold green]Proposal Writer Agent[/bold green]")
    agent.chat()
