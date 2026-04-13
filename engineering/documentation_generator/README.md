# Documentation Generator Agent

## What it does

- Read source code and generate docstrings and inline comments
- Write module-level READMEs explaining purpose and usage
- Generate changelog entries from commit diffs
- Create architecture decision records for key design choices
- Keep docs in sync with code changes over time

## Usage

```bash
python3 engineering/documentation_generator/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
