"""
product/prd_writer/agent.py
PRD Writer Agent — conducts an interview and produces a structured Product Requirements Document.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from shared.base_agent import BaseAgent, console
from shared.tools import WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, dispatch_common_tool
from shared.utils import save_output

PRD_TEMPLATE_TOOL = {
    "name": "get_prd_template",
    "description": "Get the standard PRD template structure.",
    "input_schema": {"type": "object", "properties": {}, "required": []},
}

PRD_TEMPLATE = """
# Product Requirements Document: {feature_name}

**Author**: {author}  
**Date**: {date}  
**Status**: Draft  
**Version**: 1.0

---

## 1. Problem Statement
{problem_statement}

## 2. Goals & Success Metrics
### Goals
{goals}

### Success Metrics
{metrics}

## 3. User Personas
{personas}

## 4. User Stories
{user_stories}

## 5. Functional Requirements
{functional_requirements}

## 6. Non-Functional Requirements
{non_functional_requirements}

## 7. Out of Scope
{out_of_scope}

## 8. Dependencies & Risks
{dependencies_risks}

## 9. Timeline
{timeline}

## 10. Open Questions
{open_questions}
"""


class PRDWriterAgent(BaseAgent):
    system_prompt = """You are a senior product manager helping write a thorough Product Requirements Document (PRD).

Your process:
1. First, interview the user with focused questions to understand the feature:
   - What problem does this solve? Who experiences it?
   - What does success look like? How will we measure it?
   - Who are the target users?
   - What are the key user flows?
   - What are the constraints (tech, time, resources)?
   - What is explicitly OUT of scope?
   
2. Ask follow-up questions until you have enough detail.

3. Once you have sufficient information, use the PRD template to produce a complete, 
   well-structured document.

4. Save the final PRD to a file using the write_file tool.

Be thorough — a good PRD prevents misunderstandings between product, design, and engineering."""

    tools = [WRITE_FILE_TOOL, GET_CURRENT_TIME_TOOL, PRD_TEMPLATE_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "get_prd_template":
            return PRD_TEMPLATE
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = PRDWriterAgent()
    console.print("[bold green]PRD Writer Agent[/bold green]")
    console.print("Tell me about the feature you want to document.\n")
    agent.chat()
