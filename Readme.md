# AI Agents Examples

A comprehensive collection of practical, working examples demonstrating 10 different AI agent frameworks and their real-world applications. Each example is production-ready and showcases best practices for building intelligent agents.

## Overview

This repository provides hands-on examples of AI agents using popular frameworks including LangChain, AutoGPT, CrewAI, Microsoft AutoGen, LlamaIndex, Phidata, OpenAI Assistants API, Haystack, BabyAGI, and Semantic Kernel. Each example solves a specific business problem and demonstrates the unique capabilities of its respective framework.

## Quick Start

Get started in under 5 minutes by following these steps. First, clone the repository to your local machine:

```bash
git clone https://github.com/thomascherickal/ai-agents-examples.git
cd ai-agents-examples
```

Next, install the required dependencies. You can install all dependencies at once or install them individually for specific examples:

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install for specific examples
pip install langchain openai python-dotenv  # For LangChain example
```

Configure your OpenAI API key by setting it as an environment variable:

```bash
# Linux/Mac
export OPENAI_API_KEY='your-api-key-here'

# Windows
set OPENAI_API_KEY=your-api-key-here
```

Now choose an example and run it. For instance, to run the LangChain document extractor:

```bash
python 01_langchain_document_extractor.py
```

For detailed setup instructions, refer to the QUICKSTART.md guide included in the repository.

## Examples Catalog

### 1. LangChain - Document Information Extractor

**File**: `01_langchain_document_extractor.py`

This example demonstrates how to extract structured information from meeting transcripts using LangChain's document processing capabilities. The system splits long documents into manageable chunks, processes them through a language model, and extracts key information like action items, decisions, and participants.

**Key Features**: The extractor uses recursive text splitting to handle documents of any length, Pydantic models for structured output validation, and custom prompts optimized for information extraction tasks.

**Use Case**: Process meeting transcripts, extract action items, identify key decisions, and create structured summaries for team collaboration.

**Dependencies**: langchain, openai, python-dotenv

**Run**: `python 01_langchain_document_extractor.py`

### 2. AutoGPT - Research Assistant

**File**: `02_autogpt_researcher.py`

An autonomous research agent that can plan, execute, and synthesize research on any topic. The agent breaks down research queries into subtasks, searches the web, evaluates sources, and produces comprehensive reports.

**Key Features**: Autonomous goal decomposition, multi-step planning, web search integration, source evaluation, and report generation with citations.

**Use Case**: Generate comprehensive research reports on emerging technologies, market analysis, or competitive intelligence.

**Dependencies**: autogpt, openai, selenium

**Run**: `python 02_autogpt_researcher.py`

### 3. CrewAI - Marketing Campaign Planner

**File**: `03_crewai_marketing_campaign.py`

A multi-agent system where specialized AI agents collaborate to create complete marketing campaigns. Different agents handle market research, content strategy, copywriting, and campaign analytics, working together like a real marketing team.

**Key Features**: Role-based agent specialization, inter-agent communication, sequential task execution, shared memory between agents, and collaborative decision-making.

**Use Case**: Generate complete marketing campaigns with research, strategy, content, and metrics for product launches or brand initiatives.

**Dependencies**: crewai, openai, python-dotenv

**Run**: `python 03_crewai_marketing_campaign.py`

### 4. Microsoft AutoGen - Pair Programming Assistant

**File**: `04_autogen_pair_programming.py`

Two AI agents working together in a conversational manner: one acts as a software engineer proposing solutions, the other as a code reviewer providing feedback. They iterate until reaching a satisfactory solution.

**Key Features**: Conversational multi-agent interaction, automatic conversation management, code generation and review, iterative refinement, and conversation history tracking.

**Use Case**: Generate code solutions with built-in review and quality assurance, or prototype new features through agent collaboration.

**Dependencies**: pyautogen, openai

**Run**: `python 04_autogen_pair_programming.py`

### 5. LlamaIndex - HR Knowledge Assistant

**File**: `05_llamaindex_hr_assistant.py`

A Retrieval-Augmented Generation system that answers employee questions using company documentation. The assistant indexes HR handbooks, policies, and procedures, then retrieves relevant context to answer queries accurately.

**Key Features**: Vector store integration, semantic search capabilities, context-aware responses, source attribution, and support for multiple document formats.

**Use Case**: Answer employee questions about policies, benefits, procedures, and company guidelines using internal documentation.

**Dependencies**: llama-index, openai, chromadb

**Run**: `python 05_llamaindex_hr_assistant.py`

### 6. Phidata - Financial Analysis Assistant

**File**: `06_phidata_financial_assistant.py`

A specialized agent that performs financial calculations, analyzes stock data, and generates investment insights. The agent has access to financial tools and can execute multi-step analysis workflows.

**Key Features**: Custom tool integration, financial calculations, stock data retrieval, trend analysis, and investment recommendation generation.

**Use Case**: Analyze stock performance, calculate financial metrics, and generate investment recommendations based on market data.

**Dependencies**: phidata, openai, yfinance

**Run**: `python 06_phidata_financial_assistant.py`

### 7. OpenAI Assistants API - Scheduling Assistant

**File**: `07_openai_scheduling_assistant.py`

A production-ready scheduling assistant built using OpenAI's Assistants API. The assistant manages calendar events, finds optimal meeting times, handles conflicts, and sends confirmation messages.

**Key Features**: Persistent conversation threads, function calling capabilities, state management, calendar integration, and natural language processing for scheduling requests.

**Use Case**: Automate meeting scheduling, manage calendar conflicts, and coordinate team availability.

**Dependencies**: openai, python-dotenv

**Run**: `python 07_openai_scheduling_assistant.py`

### 8. Haystack - Support Ticket Classifier

**File**: `08_haystack_ticket_classifier.py`

An NLP pipeline that automatically categorizes customer support tickets by urgency and department, then routes them to appropriate teams. The system processes ticket text, classifies content, and assigns priority levels.

**Key Features**: Document processing pipeline, classification algorithms, routing logic, priority assignment, and integration with support systems.

**Use Case**: Automatically categorize and route customer support tickets to reduce response times and improve support efficiency.

**Dependencies**: haystack-ai, openai

**Run**: `python 08_haystack_ticket_classifier.py`

### 9. BabyAGI - Project Management Agent

**File**: `09_babyagi_project_manager.py`

A task-driven autonomous agent that generates, prioritizes, and executes subtasks to accomplish complex project goals. The agent creates new tasks based on results, maintains context across executions, and adapts its approach.

**Key Features**: Automatic subtask generation, dynamic task prioritization, iterative execution with context awareness, goal-oriented behavior, and adaptive task planning.

**Use Case**: Break down complex projects into manageable tasks, automatically prioritize work, and execute tasks autonomously with minimal oversight.

**Dependencies**: babyagi, openai, pinecone

**Run**: `python 09_babyagi_project_manager.py`

### 10. Semantic Kernel - Email Composition Assistant

**File**: `10_semantic_kernel_email_assistant.py`

A professional email composition tool using Microsoft's Semantic Kernel framework. The assistant generates emails from key points and can adjust tone for different audiences and situations.

**Key Features**: Multiple tone options including professional, friendly, urgent, apologetic, and congratulatory styles. Key points integration, tone transformation capabilities, and template-based generation.

**Use Case**: Generate professional emails quickly for various business scenarios, adjust tone for different stakeholders, and maintain consistent communication quality.

**Dependencies**: semantic-kernel, openai

**Run**: `python 10_semantic_kernel_email_assistant.py`

## Framework Comparison

Understanding which framework to use for your specific needs is important. Here's how these frameworks compare across key dimensions:

LangChain excels as a general-purpose framework with medium complexity, no built-in multi-agent support, external memory management, and a medium learning curve. It's best for creating chains of operations and general-purpose applications.

AutoGPT is designed for autonomous research with high complexity, no multi-agent features, built-in memory, and a high learning curve. Choose this when you need agents that can independently plan and execute complex research tasks.

CrewAI specializes in team collaboration with medium complexity, built-in multi-agent support, shared memory between agents, and a medium learning curve. It's ideal when you need multiple specialized agents working together.

AutoGen focuses on conversational agents with medium complexity, excellent multi-agent support, thread-based memory, and a medium learning curve. Use this for applications requiring back-and-forth agent interactions.

LlamaIndex is optimized for document Q&A and RAG applications with low complexity, no multi-agent features, vector database memory, and a low learning curve. Perfect for building search and question-answering systems over documents.

Phidata handles domain-specific tasks with low complexity, no multi-agent features, context-based memory, and a low learning curve. Choose this for specialized applications with custom tools.

OpenAI Assistants API is designed for production applications with low complexity, no multi-agent features, thread-based memory, and a low learning curve. Best for production-ready applications with OpenAI's managed infrastructure.

Haystack powers search and NLP pipelines with medium complexity, no multi-agent features, document store memory, and a medium learning curve. Ideal for building search and information retrieval systems.

BabyAGI excels at task automation with high complexity, no multi-agent features, vector-based memory, and a high learning curve. Use this for autonomous task management and execution.

Semantic Kernel focuses on enterprise integration with medium complexity, no multi-agent features, plugin-based memory, and a medium learning curve. Best for integrating AI into existing enterprise applications.

## Project Structure

The repository is organized to make it easy to find and run examples:

```
ai-agents-examples/
│
├── 01_langchain_document_extractor.py    # LangChain document processing
├── 02_autogpt_researcher.py              # AutoGPT autonomous research
├── 03_crewai_marketing_campaign.py       # CrewAI multi-agent collaboration
├── 04_autogen_pair_programming.py        # Microsoft AutoGen coding
├── 05_llamaindex_hr_assistant.py         # LlamaIndex RAG system
├── 06_phidata_financial_assistant.py     # Phidata financial analysis
├── 07_openai_scheduling_assistant.py     # OpenAI Assistants API
├── 08_haystack_ticket_classifier.py      # Haystack NLP pipeline
├── 09_babyagi_project_manager.py         # BabyAGI task management
├── 10_semantic_kernel_email_assistant.py # Semantic Kernel email tools
│
├── README.md                              # This file
├── QUICKSTART.md                          # Quick start guide
├── CONTRIBUTING.md                        # Contribution guidelines
├── CHANGELOG.md                           # Version history
├── LICENSE                                # MIT License
├── requirements.txt                       # All dependencies
├── .env.example                           # Environment variables template
├── .gitignore                             # Git ignore rules
│
├── data/                                  # Sample data files
│   ├── meeting_transcript.txt
│   └── handbook_docs/
│
└── research_output/                       # Generated reports
```

## Usage Guidelines

### Working with Examples

When working with these examples, follow this general workflow. First, choose the example that best matches your use case by reviewing the descriptions above. Install the specific dependencies needed for that example using pip. Configure your API keys in environment variables, making sure to never commit them to version control. Prepare any required input files or directories as specified in each example. Run the Python script and review the console output or generated files.

### Best Practices

Protect your API keys by never committing them to version control. Monitor your OpenAI API usage carefully to control costs, as some examples can consume significant tokens. Each example includes basic error handling, but you should extend it for production use. Modify prompts and parameters to fit your specific needs and use cases. Always test with small datasets before processing large volumes of data.

## Troubleshooting

### Common Issues and Solutions

If you encounter an error that your API key is not found, the solution is to set the OPENAI_API_KEY environment variable properly. Module not found errors mean you need to install the required package using pip. Rate limiting errors can be resolved by adding delays between requests or upgrading your API plan. Memory issues when processing large documents can be fixed by reducing chunk_size or processing data in smaller batches.

### Debug Mode

Most frameworks support verbose output for debugging. Enable it like this:

```python
# LangChain
agent = initialize_agent(verbose=True)

# CrewAI
crew = Crew(verbose=True)

# AutoGen
agent = AssistantAgent(verbose=True)
```

## Contributing

Contributions are welcome and help make this repository better for everyone. To contribute, start by forking the repository to your GitHub account. Create a feature branch with a descriptive name. Add your example following the existing code structure and conventions. Test your code thoroughly to ensure it runs without errors. Update this README to include documentation for your example. Submit a pull request with a clear description of your changes.

### Guidelines for Contributors

Follow PEP 8 style guidelines for Python code. Include clear docstrings and comments explaining your code. Add comprehensive error handling and input validation. Provide sample data files if your example requires them. Update requirements.txt with any new dependencies. Test your example with both GPT-3.5-turbo and GPT-4 if possible to ensure compatibility.

## Resources

### Official Documentation

Each framework has comprehensive official documentation. LangChain's documentation covers getting started, concepts, and API reference. AutoGPT provides guides for autonomous agents. CrewAI explains multi-agent orchestration. Microsoft AutoGen documents conversational AI patterns. LlamaIndex focuses on data frameworks and RAG. Phidata covers specialized agent frameworks. OpenAI's Assistants API documentation explains the managed service. Haystack provides NLP pipeline guides. BabyAGI documentation covers autonomous task management. Semantic Kernel explains Microsoft's AI orchestration framework.

### Learning Resources

To deepen your understanding of AI agents, explore research papers on topics like ReAct (Synergizing Reasoning and Acting in Language Models), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, Constitutional AI for harmlessness from AI feedback, and Toolformer showing how language models can teach themselves to use tools.

Video tutorials provide visual learning experiences. Look for LangChain crash courses, guides on building AI agents, CrewAI tutorials, and RAG implementation guides.

For comprehensive learning, consider books like "Building LLM Powered Applications" by Valentina Alto, "Generative AI with LangChain" by Ben Auffarth, and "Hands-On Large Language Models" by Jay Alammar and Maarten Grootendorst.

### Community Support

Join communities to get help and share knowledge. The LangChain Discord server provides real-time support. The OpenAI Community Forum hosts discussions about API usage. The AI Agents subreddit connects practitioners. 

## License

This project is licensed under the MIT License, which means you're free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software. The only requirements are that you include the original copyright notice and provide the software "as is" without warranty. See the LICENSE file for complete details.

## Acknowledgments

This repository builds on the incredible work of the OpenAI team for providing the GPT models and API infrastructure. The developers and maintainers of each framework deserve recognition for their contributions to the open-source AI community. Thanks to all contributors to this repository who help improve and expand the examples.

## Support

If you encounter issues or have questions, start by checking the Troubleshooting section in this README. Review the official documentation for your chosen framework. Search existing GitHub issues to see if others have faced similar problems. If you still need help, create a new issue with detailed information about your environment, the error you're experiencing, and steps to reproduce it.

## Disclaimer

These examples are designed for educational purposes and to demonstrate framework capabilities. When deploying AI agents to production environments, remember to implement proper error handling and logging, add authentication and authorization, monitor API usage and costs carefully, follow security best practices, comply with data privacy regulations, and test thoroughly before deployment.

---

**Star this repository** if you find it helpful! Your support helps others discover these resources.

**Questions or suggestions?** Open an issue or submit a pull request. We welcome feedback and contributions from the community.

---

*Last Updated: January 2026*

*License: MIT*

*Repository: https://github.com/thomascherickal/ai-agents-examples*

Happy learning!

Thomas Cherickal (@thomascherickal)
