# Habit & Goal Tracker Agent

Logs daily habits, tracks streaks, and provides motivational coaching to keep you on track.

## What it does

- Add habits you want to build (with frequency and a personal goal)
- Log daily completions via conversation
- Tracks streaks automatically
- Provides a motivational daily check-in

## Usage

```bash
python personal/habit_tracker/agent.py
```

Example interactions:
- *"Add a habit: meditate for 10 minutes every day"*
- *"I just finished my workout"*
- *"How's my streak for reading?"*
- *"Show me all my habits"*

## Data storage

Habit data is stored locally in `habit_data.json` in the agent directory. Streaks are computed from the log history.

## Tools used

| Tool | Purpose |
|---|---|
| `add_habit` | Create a new habit to track |
| `log_habit` | Record today's completion |
| `get_habits` | View all habits and streaks |
| `get_current_time` | Date-stamp each log entry |
