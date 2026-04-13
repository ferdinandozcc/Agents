# Database Query Optimizer Agent

## What it does

- Analyze slow query logs or EXPLAIN output from the database
- Identify missing indexes, full table scans, and N+1 patterns
- Suggest query rewrites to improve efficiency
- Recommend schema changes such as indexing and partitioning
- Estimate performance improvement from each recommendation

## Usage

```bash
python3 engineering/db_query_optimizer/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
