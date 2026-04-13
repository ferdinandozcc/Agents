# Dependency Auditor Agent

## What it does

- Parse package manifests such as requirements.txt and package.json
- Identify outdated dependencies and available updates
- Flag known CVEs using public vulnerability data
- Prioritize updates by severity and ease of upgrade
- Produce an upgrade plan with estimated effort per package

## Usage

```bash
python3 engineering/dependency_auditor/agent.py
```

## Category

`engineering`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
| `search_web` | Enables search web capability |
