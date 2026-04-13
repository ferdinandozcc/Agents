# Release Notes Writer Agent

Converts git commit logs and ticket titles into polished, user-facing release notes.

## What it does

- Accepts raw git log output or a list of ticket titles
- Categorizes changes: New Features, Bug Fixes, Improvements, Security, Breaking Changes
- Rewrites technical entries in user-friendly language
- Skips internal refactors, CI changes, and dependency bumps
- Produces a formatted release notes document

## Usage

```bash
python product/release_notes_writer/agent.py
```

Then paste your commit log:
```
feat: add SSO login support
fix: crash on empty search results
chore: update lodash
refactor: extract auth middleware
fix: incorrect date formatting in reports
```

## Output format

```markdown
## What's new in v2.4.0
✨ New Features
🐛 Bug Fixes
⚡ Improvements
⚠️ Breaking Changes
```
