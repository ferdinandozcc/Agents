"""
personal/learning_assistant/agent.py
Learning Assistant Agent — Creates personalized study plans, quizzes, and tracks learning progress.
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


class LearningAssistantAgentAgent(BaseAgent):
    system_prompt = """You are a personalized learning coach and tutor. You:
1. Assess the user's current knowledge level on a topic
2. Create a structured study plan with milestones
3. Explain concepts clearly with examples and analogies
4. Quiz the user with spaced repetition
5. Track what's been learned and what needs review
Adapt explanations to the user's level — beginner to advanced."""

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
    agent = LearningAssistantAgentAgent()
    console.print(f"[bold green]Learning Assistant Agent[/bold green]")
    agent.chat()
