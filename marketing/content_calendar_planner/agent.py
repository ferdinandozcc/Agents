"""
marketing/content_calendar_planner/agent.py
Content Calendar Planner Agent — Builds a monthly content calendar aligned to campaigns and launches.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class ContentCalendarPlannerAgentAgent(BaseAgent):
    system_prompt = """You are a content strategy and editorial planning specialist. You:
1. Map content to business goals, campaigns, and product launches
2. Plan content mix: blog, social, email, video, webinar
3. Assign topics, formats, owners, and publish dates
4. Ensure SEO keyword coverage in the plan
5. Build in evergreen and seasonal content
A good content calendar has a reason for every piece."""

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
    agent = ContentCalendarPlannerAgentAgent()
    console.print(f"[bold green]Content Calendar Planner Agent[/bold green]")
    agent.chat()
