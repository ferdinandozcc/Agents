"""
engineering/architecture_advisor/agent.py
Architecture Advisor Agent — Reviews system designs and suggests improvements for scalability.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class ArchitectureAdvisorAgentAgent(BaseAgent):
    system_prompt = """You are a principal engineer and systems architect. You:
1. Review architecture diagrams or descriptions
2. Identify single points of failure and bottlenecks
3. Assess for scalability, reliability, and maintainability
4. Suggest patterns: CQRS, event sourcing, saga, circuit breaker
5. Trade-off analysis: simplicity vs. resilience vs. performance
Good architecture enables the business — don't over-engineer."""

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
    agent = ArchitectureAdvisorAgentAgent()
    console.print(f"[bold green]Architecture Advisor Agent[/bold green]")
    agent.chat()
