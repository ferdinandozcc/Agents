"""
marketing/influencer_researcher/agent.py
Influencer Researcher Agent — Finds and scores influencers by niche, audience size, and engagement.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import SEARCH_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class InfluencerResearcherAgentAgent(BaseAgent):
    system_prompt = """You are an influencer marketing strategist. You:
1. Research influencers in a given niche using web search
2. Score by: audience size, engagement rate, content quality, brand fit
3. Flag red flags: bought followers, brand conflicts, controversial content
4. Suggest outreach approach and collaboration format
5. Estimate reach and CPM for budget planning
Micro-influencers often outperform mega-influencers on ROI."""

    tools = [SEARCH_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, SEARCH_TOOL]

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
    agent = InfluencerResearcherAgentAgent()
    console.print(f"[bold green]Influencer Researcher Agent[/bold green]")
    agent.chat()
