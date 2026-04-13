"""
personal/research_assistant/agent.py
Research Assistant Agent — searches, reads, and synthesizes information on any topic.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import (
    FETCH_URL_TOOL, WRITE_FILE_TOOL,
    dispatch_common_tool
)

SEARCH_TOOL = {
    "name": "search_web",
    "description": "Search the web using DuckDuckGo and return top results.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query."},
            "num_results": {"type": "integer", "default": 5},
        },
        "required": ["query"],
    },
}


def search_web(query: str, num_results: int = 5) -> str:
    """Simple DuckDuckGo search via their HTML interface."""
    import httpx
    from bs4 import BeautifulSoup
    try:
        url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = httpx.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for r in soup.select(".result")[:num_results]:
            title_el = r.select_one(".result__title")
            snippet_el = r.select_one(".result__snippet")
            url_el = r.select_one(".result__url")
            if title_el:
                results.append(
                    f"Title: {title_el.get_text(strip=True)}\n"
                    f"URL: {url_el.get_text(strip=True) if url_el else 'N/A'}\n"
                    f"Snippet: {snippet_el.get_text(strip=True) if snippet_el else 'N/A'}"
                )
        return "\n\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search error: {e}"


class ResearchAssistantAgent(BaseAgent):
    system_prompt = """You are an expert research assistant. When given a topic or question:

1. Break it down into 2-3 specific search queries
2. Search for each, identify the most credible and relevant sources
3. Fetch and read the top sources in full
4. Synthesize findings into a structured report with:
   - Executive summary (3-4 sentences)
   - Key findings (bullets)
   - Important nuances or contradictions
   - Sources used
   - Suggested follow-up questions

Always cite your sources. Be factual, balanced, and concise."""

    tools = [SEARCH_TOOL, FETCH_URL_TOOL, WRITE_FILE_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "search_web":
            return search_web(tool_input["query"], tool_input.get("num_results", 5))
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = ResearchAssistantAgent()
    console.print("[bold green]Research Assistant[/bold green]")
    agent.chat()
