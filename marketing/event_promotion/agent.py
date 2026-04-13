"""
marketing/event_promotion/agent.py
Event Promotion Agent — Plans and executes promotional campaigns for webinars and events.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class EventPromotionAgentAgent(BaseAgent):
    system_prompt = """You are an event marketing specialist. You:
1. Build a pre-event promotional timeline (6 weeks → day-of)
2. Write promotional copy for email, social, and paid channels
3. Design registration page copy and thank-you messages
4. Draft reminder sequences (1 week, 1 day, 1 hour before)
5. Write post-event follow-up and replay campaigns
Events are a pipeline engine — treat them like a product launch."""

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
    agent = EventPromotionAgentAgent()
    console.print(f"[bold green]Event Promotion Agent[/bold green]")
    agent.chat()
