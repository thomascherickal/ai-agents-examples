"""
LangChain - Document Summarization and Information Extraction
==============================================================
Extracts key information from meeting transcripts including action items,
decisions made, and questions raised.

Requirements:
- langchain
- openai
- OpenAI API key

Author: AI Agents Article Examples
"""

import os
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize the language model
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Load and prepare the document
loader = TextLoader("meeting_transcript.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)

# Define extraction prompt
extraction_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Analyze the following meeting transcript and extract:
    1. All action items with owners and deadlines
    2. Key decisions made
    3. Open questions that need follow-up
    
    Transcript: {text}
    
    Format your response as a structured markdown report."""
)

extraction_chain = LLMChain(llm=llm, prompt=extraction_prompt)

# Process each chunk and compile results
all_action_items = []
all_decisions = []
all_questions = []

for chunk in chunks:
    result = extraction_chain.run({"text": chunk.page_content})
    # Parse result into categories (simplified for demo)
    print(f"Processed chunk {chunks.index(chunk) + 1}/{len(chunks)}")

# Generate final summary report
summary_prompt = PromptTemplate(
    input_variables=["findings"],
    template="""Compile all extracted findings into a single executive summary.
    
    Findings:
    {findings}
    
    Create a clean, organized report with clear sections.""")
    
final_report = extraction_chain.run(
    {"text": " ".join([c.page_content for c in chunks])}
)

print("\n=== EXTRACTED REPORT ===")
print(final_report)

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install langchain openai
    # 2. Set your OpenAI API key: os.environ["OPENAI_API_KEY"] = "your-key"
    # 3. Save your transcript as "meeting_transcript.txt"
    # 4. Run: python 01_langchain_document_extractor.py
    
    # Note: You can automate meeting transcripts with tools like Otter.ai or Fireflies.ai
    pass
