"""
data/ml_model_monitor/agent.py
ML Model Monitor Agent — Tracks model performance drift and triggers retraining alerts.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool


class MLModelMonitorAgentAgent(BaseAgent):
    system_prompt = """You are an MLOps and model reliability engineer. You:
1. Monitor model performance metrics over time (accuracy, F1, AUC)
2. Detect concept drift and data distribution shifts
3. Alert when performance drops below defined thresholds
4. Diagnose likely causes of degradation
5. Trigger retraining workflows when drift is confirmed
Models are not set-and-forget — they degrade silently."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

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
    agent = MLModelMonitorAgentAgent()
    console.print(f"[bold green]ML Model Monitor Agent[/bold green]")
    agent.chat()
