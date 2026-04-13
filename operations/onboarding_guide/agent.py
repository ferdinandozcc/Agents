"""
operations/onboarding_guide/agent.py
Onboarding Guide Agent — walks new team members through processes, docs, and tools step by step.
"""

import sys
import os
import json
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

GET_ONBOARDING_PLAN_TOOL = {
    "name": "get_onboarding_plan",
    "description": "Get the onboarding checklist and plan for a given role.",
    "input_schema": {
        "type": "object",
        "properties": {
            "role": {"type": "string", "description": "The new hire's role (e.g., 'PM', 'Engineer', 'Designer')."},
            "week": {"type": "integer", "description": "Which week of onboarding (1-4).", "default": 1},
        },
        "required": ["role"],
    },
}

MARK_COMPLETE_TOOL = {
    "name": "mark_task_complete",
    "description": "Mark an onboarding task as complete for tracking.",
    "input_schema": {
        "type": "object",
        "properties": {
            "task_id": {"type": "string"},
            "person_name": {"type": "string"},
            "notes": {"type": "string", "default": ""},
        },
        "required": ["task_id", "person_name"],
    },
}

ONBOARDING_PLANS = {
    "PM": {
        1: [
            {"id": "pm-1-1", "task": "Set up Notion, Jira, Figma, and Slack accounts"},
            {"id": "pm-1-2", "task": "Read the product strategy doc and company mission"},
            {"id": "pm-1-3", "task": "Shadow 3 customer calls"},
            {"id": "pm-1-4", "task": "Meet with each eng team lead for 30 min"},
            {"id": "pm-1-5", "task": "Review the current roadmap and last 3 PRDs"},
        ],
        2: [
            {"id": "pm-2-1", "task": "Run your first sprint planning session (with support)"},
            {"id": "pm-2-2", "task": "Write your first user story and get it reviewed"},
            {"id": "pm-2-3", "task": "Present a competitor analysis in team meeting"},
            {"id": "pm-2-4", "task": "Set up weekly 1:1s with design, eng, and data leads"},
        ],
        3: [
            {"id": "pm-3-1", "task": "Own a small feature end-to-end"},
            {"id": "pm-3-2", "task": "Conduct 3 user interviews independently"},
            {"id": "pm-3-3", "task": "Draft your 30-60-90 plan"},
        ],
        4: [
            {"id": "pm-4-1", "task": "Present 30-60-90 plan to leadership"},
            {"id": "pm-4-2", "task": "Submit your first PRD for review"},
            {"id": "pm-4-3", "task": "Retrospective with your manager on onboarding"},
        ],
    },
    "Engineer": {
        1: [
            {"id": "eng-1-1", "task": "Set up dev environment (follow engineering setup doc)"},
            {"id": "eng-1-2", "task": "Complete first PR — a small bug fix or doc update"},
            {"id": "eng-1-3", "task": "Read the architecture overview"},
            {"id": "eng-1-4", "task": "Attend team standup and sprint ceremonies"},
            {"id": "eng-1-5", "task": "Meet your assigned onboarding buddy"},
        ],
        2: [
            {"id": "eng-2-1", "task": "Pick up and complete a starter ticket solo"},
            {"id": "eng-2-2", "task": "Review 3 PRs from teammates"},
            {"id": "eng-2-3", "task": "Walk through the CI/CD pipeline with a senior engineer"},
        ],
    },
}

PROGRESS_FILE = Path(__file__).parent / "progress.json"


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {}


def save_progress(data: dict):
    PROGRESS_FILE.write_text(json.dumps(data, indent=2))


class OnboardingGuideAgent(BaseAgent):
    system_prompt = """You are a friendly and thorough onboarding coach for new team members.

Your role:
1. Welcome new hires warmly and learn their name and role
2. Retrieve their personalized onboarding plan for the current week
3. Walk them through each task — explain WHY it matters, not just what to do
4. Answer questions about tools, processes, and team norms
5. Track completed tasks and celebrate progress
6. Proactively surface things they should know before they ask

Tone: warm, encouraging, patient. Never make them feel bad for not knowing something.
Always offer context and point to resources when relevant.

Start by asking: "Welcome! What's your name and what role are you joining in?"
"""

    tools = [GET_ONBOARDING_PLAN_TOOL, MARK_COMPLETE_TOOL, READ_FILE_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result

        if tool_name == "get_onboarding_plan":
            role = tool_input.get("role", "PM")
            week = tool_input.get("week", 1)
            plan = ONBOARDING_PLANS.get(role, ONBOARDING_PLANS["PM"])
            week_tasks = plan.get(week, plan.get(1, []))
            progress = load_progress()
            for task in week_tasks:
                task["completed"] = task["id"] in progress
            return json.dumps({"role": role, "week": week, "tasks": week_tasks}, indent=2)

        if tool_name == "mark_task_complete":
            progress = load_progress()
            progress[tool_input["task_id"]] = {
                "person": tool_input["person_name"],
                "notes": tool_input.get("notes", ""),
            }
            save_progress(progress)
            return f"Task {tool_input['task_id']} marked complete for {tool_input['person_name']}."

        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = OnboardingGuideAgent()
    console.print("[bold green]Onboarding Guide Agent[/bold green]\n")
    agent.chat()
