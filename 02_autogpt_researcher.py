"""
AutoGPT - Autonomous Internet Research
=======================================
Autonomous agent that pursues goals without continuous human guidance.
Researches across multiple sources and generates comprehensive reports.

Requirements:
- auto-gpt
- OpenAI API key

Author: AI Agents Article Examples
"""

import os
import json
from auto_gpt_agent import AutoGPT
from auto_gpt_tools import SearchTool, FileTool, AnalysisTool

# Configure AutoGPT with your goals
goal = """Research Tesla's competitive position in the EV market as of 2024.
Include: market share data, product lineup comparison, pricing strategy,
technology advantages, and recent news. Create a comprehensive report."""

# Initialize the agent with tools
agent = AutoGPT(
    name="MarketResearchAgent",
    role="Expert market analyst specializing in automotive industry",
    goals=[goal],
    tools=[
        SearchTool(),
        FileTool(directory="./research_output"),
        AnalysisTool()
    ],
    api_key=os.environ.get("OPENAI_API_KEY")
)

# The agent will autonomously:
# 1. Break down the research goal into subtasks
# 2. Search for current market data
# 3. Analyze competitor websites and news
# 4. Compile findings into a structured report
# 5. Save results to local files

result = agent.run(max_iterations=50)

print("Research complete!")
print(f"Output saved to: ./research_output/final_report.md")

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install auto-gpt
    # 2. Set your API key in environment variables
    # 3. Configure goals in the code above
    # 4. Run: python 02_autogpt_researcher.py
    pass
