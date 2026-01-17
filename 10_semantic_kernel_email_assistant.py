"""
Semantic Kernel - Email Drafting and Tone Adjustment
=====================================================
Microsoft's Semantic Kernel combines the power of language models with
traditional software engineering patterns.

Requirements:
- semantic-kernel
- OpenAI API key

Author: AI Agents Article Examples
"""

import os
from semantic_kernel import Kernel
from semantic_kernel.contents import ChatHistory, TextContent
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.planning.basic_planner import BasicPlanner

# Initialize Semantic Kernel
kernel = Kernel()
kernel.add_service(OpenAIChatCompletion(service_id="chat", api_key=os.environ.get("OPENAI_API_KEY")))

# Define email composition skills
email_composition_prompt = """
You are a professional email writer. Compose an email based on the following parameters:

Recipient: {{$recipient}}
Subject: {{$subject}}
Tone: {{$tone}} (professional, friendly, urgent, apologetic, congratulatory)
Purpose: {{$purpose}}
Key Points to Include: {{$key_points}}

Requirements:
- Keep it concise and focused
- Include a clear call to action
- Match the specified tone
- Professional signature
"""

# Create email composition function
from semantic_kernel.functions import KernelFunction

compose_email = kernel.create_function_from_prompt(
    prompt=email_composition_prompt,
    function_name="compose_email",
    description="Compose a professional email based on parameters"
)

# Define tone adjustment skill
tone_adjustment_prompt = """
Rewrite the following email to match the specified tone while preserving all key information.

Original Email:
{{$original_email}}

Desired Tone: {{$desired_tone}}

Rewritten Email:"""

adjust_tone = kernel.create_function_from_prompt(
    prompt=tone_adjustment_prompt,
    function_name="adjust_tone",
    description="Adjust the tone of an email"
)

# Example email compositions
def generate_draft_email(recipient, subject, purpose, key_points, tone="professional"):
    """Generate a professional email draft"""
    
    result = kernel.run(
        compose_email,
        input_text={
            "recipient": recipient,
            "subject": subject,
            "tone": tone,
            "purpose": purpose,
            "key_points": key_points
        }
    )
    
    return result.value[0].text

def adjust_email_tone(original_email, desired_tone):
    """Adjust the tone of an existing email"""
    
    result = kernel.run(
        adjust_tone,
        input_text={
            "original_email": original_email,
            "desired_tone": desired_tone
        }
    )
    
    return result.value[0].text

print("=== SEMANTIC KERNEL EMAIL ASSISTANT ===\n")

# Generate different email types
emails = [
    {
        "recipient": "client@company.com",
        "subject": "Project Update - Q4 Deliverables",
        "purpose": "Provide update on project milestones and next steps",
        "key_points": "On track for deadline, two features completed, one in progress, meeting scheduled for review",
        "tone": "professional"
    },
    {
        "recipient": "team@company.com",
        "subject": "Great News - Sales Target Exceeded!",
        "purpose": "Celebrate team achievement and motivate continued effort",
        "key_points": "120% of target reached, specific contributor mentions, optional celebration event",
        "tone": "congratulatory"
    }
]

for i, email_params in enumerate(emails, 1):
    print(f"--- Email {i}: {email_params['tone'].title()} Tone ---")
    draft = generate_draft_email(**email_params)
    print(draft)
    print("-" * 60 + "\n")

# Demonstrate tone adjustment
original = """Hey,

Sorry I'm late sending this. Kinda forgot about it. Maybe we can talk later?

-Bob"""

print("--- Tone Adjustment Demo ---")
print("Original (casual):")
print(original)

print("\nAdjusted (formal):")
formal_email = adjust_email_tone(original, "formal and apologetic")
print(formal_email)

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install semantic-kernel
    # 2. Set OPENAI_API_KEY
    # 3. Run: python 10_semantic_kernel_email_assistant.py
    pass
