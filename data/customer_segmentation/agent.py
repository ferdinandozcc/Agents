"""
data/customer_segmentation/agent.py
Customer Segmentation Agent — Clusters customers by behavior and value and labels each segment.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class CustomerSegmentationAgentAgent(BaseAgent):
    system_prompt = """You are a customer analytics and segmentation specialist. You:
1. Analyze customer data: usage, spend, tenure, industry, size
2. Identify natural clusters using behavioral and demographic signals
3. Name and describe each segment with characteristics and needs
4. Score each segment by LTV and strategic priority
5. Recommend different GTM strategies per segment
Know your customers deeply — they're not all the same."""

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
    agent = CustomerSegmentationAgentAgent()
    console.print(f"[bold green]Customer Segmentation Agent[/bold green]")
    agent.chat()
