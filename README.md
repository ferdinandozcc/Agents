<div align="center">

# 🤖 Agents Repository

**108 AI agents built with the Anthropic API — ready to run, extend, and deploy.**

[![Agents](https://img.shields.io/badge/agents-108-7F77DD?style=flat-square)](#)
[![Categories](https://img.shields.io/badge/categories-7-1D9E75?style=flat-square)](#)
[![Model](https://img.shields.io/badge/model-claude--sonnet--4--5-D85A30?style=flat-square)](#)
[![Python](https://img.shields.io/badge/python-3.10+-378ADD?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-888780?style=flat-square)](#)

</div>

---

## 🚀 Quick Start

```bash
git clone https://github.com/ferdinandozcc/Agents.git && cd Agents
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
python3 personal/research_assistant/agent.py
```

---

## 📁 Categories

| | Category | Agents | What it covers |
|---|---|---|---|
| 👤 | [Personal](#-personal) | 14 | Productivity, health, finance, learning |
| 📦 | [Product](#-product-development) | 18 | PM lifecycle, research, launch, experimentation |
| ⚙️ | [Operations](#%EF%B8%8F-operations--program-management) | 16 | Ops, compliance, HR, program management |
| 💼 | [Sales](#-sales) | 15 | Pipeline, outreach, forecasting, enablement |
| 📣 | [Marketing](#-marketing) | 15 | Content, campaigns, SEO, attribution |
| 🛠️ | [Engineering](#%EF%B8%8F-engineering) | 15 | Code quality, security, infra, reliability |
| 📊 | [Data & Analytics](#-data--analytics) | 15 | BI, data quality, ML ops, forecasting |

---

## 👤 Personal

> Daily productivity, health, finance, and learning agents for individual use.

| Agent | What it does |
|---|---|
| 📋 [daily_brief](./personal/daily_brief/) | Compiles calendar, tasks, and news into a morning digest |
| 🔍 [research_assistant](./personal/research_assistant/) | Searches the web and synthesizes structured research reports |
| 📝 [meeting_note_taker](./personal/meeting_note_taker/) | Turns transcripts into summaries, decisions, and action items |
| ✅ [habit_tracker](./personal/habit_tracker/) | Logs habits, tracks streaks, and provides motivational coaching |
| 📧 [email_triage](./personal/email_triage/) | Sorts inbox, flags urgent emails, and drafts routine replies |
| ✈️ [travel_planner](./personal/travel_planner/) | Finds flights, hotels, and builds day-by-day itineraries |
| 💰 [budget_tracker](./personal/budget_tracker/) | Categorizes spending, tracks budgets, and flags overruns |
| 🏃 [health_wellness_coach](./personal/health_wellness_coach/) | Tracks workouts, nutrition, sleep, and gives wellness tips |
| 🎓 [learning_assistant](./personal/learning_assistant/) | Creates study plans, quizzes, and tracks learning progress |
| 📰 [news_summarizer](./personal/news_summarizer/) | Curates and summarizes news by topic into a daily digest |
| 💼 [job_application_tracker](./personal/job_application_tracker/) | Tracks applications, deadlines, and interview prep notes |
| 💵 [personal_finance_advisor](./personal/personal_finance_advisor/) | Analyzes spending and suggests savings and investment strategies |
| 📱 [social_media_manager](./personal/social_media_manager/) | Drafts posts, plans content calendars, and tracks engagement |
| 📄 [document_summarizer](./personal/document_summarizer/) | Reads long PDFs and reports and extracts key points |

---

## 📦 Product Development

> End-to-end product management — from discovery and research to launch and measurement.

| Agent | What it does |
|---|---|
| 📋 [prd_writer](./product/prd_writer/) | Conducts an interview and produces a full Product Requirements Doc |
| 📖 [user_story_generator](./product/user_story_generator/) | Breaks epics into user stories with acceptance criteria and estimates |
| 🔍 [competitor_intel](./product/competitor_intel/) | Monitors competitor sites and surfaces strategic signals |
| 💬 [feedback_analyzer](./product/feedback_analyzer/) | Clusters user feedback and surfaces top themes and pain points |
| 🗺️ [roadmap_assistant](./product/roadmap_assistant/) | Prioritizes backlog using RICE or Impact/Effort scoring |
| 📝 [release_notes_writer](./product/release_notes_writer/) | Converts commits and tickets into user-facing release notes |
| 🧪 [ab_test_designer](./product/ab_test_designer/) | Designs experiments, calculates sample sizes, interprets results |
| 🎨 [design_critique](./product/design_critique/) | Reviews UI designs against UX heuristics and accessibility standards |
| 🚩 [feature_flag_manager](./product/feature_flag_manager/) | Tracks flags, rollout status, and recommends cleanup candidates |
| 🔁 [sprint_retrospective](./product/sprint_retrospective/) | Facilitates retros and tracks action items over time |
| 👤 [persona_builder](./product/persona_builder/) | Creates detailed user personas from research data |
| 🗺️ [journey_map_creator](./product/journey_map_creator/) | Builds end-to-end user journey maps with pain points and opportunities |
| 🔧 [tech_debt_tracker](./product/tech_debt_tracker/) | Catalogs debt, estimates impact, and prioritizes paydown |
| 📚 [api_documentation_writer](./product/api_documentation_writer/) | Generates clean API docs from specs or endpoint descriptions |
| 🌍 [localization_manager](./product/localization_manager/) | Audits for hardcoded strings and manages translation workflows |
| 🚀 [launch_checklist](./product/launch_checklist/) | Runs pre-launch quality gates and produces a go/no-go recommendation |
| ⭐ [nps_analyzer](./product/nps_analyzer/) | Processes NPS responses and surfaces themes and action items |
| 💲 [pricing_strategy_advisor](./product/pricing_strategy_advisor/) | Analyzes pricing models and recommends adjustments |

---

## ⚙️ Operations & Program Management

> Keeping the organization running — reporting, compliance, hiring, and resource planning.

| Agent | What it does |
|---|---|
| 📊 [kpi_monitor](./operations/kpi_monitor/) | Detects metric anomalies and produces color-coded dashboards |
| 📋 [status_report](./operations/status_report/) | Collects team updates and drafts weekly program status reports |
| 🚨 [incident_responder](./operations/incident_responder/) | Guides triage, logs updates, and writes post-mortems |
| 🧭 [onboarding_guide](./operations/onboarding_guide/) | Walks new hires through week-by-week onboarding tasks |
| 📅 [meeting_scheduler](./operations/meeting_scheduler/) | Finds optimal slots and drafts meeting agendas |
| 📑 [vendor_tracker](./operations/vendor_tracker/) | Monitors contract renewals, SLAs, and vendor deliverables |
| 💰 [budget_forecaster](./operations/budget_forecaster/) | Projects spend vs budget and flags department variances |
| ⏱️ [sla_monitor](./operations/sla_monitor/) | Tracks SLA compliance and alerts on approaching breaches |
| 📝 [process_documentation_writer](./operations/process_documentation_writer/) | Interviews teams and produces SOPs and process docs |
| ⚠️ [risk_register_manager](./operations/risk_register_manager/) | Maintains a live risk register with scoring and mitigations |
| 🔄 [change_management_planner](./operations/change_management_planner/) | Plans org change with stakeholder comms and training plans |
| 🔍 [audit_trail](./operations/audit_trail/) | Logs key decisions and actions for compliance audits |
| 📐 [resource_allocator](./operations/resource_allocator/) | Matches team capacity to project demand and flags over-allocation |
| 🎯 [okr_tracker](./operations/okr_tracker/) | Tracks OKR progress and flags at-risk objectives mid-quarter |
| 🛒 [procurement_assistant](./operations/procurement_assistant/) | Manages RFPs, vendor comparisons, and purchase order workflows |
| 👥 [hiring_pipeline_tracker](./operations/hiring_pipeline_tracker/) | Tracks candidates across stages and surfaces pipeline bottlenecks |

---

## 💼 Sales

> From first touch to closed deal — prospecting, coaching, forecasting, and enablement.

| Agent | What it does |
|---|---|
| 🎯 [lead_qualifier](./sales/lead_qualifier/) | Scores inbound leads against ICP criteria and routes to reps |
| ✉️ [outreach_writer](./sales/outreach_writer/) | Writes personalized cold emails and LinkedIn messages |
| 🧹 [crm_hygiene](./sales/crm_hygiene/) | Audits CRM for missing fields, duplicates, and stale data |
| 🏋️ [deal_coach](./sales/deal_coach/) | Reviews deal health and recommends next best actions |
| 📄 [proposal_writer](./sales/proposal_writer/) | Drafts customized sales proposals from templates and deal context |
| 📈 [win_loss_analyzer](./sales/win_loss_analyzer/) | Analyzes won/lost deals to surface patterns and coaching insights |
| 🔮 [pipeline_forecaster](./sales/pipeline_forecaster/) | Predicts close probability and projects monthly revenue |
| 📞 [call_prep](./sales/call_prep/) | Researches prospects and preps talking points before calls |
| 📨 [follow_up_automator](./sales/follow_up_automator/) | Drafts post-call follow-ups and multi-touch sequences |
| 📜 [contract_redline_reviewer](./sales/contract_redline_reviewer/) | Flags non-standard clauses and summarizes redline deltas |
| ⚡ [churn_predictor](./sales/churn_predictor/) | Identifies at-risk accounts using usage and engagement signals |
| 📦 [upsell_finder](./sales/upsell_finder/) | Scans customer data for expansion and upsell opportunities |
| 📚 [sales_playbook_builder](./sales/sales_playbook_builder/) | Creates battle cards, objection handlers, and qualification guides |
| 💵 [commission_calculator](./sales/commission_calculator/) | Computes commissions, SPIFs, and quota attainment per rep |
| 🗺️ [territory_planner](./sales/territory_planner/) | Designs balanced territories based on revenue potential |

---

## 📣 Marketing

> Content creation, campaign management, SEO, and growth — end to end.

| Agent | What it does |
|---|---|
| ♻️ [content_repurposer](./marketing/content_repurposer/) | Turns one blog post into LinkedIn, tweets, email, and video script |
| 🔍 [seo_optimizer](./marketing/seo_optimizer/) | Audits pages for SEO issues and improves meta copy and keywords |
| 📊 [campaign_performance_analyst](./marketing/campaign_performance_analyst/) | Surfaces over/underperforming campaigns and reallocates budget |
| ✍️ [email_copywriter](./marketing/email_copywriter/) | Writes subject lines, body copy, and CTAs for marketing emails |
| 🎙️ [brand_voice_checker](./marketing/brand_voice_checker/) | Reviews content against brand guidelines and flags off-brand language |
| 👂 [social_listening](./marketing/social_listening/) | Monitors brand mentions and competitor buzz across social channels |
| 📅 [content_calendar_planner](./marketing/content_calendar_planner/) | Builds monthly content calendars aligned to campaigns and launches |
| 🏠 [landing_page_optimizer](./marketing/landing_page_optimizer/) | Reviews landing pages and suggests CRO improvements |
| 🌟 [influencer_researcher](./marketing/influencer_researcher/) | Finds and scores influencers by niche, audience, and engagement |
| 🎪 [event_promotion](./marketing/event_promotion/) | Plans and executes promotional campaigns for webinars and events |
| 📢 [ad_copy_generator](./marketing/ad_copy_generator/) | Writes A/B ad copy variants for Google, Meta, and LinkedIn |
| 🧲 [lead_magnet_creator](./marketing/lead_magnet_creator/) | Designs and writes guides, checklists, and templates |
| 📰 [newsletter_writer](./marketing/newsletter_writer/) | Writes weekly newsletters with subject line variants |
| 🌐 [market_research](./marketing/market_research/) | Researches TAM, SAM, SOM, and buyer trends for a target market |
| 📍 [attribution_analyzer](./marketing/attribution_analyzer/) | Maps touchpoints to revenue and scores channel contribution |

---

## 🛠️ Engineering

> Code quality, security, infrastructure, and reliability — for engineering teams.

| Agent | What it does |
|---|---|
| 👀 [code_reviewer](./engineering/code_reviewer/) | Reviews PRs for bugs, security issues, and performance problems |
| 🐛 [bug_triage](./engineering/bug_triage/) | Classifies bugs by severity, assigns owners, and tracks fixes |
| 🧪 [test_case_generator](./engineering/test_case_generator/) | Writes unit and integration tests from specs or function signatures |
| 📦 [dependency_auditor](./engineering/dependency_auditor/) | Scans packages for outdated versions and known CVEs |
| 🏛️ [architecture_advisor](./engineering/architecture_advisor/) | Reviews system designs for scalability and reliability |
| 🚀 [deployment_monitor](./engineering/deployment_monitor/) | Watches deployments for errors and triggers rollback decisions |
| 🗄️ [db_query_optimizer](./engineering/db_query_optimizer/) | Analyzes slow queries and recommends indexes and schema fixes |
| 📝 [documentation_generator](./engineering/documentation_generator/) | Generates docstrings, READMEs, and architecture decision records |
| 🔒 [security_scanner](./engineering/security_scanner/) | Flags OWASP Top 10 vulnerabilities in code |
| 📈 [sprint_velocity_tracker](./engineering/sprint_velocity_tracker/) | Tracks velocity trends and forecasts delivery dates |
| 📋 [oncall_handoff_writer](./engineering/oncall_handoff_writer/) | Generates structured on-call handoff notes from incident logs |
| 🔌 [api_contract_tester](./engineering/api_contract_tester/) | Validates API responses against OpenAPI specs |
| ⚡ [performance_profiler](./engineering/performance_profiler/) | Identifies bottlenecks and recommends targeted optimizations |
| 🌿 [feature_branch_manager](./engineering/feature_branch_manager/) | Flags stale branches and assesses merge readiness |
| ☁️ [infra_cost_analyzer](./engineering/infra_cost_analyzer/) | Reviews cloud spend and recommends rightsizing and savings |

---

## 📊 Data & Analytics

> Data quality, SQL, BI, ML ops, and turning numbers into business insights.

| Agent | What it does |
|---|---|
| 🔍 [data_quality_monitor](./data/data_quality_monitor/) | Scans datasets for nulls, outliers, duplicates, and schema drift |
| 🗃️ [sql_query_writer](./data/sql_query_writer/) | Converts natural language questions into optimized SQL |
| 📊 [dashboard_builder](./data/dashboard_builder/) | Designs metric dashboards from business questions and data |
| 🔄 [etl_pipeline_monitor](./data/etl_pipeline_monitor/) | Monitors pipelines for failures, delays, and anomalies |
| 👥 [cohort_analysis](./data/cohort_analysis/) | Builds retention and engagement cohort reports |
| 🔮 [forecasting_agent](./data/forecasting_agent/) | Builds time-series forecasts with confidence intervals |
| 🧪 [ab_test_analyzer](./data/ab_test_analyzer/) | Calculates significance and produces ship/no-ship recommendations |
| 📖 [data_dictionary_writer](./data/data_dictionary_writer/) | Generates human-readable data dictionaries from schemas |
| 📋 [executive_report_writer](./data/executive_report_writer/) | Turns raw metrics into narrative executive summaries |
| 🎯 [customer_segmentation](./data/customer_segmentation/) | Clusters customers by behavior and labels each segment |
| 📉 [churn_analysis](./data/churn_analysis/) | Models churn drivers and surfaces leading indicators |
| 🔎 [event_tracking_auditor](./data/event_tracking_auditor/) | Audits analytics taxonomy for gaps and naming issues |
| 🤖 [ml_model_monitor](./data/ml_model_monitor/) | Tracks model performance drift and triggers retraining alerts |
| 🏛️ [data_governance](./data/data_governance/) | Tags PII, enforces access policies, and documents lineage |
| 📖 [insight_narrator](./data/insight_narrator/) | Takes a chart or table and writes a plain-language business story |

---

## 🏗️ Architecture

All agents extend `shared/base_agent.py` and follow the same agentic loop:

```
User Input → Agent Loop (Claude reasoning) → Tool Use → Structured Output
```

**Shared modules:**
- `shared/base_agent.py` — core agentic loop using the Anthropic API
- `shared/tools.py` — reusable tool definitions (web search, file I/O, etc.)
- `shared/utils.py` — shared utilities (output saving, JSON parsing, etc.)

---

## 🔧 Adding a New Agent

```bash
mkdir category/my_new_agent
# Subclass BaseAgent, define system_prompt + tools + handle_tool_call
# Add README.md
python3 category/my_new_agent/agent.py
```

---

<div align="center">

Made with the [Anthropic API](https://docs.anthropic.com) · MIT License

</div>
