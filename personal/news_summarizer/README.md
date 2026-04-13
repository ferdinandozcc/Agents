# News Summarizer Agent

## What it does

- Fetch news from configured sources and topics
- Filter out low-quality or clickbait content
- Write 2-3 sentence summaries for each story
- Group stories by topic (tech, business, world, etc.)
- Flag breaking news and distinguish opinion from reporting

## Usage

```bash
python3 personal/news_summarizer/agent.py
```

## Category

`personal`

## Tools used

| Tool | Purpose |
|---|---|
| `fetch_url` | Enables fetch url capability |
| `write_file` | Enables write file capability |
| `get_current_time` | Enables get current time capability |
