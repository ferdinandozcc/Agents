# PRD Writer Agent

Conducts a structured interview and produces a complete, well-formatted Product Requirements Document.

## What it does

- Interviews you about the feature you want to document
- Asks targeted follow-up questions to fill gaps
- Generates a full PRD with: problem statement, goals, personas, user stories, functional/non-functional requirements, risks, and open questions
- Saves the PRD as a markdown file

## Usage

```bash
python product/prd_writer/agent.py
```

Start with: *"I want to document a feature for [your feature idea]"*

## Output

A complete PRD following this structure:
1. Problem Statement
2. Goals & Success Metrics
3. User Personas
4. User Stories
5. Functional Requirements
6. Non-Functional Requirements
7. Out of Scope
8. Dependencies & Risks
9. Timeline
10. Open Questions
