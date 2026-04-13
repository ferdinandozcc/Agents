"""
product/feedback_analyzer/agent.py
Feedback Analyzer Agent — clusters user feedback and surfaces top themes and pain points.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool

CLUSTER_FEEDBACK_TOOL = {
    "name": "cluster_feedback",
    "description": "Cluster a list of feedback items into themes and count occurrences.",
    "input_schema": {
        "type": "object",
        "properties": {
            "feedback_items": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of raw feedback strings.",
            },
            "max_clusters": {"type": "integer", "default": 8},
        },
        "required": ["feedback_items"],
    },
}

SENTIMENT_TOOL = {
    "name": "analyze_sentiment",
    "description": "Analyze the overall sentiment of a feedback collection (positive/neutral/negative breakdown).",
    "input_schema": {
        "type": "object",
        "properties": {
            "feedback_text": {"type": "string"},
        },
        "required": ["feedback_text"],
    },
}


class FeedbackAnalyzerAgent(BaseAgent):
    system_prompt = """You are a user research analyst specializing in qualitative feedback analysis.

When given user feedback (from surveys, reviews, support tickets, NPS responses, etc.), you will:

1. **Cluster** the feedback into 5-10 distinct themes
2. **Quantify** each theme (approximate % or count)
3. **Prioritize** themes by frequency × severity
4. **Extract** representative quotes for each theme
5. **Identify** the top 3 pain points and top 3 positive signals
6. **Recommend** 3 actionable product improvements

Output format:
## Feedback Analysis Report

### Summary
[2-3 sentence executive summary]

### Sentiment Overview
[Positive / Neutral / Negative breakdown]

### Top Themes
| Theme | Volume | Sentiment | Representative Quote |
|---|---|---|---|

### Pain Points (Top 3)

### Positive Signals (Top 3)

### Recommended Actions

You can analyze text pasted directly or from a file."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, CLUSTER_FEEDBACK_TOOL, SENTIMENT_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name in ("cluster_feedback", "analyze_sentiment"):
            # Signal to Claude to do this analysis itself
            return "Use your language understanding to perform this analysis on the provided feedback."
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = FeedbackAnalyzerAgent()
    console.print("[bold green]Feedback Analyzer Agent[/bold green]")
    console.print("Paste your feedback data, or provide a file path to analyze.\n")
    agent.chat()
