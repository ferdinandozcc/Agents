"""
product/user_story_generator/agent.py
User Story Generator — breaks down epics into detailed user stories with acceptance criteria.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, dispatch_common_tool

ESTIMATE_STORY_TOOL = {
    "name": "estimate_story_points",
    "description": "Estimate story points for a user story based on complexity signals.",
    "input_schema": {
        "type": "object",
        "properties": {
            "story": {"type": "string", "description": "The user story text."},
            "acceptance_criteria_count": {"type": "integer"},
            "has_api_integration": {"type": "boolean", "default": False},
            "has_ui_changes": {"type": "boolean", "default": False},
        },
        "required": ["story"],
    },
}


def estimate_points(story: str, ac_count: int = 0, has_api: bool = False, has_ui: bool = False) -> str:
    """Simple heuristic story point estimator."""
    base = 1
    if ac_count > 5:
        base += 2
    elif ac_count > 3:
        base += 1
    if has_api:
        base += 2
    if has_ui:
        base += 1
    scale = [1, 2, 3, 5, 8, 13]
    points = min(scale, key=lambda x: abs(x - base))
    return f"Estimated story points: {points} (based on {ac_count} ACs, API: {has_api}, UI: {has_ui})"


class UserStoryGeneratorAgent(BaseAgent):
    system_prompt = """You are a product manager and agile coach specializing in writing clear, 
actionable user stories.

Given an epic or feature description, you will:
1. Clarify the scope if needed (ask 1-2 targeted questions)
2. Break it down into individual user stories
3. For each story, produce:
   - Title
   - User story: "As a [persona], I want [action] so that [benefit]"
   - Acceptance criteria (3-6 BDD-style: Given/When/Then or checkbox format)
   - Story point estimate
   - Dependencies (if any)
   - Labels/tags (e.g., frontend, backend, API, UX)

Format the output as a clean, copy-paste-ready backlog.
Group stories by theme if there are more than 5."""

    tools = [WRITE_FILE_TOOL, ESTIMATE_STORY_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "estimate_story_points":
            return estimate_points(
                tool_input["story"],
                tool_input.get("acceptance_criteria_count", 0),
                tool_input.get("has_api_integration", False),
                tool_input.get("has_ui_changes", False),
            )
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = UserStoryGeneratorAgent()
    console.print("[bold green]User Story Generator[/bold green]")
    console.print("Describe your epic or feature and I'll generate user stories.\n")
    agent.chat()
