# Research Assistant Agent

Searches the web, reads sources, and synthesizes a structured research report on any topic.

## What it does

- Breaks your research question into targeted sub-queries
- Searches DuckDuckGo for each
- Fetches and reads the full content of top sources
- Synthesizes findings into a structured report with citations

## Usage

```bash
python personal/research_assistant/agent.py
```

Then enter any research question interactively, e.g.:
- *"What are the best practices for OKR goal-setting in product teams?"*
- *"What is the current state of AI regulation in the EU?"*

## Output format

- Executive summary
- Key findings (bullets)
- Nuances and contradictions
- Sources used
- Suggested follow-up questions

## Tools used

| Tool | Purpose |
|---|---|
| `search_web` | DuckDuckGo search |
| `fetch_url` | Read full page content |
| `write_file` | Save report to disk |
