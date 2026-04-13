"""
personal/social_media_manager/agent.py
Social Media Manager Agent — Drafts posts, schedules content, and tracks engagement across platforms.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class SocialMediaManagerAgentAgent(BaseAgent):
    system_prompt = """You are a social media strategist and content creator. Help users:
1. Draft platform-optimized posts (LinkedIn, Twitter/X, Instagram)
2. Build content calendars aligned to goals
3. Suggest hashtags, posting times, and engagement tactics
4. Repurpose long-form content into social snippets
5. Analyze what content is performing well
Adapt tone per platform — professional for LinkedIn, casual for Twitter."""

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
    agent = SocialMediaManagerAgentAgent()
    console.print(f"[bold green]Social Media Manager Agent[/bold green]")
    agent.chat()
