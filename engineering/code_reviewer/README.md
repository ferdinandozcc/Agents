# Code Reviewer Agent

## What it does

- Check for correctness including logic errors and edge cases
- Identify security risks such as injection and exposed secrets
- Assess performance for N+1 queries and memory leaks
- Review style including naming conventions and readability
- Evaluate test coverage and test quality for new code

## Usage

```bash
python3 engineering/code_reviewer/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
