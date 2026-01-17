"""
BabyAGI - Task List Prioritization and Execution
=================================================
Task-driven autonomous agents that automatically generate sub-tasks,
prioritize them, execute them, and create new tasks based on results.

Requirements:
- langchain
- openai
- faiss-cpu
- OpenAI API key

Author: AI Agents Article Examples
"""

import os
from collections import deque
from typing import List, Tuple
from pydantic import BaseModel
from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

# Define task structure
class Task(BaseModel):
    task_id: int
    name: str
    status: str = "pending"
    result: str = ""

# Initialize components
llm = OpenAI(model="gpt-4", temperature=0)
embedding_model = OpenAIEmbeddings()
vector_store = FAISS.from_texts(["Initial task memory"], embedding_model)

# Task generation prompt
task_generation_prompt = PromptTemplate(
    input_variables=["objective", "result", "task_description"],
    template="""You are a project management AI. Based on the original objective 
    and the result of the previous task, generate new tasks that need to be 
    completed to achieve the objective.
    
    Original Objective: {objective}
    Previous Task Result: {result}
    Previous Task Description: {task_description}
    
    Return a list of new tasks, one per line, in priority order."""
)

task_chain = LLMChain(llm=llm, prompt=task_generation_prompt)

# Task execution with result extraction
execution_prompt = PromptTemplate(
    input_variables=["task", "context"],
    template="""Execute the following task and provide a detailed result.
    
    Task: {task}
    Context: {context}
    
    Result:""")

execution_chain = LLMChain(llm=llm, prompt=execution_prompt)

def babyagi(objective: str, initial_tasks: List[str]):
    """Execute BabyAGI workflow"""
    
    task_queue = deque()
    completed_tasks = []
    
    # Initialize task queue
    for i, task in enumerate(initial_tasks, 1):
        task_queue.append(Task(task_id=i, name=task))
    
    print(f"=== BABYAGI: {objective} ===\n")
    iteration = 0
    
    while task_queue and iteration < 20:
        iteration += 1
        current_task = task_queue.popleft()
        current_task.status = "executing"
        
        print(f"[{iteration}] Executing: {current_task.name}")
        
        # Execute the task
        context = "\n".join([f"- {t.name}: {t.result}" for t in completed_tasks[-5:]])
        result = execution_chain.run({
            "task": current_task.name,
            "context": context or "No previous context"
        })
        
        current_task.result = result
        current_task.status = "completed"
        completed_tasks.append(current_task)
        
        print(f"    Result: {result[:100]}...")
        
        # Generate new tasks based on result
        new_tasks_text = task_chain.run({
            "objective": objective,
            "result": result,
            "task_description": current_task.name
        })
        
        # Parse and add new tasks
        new_tasks = [t.strip() for t in new_tasks_text.split("\n") if t.strip()]
        for i, task_name in enumerate(new_tasks, len(task_queue) + 1):
            task_queue.append(Task(task_id=i, name=task_name))
        
        print(f"    Added {len(new_tasks)} new tasks")
        print(f"    Queue size: {len(task_queue)}\n")
    
    print(f"\n=== COMPLETED {len(completed_tasks)} TASKS ===")
    return completed_tasks

# Example: Research and create a product launch plan
project_objective = "Research competitor pricing and create a product launch plan for a new SaaS product"

initial_tasks = [
    "Identify top 5 competitors in the project management software space",
    "Research each competitor's pricing model and features",
    "Analyze market positioning and gaps",
    "Define our unique value proposition",
    "Create pricing strategy recommendation",
    "Draft launch timeline with key milestones",
    "Identify marketing channels and tactics"
]

completed = babyagi(project_objective, initial_tasks)

# Generate final summary
print("\n=== PROJECT SUMMARY ===")
for task in completed:
    print(f"✓ {task.name}")
    print(f"  {task.result[:150]}...\n")

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install langchain openai faiss-cpu
    # 2. Set OPENAI_API_KEY
    # 3. Run: python 09_babyagi_project_manager.py
    pass
