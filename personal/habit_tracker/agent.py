"""
personal/habit_tracker/agent.py
Habit & Goal Tracker Agent — logs habits, tracks streaks, and provides motivational nudges.
"""

import sys
import os
import json
from datetime import datetime, timedelta
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import GET_CURRENT_TIME_TOOL, dispatch_common_tool

DATA_FILE = Path(__file__).parent / "habit_data.json"

LOG_HABIT_TOOL = {
    "name": "log_habit",
    "description": "Log completion of a habit for today.",
    "input_schema": {
        "type": "object",
        "properties": {
            "habit_name": {"type": "string"},
            "completed": {"type": "boolean", "default": True},
            "notes": {"type": "string", "default": ""},
        },
        "required": ["habit_name"],
    },
}

GET_HABITS_TOOL = {
    "name": "get_habits",
    "description": "Get all habits and their current streak data.",
    "input_schema": {"type": "object", "properties": {}, "required": []},
}

ADD_HABIT_TOOL = {
    "name": "add_habit",
    "description": "Add a new habit to track.",
    "input_schema": {
        "type": "object",
        "properties": {
            "habit_name": {"type": "string"},
            "frequency": {"type": "string", "enum": ["daily", "weekdays", "weekly"], "default": "daily"},
            "goal": {"type": "string", "description": "Why you want to build this habit."},
        },
        "required": ["habit_name"],
    },
}


def load_data() -> dict:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {"habits": {}, "logs": {}}


def save_data(data: dict):
    DATA_FILE.write_text(json.dumps(data, indent=2))


def compute_streak(logs: dict, habit_name: str) -> int:
    today = datetime.now().date()
    streak = 0
    for i in range(365):
        day = (today - timedelta(days=i)).isoformat()
        if logs.get(day, {}).get(habit_name):
            streak += 1
        else:
            break
    return streak


class HabitTrackerAgent(BaseAgent):
    system_prompt = """You are an encouraging habit and goal tracking coach. 

You help users:
- Log their daily habits
- Check their current streaks
- Add new habits to track
- Get motivational summaries and insights about their progress

When a user logs in, greet them warmly, show their current streaks, celebrate completions, 
and gently encourage any missed habits. Be positive, specific, and brief.

Use the available tools to read and write habit data. Always show streak counts when relevant."""

    tools = [LOG_HABIT_TOOL, GET_HABITS_TOOL, ADD_HABIT_TOOL, GET_CURRENT_TIME_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result

        data = load_data()
        today = datetime.now().date().isoformat()

        if tool_name == "log_habit":
            habit = tool_input["habit_name"]
            completed = tool_input.get("completed", True)
            notes = tool_input.get("notes", "")
            if today not in data["logs"]:
                data["logs"][today] = {}
            data["logs"][today][habit] = {"completed": completed, "notes": notes}
            save_data(data)
            streak = compute_streak(data["logs"], habit)
            return f"Logged '{habit}' as {'completed' if completed else 'skipped'} for {today}. Current streak: {streak} days."

        if tool_name == "get_habits":
            if not data["habits"]:
                return "No habits tracked yet. Use add_habit to get started."
            output = []
            for name, info in data["habits"].items():
                streak = compute_streak(data["logs"], name)
                today_done = data["logs"].get(today, {}).get(name, {}).get("completed", False)
                output.append(
                    f"- {name} | Streak: {streak} days | Today: {'✓' if today_done else '○'} | Goal: {info.get('goal', '')}"
                )
            return "\n".join(output)

        if tool_name == "add_habit":
            name = tool_input["habit_name"]
            data["habits"][name] = {
                "frequency": tool_input.get("frequency", "daily"),
                "goal": tool_input.get("goal", ""),
                "created": today,
            }
            save_data(data)
            return f"Habit '{name}' added successfully."

        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = HabitTrackerAgent()
    console.print("[bold green]Habit Tracker Agent[/bold green]")
    agent.chat()
