"""
personal/daily_brief/agent.py
Daily Brief Agent — compiles a morning digest from calendar, tasks, and news.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import (
    FETCH_URL_TOOL, GET_CURRENT_TIME_TOOL, WRITE_FILE_TOOL,
    dispatch_common_tool
)

BRIEFING_TOPICS_TOOL = {
    "name": "get_briefing_topics",
    "description": "Get the user's configured briefing topics and news sources.",
    "input_schema": {
        "type": "object",
        "properties": {},
        "required": [],
    },
}

DEFAULT_TOPICS = {
    "news_sources": [
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://techcrunch.com",
    ],
    "topics_of_interest": ["AI", "product management", "tech industry"],
    "tasks": [
        "Review Q2 roadmap draft",
        "Send weekly update to stakeholders",
        "Follow up with design team on mockups",
    ],
    "calendar_events": [
        {"time": "09:00", "title": "Standup"},
        {"time": "14:00", "title": "Product review with eng"},
        {"time": "16:30", "title": "1:1 with manager"},
    ],
}


class DailyBriefAgent(BaseAgent):
    system_prompt = """You are a personal morning brief assistant. Your job is to compile a concise, 
actionable daily digest for the user. 

Start by getting the current time, then gather news from the configured sources, and finally 
produce a structured brief that includes:
1. Date and greeting
2. Today's calendar events
3. Top 3 tasks for the day
4. 3-5 news headlines relevant to the user's interests with one-line summaries
5. A one-line motivational close

Keep it scannable — use headers and bullets. Aim for something readable in under 2 minutes."""

    tools = [FETCH_URL_TOOL, GET_CURRENT_TIME_TOOL, WRITE_FILE_TOOL, BRIEFING_TOPICS_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "get_briefing_topics":
            import json
            return json.dumps(DEFAULT_TOPICS, indent=2)
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = DailyBriefAgent()
    console.print("[bold green]Daily Brief Agent[/bold green]")
    response = agent.run("Generate my morning brief for today.")
    from rich.markdown import Markdown
    console.print(Markdown(response))
