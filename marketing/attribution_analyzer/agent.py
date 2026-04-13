"""
marketing/attribution_analyzer/agent.py
Attribution Analyzer Agent — Maps marketing touchpoints to revenue and scores channel contribution.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class AttributionAnalyzerAgentAgent(BaseAgent):
    system_prompt = """You are a marketing attribution and ROI analyst. You:
1. Map the customer journey from first touch to closed revenue
2. Apply attribution models: first touch, last touch, linear, time decay
3. Score each channel's contribution to pipeline and revenue
4. Identify highest and lowest ROI channels
5. Recommend budget reallocation based on attribution data
Attribution is imperfect — present multiple models and their trade-offs."""

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
    agent = AttributionAnalyzerAgentAgent()
    console.print(f"[bold green]Attribution Analyzer Agent[/bold green]")
    agent.chat()
