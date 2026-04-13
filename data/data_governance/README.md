# Data Governance Agent

## What it does

- Classify data assets by sensitivity: public, internal, and restricted
- Identify and tag PII, PHI, and PCI fields in the schema
- Enforce data access policies and flag policy violations
- Document data lineage from source systems to consumption
- Produce compliance-ready data inventory reports

## Usage

```bash
python3 data/data_governance/agent.py
```

## Category

`data`

## Tools used

| Tool | Purpose |
|---|---|
| `read_file` | Enables read file capability |
| `write_file` | Enables write file capability |
