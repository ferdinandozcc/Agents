"""
personal/document_summarizer/agent.py
Document Summarizer Agent — Reads long PDFs, contracts, or reports and extracts key points.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class DocumentSummarizerAgentAgent(BaseAgent):
    system_prompt = """You are an expert document analyst. When given a document:
1. Provide a 3-5 sentence executive summary
2. Extract key facts, numbers, and dates
3. List action items or decisions required
4. Flag any risks, obligations, or unusual clauses
5. Answer specific questions about the document
Handle legal docs, research papers, reports, and contracts."""

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
    agent = DocumentSummarizerAgentAgent()
    console.print(f"[bold green]Document Summarizer Agent[/bold green]")
    agent.chat()
