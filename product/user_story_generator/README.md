# User Story Generator Agent

Breaks down epics or feature descriptions into detailed, copy-paste-ready user stories with acceptance criteria and story point estimates.

## What it does

- Takes an epic or feature description
- Generates individual user stories in "As a / I want / So that" format
- Writes 3-6 BDD acceptance criteria per story
- Estimates story points using a RICE-style heuristic
- Tags each story (frontend, backend, API, UX, etc.)

## Usage

```bash
python product/user_story_generator/agent.py
```

Example: *"Generate user stories for a notification preferences center where users can control email and push notification settings"*
