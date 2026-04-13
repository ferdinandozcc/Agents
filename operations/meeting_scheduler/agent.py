"""
operations/meeting_scheduler/agent.py
Meeting Scheduler Agent — finds optimal slots across calendars and drafts agendas.
"""

import sys
import os
import json
from datetime import datetime, timedelta
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

FIND_SLOTS_TOOL = {
    "name": "find_available_slots",
    "description": "Find available time slots for a group of attendees over a date range.",
    "input_schema": {
        "type": "object",
        "properties": {
            "attendees": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of attendee names or emails.",
            },
            "duration_minutes": {"type": "integer", "default": 60},
            "days_ahead": {"type": "integer", "default": 5, "description": "How many business days to look ahead."},
            "preferred_hours": {
                "type": "object",
                "properties": {
                    "start": {"type": "string", "default": "09:00"},
                    "end": {"type": "string", "default": "17:00"},
                },
            },
        },
        "required": ["attendees"],
    },
}

DRAFT_AGENDA_TOOL = {
    "name": "draft_agenda",
    "description": "Draft a meeting agenda given a purpose and participant list.",
    "input_schema": {
        "type": "object",
        "properties": {
            "meeting_title": {"type": "string"},
            "purpose": {"type": "string"},
            "duration_minutes": {"type": "integer"},
            "attendees": {"type": "array", "items": {"type": "string"}},
            "desired_outcomes": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["meeting_title", "purpose", "duration_minutes"],
    },
}

SEND_INVITE_TOOL = {
    "name": "send_calendar_invite",
    "description": "Send a calendar invite to attendees (simulated).",
    "input_schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "datetime_iso": {"type": "string"},
            "duration_minutes": {"type": "integer"},
            "attendees": {"type": "array", "items": {"type": "string"}},
            "agenda": {"type": "string"},
            "location": {"type": "string", "default": "Zoom"},
        },
        "required": ["title", "datetime_iso", "attendees"],
    },
}


def find_slots(attendees: list, duration: int = 60, days_ahead: int = 5) -> str:
    """Simulate finding available slots."""
    slots = []
    base = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    for day in range(days_ahead):
        candidate = base + timedelta(days=day + 1)
        if candidate.weekday() >= 5:
            continue
        for hour in [9, 10, 14, 15, 16]:
            slot = candidate.replace(hour=hour)
            slots.append({
                "datetime": slot.isoformat(),
                "display": slot.strftime("%A %b %d, %I:%M %p"),
                "available_for": attendees,
                "conflicts": [],
            })
        if len(slots) >= 5:
            break
    return json.dumps(slots[:5], indent=2)


class MeetingSchedulerAgent(BaseAgent):
    system_prompt = """You are an executive assistant specializing in meeting coordination.

Your workflow:
1. Understand the meeting purpose, required attendees, and constraints
2. Find optimal time slots that work for everyone
3. Recommend the best slot with reasoning (avoid Monday mornings, end-of-day Fridays, etc.)
4. Draft a tight, purposeful agenda with clear time allocations
5. Send the calendar invite with the agenda attached

Always ask:
- Who needs to attend (required vs. optional)?
- What's the meeting for? What decisions need to be made?
- How long does it need to be? (Challenge if it seems too long)
- Any time constraints or preferences?

Good meetings have: a clear purpose, right attendees, tight agenda, pre-reads, and end 5 min early."""

    tools = [FIND_SLOTS_TOOL, DRAFT_AGENDA_TOOL, SEND_INVITE_TOOL, GET_CURRENT_TIME_TOOL, WRITE_FILE_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result

        if tool_name == "find_available_slots":
            return find_slots(
                tool_input.get("attendees", []),
                tool_input.get("duration_minutes", 60),
                tool_input.get("days_ahead", 5),
            )

        if tool_name == "draft_agenda":
            duration = tool_input.get("duration_minutes", 60)
            outcomes = tool_input.get("desired_outcomes", ["Alignment on next steps"])
            attendees = tool_input.get("attendees", [])
            agenda = f"""# {tool_input['meeting_title']}
**Purpose**: {tool_input['purpose']}  
**Duration**: {duration} minutes  
**Attendees**: {', '.join(attendees) if attendees else 'TBD'}

## Agenda
- **[5 min]** Welcome & context setting
- **[{duration - 20} min]** Discussion: {tool_input['purpose']}
- **[10 min]** Decisions & action items
- **[5 min]** Next steps & close

## Desired Outcomes
{chr(10).join(f'- {o}' for o in outcomes)}

## Pre-reads
- [Add relevant docs here]
"""
            return agenda

        if tool_name == "send_calendar_invite":
            return (
                f"✓ Invite sent: '{tool_input['title']}' on {tool_input['datetime_iso']} "
                f"to {', '.join(tool_input['attendees'])} via {tool_input.get('location', 'Zoom')}."
            )

        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = MeetingSchedulerAgent()
    console.print("[bold green]Meeting Scheduler Agent[/bold green]")
    console.print("Who needs to meet, and what's it about?\n")
    agent.chat()
