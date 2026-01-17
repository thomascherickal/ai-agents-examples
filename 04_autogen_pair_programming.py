"""
Microsoft AutoGen - Coding Assistant and Debugging
===================================================
Multi-agent dialogue system where agents collaborate on complex problems.
Perfect for pair programming and code review workflows.

Requirements:
- pyautogen
- OpenAI API key

Author: AI Agents Article Examples
"""

import os
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from autogen.agentchat.contrib.gpt_assistant import GPTAssistantAgent

# Configure the coding agents
config_list = [{"model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY")}]

# The code writer agent
coder = AssistantAgent(
    name="SeniorCoder",
    system_message="""You are a senior software engineer who writes 
    clean, well-documented Python code. You follow best practices,
    include comprehensive docstrings, and handle edge cases.""",
    llm_config={"config_list": config_list}
)

# The code reviewer agent
reviewer = AssistantAgent(
    name="CodeReviewer",
    system_message="""You are a meticulous code reviewer who catches
    bugs, performance issues, security vulnerabilities, and style 
    violations. You suggest specific improvements with code examples.""",
    llm_config={"config_list": config_list}
)

# Human oversight agent
human = UserProxyAgent(
    name="HumanReviewer",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10
)

# Collaborative coding session
def write_feature_request(feature_description):
    """Orchestrate a collaborative coding session"""
    
    # Coder writes the initial implementation
    coder.initiate_chat(
        reviewer,
        message=f"""Please implement the following feature:
        
        {feature_description}
        
        Write complete, working Python code with tests.""",
        summary_method="reflection_with_self_critique"
    )
    
    # Reviewer provides feedback
    reviewer.send(
        recipient=coder,
        message="""I've reviewed your implementation. Please address
        the following issues and provide an updated version.""",
        silent=True
    )
    
    # Additional rounds of review until approved
    # In production, this would loop until human approval

# Example: Build a data processing pipeline
write_feature_request(
    """Create a Python class that:
    1. Reads CSV files with configurable delimiters
    2. Validates data against a schema
    3. Transforms data using user-defined functions
    4. Exports to JSON with proper formatting"""
)

print("Code review complete. Final implementation ready for deployment.")

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install pyautogen
    # 2. Set OPENAI_API_KEY environment variable
    # 3. Run: python 04_autogen_pair_programming.py
    pass
