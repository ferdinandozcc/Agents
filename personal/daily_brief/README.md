# Daily Brief Agent

Compiles a personalized morning digest — calendar events, top tasks, and relevant news — into a scannable brief you can read in under 2 minutes.

## What it does

- Fetches the current date/time
- Reads your configured calendar events and task list
- Scrapes configured news sources for headlines relevant to your interests
- Produces a structured markdown digest

## Usage

```bash
python personal/daily_brief/agent.py
```

## Configuration

Edit the `DEFAULT_TOPICS` dict in `agent.py` to configure:

| Field | Description |
|---|---|
| `news_sources` | URLs to fetch headlines from |
| `topics_of_interest` | Keywords to filter relevant news |
| `tasks` | Your task list for the day |
| `calendar_events` | Today's scheduled events |

## Output example

```
## Good morning! Monday, April 14 2026

### Today's Calendar
- 09:00 Standup
- 14:00 Product review
- 16:30 1:1 with manager

### Top Tasks
- Review Q2 roadmap draft
- Send weekly update to stakeholders

### Headlines
- [AI] OpenAI launches new reasoning model...
- [Tech] EU proposes new data portability rules...
```

## Tools used

| Tool | Purpose |
|---|---|
| `fetch_url` | Pull news from configured sources |
| `get_current_time` | Timestamp the brief |
| `write_file` | Optionally save the brief to disk |
