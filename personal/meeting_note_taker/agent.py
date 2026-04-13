"""
personal/meeting_note_taker/agent.py
Meeting Note-Taker Agent — processes transcripts into structured summaries and action items.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

EXTRACT_ACTION_ITEMS_TOOL = {
    "name": "extract_action_items",
    "description": "Extract action items from a block of meeting text. Returns a JSON list of {owner, action, due_date}.",
    "input_schema": {
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "Raw meeting text to extract from."},
        },
        "required": ["text"],
    },
}


class MeetingNoteTakerAgent(BaseAgent):
    system_prompt = """You are a professional meeting note-taker and summarizer. 

When given a meeting transcript or notes (raw or structured), produce:

## Meeting Summary
- **Date**: [date]
- **Attendees**: [list]
- **Duration**: [if available]

## Key Discussion Points
[3-7 bullet points covering the main topics]

## Decisions Made
[List of concrete decisions]

## Action Items
| Owner | Action | Due Date |
|---|---|---|
| ... | ... | ... |

## Next Meeting
[Date/topic if mentioned]

---
Be specific about owners for action items. If an owner isn't named, write "TBD". 
Extract due dates when mentioned, otherwise leave blank."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, EXTRACT_ACTION_ITEMS_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "extract_action_items":
            # In a real implementation this could call a specialized parser
            return "Use your language understanding to extract action items from the provided text."
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = MeetingNoteTakerAgent()
    console.print("[bold green]Meeting Note-Taker Agent[/bold green]")
    console.print("Paste your meeting transcript below, or provide a file path.\n")
    agent.chat()
