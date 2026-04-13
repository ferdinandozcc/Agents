"""
personal/job_application_tracker/agent.py
Job Application Tracker Agent — Tracks applications, deadlines, follow-ups, and interview prep notes.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, SEARCH_TOOL, dispatch_common_tool

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web for current information.",
    "input_schema": {
        "type": "object",
        "properties": {"query": {"type": "string"}},
        "required": ["query"],
    },
}


class JobApplicationTrackerAgentAgent(BaseAgent):
    system_prompt = """You are a career coach and job search assistant. Help users:
1. Log job applications with company, role, date, and status
2. Track deadlines and follow-up reminders
3. Store interview notes and feedback
4. Prep for interviews with company research and common questions
5. Produce a weekly job search summary
Be encouraging throughout the job search process."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, SEARCH_TOOL, SEARCH_TOOL]

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
    agent = JobApplicationTrackerAgentAgent()
    console.print(f"[bold green]Job Application Tracker Agent[/bold green]")
    agent.chat()
