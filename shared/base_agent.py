"""
shared/base_agent.py
Base class for all agents in this repository.
Implements the core agentic loop using the Anthropic API.
"""

import json
import os
from typing import Any
from anthropic import Anthropic
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

console = Console()
MODEL = "claude-sonnet-4-5"
MAX_TOKENS = 4096
MAX_ITERATIONS = 10


class BaseAgent:
    """
    Base agent class. Subclass this and override:
      - system_prompt: str
      - tools: list[dict]
      - handle_tool_call(tool_name, tool_input) -> str
    """

    system_prompt: str = "You are a helpful AI agent."
    tools: list[dict] = []

    def __init__(self):
        self.client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.conversation_history: list[dict] = []

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        """Override in subclass to handle tool calls."""
        return f"Tool '{tool_name}' not implemented."

    def run(self, user_message: str) -> str:
        """Run the agent on a user message, executing the agentic loop."""
        self.conversation_history.append({"role": "user", "content": user_message})

        for iteration in range(MAX_ITERATIONS):
            kwargs: dict[str, Any] = {
                "model": MODEL,
                "max_tokens": MAX_TOKENS,
                "system": self.system_prompt,
                "messages": self.conversation_history,
            }
            if self.tools:
                kwargs["tools"] = self.tools

            response = self.client.messages.create(**kwargs)

            # Collect all content blocks from the response
            tool_uses = []
            tool_results = []
            final_text = ""

            for block in response.content:
                if block.type == "text":
                    final_text = block.text
                elif block.type == "tool_use":
                    tool_uses.append(block)

            # If there are tool calls, execute them all before continuing
            if tool_uses:
                self.conversation_history.append(
                    {"role": "assistant", "content": response.content}
                )
                for tool_use in tool_uses:
                    console.print(f"[dim]→ Using tool: {tool_use.name}[/dim]")
                    result = self.handle_tool_call(tool_use.name, tool_use.input)
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": str(result),
                        }
                    )

                self.conversation_history.append(
                    {"role": "user", "content": tool_results}
                )
                continue  # Continue the loop so Claude can process tool results

            # No tool calls — we have a final response
            self.conversation_history.append(
                {"role": "assistant", "content": final_text}
            )
            return final_text

        return "Max iterations reached. Please try again with a more specific request."

    def chat(self):
        """Interactive chat loop for the agent."""
        console.print(f"\n[bold]Agent ready.[/bold] Type 'exit' to quit.\n")
        while True:
            try:
                user_input = input("You: ").strip()
                if user_input.lower() in ("exit", "quit"):
                    break
                if not user_input:
                    continue
                response = self.run(user_input)
                console.print("\n[bold]Agent:[/bold]")
                console.print(Markdown(response))
                console.print()
            except KeyboardInterrupt:
                break
