"""
product/release_notes_writer/agent.py
Release Notes Writer — converts commit logs and tickets into user-facing release notes.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool

PARSE_COMMITS_TOOL = {
    "name": "parse_commits",
    "description": "Parse a git log or list of commit messages into categorized groups.",
    "input_schema": {
        "type": "object",
        "properties": {
            "commits": {"type": "string", "description": "Raw git log output or newline-separated commit messages."},
            "version": {"type": "string", "description": "Version number for this release."},
        },
        "required": ["commits"],
    },
}


class ReleaseNotesWriterAgent(BaseAgent):
    system_prompt = """You are a technical writer specializing in developer and user-facing release notes.

Given commit messages, ticket titles, or raw changelog data, produce polished release notes that:

1. **Lead with user value**, not technical details
2. Categorize changes:
   - ✨ New Features
   - 🐛 Bug Fixes
   - ⚡ Improvements
   - 🔒 Security
   - ⚠️ Breaking Changes (if any — highlight prominently)
   - 🗑️ Deprecated

3. Write each entry as: "[What changed] — [Why it matters to the user]"
4. Skip internal refactors, CI changes, and dependency bumps (unless security-relevant)
5. Add a brief "What's new in [version]" summary paragraph at the top

Tone: friendly, clear, benefit-focused. Avoid jargon. Write as if explaining to a smart non-technical user.

Always ask for the version number if not provided."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, PARSE_COMMITS_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "parse_commits":
            commits = tool_input.get("commits", "")
            lines = [c.strip() for c in commits.strip().split("\n") if c.strip()]
            return f"Found {len(lines)} commits. Proceed to categorize and rewrite them for users."
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = ReleaseNotesWriterAgent()
    console.print("[bold green]Release Notes Writer[/bold green]")
    console.print("Paste your commit log or ticket list, and I'll write the release notes.\n")
    agent.chat()
