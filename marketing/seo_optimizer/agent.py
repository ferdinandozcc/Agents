"""
marketing/seo_optimizer/agent.py
SEO Optimizer Agent — Audits pages for SEO issues, suggests keywords, and improves meta copy.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import FETCH_URL_TOOL, SEARCH_TOOL, WRITE_FILE_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class SEOOptimizerAgentAgent(BaseAgent):
    system_prompt = """You are an SEO strategist and content optimizer. You:
1. Audit a page for on-page SEO: title, meta, headers, keyword density, internal links
2. Research relevant keywords and search intent
3. Rewrite titles and meta descriptions to improve CTR
4. Suggest content additions to improve topical authority
5. Flag technical issues: missing alt text, slow load signals, canonical issues
SEO is a long game — focus on user value first."""

    tools = [FETCH_URL_TOOL, SEARCH_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL]

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
    agent = SEOOptimizerAgentAgent()
    console.print(f"[bold green]SEO Optimizer Agent[/bold green]")
    agent.chat()
