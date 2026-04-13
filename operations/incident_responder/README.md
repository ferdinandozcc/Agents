# Incident Responder Agent

Guides triage, coordinates response, tracks updates, and writes post-mortems for production incidents.

## What it does

- Declares and classifies incidents (SEV1 / SEV2 / SEV3)
- Guides triage with structured questions and investigation steps
- Logs timestamped updates to a persistent incident log
- Marks incidents as resolved with root cause
- Writes blameless post-mortems following industry best practices

## Usage

```bash
python operations/incident_responder/agent.py
```

Example: *"We have a SEV1 — checkout is returning 500 errors for all users"*

## Severity guide

| Level | Definition | Response Time |
|---|---|---|
| SEV1 | Critical — major user impact, revenue loss | Immediate |
| SEV2 | Major — significant degradation, workaround exists | < 30 min |
| SEV3 | Minor — limited impact, non-critical | < 4 hours |

## Data storage

Incidents are stored in `incidents.json` in the agent directory.
