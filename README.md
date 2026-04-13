# 🤖 Agents Repository

A curated collection of AI agents built with the [Anthropic API](https://docs.anthropic.com), organized across three domains: **Personal productivity**, **Product development**, and **Operations & program management**.

Each agent is self-contained, uses Claude as its reasoning engine, and is designed to be run independently or composed into larger workflows.

---

## 📁 Structure

```
agents-repo/
├── personal/
│   ├── daily_brief/
│   ├── research_assistant/
│   ├── meeting_note_taker/
│   └── habit_tracker/
├── product/
│   ├── prd_writer/
│   ├── user_story_generator/
│   ├── competitor_intel/
│   ├── feedback_analyzer/
│   ├── roadmap_assistant/
│   └── release_notes_writer/
├── operations/
│   ├── kpi_monitor/
│   ├── status_report/
│   ├── incident_responder/
│   ├── onboarding_guide/
│   ├── meeting_scheduler/
│   └── vendor_tracker/
└── shared/
    ├── base_agent.py
    ├── tools.py
    └── utils.py
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com/)

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/agents-repo.git
cd agents-repo
pip install -r requirements.txt
```

### Configuration

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or create a `.env` file:

```
ANTHROPIC_API_KEY=your-api-key-here
```

### Running an agent

```bash
python personal/daily_brief/agent.py
python product/prd_writer/agent.py
python operations/kpi_monitor/agent.py
```

---

## 🧠 Agent Categories

### Personal
| Agent | Description |
|---|---|
| [Daily Brief](./personal/daily_brief/) | Morning digest from calendar, email, tasks, and news |
| [Research Assistant](./personal/research_assistant/) | Web search, summarization, and structured reports |
| [Meeting Note-Taker](./personal/meeting_note_taker/) | Transcription, action items, and meeting summaries |
| [Habit Tracker](./personal/habit_tracker/) | Goal logging, streak tracking, and nudges |

### Product Development
| Agent | Description |
|---|---|
| [PRD Writer](./product/prd_writer/) | Interview-driven Product Requirements Documents |
| [User Story Generator](./product/user_story_generator/) | Epics → user stories with acceptance criteria |
| [Competitor Intel](./product/competitor_intel/) | Monitor competitor signals across web sources |
| [Feedback Analyzer](./product/feedback_analyzer/) | Cluster and theme user feedback from multiple sources |
| [Roadmap Assistant](./product/roadmap_assistant/) | Backlog prioritization with impact/effort scoring |
| [Release Notes Writer](./product/release_notes_writer/) | Commits and tickets → user-facing release notes |

### Operations & Program Management
| Agent | Description |
|---|---|
| [KPI Monitor](./operations/kpi_monitor/) | Dashboard watching, anomaly alerts, trend explanations |
| [Status Report](./operations/status_report/) | Weekly/monthly program status report generation |
| [Incident Responder](./operations/incident_responder/) | Triage guide, owner assignment, post-mortem writer |
| [Onboarding Guide](./operations/onboarding_guide/) | Step-by-step onboarding for new team members |
| [Meeting Scheduler](./operations/meeting_scheduler/) | Optimal slot finding and agenda drafting |
| [Vendor Tracker](./operations/vendor_tracker/) | Contract renewals, SLAs, and vendor deliverable alerts |

---

## 🏗️ Architecture

All agents share a common pattern:

```
User Input
    │
    ▼
┌─────────────┐
│  Agent Loop  │  ← Claude (claude-sonnet-4-5) as reasoning engine
│             │
│  think →    │
│  tool_use → │  ← Tools (web search, file I/O, APIs, etc.)
│  respond    │
└─────────────┘
    │
    ▼
Structured Output
```

The `shared/` module provides reusable base classes, tool definitions, and utilities used across all agents.

---

## 🔧 Adding a New Agent

1. Create a folder under the appropriate category
2. Copy the `shared/base_agent.py` pattern
3. Define your tools in `tools.py`
4. Add a `README.md` describing inputs, outputs, and usage
5. Submit a PR!

---

## 📄 License

MIT
