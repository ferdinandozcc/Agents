# Meeting Scheduler Agent

Finds optimal meeting slots across attendees, drafts tight agendas, and sends calendar invites.

## What it does

- Understands the meeting purpose and required attendees
- Finds available time slots (simulated; plug in a real calendar API)
- Recommends the best slot with reasoning
- Drafts a structured agenda with time allocations and desired outcomes
- Sends a calendar invite with the agenda attached (simulated)

## Usage

```bash
python operations/meeting_scheduler/agent.py
```

Example: *"Schedule a 60-minute product review with Alice, Bob, and Carol this week"*

## Extending with real calendar data

Replace the `find_slots()` function with a call to:
- Google Calendar API
- Microsoft Graph (Outlook)
- Calendly API

## Tools used

| Tool | Purpose |
|---|---|
| `find_available_slots` | Find open times for all attendees |
| `draft_agenda` | Generate a structured meeting agenda |
| `send_calendar_invite` | Send the invite (simulated) |
