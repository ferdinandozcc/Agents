# Security Scanner Agent

## What it does

- Scan code for injection vulnerabilities including SQL and command
- Identify broken authentication and session management issues
- Flag sensitive data exposure such as hardcoded secrets
- Detect insecure direct object references in the codebase
- Map findings to OWASP Top 10 with remediation guidance

## Usage

```bash
python3 engineering/security_scanner/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
