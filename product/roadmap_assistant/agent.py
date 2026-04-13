"""
product/roadmap_assistant/agent.py
Roadmap Assistant — prioritizes backlog items using impact/effort scoring.
"""

import sys
import os
import json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool

SCORE_ITEMS_TOOL = {
    "name": "score_backlog_items",
    "description": "Score backlog items using RICE or Impact/Effort framework.",
    "input_schema": {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "reach": {"type": "integer", "description": "Users impacted (1-10)"},
                        "impact": {"type": "integer", "description": "Impact per user (1-10)"},
                        "confidence": {"type": "integer", "description": "Confidence % (0-100)"},
                        "effort": {"type": "integer", "description": "Effort in weeks"},
                    },
                },
            },
            "framework": {"type": "string", "enum": ["RICE", "impact_effort"], "default": "RICE"},
        },
        "required": ["items"],
    },
}


def score_items(items: list, framework: str = "RICE") -> str:
    results = []
    for item in items:
        name = item.get("name", "Unknown")
        if framework == "RICE":
            reach = item.get("reach", 5)
            impact = item.get("impact", 5)
            confidence = item.get("confidence", 80) / 100
            effort = max(item.get("effort", 1), 0.1)
            score = (reach * impact * confidence) / effort
            results.append({"name": name, "score": round(score, 2), "framework": "RICE"})
        else:
            impact = item.get("impact", 5)
            effort = item.get("effort", 5)
            score = impact / max(effort, 0.1)
            results.append({"name": name, "score": round(score, 2), "framework": "Impact/Effort"})

    results.sort(key=lambda x: x["score"], reverse=True)
    return json.dumps(results, indent=2)


class RoadmapAssistantAgent(BaseAgent):
    system_prompt = """You are a product strategy advisor helping teams prioritize their roadmap.

Your approach:
1. Help the user define or import their backlog items
2. Guide them through scoring each item (RICE or Impact/Effort)
3. Score and rank items
4. Present a prioritized roadmap with reasoning
5. Flag strategic considerations (dependencies, quick wins, big bets)

Output a prioritized roadmap table:
| Priority | Item | Score | Rationale | Quarter |
|---|---|---|---|---|

Also identify:
- **Quick wins** (high impact, low effort)
- **Big bets** (high impact, high effort — need confidence)
- **Traps** (low impact, high effort — cut or descope)

Always explain the reasoning behind prioritization, not just the scores."""

    tools = [SCORE_ITEMS_TOOL, READ_FILE_TOOL, WRITE_FILE_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "score_backlog_items":
            return score_items(tool_input["items"], tool_input.get("framework", "RICE"))
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = RoadmapAssistantAgent()
    console.print("[bold green]Roadmap Assistant[/bold green]")
    console.print("Let's prioritize your backlog. Describe your items or paste a list.\n")
    agent.chat()
