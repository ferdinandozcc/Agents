# Architecture Advisor Agent

## What it does

- Review architecture diagrams or descriptions for issues
- Identify single points of failure and performance bottlenecks
- Assess for scalability, reliability, and maintainability
- Suggest relevant patterns such as CQRS, saga, and circuit breaker
- Provide trade-off analysis across simplicity, resilience, and performance

## Usage

```bash
python3 engineering/architecture_advisor/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
