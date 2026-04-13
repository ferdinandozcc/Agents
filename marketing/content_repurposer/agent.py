"""
marketing/content_repurposer/agent.py
Content Repurposer Agent — Turns a blog post into LinkedIn posts, tweets, email, and video scripts.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ContentRepurposerAgentAgent(BaseAgent):
    system_prompt = """You are a content strategist and repurposing specialist. Given a piece of content:
1. Extract the 5 most shareable insights
2. Write 3 LinkedIn posts (thought leadership angle)
3. Write 5 tweets/X posts (punchy, engaging)
4. Write an email newsletter version
5. Write a short-form video script (60-90 seconds)
Adapt tone per platform — same message, different voice."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL]

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
    agent = ContentRepurposerAgentAgent()
    console.print(f"[bold green]Content Repurposer Agent[/bold green]")
    agent.chat()
