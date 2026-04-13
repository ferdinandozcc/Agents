# 🤖 Agents Repository

A curated collection of **108 AI agents** built with the [Anthropic API](https://docs.anthropic.com), organized across **7 domains**: Personal, Product Development, Operations & PM, Sales, Marketing, Engineering, and Data & Analytics.

Each agent is self-contained, uses Claude as its reasoning engine, and is designed to be run independently or composed into larger workflows.

---

## 🚀 Getting Started

### Installation

```bash
git clone https://github.com/ferdinandozcc/Agents.git
cd Agents
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-api-key-here"
```

### Run any agent

```bash
python3 personal/research_assistant/agent.py
python3 sales/deal_coach/agent.py
python3 data/sql_query_writer/agent.py
```

---

## 📁 Categories

| Category | Agents | Focus |
|---|---|---|
| [personal/](./personal/) | 14 | Daily productivity, health, finance, learning |
| [product/](./product/) | 18 | PM lifecycle, research, launch, experimentation |
| [operations/](./operations/) | 16 | Ops, program management, compliance, HR |
| [sales/](./sales/) | 15 | Pipeline, outreach, forecasting, enablement |
| [marketing/](./marketing/) | 15 | Content, campaigns, SEO, attribution |
| [engineering/](./engineering/) | 15 | Code quality, security, infra, reliability |
| [data/](./data/) | 15 | Analytics, BI, data quality, ML ops |
| **Total** | **108** | |

---

## 🧠 All Agents

### Personal
daily_brief · research_assistant · meeting_note_taker · habit_tracker · email_triage · travel_planner · budget_tracker · health_wellness_coach · learning_assistant · news_summarizer · job_application_tracker · personal_finance_advisor · social_media_manager · document_summarizer

### Product
prd_writer · user_story_generator · competitor_intel · feedback_analyzer · roadmap_assistant · release_notes_writer · ab_test_designer · design_critique · feature_flag_manager · sprint_retrospective · persona_builder · journey_map_creator · tech_debt_tracker · api_documentation_writer · localization_manager · launch_checklist · nps_analyzer · pricing_strategy_advisor

### Operations
kpi_monitor · status_report · incident_responder · onboarding_guide · meeting_scheduler · vendor_tracker · budget_forecaster · sla_monitor · process_documentation_writer · risk_register_manager · change_management_planner · audit_trail · resource_allocator · okr_tracker · procurement_assistant · hiring_pipeline_tracker

### Sales
lead_qualifier · outreach_writer · crm_hygiene · deal_coach · proposal_writer · win_loss_analyzer · pipeline_forecaster · call_prep · follow_up_automator · contract_redline_reviewer · churn_predictor · upsell_finder · sales_playbook_builder · commission_calculator · territory_planner

### Marketing
content_repurposer · seo_optimizer · campaign_performance_analyst · email_copywriter · brand_voice_checker · social_listening · content_calendar_planner · landing_page_optimizer · influencer_researcher · event_promotion · ad_copy_generator · lead_magnet_creator · newsletter_writer · market_research · attribution_analyzer

### Engineering
code_reviewer · bug_triage · test_case_generator · dependency_auditor · architecture_advisor · deployment_monitor · db_query_optimizer · documentation_generator · security_scanner · sprint_velocity_tracker · oncall_handoff_writer · api_contract_tester · performance_profiler · feature_branch_manager · infra_cost_analyzer

### Data & Analytics
data_quality_monitor · sql_query_writer · dashboard_builder · etl_pipeline_monitor · cohort_analysis · forecasting_agent · ab_test_analyzer · data_dictionary_writer · executive_report_writer · customer_segmentation · churn_analysis · event_tracking_auditor · ml_model_monitor · data_governance · insight_narrator

---

## 🏗️ Architecture

All agents extend `shared/base_agent.py` and follow the same agentic loop pattern using the Anthropic API with tool use.

## 📄 License

MIT
