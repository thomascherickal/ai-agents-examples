"""
OpenAI Assistants API - Calendar and Scheduling Management
===========================================================
Purpose-built solution for building AI assistants with persistent threads,
built-in retrieval, and function calling capabilities.

Requirements:
- openai
- OpenAI API key

Author: AI Agents Article Examples
"""

import os
import time
from openai import OpenAI

# Initialize the client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Create the scheduling assistant
assistant = client.beta.assistants.create(
    name="MeetingScheduler",
    instructions="""You are a professional scheduling assistant.
    Help users schedule meetings by finding suitable times, checking
    availability, and managing calendar conflicts. Be proactive about
    suggesting alternatives when preferred times are unavailable.""",
    model="gpt-4-turbo-preview",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "check_calendar_availability",
                "description": "Check calendar for available time slots",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"},
                        "duration_minutes": {"type": "integer", "description": "Meeting duration"}
                    },
                    "required": ["date", "duration_minutes"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "send_calendar_invite",
                "description": "Send calendar invitation to attendees",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "attendee_emails": {"type": "array", "items": {"type": "string"}},
                        "meeting_title": {"type": "string"},
                        "start_time": {"type": "string"},
                        "duration_minutes": {"type": "integer"}
                    },
                    "required": ["attendee_emails", "meeting_title", "start_time"]
                }
            }
        }
    ]
)

# Create a new thread for the conversation
thread = client.beta.threads.create(
    thread={"messages": []}
)

def schedule_meeting(user_request: str):
    """Handle a scheduling request"""
    
    # Add user message to thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_request
    )
    
    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    
    # Poll for completion
    while run.status in ["queued", "in_progress"]:
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    
    # Handle function calls if needed
    if run.status == "requires_action":
        # Function calling logic here
        pass
    
    # Display assistant response
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    return messages.data[0].content[0].text.value

# Example scheduling conversations
print("=== SCHEDULING ASSISTANT ===\n")

response1 = schedule_meeting("Schedule a 1-hour meeting with the design team next Tuesday afternoon.")
print(f"User: Schedule a 1-hour meeting with the design team next Tuesday afternoon.")
print(f"Assistant: {response1}\n")

response2 = schedule_meeting("What times are available Thursday morning for a client demo?")
print(f"User: What times are available Thursday morning for a client demo?")
print(f"Assistant: {response2}\n")

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install openai
    # 2. Set OPENAI_API_KEY
    # 3. Run: python 07_openai_scheduling_assistant.py
    pass
