# Meeting Note-Taker Agent

Processes meeting transcripts or raw notes into structured summaries, decisions, and action items.

## What it does

- Parses raw meeting transcripts or notes
- Extracts attendees, key discussion points, and decisions
- Produces a clean action items table with owners and due dates
- Saves the summary as a markdown file

## Usage

```bash
python personal/meeting_note_taker/agent.py
```

Then either:
- Paste a transcript directly into the chat, or
- Provide a file path: `"Summarize the meeting in /path/to/transcript.txt"`

## Output format

```markdown
## Meeting Summary
- Date / Attendees / Duration

## Key Discussion Points
## Decisions Made
## Action Items (table with owner + due date)
## Next Meeting
```

## Tips

- Works best with transcripts from Zoom, Google Meet, or Otter.ai
- If ownership is unclear, the agent marks it "TBD" rather than guessing

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Load transcript from disk |
| `write_file` | Save summary to disk |
| `get_current_time` | Timestamp the summary |
