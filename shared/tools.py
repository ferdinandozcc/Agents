"""
shared/tools.py
Reusable tool definitions and implementations shared across agents.
"""

import httpx
from bs4 import BeautifulSoup
from datetime import datetime


# ---------------------------------------------------------------------------
# Tool definitions (passed to the Anthropic API)
# ---------------------------------------------------------------------------

WEB_SEARCH_TOOL = {
    "name": "web_search",
    "description": "Search the web for current information on a topic. Returns a list of results with titles, URLs, and snippets.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The search query."},
            "num_results": {"type": "integer", "description": "Number of results to return (default 5).", "default": 5},
        },
        "required": ["query"],
    },
}

FETCH_URL_TOOL = {
    "name": "fetch_url",
    "description": "Fetch and extract the main text content of a webpage.",
    "input_schema": {
        "type": "object",
        "properties": {
            "url": {"type": "string", "description": "The URL to fetch."},
        },
        "required": ["url"],
    },
}

READ_FILE_TOOL = {
    "name": "read_file",
    "description": "Read the contents of a local file.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Path to the file."},
        },
        "required": ["path"],
    },
}

WRITE_FILE_TOOL = {
    "name": "write_file",
    "description": "Write content to a local file.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Path to the file."},
            "content": {"type": "string", "description": "Content to write."},
        },
        "required": ["path", "content"],
    },
}

GET_CURRENT_TIME_TOOL = {
    "name": "get_current_time",
    "description": "Get the current date and time.",
    "input_schema": {
        "type": "object",
        "properties": {},
        "required": [],
    },
}


# ---------------------------------------------------------------------------
# Tool implementations
# ---------------------------------------------------------------------------

def fetch_url(url: str) -> str:
    """Fetch and extract text from a URL."""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; AgentBot/1.0)"}
        response = httpx.get(url, headers=headers, timeout=10, follow_redirects=True)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        return text[:8000]  # Limit to avoid context overflow
    except Exception as e:
        return f"Error fetching URL: {e}"


def read_file(path: str) -> str:
    """Read a local file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"


def write_file(path: str, content: str) -> str:
    """Write to a local file."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File written successfully: {path}"
    except Exception as e:
        return f"Error writing file: {e}"


def get_current_time() -> str:
    """Return the current datetime."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------------------------------
# Dispatcher — call this from handle_tool_call in any agent
# ---------------------------------------------------------------------------

def dispatch_common_tool(tool_name: str, tool_input: dict) -> str | None:
    """
    Handle common tools. Returns None if the tool is not handled here
    (so the agent can try its own tools).
    """
    if tool_name == "fetch_url":
        return fetch_url(tool_input["url"])
    if tool_name == "read_file":
        return read_file(tool_input["path"])
    if tool_name == "write_file":
        return write_file(tool_input["path"], tool_input["content"])
    if tool_name == "get_current_time":
        return get_current_time()
    return None
