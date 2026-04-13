"""
shared/utils.py
Utility helpers shared across agents.
"""

import json
import re
from datetime import datetime
from pathlib import Path


def save_output(content: str, filename: str, output_dir: str = "outputs") -> str:
    """Save agent output to a timestamped file."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{output_dir}/{timestamp}_{filename}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def extract_json(text: str) -> dict | list | None:
    """Extract the first JSON block from a text string."""
    match = re.search(r"```json\s*([\s\S]*?)\s*```", text)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def truncate(text: str, max_chars: int = 2000) -> str:
    """Truncate text to a maximum character count."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + f"\n\n[... truncated {len(text) - max_chars} chars ...]"


def format_list(items: list[str], bullet: str = "-") -> str:
    """Format a list of strings as a bulleted list."""
    return "\n".join(f"{bullet} {item}" for item in items)
