# API Contract Tester Agent

## What it does

- Compare API responses against OpenAPI and Swagger specs
- Flag fields that are missing, extra, or of the wrong type
- Test required vs optional field handling in responses
- Validate error responses and HTTP status codes
- Generate a contract compliance report for the team

## Usage

```bash
python3 engineering/api_contract_tester/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
