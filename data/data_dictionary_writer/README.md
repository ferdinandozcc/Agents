# Data Dictionary Writer Agent

## What it does

- Parse database schemas or dbt models for documentation
- Generate human-readable descriptions for tables and columns
- Identify and tag PII and sensitive fields in the schema
- Document business logic for derived and calculated fields
- Keep the dictionary in sync as schemas evolve over time

## Usage

```bash
python3 data/data_dictionary_writer/agent.py
```

## Category

`data`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
