# Status Report Agent

Collects team updates and drafts clean, executive-ready weekly or monthly status reports.

## What it does

- Collects updates from configured teams/workstreams
- Assigns RAG status (🟢 On track / 🟡 At risk / 🔴 Blocked)
- Produces a structured report with executive summary, workstream table, risks, and upcoming milestones
- Saves the report as a markdown file

## Usage

```bash
python operations/status_report/agent.py
```

Or run interactively to feed in real updates:
- *"Engineering is blocked on the infra decision, everything else is on track"*

## Customization

Replace `SAMPLE_UPDATES` in `agent.py` with real integrations:
- Pull from Jira, Linear, or Asana
- Read from a shared Notion or Google Doc
- Parse Slack channel updates
