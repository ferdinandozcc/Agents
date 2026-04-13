# Vendor & Contract Tracker Agent

Monitors vendor contracts, renewal dates, SLAs, and spend — with proactive alerts before things slip.

## What it does

- Tracks all vendors with contract end dates, annual value, SLA commitments, and owners
- Alerts on renewals due within 90 days (🔴 < 30 days, 🟡 30-90 days)
- Summarizes total spend by category
- Surfaces negotiation tips and risks per vendor
- Saves the vendor database locally

## Usage

```bash
python operations/vendor_tracker/agent.py
```

Runs a health check automatically. Or interact:
- *"Add a new vendor: Datadog, $36k/year, contract ends 2026-09-01"*
- *"Which contracts are renewing in the next 60 days?"*

## Data storage

Vendor data is stored in `vendors.json` in the agent directory. The file is pre-populated with sample vendors on first run.

## Tools used

| Tool | Purpose |
|---|---|
| `get_vendors` | Load all vendor records |
| `add_vendor` | Add or update a vendor |
| `check_renewal_alerts` | Flag upcoming renewals |
| `write_file` | Save tracker report |
