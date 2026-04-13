"""
product/nps_analyzer/agent.py
NPS Analyzer Agent — Processes NPS responses, segments by score, and surfaces action items.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class NPSAnalyzerAgentAgent(BaseAgent):
    system_prompt = """You are a customer insights analyst specializing in NPS analysis. You:
1. Calculate NPS score from raw responses (Promoters − Detractors)
2. Segment feedback by promoter / passive / detractor
3. Extract themes from open-text comments
4. Identify top drivers of high and low scores
5. Recommend 3 targeted actions to improve NPS
Track NPS trends over time and correlate with product changes."""

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
    agent = NPSAnalyzerAgentAgent()
    console.print(f"[bold green]NPS Analyzer Agent[/bold green]")
    agent.chat()
