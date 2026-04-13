"""
engineering/sprint_velocity_tracker/agent.py
Sprint Velocity Tracker Agent — Tracks story points, velocity trends, and capacity for planning.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class SprintVelocityTrackerAgentAgent(BaseAgent):
    system_prompt = """You are an agile metrics and delivery forecasting assistant. You:
1. Track story points completed per sprint
2. Calculate rolling average velocity over last 3-6 sprints
3. Flag velocity drops and investigate causes
4. Forecast delivery dates for roadmap items based on velocity
5. Capacity plan for upcoming sprints accounting for PTO
Velocity is a planning tool, not a performance metric."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

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
    agent = SprintVelocityTrackerAgentAgent()
    console.print(f"[bold green]Sprint Velocity Tracker Agent[/bold green]")
    agent.chat()
