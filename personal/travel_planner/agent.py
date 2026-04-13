"""
personal/travel_planner/agent.py
Travel Planner Agent — Books trips, finds flights, hotels, and builds day-by-day itineraries.
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


class TravelPlannerAgentAgent(BaseAgent):
    system_prompt = """You are an expert travel planner. Help users plan trips by:
1. Understanding their destination, dates, budget, and preferences
2. Searching for flight and hotel options
3. Building a detailed day-by-day itinerary with times
4. Including restaurant recommendations, transport tips, and must-sees
5. Flagging visa requirements, safety advisories, and packing tips
Always ask about travel style (luxury / budget / adventure / cultural)."""

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
    agent = TravelPlannerAgentAgent()
    console.print(f"[bold green]Travel Planner Agent[/bold green]")
    agent.chat()
