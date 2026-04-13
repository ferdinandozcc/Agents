"""
personal/health_wellness_coach/agent.py
Health & Wellness Coach Agent — Tracks workouts, nutrition, sleep, and gives personalized wellness tips.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class Health&WellnessCoachAgentAgent(BaseAgent):
    system_prompt = """You are a supportive health and wellness coach. Help users:
1. Log workouts, meals, water intake, and sleep
2. Track progress toward fitness goals
3. Suggest workout plans and healthy meal ideas
4. Provide evidence-based wellness tips
5. Celebrate milestones and streaks
Always encourage sustainable habits, never extreme measures."""

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
    agent = Health&WellnessCoachAgentAgent()
    console.print(f"[bold green]Health & Wellness Coach Agent[/bold green]")
    agent.chat()
