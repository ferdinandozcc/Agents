# Onboarding Guide Agent

Walks new team members through their first 4 weeks with personalized task lists, explanations, and progress tracking.

## What it does

- Greets new hires and identifies their role
- Presents a week-by-week onboarding checklist tailored to their role (PM, Engineer, Designer)
- Explains the WHY behind each task — not just what to do
- Tracks task completion with a persistent progress file
- Answers questions about tools, processes, and team norms

## Usage

```bash
python operations/onboarding_guide/agent.py
```

The agent will ask the new hire's name and role, then guide them from there.

## Customization

Edit `ONBOARDING_PLANS` in `agent.py` to add roles or customize tasks per week. Each task needs a unique `id` for progress tracking.

## Data storage

Progress is saved in `progress.json` in the agent directory.
