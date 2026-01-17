"""
Haystack - Customer Support Ticket Classification
==================================================
Open-source framework for building sophisticated search systems
and question-answering applications.

Requirements:
- farm-haystack[transformers,all]
- OpenAI API key (optional)

Author: AI Agents Article Examples
"""

import os
from haystack import Pipeline
from haystack.components.readers import ExtractiveReader
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.components.classifiers import TextClassificationClassifier
from haystack import Document
from haystack.document_stores.in_memory import InMemoryDocumentStore

# Define ticket categories
TICKET_CATEGORIES = [
    "billing_issue",
    "technical_bug",
    "feature_request",
    "account_access",
    "general_inquiry",
    "performance_complaint"
]

# Create training documents for classification
category_documents = [
    Document(content="Billing discrepancy invoice wrong charge refund request", meta={"category": "billing_issue"}),
    Document(content="Cannot login password reset not working account locked", meta={"category": "account_access"}),
    Document(content="Application crashes error message freeze not responding", meta={"category": "technical_bug"}),
    Document(content="Would like new integration API capability add feature", meta={"category": "feature_request"}),
    Document(content="Slow performance page loading timeout response time", meta={"category": "performance_complaint"}),
    Document(content="How to use product questions about functionality guide", meta={"category": "general_inquiry"}),
]

# Set up the document store
document_store = InMemoryDocumentStore()
document_store.write_documents(category_documents)

# Create the classification pipeline
pipeline = Pipeline()

# Add retriever for context
retriever = InMemoryBM25Retriever(document_store=document_store)
pipeline.add_component(instance=retriever, name="retriever")

# Add classifier
classifier = TextClassificationClassifier(
    model="cross-encoder/nli-deberta-v3-small",
    labels=TICKET_CATEGORIES
)
pipeline.add_component(instance=classifier, name="classifier")

# Add reader for additional context
reader = ExtractiveReader(model="distilbert-base-uncased-distilled-squad")
pipeline.add_component(instance=reader, name="reader")

# Connect components
pipeline.connect("retriever", "classifier")
pipeline.connect("retriever", "reader")

def classify_ticket(ticket_text: str, priority: str = "medium"):
    """Classify a support ticket and suggest routing"""
    
    # Run classification
    result = pipeline.run({
        "retriever": {"query": ticket_text, "filters": None},
        "classifier": {"text": ticket_text},
        "reader": {"query": "What is the main issue?", "documents": []}
    })
    
    predicted_category = result["classifier"]["predictions"][0]
    confidence = result["classifier"]["confidences"][0]
    
    # Suggest routing based on category
    routing_map = {
        "billing_issue": "Finance Team - Response SLA: 4 hours",
        "technical_bug": "Engineering Triage - Response SLA: 2 hours",
        "feature_request": "Product Team - Response SLA: 24 hours",
        "account_access": "Support Tier 1 - Response SLA: 1 hour",
        "performance_complaint": "Engineering Priority - Response SLA: 2 hours",
        "general_inquiry": "Support Tier 1 - Response SLA: 8 hours"
    }
    
    return {
        "ticket_text": ticket_text,
        "category": predicted_category,
        "confidence": confidence,
        "suggested_routing": routing_map.get(predicted_category, "General Support"),
        "priority_suggestion": priority
    }

# Example ticket classifications
tickets = [
    "I was charged twice for my subscription this month. Please refund the duplicate charge.",
    "The dashboard takes 30 seconds to load. This is unusable. Fix it now.",
    "Can you add a dark mode to the application? It would really help my eyes.",
    "I've tried to reset my password 5 times but the email never arrives. My account is john@company.com",
    "Where can I find the documentation for the API endpoints?"
]

print("=== SUPPORT TICKET CLASSIFICATION ===\n")
for ticket in tickets:
    result = classify_ticket(ticket)
    print(f"Ticket: {ticket[:60]}...")
    print(f"Category: {result['category']} (confidence: {result['confidence']:.2f})")
    print(f"Route to: {result['suggested_routing']}")
    print("-" * 50)

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install farm-haystack[transformers,all]
    # 2. Set OPENAI_API_KEY for classifier if needed
    # 3. Run: python 08_haystack_ticket_classifier.py
    pass
