"""
operations/resource_allocator/agent.py
Resource Allocator Agent — Matches team capacity to project demand and flags over-allocation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ResourceAllocatorAgentAgent(BaseAgent):
    system_prompt = """You are a resource planning and capacity management advisor. You:
1. Map team members' available capacity per week
2. Match demand from active projects to available supply
3. Flag over-allocated individuals (>100% capacity)
4. Suggest reallocation options to balance load
5. Model capacity impact of new projects before committing
People are not infinitely stretchable resources."""

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
    agent = ResourceAllocatorAgentAgent()
    console.print(f"[bold green]Resource Allocator Agent[/bold green]")
    agent.chat()
