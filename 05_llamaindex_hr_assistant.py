"""
LlamaIndex - RAG-Based Employee Handbook Q&A
=============================================
Retrieval-Augmented Generation system for knowledge bases and documentation.
Creates an interactive Q&A system with source citations.

Requirements:
- llama-index
- chromadb
- OpenAI API key

Author: AI Agents Article Examples
"""

import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.tools import QueryEngineTool
from llama_index.agent import OpenAIAgent
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores import ChromaVectorStore
import chromadb

# Load employee handbook documents
documents = SimpleDirectoryReader("./handbook_docs").load_data()

# Create vector store for semantic search
chroma_client = chromadb.PersistentClient(path="./vector_db")
chroma_collection = chroma_client.create_collection(name="employee_handbook")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, 
    storage_context=storage_context,
    show_progress=True
)

# Create query engine with source citation
query_engine = index.as_query_engine(
    similarity_top_k=3,
    response_mode="tree_summarize",
    text_qa_template="""
    You are a helpful HR assistant. Use the provided context 
    from the employee handbook to answer questions. Always cite 
    your sources by referencing the document sections.
    
    Context: {context_str}
    Question: {query_str}
    """
)

# Wrap in a tool for agent use
hr_tool = QueryEngineTool(
    query_engine=query_engine,
    name="hr_policy_search",
    description="Search employee handbook for HR policy information"
)

# Create conversational agent
agent = OpenAIAgent.from_tools([hr_tool], verbose=True)

# Example conversation
conversations = [
    "What is the vacation policy for new employees?",
    "How do I submit expenses for reimbursement?",
    "What are the remote work guidelines?",
    "Can you explain the promotion review process?"
]

print("=== HR ASSISTANT SESSION ===\n")
for question in conversations:
    print(f"Employee: {question}")
    response = agent.chat(question)
    print(f"HR Assistant: {response}\n")
    print("-" * 50)

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install llama-index chromadb
    # 2. Create ./handbook_docs folder with PDF/TXT policy documents
    # 3. Set OPENAI_API_KEY
    # 4. Run: python 05_llamaindex_hr_assistant.py
    pass
