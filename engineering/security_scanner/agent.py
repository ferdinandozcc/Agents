"""
engineering/security_scanner/agent.py
Security Scanner Agent — Flags common security vulnerabilities in code (OWASP top 10).
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from shared.base_agent import BaseAgent, console
from shared.tools import READ_FILE_TOOL, WRITE_FILE_TOOL, dispatch_common_tool


class SecurityScannerAgentAgent(BaseAgent):
    system_prompt = """You are an application security engineer. You scan code for:
1. Injection vulnerabilities (SQL, command, LDAP)
2. Broken authentication and session management
3. Sensitive data exposure (hardcoded secrets, unencrypted storage)
4. Insecure direct object references
5. Security misconfigurations
Map findings to OWASP Top 10 and provide remediation guidance."""

    tools = [READ_FILE_TOOL, WRITE_FILE_TOOL]

    def handle_tool_call(self, tool_name: str, tool_input: dict) -> str:
        result = dispatch_common_tool(tool_name, tool_input)
        if result is not None:
            return result
        if tool_name == "search_web":
            try:
                from personal.research_assistant.agent import search_web
                return search_web(tool_input["query"], tool_input.get("num_results", 5))
            except Exception as e:
                return f"Search unavailable: {e}"
        return f"Unknown tool: {tool_name}"


if __name__ == "__main__":
    agent = SecurityScannerAgentAgent()
    console.print(f"[bold green]Security Scanner Agent[/bold green]")
    agent.chat()
