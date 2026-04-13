"""
operations/change_management_planner/agent.py
Change Management Planner Agent — Plans org change initiatives with stakeholder comms and training plans.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, dispatch_common_tool


class ChangeManagementPlannerAgentAgent(BaseAgent):
    system_prompt = """You are an organizational change management consultant. You:
1. Assess the scope and impact of a change initiative
2. Identify and map stakeholders (supporters, resistors, neutral)
3. Create a communication plan with messages per audience
4. Build a training and enablement plan
5. Define success metrics and adoption milestones
Use ADKAR or Kotter frameworks where appropriate."""

    tools = [WRITE_FILE_TOOL]

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
    agent = ChangeManagementPlannerAgentAgent()
    console.print(f"[bold green]Change Management Planner Agent[/bold green]")
    agent.chat()
